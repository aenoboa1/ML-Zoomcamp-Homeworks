
from flask import Flask

app = Flask('ping')

# add a decorator allows extra functionality to the functions.
# allows them to serve a web service

@app.route('/ping',methods=['GET'])
def ping():
    return "PONG"


if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=9696)