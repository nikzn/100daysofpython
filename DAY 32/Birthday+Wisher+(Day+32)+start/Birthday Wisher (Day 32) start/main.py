import random
import smtplib
import datetime as dt
import pandas


birthday_data=pandas.read_csv('birthday/Birthday.csv')
template_one_data=pandas.read_csv('birthday/template/Friend-birthday-Template.txt')
template_two_data=pandas.read_csv('birthday/template/Family-birthday.txt')
template_three_data=pandas.read_csv('birthday/template/collegue-birthday-template.txt')
template=[template_one_data,template_two_data,template_three_data]
data=random.choice(template)
send_template=data.to_string()


now=dt.datetime.now()
day=now.day
month=now.month
MY_EMAIL='nikhilchandrapegasusone@gmail.com'
PASSWORD='zgmnlqilvsbnhfqb'



birthday_dict=birthday_data.to_dict(orient='index')
birthday_list=[data for (index,data) in birthday_dict.items() if data['Month']==month and data['Day']==day]
if birthday_list:
    for list in birthday_list:
        personalised_message=send_template.replace('[Name]',list['Name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=list['mail'],
                msg=f"Subject:Happy Birthday {list['Name']} \n\n  {personalised_message} "
            )




