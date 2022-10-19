import functools
import unittest


def rely(case_name:str=None):
    """
    :param case
    :return:
    """
    def wrapper_case(test_func):

        @functools.wraps(test_func)
        def _func(cur):

            if case_name == test_func.__name__:
                raise ValueError("{} 你不能将依赖作为自己".format(case_name))

            failures = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.failures]

            errors = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.errors]

            skipped = [str(fail_[0]).split("=")[0].split(" ")[0] for fail_ in cur._outcome.result.skipped]

            tag_status = (case_name in failures) or (case_name in errors) or (case_name in skipped)

            test = unittest.skipIf(tag_status, '{} ({} rely {})'.format(test_func.__name__,test_func.__name__,case_name))(test_func)
            return test(cur)
        return _func
    return wrapper_case





from sveltest.support.common import ObjectDict

def env(cls):
    from sveltest.bin.conf import settings
    cls_name = cls.__name__

    try:
        cls.obj_conf = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)
    except:
        pass


    cls.env = cls.obj_conf.DEFAULT_ENVIRONMENT_NAME
    cls.current_env_host = cls.obj_conf.ENVIRONMENT_HOST[0]
    cls.current_env_port = cls.obj_conf.ENVIRONMENT_PORT[0]
    return cls


# @test_data
def ap():
    return 1


print(ap())
