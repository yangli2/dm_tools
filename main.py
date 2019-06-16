from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
  name = StringField('Name:', validators=[validators.data_required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
  form = ReusableForm(request.form)
  if request.method == 'POST':
    if form.validate():
      name = request.form['name']
      flash('Hello ' + name)
    else:
      flash('All the form fields are required. ')

  return render_template('hello.html', form=form)


if __name__ == "__main__":
  app.run()
