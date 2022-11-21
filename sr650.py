import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing



def ssl_continue():
    ssl_advanced = driver.find_element_by_xpath('//*[@id="details-button"]')
    ssl_advanced.click()
    ssl_advanced = driver.find_element_by_xpath('//*[@id="proceed-link"]')
    ssl_advanced.click()
    #time.sleep(8)

def login_bmc(user,passwd,newpasswd):
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login_username"]')))
    loginuser = driver.find_element_by_name('username')
    loginuser.send_keys(user)
    loginpass = driver.find_element_by_name('password')
    loginpass.send_keys(passwd)
    commit = driver.find_element_by_xpath('//*[@id="login_right_submit_btn"]').click()
    time.sleep(6)
    first_changepassword(newpasswd)
    sreach_window = driver.current_window_handle

def first_changepassword(newpasswd):
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="change_password"]')))
    changepassd1 = driver.find_element_by_name('change_password')
    changepassd1.send_keys(newpasswd)
    changepassd_confirm = driver.find_element_by_name('change_password_confirm')
    changepassd_confirm.send_keys(newpasswd)


def close_bmc():
    driver.close()

def poweron():
    poweron_s1 = driver.find_element_by_xpath('//*[@id="powerActionDiv"]/div[2]').click()
    poweron_s2 = driver.find_element_by_xpath('//*[@id="powerActionMenuDiv"]/ul/li[1]/a').click()
    poweron_s3 = driver.find_element_by_xpath('//*[@id="quickActionDiv"]/div[2]/div[2]/button[1]').click()
def raid_edit():
    servercfg = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[7]/a/div[1]/div').click()
    raid_setup = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[7]/ul/li[4]/a/div').click()
    time.sleep(180)
    driver.refresh()
    time.sleep(3)

    edit_mode = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/div/span[2]/font').click()

def disk_Make_drive_unconfigured_good(path):
    disk_mark_1 = driver.find_element_by_xpath(path).click()
    time.sleep(2)
    disk_mark_1_good = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[16]/li/ul/li[17]/span').click()
    time.sleep(5)

def raid5():
    create_vd = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[8]/div[1]/div/div[3]/div/div/span').click()
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[4]/div[1]/div[3]/div[1]/div[1]/div[1]/div/select/option[3]')))
    select_raid5 = driver.find_element_by_xpath('//*[@id="raidlvl"]/option[3]').click()
    select_disk1 = driver.find_element_by_xpath('//*[@id="drive_2"]').click()
    select_disk2 = driver.find_element_by_xpath('//*[@id="drive_1"]').click()
    select_disk3 = driver.find_element_by_xpath('//*[@id="drive_3"]').click()
    select_disk4 = driver.find_element_by_xpath('//*[@id="drive_4"]').click()
    add_mem = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[3]/div[1]/div[3]/div[2]/div/button[1]').click()
    time.sleep(1)
    add_mem_next = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[4]/button[2]').click()
    time.sleep(1)
    add_mem_next_1 = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[3]/button[2]').click()
    time.sleep(1)
    finish_vd = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[3]/button[3]').click()
    time.sleep(10)


def reset_raid():
    cls_raid = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[8]/div[1]/div/div[1]/div[2]/a/span').click()
    cls_raid_1 = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[8]/div[1]/div/div[1]/div[2]/ul/li[1]').click()
    time.sleep(2)
    cls_raid_ok_2 = driver.find_element_by_xpath('//*[@id="clearRAIDCfg"]/div/div/div[3]/button[1]').click()
    time.sleep(5)
    storage_inventory = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[1]/div[2]/div').click()
    time.sleep(2)
    disk_Make_drive_unconfigured_good(path='//*[@id="imm3Content"]/div[8]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[7]/li/span')
    disk_Make_drive_unconfigured_good(path='//*[@id="imm3Content"]/div[8]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[7]/li/span')
    disk_Make_drive_unconfigured_good(path='//*[@id="imm3Content"]/div[8]/div[2]/div/div[2]/div[2]/table/tbody/tr[4]/td[7]/li/span')
    disk_Make_drive_unconfigured_good(path='//*[@id="imm3Content"]/div[8]/div[2]/div/div[2]/div[2]/table/tbody/tr[5]/td[7]/li/span')
    array_cfg = driver.find_element_by_xpath('//*[@id="imm3Content"]/div[1]/div[1]/div[1]/div').click()
    time.sleep(3)
    raid5()

