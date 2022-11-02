from flask import Flask,render_template,redirect,url_for,request
import pickle
import os
from google.cloud import pubsub_v1
import json 
from google.cloud import aiplatform
import joblib
import warnings
from datetime import datetime
warnings.filterwarnings("ignore")

app=Flask(__name__)

#credentials_path="C:\\Users\\krishna\\Downloads\\secondproject-336202-5dd850bd4198.json"
credentials_path="news-scrapping-334015-f39648c917d2.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credentials_path
'''
PROJECT_ID = 'secondproject-336202'         # <---CHANGE THIS
REGION = 'us-central1'                 # <---CHANGE THIS
PIPELINE_ROOT = 'gs://vikasbucketnews/vertexai/hello_world_scheduled_pipeline.json'   # <---CHANGE THIS
#pipeline_spec_uri= 'gs://vikasbucketnews/vertexai/hello_world_scheduled_pipeline.json'
'''

publisher=pubsub_v1.PublisherClient()
topic_path='projects/news-scrapping-334015/topics/accion-topic'
# projects/news-scrapping-334015/topics/function-topic

@app.route("/",methods=['GET','POST'])
@app.route("/urlsubmit",methods=['GET','POST'])
def process_request():
	if request.method=='POST':
		print('Reached here...................')
		key = datetime.now().strftime('%Y%m%d%H%M%S')
		data=request.form['url']+'@#@'+key
		data=data.encode('utf-8')
		print(data)
		future=publisher.publish(topic_path,data)
	return render_template('test_sample_2.html')
{'sports': 4,
 'local-stories': 5,
 'business': 0,
 'entertainment': 1,
 'international-news': 2,
 'science': 3,
 'politics': 6,
 'marketing': 7,
 'information-technology': 8,
 'arts': 9,
 'social-issues': 10}

@app.route("/predict",methods=['GET','POST'])
def predict():
	if request.method=='POST':
		data=request.form['input_text']
		data=data.encode('utf-8')
		data=str(data)
		content = joblib.load('cvtransform')
		final_vector=content.transform([data])
		'''with open('newsmodel.pkl', 'rb') as pickle_file1:
			model=pickle.load(pickle_file1)
			output=model.predict(final_vector)'''
		model=joblib.load('newsjob')
		output=model.predict(final_vector)
		if output==4:
			final='sports'
		elif output==5:
			final='local-stories'
		elif output==0:
			final='business'
		elif output==1:
			final='entertainment'
		elif output==2:
			final='international-news'
		elif output==3:
			final='science'
		elif output==6:
			final='politics'
		elif output==8:
			final='information-technology'
		elif output==7:
			final='marketing'
		elif output==9:
			final='arts'
		else:
			final='social-issues'
		return render_template('test_sample_3.html',final=final)
	return render_template('test_sample_3.html')


if __name__=='__main__':
	app.run()

