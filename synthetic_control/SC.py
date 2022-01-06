import pandas as pd
import numpy as np
from pandas.core.accessor import register_index_accessor

from base import Base
from data.Repository import Repository 

class SC(Base):
    """
    Synthetic Control Class
    """

    def __init__(self, pillar, month, metric, long_metric, sku= False ):
        """
        Args:
            pillar:  pillar to analyze lift.
            month: month for tests
            metric: enter the metric, 'vol', 'net_rev', 'maco'
            long_metric: enter the long name of metric, 'volume', 'net_revenue', 'maco'
        """
        self.pillar = pillar
        self.month = month
        self.metric = metric
        self.long_metric = long_metric
        self.baseline_df = None 
        self.treatment_df = None 
        self.baseline_df_wide = None 
        self.treatment_df_wide = None
        self.get_baseline_df = Repository.get_baseline_sku_df if sku else Repository.get_baseline_df
        self.get_treatment_df = Repository.get_treatment_sku_df if sku else Repository.get_treatment_df
        #TODO Create case for get_treatment_df_2 
    
    def prepare_data(self):
        """
        Method to get data and do data processing  
        Returns:
            dictionary: 
                pd.DataFrame: baseline_df 
                pd.DataFrame: baseline_df_wide
                pd.DataFrame: treatment_df
                pd.DataFrame: treatment_df_wide
        """
        self.baseline_df = self.get_baseline_df(self.pillar, self.month)
        self.treatment_df = self.get_treatment_df(self.pillar, self.month)

        self.baseline_df_wide = (
            self.baseline_df
            .loc[self.baseline_df[self.long_metric] > 0]
            .assign(week_name = lambda x: self.metric + '_' + x['week_num'],
                    met = lambda x: x[self.long_metric] / 7)
            .pivot_table(index=['store_id', 'DRV', 'UEN', 'poc_segmentation', 'sub_test_id', 'test_group'], columns='week_name', values='met')
            .reset_index() 
            #TODO create constant variables for indexes 
        )

        self.treatment_df_wide = (
            self.treatment_df
            .loc[self.baseline_df[self.long_metric] > 0]
            .assign(week_name = lambda x: self.metric + '_' + x['week_num'],
                    met = lambda x: x[self.long_metric] / x['n_days'])
            .pivot_table(index=['store_id', 'DRV', 'UEN', 'poc_segmentation', 'sub_test_id', 'test_group'], columns='week_name', values='met')
            .reset_index()
            #TODO create constant variables for indexes 
        )

        output = {
            "baseline_df" : self.baseline_df,
            "baseline_df_wide" : self.baseline_df_wide,
            "treatment_df" :  self.treatment_df,
            "treatment_df_wide" : self.treatment_df_wide
        } 
        return output
