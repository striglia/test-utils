from testify import assert_equal
from testify import run
from testify import TestCase

import utils

class TestMockListPop(TestCase):
    def test_pops_proper_values(self):
        vals = ['foo', 'bar', 'baz']
        mock = utils.MockListPop(vals)
        for v in vals:
            assert_equal(v, mock('random', 'args'))

    def test_no_reference_bugs(self):
        old_vals = ['foo', 'bar']
        mock = utils.MockListPop(old_vals)
        
        # Modify list and make sure it doesn't modify responses
        vals = ['baz', 'bar']
        assert_equal(old_vals[0], mock())

class TestMockCallRespond(TestCase):
    def test_call_response(self):
        vals = {'foo': 1, 'bar': 2, 3: 'baz'}
        default = 'nope'
        mock = utils.MockCallRespond(vals, default)
        for k, v in vals.items():
            assert_equal(v, mock(k))

    def test_default_response(self):
        default = 'nope'
        mock = utils.MockCallRespond({}, default)
        assert_equal(default, mock('anything'))

if __name__ == '__main__':
    run()
