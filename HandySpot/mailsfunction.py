import smtplib

def email_sender(to_,sub_,mesz_,from_,pass_):
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(from_,pass_)
    mesz="Subject: {}\n\n{}".format(sub_,mesz_)
    s.sendmail(from_,to_,mesz)
    x = s.ehlo()
    if x[0]==250:
        return "s"
    else:
        return "f"
    s.close()
