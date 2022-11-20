#coding:gbk
import time
import smtplib
import schedule
import requests
import random
from email.mime.text import MIMEText
from  email.header import Header
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from holidays import festival
from bs4 import BeautifulSoup


domain_account = 'xin.zhou'
domain_password = '3edc$RFV'
mail_account = 'xin.zhou@gigadevice.com'


def festival():
    url='https://wannianrili.bmcx.com/'

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    res = requests.get(url, headers=headers)
    bs_res = BeautifulSoup(res.text,'html.parser')

    dates = bs_res.find_all('div',class_='wnrl_riqi')

    holiday_list = []
    for date in dates:
        day = date.find(class_='wnrl_td_gl')
        day_mo = date.find('a',class_='wnrl_riqi_mo')
        day_xiu = date.find('a',class_='wnrl_riqi_xiu')
        #print(day_mo)
        if (day_mo or day_xiu):
            #print(type(day.text))
            holiday_list.append(day.text)
            #print(day.text)
            #print('休假')
    today = time.strftime('%d')
    #print(today)
    #print(holiday_list)
    return today,holiday_list

def get_attendance():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--headless')


    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    #return driver

    driver.get('https://172.21.5.26/')
    time.sleep(8)

    loguser = driver.find_element_by_name('username')
    loguser.send_keys(domain_account)

    logpass = driver.find_element_by_name('password')
    logpass.send_keys(domain_password)

    log_buttion = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/form/div/div[4]/div/button')
    log_buttion.click()
    time.sleep(3)

    #driver.maximize_window()
    #点击签到签退
    attendance = driver.find_element_by_class_name('punch')
    attendance.click()
    time.sleep(2)
    #更新打卡时间
    clock_in = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div/button')
    clock_in.click()
    time.sleep(2)

    #打卡
    #try:
    #    clock_in = driver.find_element_by_class_name('signBtnPanel').find_element_by_name('signBtn')
    #    clock_in.click()
    #    time.sleep(5)
    #except:

    #    #更新打卡时间
    #    clock_in = driver.find_element_by_class_name('resign')
    #    clock_in.click()
    #   time.sleep(3)

    #打卡时间
    HTML = driver.page_source
    bs_HTML = BeautifulSoup(HTML,'html.parser')

    #打卡日期
    #attendance_date = bs_HTML.find('div',class_='ant-popover-title')
    #print(attendance_date.text)
    attendance_times = bs_HTML.find_all(class_='right-inner')
    attendance_list =[]
    for attendance_time in attendance_times:
        attendance_list.append(attendance_time.text)

    #print(attendance_time.text)
    return attendance_list
    time.sleep(2)

    driver.close()
def sendmail(date,time,sender,pwd,recevier):
    mailhost = 'mail.gigadevice.com'

    gdmail = smtplib.SMTP(mailhost,25)
    #gdmail.connect(mailhost, 25)
    gdmail.starttls()



    gdmail.login(sender, pwd)

    content = '时间：\n'+date+'\n'+'\n'.join(time)
    message = MIMEText(content, 'plain', 'utf-8')
    subject = 'Hello Gd'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        gdmail.sendmail(sender, recevier, message.as_string())
        return True
    except:
        return False
    gdmail.quit()

def job():
    print('开始第一次发送任务')
    date,time = get_attendance()
    IsSuccess = sendmail(date,time,sender=mail_account,pwd=domain_password,recevier=mail_account)
    while IsSuccess is False:
        print('发送邮件失败，正在尝试重新发送')
        IsSuccess = sendmail(date, time, sender=mail_account, pwd=domain_password,
                             recevier=mail_account)
        print('任务完成')

today,holidays_list = festival()
if today  not  in holidays_list:
    #print(today,holidays_list)
    t = random.randint(20,200)
    #t = random.randint(1,10)
    time.sleep(t)
    job()
    #get_attendance()
    #schedule.every().days.at('07:55').do(job)
    #schedule.every().days.at('17:05').do(job)
