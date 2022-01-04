from utils import config_reader as get_config


class Test_dim:
    """
    This is a static class for customer and its attributes that will be inherited by algorithms base class to be able
    to use this as column names
    """

    def __init__(self):
        self.TEST_ID = get_config('TEST_DIM', 'TEST_ID')
        self.MONTH = get_config('TEST_DIM', 'MONTH')
        self.YEAR = get_config('TEST_DIM', 'YEAR')
        self.TEST_CATEGORY = get_config('TEST_DIM', 'TEST_CATEGORY')
        self.BASELINE_START = get_config('TEST_DIM', 'BASELINE_START')
        self.BASELINE_END = get_config('TEST_DIM', 'BASELINE_END')
        self.ANALYSIS_START = get_config('TEST_DIM', 'ANALYSIS_START')
        self.ANALYSIS_END = get_config('TEST_DIM', 'ANALYSIS_END')