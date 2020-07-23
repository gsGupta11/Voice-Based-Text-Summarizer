import smtplib 

def sendMail(message):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("gaurigsg9999@gmail.com", "password") 
        s.sendmail("gaurigsg9999@gmail.com", "gaurigsg9999@gmail.com", message) 
        s.quit()
        return "Mail Sent Successfully"
    except:
        return "Some Problem Occurred"