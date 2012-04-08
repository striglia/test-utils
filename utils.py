import mock

class MockListPop(mock.Mock):
    """Mock subclass for mocking out methods or attributes which should return a series of values in sequence."""

    def __init__(self, return_values, *args, **kwargs):
        super(MockListPop, self).__init__(*args, **kwargs)
        # Copy to avoid silly reference issues
        self.original_values = return_values[:]
        self.values = return_values[:]

    def __call__(self, *args, **kwargs):
        """Swallows all input and pops the next value."""
        return self.values.pop(0)

class MockCallRespond(mock.Mock):
    """Mock subclass for mocking out methods or attributes which should return a particular value for different input strings."""

    def __init__(self, response_dict, default=None, *args, **kwargs):
        super(MockCallRespond, self).__init__(*args, **kwargs)
        # Copy to avoid silly reference issues
        self.response_dict = response_dict
        self.default_response = default

    def __call__(self, key, *args, **kwargs):
        """Returns the value associated with the input key or the default."""
        return self.response_dict.get(key, self.default_response)
