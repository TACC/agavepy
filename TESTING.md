# Testing

## Writing new tests

Most code changes will fall into one of the following categories.

### Writing tests for new features

New code should be covered by unit tests. If the code is difficult to test with
a unit tests then that is a good sign that it should be refactored to make it
easier to reuse and maintain. Consider accepting unexported interfaces instead
of structs so that fakes can be provided for dependencies.


### Writing tests for bug fixes

Bugs fixes should include a unit test case which exercises the bug.


### Test structure

Test serve a dual purpose: test functionality and document the expected
response from the agave API.

The test suite uses valid sample responses, see 
[sample responses](tests/sample_responses) to mock the agave API by spawning a
mock server in the local host to handle any requests from the cli.


## Running tests

To run the unit test suite run the development container:
```
$ make shell
```

### Testing Python 3
Before you start testing, you'll need to install all the package dependencies.
```
$ make install
```

Inside the container run:
```
$ make tests
```


### Testing Python 2
Install all dependencies
```
$ make install-p2
```

Run tests
```
$ make tests-py2
```
