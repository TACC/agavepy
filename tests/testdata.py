__author__ = 'jstubbs'

import json

import agavepy.agave as a


class TestData(object):

    def __init__(self, credentials):
        self.local_data = credentials

    def get_test_storage_system(self):
        """
        Example storage system read from an external file.
        """
        storage = self.file_to_json('test-storage.nebula.tacc.json')
        storage['id'] = self.local_data['storage']
        return self.api_client.deserialize(storage, 'SystemRequest')

    def get_test_compute_system(self):
        """
        Example compute system defined inline.
        """
        compute = self.file_to_json('test-compute.nebula.tacc.json')
        compute['id'] = self.local_data['execution']
        return self.api_client.deserialize(compute, 'SystemRequest')

    def get_test_app(self):
        """
        Example application defined inline.
        """
        test_app = a.AttrDict()
        #Whether the application is available.
        test_app.available = True
        #Whether the application supports checkpointing.
        test_app.checkpointable = False # bool
        #The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.
        test_app.defaultMaxRunTime = None # str
        #The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.
        test_app.defaultMemory = 1 # str
        #The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.
        test_app.defaultNodeCount = None # str
        #The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.
        test_app.defaultProcessors = 1 # str
        #The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.
        test_app.defaultQueue = None # str
        #The location in the user's default storage system containing the application wrapper and dependencies.
        test_app.deploymentPath = self.local_data['deployment_path'] # str
        #The system id of the storage system where this app should run.
        test_app.deploymentSystem = self.local_data['storage'] # str
        #The system id of the execution system where this app should run.
        test_app.executionSystem = self.local_data['execution'] # str
        #The execution type of the application. If you're unsure, it's probably HPC.
        test_app.executionType = 'HPC' # str
        #The URL where users can go for more information about the app.
        test_app.helpURI = 'http://www.gnu.org/s/coreutils/manual/html_node/wc-invocation.html' # str
        #The icon to associate with this app.
        test_app.icon = None # str

        #The inputs files for this application. -- list[ApplicationInput]
        test_app.inputs = [
              {
                 "id":"query1",
                 "value":{
                    "default":"agave://demo.storage.example.com/apps/wc-1.00/picksumipsum.txt",
                    "validator":"",
                    "required":True,
                    "visible":True
                 },
                 "details":{
                    "label":"File to count words in:",
                    "description":""
                 },
                 "semantics":{
                    "ontology":[
                       "http://sswapmeet.sswap.info/util/TextDocument"
                    ],
                    "minCardinality":1,
                    "maxCardinality":1,
                    "fileTypes":[
                       "text-0"
                    ]
                 }
              }
           ]
        #The label to use when generating forms.
        test_app.label = 'Word Count' # str
        #The full text description of this input to use when generating forms.
        test_app.longDescription = '' # str
        #An array of modules to load prior to the execution of the application.
        test_app.modules = ["purge", "load TACC"] # list[str]
        #The name of the application. The name does not have to be unique, but the combination of name and version does.
        test_app.name = self.local_data['app_name'] # str
        #An array of ontology values describing this application.
        test_app.ontology = ["http://sswapmeet.sswap.info/algorithms/wc"] # list[str]
        #The outputs files for this application.
        test_app.outputs = None # list[ApplicationOutput]
        #The parallelism type of the application. If you're unsure, it's probably SERIAL.
        test_app.parallelism = 'SERIAL' # str

        #The inputs parameters for this application - list[ApplicationParameter]
        test_app.parameters =  [
              {
                 "id":"printLongestLine",
                 "value":{
                    "default":False,
                    "type":"string",
                    "validator":"",
                    "visible":True,
                    "required":False
                 },
                 "details":{
                    "label":"Print the length of the longest line",
                    "description":"Command option -L"
                 },
                 "semantics":{
                    "ontology":[
                       "xs:boolean"
                    ]
                 }
              }
           ]
        #The short description of this application.
        test_app.shortDescription = 'Counts words in a file' # str
        #An array of tags related to this application.
        test_app.tags = ["textutils", "gnu"] # list[str]
        #The path to the wrapper script relative to the deploymentPath.
        test_app.templatePath = 'wrapper.sh' # str
        #The path to the test script relative to the deploymentPath.
        test_app.testPath = 'wrapper.sh' # str
        #The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.
        test_app.version = '1.00' # str

        return test_app

    def get_test_job(self):
        """
        Example job defined inline.
        """
        test_job = JobRequest()
        test_job.name = self.local_data['app_name']
        test_job.appId = '{}-{}'.format(self.local_data['app_name'],
                                        self.local_data['app_version'])
        test_job.memoryPerNode = 1
        test_job.inputs = {"query1":"agave://data.iplantcollaborative.org/jstubbs/5kB.txt"}
        return test_job

    def get_test_job_from_file(self):
        """
        Example job request read in from an external file.
        """
        filename = '{}-{}-job.json'.format(self.local_data['app_name'],
                                           self.local_data['app_version'])
        return self.api_client.deserialize(self.file_to_json(filename),
                                           'JobRequest')
