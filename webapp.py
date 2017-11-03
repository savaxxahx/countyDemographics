from flask import Flask, url_for, render_template, request , Markup, Flash , Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


def get_state_options(counties):
  states = []
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
        
  options = str( " ")
    if s not in states:
       return options+=Markup("<option value=\"" + s + "\">" + s + "</option>")
def fun_fact(states):
   

@app.route("/")
def render_main():
    return render_template('page1.html', options = get_state_options(counties))


if __name__=="__main__":
    app.run(debug=False, port=54321)
