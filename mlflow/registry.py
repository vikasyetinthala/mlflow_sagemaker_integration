import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

# Create an experiment with a name that is unique and case sensitive.
client = MlflowClient()
remote_server_uri = "http://35.184.179.4:5000/" # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

model_name = "ElasticnetWineModel"
model_version = 2
mr_uri = mlflow.get_registry_uri()
#print("Current registry uri: {}".format(mr_uri))

def load_model(model_name,model_version):
    model = mlflow.sklearn.load_model(
        model_uri=f"models:/{model_name}/{model_version}"
        )
    return model

model=load_model(model_name,model_version)
print(model)

#print(model.predict(data))
