import smtplib, ssl


def Send_email(message):
	port = 465
	sender, password = "kanishkd31100@gmail.com", "Canthrift@24"
	reciever = "kanishkmain@gmail.com"	
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com",port, context = context) as server:
		server.login(sender, password)
		server.sendmail(sender, reciever, message)
		print("Email Sent")

