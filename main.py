from flask import *
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='suganyav459@gmail.com'
app.config['MAIL_PASSWORD']='9597300361'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

users=[{'name':'sudhakutty','email':'sudhagarsvs232@gmail.com'},{'name':'sudha','email':'sudhagarsvs2332@gmail.com'},{'name':'sugan','email':'suganyav459@gmail.com'}]
mail=Mail(app)

@app.route('/')
def index():
    print("connection strated")

    with mail.connect() as conn:

        for user in users:
            msg='Hello%s'%user['name']

            msgs=Message(recipients=[user['email']],body=msg,subject='hellow',sender='suganyav459@gmail.com')

            with app.open_resource("S:/coding/html/wp2153319.jpg") as fp:
                msgs.attach("wp2153319.jpg","image/png",fp.read())

            conn.send(msgs)

    return "<h2>Email has been sent to all the given mail id's</h2>"

if __name__=="__main__":
    app.run(debug=True)


