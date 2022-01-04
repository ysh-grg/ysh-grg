from utils import config_reader as get_config


class Test_clients:
    """
    This is a static class for customer and its attributes that will be inherited by algorithms base class to be able
    to use this as column names
    """

    def __init__(self):
        self.CLIENT_ID = get_config('TEST_CLIENT', 'CLIENT_ID')
        self.MONTH = get_config('TEST_CLIENT', 'MONTH')
        self.YEAR = get_config('TEST_CLIENT', 'YEAR')
        self.TEST_ID = get_config('TEST_CLIENT', 'TEST_ID')
        self.TEST_GROUP = get_config('TEST_CLIENT', 'TEST_GROUP')
        self.BASELINE_END = get_config('TEST_DIM', 'BASELINE_END')
        self.ANALYSIS_START = get_config('TEST_DIM', 'ANALYSIS_START')
        self.ANALYSIS_END = get_config('TEST_DIM', 'ANALYSIS_END')