import joblib 
import json 
from azureml.core.model import Model 


def init():
    global ref_cols, predictor 
    model_path=Model.get_model_path('modelname')
    ref_cols, predictor = joblib.load(model_path)

def run(raw_data):
    data_dict=json.loads(raw_data)['data']
    data= pd.DataFrame.from_dict(data_dict)
    "......................."
    "some stuff we have to do it"
    "......................."
    predictions = predict("....")
    classes=["...","..."]
    predicted_classes=[]
    for prediction in predictions:
        predicted_classes.append("......")
    return json.dumps(predicted_classes)