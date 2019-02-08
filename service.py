from flask import Flask , request
import yagmail,sys


app= Flask(__name__)
# username,password passed as command line arguments
yag = yagmail.SMTP(sys.argv[1], sys.argv[2])

@app.route('/email', methods=['POST'])
def sendEmail():

    receiver = request.json["receiver"]
    print("receiver: "+receiver)
    body = request.json["body"]
    print("body: "+body)
    subject = request.json["subject"]
    print("subject: "+subject)
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
    )

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')