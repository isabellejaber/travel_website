from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/nyc', methods = ["GET", "POST"])
def nyc():
    if request.method == "GET": 
        return render_template('nyc.html')
    else:
        user = formopener.dict_from(request.form)
        activity = (user["activity"]).decode('utf-8')
        walking = (user["walking"]).decode('utf-8')
        crowds = (user["crowds"]).decode('utf-8')
        activity_generator = model.nyc_activity(activity, walking, crowds)
        print(activity_generator)
        return render_template('nyc.html', activity_generator = activity_generator)