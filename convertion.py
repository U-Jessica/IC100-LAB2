import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
#QUESTION1
    a=int(jsonObj['a'])
    temp=a
    add=0
    n=len(str(a))

    while (temp!=0):
        new=temp%10
        temp=temp//10
        add=add+(new**n)
    if(add==a):
        response+="<b> It is an amstrong number</b><br>"
    else:
        response+="<b> It is not an amstrong number</b><br>" 
#QUESTION2
    age=int(jsonObj['age'])
    ms=int(jsonObj['ms'])
    c=int(jsonObj['c'])
    if(ms==0)or(ms==1 and age>45 and c>=2)or(ms==1 and age>35 and c>=1):
    	response+="<b> You got the insurance</b><br>"	
    else:
    	response+="<b> You cant get the insurance</b><br>"
#QUESTION3
    k=int(jsonObj['k'])
   
    if (k|1 == k):
    	response+="<b> Its an odd number</b><br>"	
    else:
    	response+="<b> Its an even number</b><br>"
#QUESTION4
    y=int(jsonObj['y'])
    if(y%4==0):
        if(y%100==0):
            if(y%400==0):
                response+="<b> It is leap year</b><br>"	
            else:
                response+="<b> It is not leap year</b><br>"	
        else:
            response+="<b> It is leap year</b><br>"	
    else:
        response+="<b> It is not leap year</b><br>" 	
	 	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
