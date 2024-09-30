from  flask import Flask,render_template,request
from matplotlib import widgets
from wtforms import Form,StringField,validators,IntegerField,DateTimeField,PasswordField,SelectField

app=Flask(__name__)

class RegistrationForm(Form):
    Uname = StringField("Name", validators=[validators.input_required(),validators.Length(min=4, max=20)])
    Upassword = PasswordField("password", validators=[validators.input_required(),validators.Length(min=4, max=20)])
    Ugender = SelectField("Gender", validators=[validators.input_required()], choices=[(1,"male"), (2,"female"), (3,"other")])
    Udob = DateTimeField("Date of birth", validators=[validators.Optional()], format='%y-%m-%d')
    Uphone = IntegerField("phone", validators=[validators.input_required(),validators.length(min=6000000000, max=10000000000)])


@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        print(form.Uname.data)
        print(type(form.Uphone.data))
        print(type(form.Udob.data))
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)