from azureml.core import Run 
import pandas as pd 
import os 
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--datafolder",type=str)
args= parser.parse_args() 

new_run=Run.get_context() 


ws=new_run.experiment.workspace 


df= new_run.input_datasets["raw_data"].to_pandas_dataframe()




os.makedirs(args.datafolder,exists=True)
path=os.path.join(args.datafolder,'csv_file')

df.to_csv(path,index=False)

new_run.complete()