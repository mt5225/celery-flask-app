import celery
import os
import salt.client
import json

app = celery.Celery('scalingo-sample')


app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
@app.task
def hello(name):
    return "Hello "+name

@app.task
def ping():
   local = salt.client.LocalClient()
   output = local.cmd_iter('*', 'test.ping')
   ret = []
   for i in output:
      print(i)
      ret.append(i) 
   return json.dumps(ret)
