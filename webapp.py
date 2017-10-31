from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


def get_state_options(counties):
  options = str( " ")
  for c in counties
    if 
  

@app.route("/")
def render_main():
    return render_template('page1.html')


if __name__=="__main__":
    app.run(debug=False, port=54321)
