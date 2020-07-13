# __author__ = 'Rakesh Kumar Gupta'

from flask import Flask, render_template
from flask_mail import Mail, Message

# Credential Detail
mail_user_name = "foodeebotraka@gmail.com"
mail_password = "QAZX@100"

# Reciever
receiver_trishala_mail = "trishla.singh0035@gmail.com"
receiver_raka_mail = "raka0006184@gmail.com"

# Initialize the app.
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=mail_user_name,
    MAIL_PASSWORD=mail_password,
    MAIL_DEBUG=True
)
mail = Mail(app)


@app.route("/")
def send():
    msg = Message("Hi! Welcome to Flask Mail!", sender=mail_user_name,
                  recipients=[receiver_raka_mail])
    msg.body = "This is the email body"
    mail.send(msg)
    print("Mail sent")
    # return "Please check you email,Sent"
    return render_template("send_mail.html")


@app.route("/images")
def send_image_body():
    msg = Message("Hi! Welcome to Flask Mail!", sender=mail_user_name,
                  recipients=[receiver_trishala_mail])

    with app.open_resource("s2.jpg") as fp:
        msg.attach("s2.jpg", "image/jpg", fp.read())

    with app.open_resource("s3.jpg") as fp:
        msg.attach("s3.jpg", "image/jpg", fp.read())

    msg.body = "This is the email body  working"

    msg.html = """   

    <!DOCTYPE html>
    <html>
    <head>
        <title>Email Template</title>
        <link href="https://drive.google.com/file/d/0B6wwyazyzml-OGQ3VUo0Z2thdmc/view" rel="stylesheet">
        <style>
            .paragraph{
        font-family: 'Niramit', sans-serif;
        font-style: 50px

    }
    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }

    .button3 {background-color: #f44336;} /* Red */ 

        </style>

    </head>
    <body style="margin: 0; ">

        <table align="center" border="0" cellpadding="20" cellspacing="0" >
            <tr><td>
        <table align="center" border="0" cellspacing="0" width="300">
                
                <tr>
                    <td align="center">
                    <p class="paragraph">“1st image : Beautiful” </p>
                    </td>
                </tr>
                
                <tr>
                    <td align="center">
                    <p class="paragraph">“2nd image : So Cute” </p>
                    </td>
                </tr>
        </tr>
        </td>
    </tr>
    </table>
    </table>
    </body>
    </html>

    """

    mail.send(msg)
    print("Mail sent")
    # return "Sent"
    return render_template("send_mail.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


#
# @app.route("/")
# def send():
#     msg = Message("Hi! Welcome to Flask Mail!", sender=mail_user_name, recipients=[sender_mail, sender_trishala_mail])
#     msg.body = "Message from Bot"
#     mail.send(msg)
#     print("Mail sent")
#     # return "Please check you email,Sent"
#     return render_template("send_mail.html")


if __name__ == "__main__":
    app.run(port=2000, debug=True)
