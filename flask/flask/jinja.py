from flask import Flask, render_template,request

'''
it creates an instance of the flask class, which will be your WSGi application
'''


'''
@app.route('router') after that function which we need to run; 

start the server every time to show changes ; if we need to automate it then use app.name(debug = True)

'''

'''

'''

app = Flask(__name__); ## instance of flask class

## creating a basic route 

@app.route('/',) ## first  parameter router ; 2nd function you want to show ui
## niche vala run hoga jo likha hoga function
def welcome():
  return 'Welcome to my home page '
@app.route('/index',methods = ["GET"])
def secondPage():
   return '<html> <h1> HELLO MY HTML </h1> </html>'

@app.route('/html')
def html():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')


@app.route('/form',methods =['GET','POST'])
def form():
   if request.method == 'POST':
    name = request.form['name']
    return f'Hello {name}!'
    
   return render_template('form.html')

@app.route('/submit',methods =['GET','POST'])
def submmit():
   if request.method == 'POST':
    name = request.form['name']
    return f'Hello {name}!'
    
   return render_template('form.html')


##  params these are params that we passed in url; called variable rule  ... and we can handle it by argument in fncs
# need to type cast the data type  

@app.route('/success/<int:score>')
def success(score):
## dynamic variables  == props passing 
  res = ""
  if int(score) > 50:
    res ="Passed"
  else : res = "failed"
    # return f"The marks you got is {score}" 
  
  exp = {'Score : ', score , "res : "  ,res }
  return render_template('result1.html', results = exp)


      



if __name__=="__main__": ## entry point of app exceution start from here 
  app.run(debug=True) ## running flask interface







