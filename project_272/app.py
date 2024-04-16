# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACb98af3a472c6b47c2e1dd6d3887244b1'
        auth_token = 'SK4bcb72141d8b52a9725aaf44e42d93b6'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('ISb52489b7da52152f1ae19abae5bb343d') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ISb52489b7da52152f1ae19abae5bb343d'
    auth_token = 'SK4bcb72141d8b52a9725aaf44e42d93b6'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('ISb52489b7da52152f1ae19abae5bb343d') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://project-c272.onrender.com/")


if __name__ == "__main__":
    app.run()

