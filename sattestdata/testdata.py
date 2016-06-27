import os


class TestDataError(Exception):
    pass


class TestData(object):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

    def __init__(self):
        """ Initialize testdata for a scene """
        pass

    @classmethod
    def list_scenes(cls):
        """ List the scenes in the directory """
        return [d for d in os.listdir(cls.path) if os.path.isdir(os.path.join(cls.path, d))]
