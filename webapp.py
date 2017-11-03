from flask import Flask, url_for, render_template, request , Markup, Flash , Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


"""def get_state_options(counties):
  states = []
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            
     options = Str("")
    for s in states:
       options+=Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
def fun_fact(states):"""
   

@app.route("/")
def render_main():
    """with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)"""
    return render_template('page1.html', options = str(" "))


if __name__=="__main__":
    app.run(debug=False, port=54321)
