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
        pic = model.image(activity)
        print(activity_generator)
        return render_template('nyc.html', activity_generator = activity_generator, pic = pic)

@app.route('/rome', methods = ["GET", "POST"])
def rome():
    if request.method == "GET": 
        return render_template('rome.html')
    else:
        user = formopener.dict_from(request.form)
        activity = (user["activity"]).decode('utf-8')
        walking = (user["walking"]).decode('utf-8')
        crowds = (user["crowds"]).decode('utf-8')
        rome_activity_generator = model.rome_activity(activity, walking, crowds)
        pic = model.image(activity)
        print(rome_activity_generator)
        return render_template('rome.html', rome_activity_generator = rome_activity_generator, pic = pic)

@app.route('/brussels', methods = ["GET", "POST"])
def brussels():
    if request.method == "GET": 
        return render_template('brussels.html')
    else:
        user = formopener.dict_from(request.form)
        activity = (user["activity"]).decode('utf-8')
        walking = (user["walking"]).decode('utf-8')
        crowds = (user["crowds"]).decode('utf-8')
        brussels_activity_generator = model.brussels_activity(activity, walking, crowds)
        pic = model.image(activity)
        print(brussels_activity_generator)
        return render_template('brussels.html', brussels_activity_generator = brussels_activity_generator, pic = pic)