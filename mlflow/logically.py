import pprint
import numpy as np
from sklearn.linear_model import LinearRegression
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()
remote_server_uri = "s3://vikasbucket1/mlflowserver/" # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

def fetch_logged_data(run_id):
    client = mlflow.tracking.MlflowClient()
    data = client.get_run(run_id).data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts


for name in list(client.list_registered_models()):
    print(name)
