def sendmail(who,productAdress):

  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText

  me="your email adress" #Insert mail adress here

  fromaddr = me
  toaddr =who
  msg = MIMEMultipart()
  msg['From'] = me
  msg['To'] = toaddr
  msg['Subject'] = "Product Alert"
  
  body = "Product on the following link is available :"+" "+productAdress

  msg.attach(MIMEText(body, 'plain'))
  
  server = smtplib.SMTP('smtp.gmail.com', 587) #Depend on your mail server
  server.starttls()
  server.login(me, "Your password") #Add your email account password
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()