import logging
import logging.config
from azureml.core import Datastore

# Import local files
from config.config import Config

class Base:
    """
    This will define common functionality across various subprocess of maz-optimizer.
    """

    def __init__(self):
        """
        Initializes the required variables.
        """
        if 'FileHandler ' in Config.logging['handlers']:
            # Define file handler and set formatter.
            file_handler = logging.FileHandler(Config.logging['filename'])
            formatter = logging.Formatter(
                '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
            file_handler.setFormatter(formatter)
            # Gets or creates a logger.
            self.logger = logging.getLogger(__name__)
            # Set log level.
            self.logger.setLevel(Config.logging['level'])
            # Add file handler to logger
            self.logger.addHandler(file_handler)
        else:
            logging.basicConfig(
                level=Config.logging['level'], format=Config.logging['format'])
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(Config.logging['level'])

        self.logger.info('logging initialized')
