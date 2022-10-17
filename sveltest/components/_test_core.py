import functools
import unittest


def rely(case_name:str=None):
    """
    :param case
    :return:
    """
    def wrapper_func(test_func):

        @functools.wraps(test_func)
        def inner_func(self):

            if case_name == test_func.__name__:
                raise ValueError("{} 你不能将依赖作为自己".format(case_name))



            failures = str([fail_[0] for fail_ in self._outcome.result.failures])

            errors = str([error_[0] for error_ in self._outcome.result.errors])

            skipped = str([skip_[0] for skip_ in self._outcome.result.skipped])


            flag = (case_name in failures) or (case_name in errors) or (case_name in skipped)
            test = unittest.skipIf(flag, '{} 该用例所关联的用例执行失败或已被跳过执行'.format(case_name))(test_func)
            return test(self)
        return inner_func
    return wrapper_func
