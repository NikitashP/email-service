### Email service

- runs on port 5000
- python-flask application
- uses yagmail to send out emails
- email id and password can be given as arguments
during application startup. check docker file.


#### request
````text
curl -X POST \
  http://127.0.0.1:5000/email \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: abcdef123456' \
  -d '{
	"receiver":"xxx@gmail.com",
	"body":"test email",
	"subject":"hello!"
}'
```` 