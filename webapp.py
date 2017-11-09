from flask import Flask, render_template, request , Markup, flash , Markup
import os 
import json 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('page1.html', states= get_state_options())
@app.route("/answer")
def render_secondtime():
    return render_template('page1.html' , states = get_state_options(), funFact= fun_fact("CA"))
                           
def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    states = []
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
         
    options = ""
    for s in states:
        options+=Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options


def fun_fact(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    first = counties[0]["Miscellaneous"]["Percent Female"]
    for c in counties:
        if c["counties"] in state:
            if c["Miscellaneous"]["Percent Female"]> first:
                first =c["Miscellaneous"]["Percent Female"]
    return str(first)                 

    


if __name__=="__main__":
    app.run(debug=False, port=54321)