def passwd_value(path,vaule):
    element = driver.find_element_by_xpath(path)
    element.clear()
    time.sleep(1)
    element.send_keys(vaule)

def passwd_policy(passwd_expiration_period,passwd_expiration_warning_period,minimum_passwd_len,
                  minimum_passwd_reuse_cycle,minimum_passwd_change_interval,maximum_number_of_login_failures,lockout_period_after_maxmum_login_failures):
    bmc_configure = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[8]/a').click()
    user_settings = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[8]/ul/li[5]/a').click()
    time.sleep(1)
    global_settings =driver.find_element_by_xpath('//*[@id="createUserSettingsLnk"]/div[2]/div/span[3]').click()
    time.sleep(3)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[1]/div[2]/form/input',vaule=passwd_expiration_period)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[2]/div[2]/form/input',vaule=passwd_expiration_warning_period)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[3]/div[2]/form/input',vaule=minimum_passwd_len)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[4]/div[2]/form/input',vaule=minimum_passwd_reuse_cycle)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[5]/div[2]/form/input',vaule=minimum_passwd_change_interval)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[6]/div[2]/form/input',vaule=maximum_number_of_login_failures)
    passwd_value(path='//*[@id="global_setting"]/div[3]/div/div[2]/div[2]/div[8]/div[2]/form/input',vaule=lockout_period_after_maxmum_login_failures)
    first_change_passwd = driver.find_element_by_xpath('//*[@id="pwdForceChange"]').click()
    change_default_passwd = driver.find_element_by_xpath('//*[@id="pwdChangedNextLogin"]').click()
    passwd_required = driver.find_element_by_xpath('//*[@id="pwdComplexRequired"]').click()
    passwd_ok = driver.find_element_by_xpath('//*[@id="global_setting"]/div[4]/div/button[1]').click()
    time.sleep(3)

def bootwithPXE():
    servercfg = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[7]/a/div[1]/div').click()
    boot_option = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[7]/ul/li[2]/a/div').click()
    time.sleep(3)
    pxe_boot = driver.find_element_by_xpath('//*[@id="selTest"]/option[1]').click()
    #restart_select = driver.find_element_by_xpath('//*[@id="OneTimeBoot"]/div[4]/div[2]/div[2]').click()
    pxe_boot_ok = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[1]/div[2]/div[1]/div[4]/div[3]/button[1]').click()
    time.sleep(2)
    restart_ok = driver.find_element_by_xpath('//*[@id="confirmBootDev"]/div/div/div[2]/button[1]').click()
    time.sleep(1)
    restart_ok_1 = driver.find_element_by_xpath('//*[@id="deviceResult"]/div/div/div[2]/button').click()

def bmc_init(url):
    print("msg %s is running" % url )
    ssl_continue()
    login_bmc(user=default_user,passwd=default_passwd,newpasswd=change_passwd)
    #poweron()
    #passwd_policy(passwd_expiration_period=0,passwd_expiration_warning_period=0,minimum_passwd_len=10,
    #              minimum_passwd_reuse_cycle=0,minimum_passwd_change_interval=0,maximum_number_of_login_failures=0,lockout_period_after_maxmum_login_failures=0)
    #raid_edit()
    #reset_raid()
    #bootwithPXE()
    close_bmc()

if __name__ == "__main__":
    default_user = 'USERID'
    default_passwd = 'PASSW0RD'
    change_passwd = '8VrtFY16ic'

    df = pd.read_excel('./ip.xlsx',sheet_name='Sheet1',header=0)
    for index,row in df.iterrows():
        url = 'https://' + row['ip']
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        bmc_init(url)
