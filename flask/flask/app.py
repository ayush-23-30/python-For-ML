from flask import Flask, render_template

'''
it creates an instance of the flask class, which will be your WSGi application
'''


'''
@app.route('router') after that function which we need to run; 

start the server every time to show changes ; if we need to automate it then use app.name(debug = True)

'''

'''
integrating Html file 
1. we can direct use <html> <p> hello i am hmtl </p> </html> 
2. we can create a seperate file and then call it -> by using render_template 
this render works with the jinja 2 ---- it go to template folder and then find and search it 
'''

app = Flask(__name__); ## instance of flask class

## creating a basic route 

@app.route('/') ## first  parameter router ; 2nd method [get,post] by-default = GET 
## niche vala run hoga jo likha hoga function
def welcome():
  return 'Welcome to my home page '
@app.route('/index')
def secondPage():
   return '<html> <h1> HELLO MY HTML </h1> </html>'

@app.route('/html')
def html():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')


if __name__=="__main__": ## entry point of app exceution start from here 
  app.run(debug=True) ## running flask interface







