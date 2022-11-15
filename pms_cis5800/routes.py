from app import app
from flask import render_template

import forms

@app.route('/')



@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/packages', methods = ['GET', 'POST'])
def packages():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Entry Submitted', form.title.data)
    return render_template('packages.html', form = form)



@app.route('/maintenance', methods = ['GET', 'POST'])
def maintenance():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Request Submitted', form.title.data)
        return render_template('maintenance.html', form=form, title=form.title.data)
    return render_template('maintenance.html', form=form)



@app.route('/directory')
def directory():
    return render_template('directory.html')