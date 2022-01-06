"""
Module to store common config variables.
"""
import os
# Initializing azure ml variables
from azureml.core import Workspace, Datastore
from azureml.core.authentication import ServicePrincipalAuthentication


class Config():

    # Initializing the logging variable
    logging = {
        "filename": "rtc.log",
        "format": "%(asctime)s:%(levelname)s:%(process)d:%(name)s:%(module)s:%(lineno)d:%(message)s",
        "handlers": "FileHandler",
        "level": "INFO",
        "version": 1
    }

    # Initializing the vertica info
    vert_info = {
        "host": "10.92.22.22",
        "port": 5433,
        "database": "modelobi",
        "user": "usrGAC",
        "password": "G4CTeam!"
    }

    subscription_id = '73f88e6b-3a35-4612-b550-555157e7059f'
    resource_group = 'GLOBAL-BREWDAT-SANDBOX-MAZ103-RG-GB-DEV'
    workspace_name = 'aml-weu-dev-asx-131'

    # Get workspace from the config
    try:
        TENANT_ID =  os.environ["smdc_tenant_id"]
        CLIENT_ID =  os.environ["smdc_client_id"]
        CLIENT_SECRET = os.environ["smdc_client_secret"]
        sp = ServicePrincipalAuthentication(tenant_id=TENANT_ID, # tenantID
                                        service_principal_id=CLIENT_ID, # clientId
                                service_principal_password=CLIENT_SECRET) # clientSecret
        workspace = Workspace(subscription_id = subscription_id,
        resource_group=resource_group, workspace_name=workspace_name,auth = sp)
    except:
        workspace = Workspace(subscription_id, resource_group, workspace_name, _location=None,
        _disable_service_check=False, _workspace_id=None, sku='basic', tags=None, _cloud='AzureCloud')

    # Initialzing azure ml datastore
    mazo_datastore = Datastore.get(workspace, "mazoptimizer")
    testops_datastore =   Datastore.get(workspace, "testops_datastore")
    sql_datastore = Datastore.get(workspace,"synapse_aswweudevasx131")
