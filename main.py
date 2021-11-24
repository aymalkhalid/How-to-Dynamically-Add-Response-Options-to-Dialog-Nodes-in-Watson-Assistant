from flask import Flask,redirect,url_for,render_template,request
from copy import deepcopy
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/index')
@app.route('/')
def index():
        # Handle POST Request heres
    return render_template("index.html")
#Webhook
@app.route('/webhook',methods=['POST'])
def webhook():
    list_foci=request.json['Focus']
    list_size=len(list_foci)
    foci=[
        {
            "label": "Monday 1:00 pm",
            "value": {
                "input": {
                    "text": "Monday 1:00 pm"
                }
            }
        }
    ]
    #size for copying
    copy_size=list_size-1
    for x in range(copy_size):
        foci.append(deepcopy(foci[0]))
    #adding foci values
    for foci_value in range(list_size):
        foci[foci_value]['label']=list_foci[foci_value]
        foci[foci_value]['value']['input']['text']=list_foci[foci_value]
    response={
      "arr": [
        {
          "title": "Wählen Sie das passende Rechtsgebiet:",
          "options": foci,
          "description": "",
          "response_type": "option"
        }
      ]
      }
    return {'statusCode':200,
            'headers':{'Content-Type':'application/json'},
      'body':{"response":response
            }
    }

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)


