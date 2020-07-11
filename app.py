from flask import Flask, render_template, request
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from sql_util import sql_util
from sql import removeCount,getSongByGenreName
request_list='none'
key='none'
def deleteSession(service,assistant_id,session_id):
    service.delete_session(
        assistant_id = assistant_id,
        session_id = session_id
    )
def getMessage(assistantId,message_input,service,session_id):
    response = service.message(
        assistant_id=assistantId,
        session_id=session_id,
        input = message_input
    ).get_result()

    if response['output']['generic']:
        if response['output']['generic'][0]['response_type'] == 'text':
            return response['output']['generic'][0]['text']
            #print(response['output']['generic'][0]['text'])
app = Flask(__name__)
API_KEY="WdSkDbbrIFUSb-oCDSBKSTb8GDq4NWRHOR22IRmYiM0R"
assistantId='2692f224-dfcb-4466-8c01-7b5bc034f2de'
authenticator = IAMAuthenticator(API_KEY) # replace with API key
service = AssistantV2(
    version = '2019-02-28',
    authenticator = authenticator
)
service.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/4111ff01-75a0-48f1-8eac-1ecb082860d6')
assistant_id =assistantId 
# Create session.
session_id = service.create_session(
    assistant_id = assistant_id
).get_result()['session_id']
message_input = {
    'message_type:': 'text',
    'text': ''
    }
getMessage(assistantId,message_input,service,session_id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    global request_list
    global key
    userText = request.args.get('msg')
    if userText in['movie name','song name','composer name','top songs','singer name','melody','pop','jazz']:
        request_list=userText
    message_input = {
        'text': userText
    }
    if message_input['text'] == 'quit':
        removeCount()
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return "SERVER CLOSED !"
    message=getMessage(assistantId,message_input,service,session_id)
    if "Listing Top Songs !" in message and message_input['text'] != 'quit' and message_input['text'] != 'list songs':
        message='<br>'+'Listing Top Songs'+'<br>'
        message=message+sql_util(request_list,key)
        return message
    if "required Music" in message and message_input['text'] != 'quit':
        if userText=="turn on" or request_list not in['movie name','song name','composer name','top songs','singer name','genre name','melody','pop','jazz']:
            return message
        key=userText
        #key=key[len(key)-1]
        if(sql_util(request_list,key)!='none'):
            if request_list in('melody','pop','jazz'):
                 message=message+"link"+getSongByGenreName(request_list)
            else:
                message=message+"link"+sql_util(request_list,key)        
        else:
            message='The Required Song is not available in database'
    return message
if __name__ == "__main__":
    app.run()