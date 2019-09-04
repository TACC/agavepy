import time

class Error(Exception):
    pass

class TimeoutError(Error):
    pass

class AgaveAsyncResponse(object):
    """
    Implements parts of the concurrent.futures.Future interface for nonblocking Agave responses.
    """
    def __init__(self, ag, response):
        """Construct an asynchronous response object from an Agave response which should be an agavepy.agave.AttrDict
        """
        self.ag = ag
        self.response = response
        self.status = response.status
        self.retries = 0
        self.url = response._links.get('history').get('href')
        if not self.url:
            raise Error("Error parsing response object: no URL detected. response: " + str(response))
        # url's returned by agave sometimes point to docker.example.com
        self.url = self.url.replace('https://docker.example.com', self.ag.api_server)
        # url's returned by agave sometimes have the version as 2.0, so we replace that here
        self.url = self.url.replace('/2.0/','/v2/')

    def _update_status(self):
        rsp = self.ag.geturl(self.url)
        if (rsp.status_code == 404 or rsp.status_code == 403) and self.retries < 10:
            time.sleep(1.5)
            self.retries += 1
            return self._update_status()
        if not rsp.status_code == 200:
            raise Error("Error updating status; invalid status code:  " + str(rsp.status_code) + str(rsp.content))
        result = rsp.json().get('result')
        if not result:
            raise Error("Error updating status: " + str(rsp))
        # if the transfer ever completed, we'll call it good:
        if len([x for x in result if 'COMPLETE' in x['status']]) > 0:
            self.status = 'FINISHED'
        # jobs end in 'finished' status
        elif len([x for x in result if 'FINISHED' in x['status']]) > 0:
            self.status = 'FINISHED'
        # job ended in 'failed' status
        elif len([x for x in result if 'FAILED' in x['status']]) > 0:
            self.status = 'FAILED'
        else:
            # sort on creation time of the history object
            result = sorted(result, key=lambda k: k['created'])
            self.status = result[0].get('status')

    def _is_done(self):
        return self.status == 'FINISHED' or self.status == 'FAILED'

    def done(self):
        """Return True if the call was successfully cancelled or finished running."""
        self._update_status()
        return self._is_done()

    def result(self, timeout=None):
        """
        Returns the result of the original call, blocking until the result is returned or the timeout parameter is
        reached. The timeout paramter is interpreted in seconds.
        :param timeout:
        :return:
        """
        if self._is_done():
            return self.status
        self._update_status()
        now = time.time()
        if timeout:
            future = now + timeout
        else:
            future = float("inf")
        while time.time() < future:
            time.sleep(1)
            self._update_status()
            if self._is_done():
                return self.status
        raise TimeoutError()
