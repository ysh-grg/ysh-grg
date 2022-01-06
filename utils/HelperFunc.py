"""
Module to add helper function to be used in the maz_optim module
"""
# import external libraries.
import pandas as pd
from azureml.core import Dataset
from azureml.data.datapath import DataPath
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess
from io import BytesIO
import pyarrow as pa
import pyarrow.parquet as pq

# import internal modules.
from config import Config as con

class HelperFunc():
    """
    Module to store helper functions
    """

    @classmethod
    def get_vertica_db(cls, query: str):
        """
        Method to establish the connect with vertica and ingest the database required as per the query
        Args:
            query: string of the query to be executed
        Returns:
            pd.DataFrame: resultant dataframe from the query
        """
        # Getting the dict variable ver_info which contains the required credentials.
        vert_info = con.vert_info
        user = vert_info['user']
        pwd = vert_info['password']
        host= vert_info['host']
        port = vert_info['port']
        database = vert_info['database']
        sqlstring = 'vertica+vertica_python://' + user + ':' + pwd + '@' + host + ':' + str(port) + '/' + database
        result_df = pd.read_sql(query, sqlstring)
        result_df = result_df._to_pandas()
        return result_df

    @classmethod
    def get_azure_sql_db(cls, query: str):
        """
        Method to get pandas dataframe from azure sql server based on the query provided
        Args:
            query: sql query to execute against the azure sql db
        Returns:
            pd.DataFrame
        """
        # Ingesting the table from the path defined in config file.
    
        querypath = DataPath(con.sql_datastore, query)
        try:
            tabular = Dataset.Tabular.from_sql_query(querypath, query_timeout=100)
            df = tabular.to_pandas_dataframe()
        except Exception as err:
            print("error type",type(err))
            df = pd.DataFrame([])
        return df

    @classmethod
    def write_pandas_to_csv_adls(cls, df: pd.DataFrame):
        """
        Method to upload dataframe to adls blob storage as csv
        Args:
            df: pandas dataframe to save as csv to adls blob storage
        Returns:
            pd.DataFrame
        """
        df_csv = df.to_csv()
        filename = df.columns.name +'.csv'
        block_blob_service = BlockBlobService(
            account_name=con.adls_account_name, account_key=con.adls_account_key)
        blob_file_name = con.adls_testops_folder + filename
        block_blob_service.create_blob_from_text(
            con.adls_container_name, blob_file_name, df_csv)
        return

    @classmethod
    def write_pandas_to_parquet_adls(cls, df: pd.DataFrame):
        """
        Method to upload pandas dataframe to adls blob storage as parquets
        Args:
            df: pandas dataframe to save as parquet to adls blob storage
        Returns:
            pd.DataFrame
        """
        filename = df.columns.name +'.parquet'
        block_blob_service = BlockBlobService(
            account_name=con.adls_account_name, account_key=con.adls_account_key)
        blob_file_name = con.adls_testops_folder + filename
        table = pa.Table.from_pandas(df)
        buf = pa.BufferOutputStream()
        pq.write_table(table, buf)
        block_blob_service.create_blob_from_bytes(
            con.adls_container_name,
            blob_file_name,
            buf.getvalue().to_pybytes()
        )
        return
