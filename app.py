'''
Created on 4 abr. 2017

@author: jeiglesias
'''
from flask import Flask

app = Flask(__name__)
app.secret_key ='random string'

@app.route('/')
def index():
    return 'hello SF'

if __name__ == '__main__':
    #Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
   #pp.debug = True
   #app.run()