from data.Queries import Queries as Q
from utils.HelperFunc import HelperFunc as HF

import numpy as np
import pandas as pd
from base import Base

class Repository(Base):
    """
    Repository to ingest data from Database
    """

    def __init__():
        super().__init__()


    @classmethod
    def get_baseline_df(cls, pillar, month):
        """
        Method to import the baseline dataframe 
        Args:
            pillar: Pillar
            month: Month 
        Returns:
            pd.DataFrame: baseline dataframe
        """
        baseline_df = HF.get_azure_sql_db(query = Q.baseline_sls.format(PILLAR = pillar, Month = month))
        return baseline_df
        
        
    @classmethod
    def get_treatment_df(cls, pillar, month, metric = 'maco', long_metric = 'maco'):
        """
        Method to import the treatment dataframe 
        Args:
            pillar: Pillar
            month: Month 
        Returns:
            pd.DataFrame: treatment dataframe
        """

        treatment_df = HF.get_azure_sql_db(query = Q.treatment_sls.format(PILLAR = pillar, Month = month))
        return treatment_df

    @classmethod
    def get_baseline_sku_df(cls, pillar, month):
        """
        Method to import the baseline_sku dataframe 
        Args:
            pillar: Pillar
            month: Month 
        Returns:
            pd.DataFrame: baseline_sku dataframe
        """
        baseline_sku = HF.get_azure_sql_db(query = Q.baseline_sku_sls.format(PILLAR = pillar, Month = month))
        return baseline_sku
        
        
    @classmethod
    def get_treatment_sku_df(cls, pillar, month):
        """
        Method to import the treatment_sku dataframe 
        Args:
            pillar: Pillar
            month: Month 
        Returns:
            pd.DataFrame: treatment_sku dataframe
        """

        treatment_sku = HF.get_azure_sql_db(query = Q.treatment_sku_sls.format(PILLAR = pillar, Month = month))
        return treatment_sku
       
        
    @classmethod
    def get_treatment_df_2(cls, pillar, month):
        """
        Method to import the treatment_df_2 dataframe 
        Args:
            pillar: Pillar
            month: Month 
        Returns:
            pd.DataFrame: treatment_df_2 dataframe
        """

        treatment_df_2 = HF.get_azure_sql_db(query = Q.treatment_sls2.format(PILLAR = pillar, Month = month))
        return treatment_df_2