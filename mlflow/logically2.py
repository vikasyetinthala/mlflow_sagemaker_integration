import pprint
import numpy as np
from sklearn.linear_model import LinearRegression
import mlflow
from mlflow.tracking import MlflowClient
import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

local_dir="C:\\Users\\krishna\\Desktop\\registry\\run_id"

#if not os.path.exists(local_dir):
#  os.mkdir(local_dir)
def load_model():
    client = mlflow.tracking.MlflowClient()
    df = mlflow.search_runs(filter_string="metrics.rmse < 1")
    run_id = df.loc[df['metrics.rmse'].idxmin()]['run_id']
    model = mlflow.sklearn.load_model("runs:/" + run_id + "/model")
    #artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    local_dir="C:\\Users\\krishna\\Desktop\\registry\\run_id"
    if not os.path.exists(local_dir):
      os.mkdir(local_dir)
    artifacts=client.download_artifacts(run_id, "model", local_dir)
    return run_id,model,artifacts


csv_url = (
    "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
)
try:
    data = pd.read_csv(csv_url, sep=";")
except Exception as e:
    logger.exception(
        "Unable to download training & test CSV, check your internet connection. Error: %s", e
    )

# Split the data into training and test sets. (0.75, 0.25) split.
train, test = train_test_split(data)

# The predicted column is "quality" which is a scalar from [3, 9]
train_x = train.drop(["quality"], axis=1)
test_x = test.drop(["quality"], axis=1)
train_y = train[["quality"]]
test_y = test[["quality"]]

run_id,model,artifacts=load_model()

print(artifacts)
