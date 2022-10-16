from flask import Flask, request
import json

# initialize the flask app
app = Flask(__name__)

@app.route('/route')
def route():
  studentID = 200490537
  value = {'StudentID' : studentID}
  return json.dump(value)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  text = 'i have integrated with flask'
  values = {'text':text}
  return json.dump(values)

# run the app
if __name__ == '__main__':
    app.run()
