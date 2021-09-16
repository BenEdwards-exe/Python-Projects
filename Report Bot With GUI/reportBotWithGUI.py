import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import PySimpleGUI as sg 
import os.path


def main():
    chromedriver_autoinstaller.install()

    sg.theme("DarkGreen4")

    instructions_column = [
        [
            sg.Text(
                "Instructions:\n"
                "1. Install Google Chrome.\n"
                "2. Create a text file with the name \"acc.txt\".\n"
                "3. Enter the usernames and passwords of the accounts that will\n"
                " do the reporting in \"acc.txt\" in the format username:password\n"
                " e.g. michael_scott:12hqz9\n"
                "4. Enter the path to the folder that contains \"acc.txt\" with\n"
                " the \'Browse\' button.\n"
                "5. Enter internet speed.\n"
                "6. Enter the amount of times each account should report.\n"
                "7. Enter the handle of the account that you want to report.\n"
                "8. Click \'Run\'.\n"
                "9. Give the software time to report/\n"
                )
        ]
    ]

    # For now will only show the name of the file that was chosen
    user_input_column = [
        [
            sg.Text("Folder With Accounts Text File"),
            sg.In(size=(25, 1), enable_events=True, key="-ACCOUNTS FILE-"),
            sg.FolderBrowse()
        ],

        [
            sg.Text("Account To Report"),
            sg.In(size=(25,1), enable_events=True, key="-ACCOUNT TO REPORT-")
        ],

        [
            sg.Text("Internet Speed (value between 0.5(fast) and 3(slow))"),
            sg.In(size=(4, 1), enable_events=True, key="-SPEED-")
        ],

        [
            sg.Text("Reports Per Account"),
            sg.In(size=(4, 1), enable_events=True, key="-REPORTS-")
        ],

        [
            sg.Checkbox("Run in headless mode", enable_events=True, key="-HEADLESS-")
        ],

        [
            sg.ProgressBar(100, orientation='h',size=(40,20), key='bar')
        ],

        [
            sg.Button("RUN")
        ],

        [
            sg.Button("CLOSE")
        ],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(instructions_column),
            sg.VSeperator(),
            sg.Column(user_input_column),
        ]
    ]

    window = sg.Window("Instagram Report Bot", layout, keep_on_top=False)
  
    accounts_path = str()
    account_to_report = str()
    speed = 1.0
    reports = 1


    # Create an event loop
    while True:
        event, values = window.read()

        # End program if user closes window or
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break

        # Folder with fake accounts path entered
        if (event == "-ACCOUNTS FILE-"):
            folder_path = values["-ACCOUNTS FILE-"]
            accounts_path = folder_path + "/acc.txt"

        # Account to report entered
        if (event == "-ACCOUNT TO REPORT-"):
            account_to_report = values["-ACCOUNT TO REPORT-"]
        
        # Speed input received
        if (event == "-SPEED-"):
            speed = float(values["-SPEED-"])

        # Reports per account input
        if (event == "-REPORTS-"):
            reports = int(values["-REPORTS-"])

        # Run Bot
        if (event == "RUN"):
            run_bot(accounts_path, account_to_report, values["-HEADLESS-"], reports, speed, window)

    window.close()

    return

def run_bot(acc_file_path: str, account_to_report: str, isHeadless: bool, reports: int, wait_time: float, window):

    a = open(acc_file_path, "r").readlines()
    file = [s.rstrip()for s in a]
    file.reverse()

    accounts = dict()

    for lines in file:
        file = lines.split(":")

        un = file[0]
        pw = file[1]
        accounts[un] = pw


    reportAccount(accounts, account_to_report, wait_time, isHeadless, reports, window)

    return



def reportAccount(users: dict, acc_to_report: str, wait_time: float, isHeadless: bool, reports: int, window):

    options = Options()
    options.headless = isHeadless

    #progres_bar_current = 0
    #progres_bar_max = len(users)

    #sg.one_line_progress_meter("Progress", 0, progres_bar_max, key='key', orientation='h')
    progress_bar_increments = 100.0 / (float(len(users))*float(reports))
    current_progress = 0.0

    for _ in range(reports):
    
        for key, value in users.items():
            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1920, 1080)

            res = login_and_report(driver, key, value, acc_to_report, wait_time)

            if (res == 1):
                print("Seccessfully reported {} with {}\n".format(acc_to_report, key))
            elif (res == -1):
                print("{} could not be checked".format(key))

            current_progress += progress_bar_increments
            window['bar'].update(current_progress)
                           
            driver.quit()

            #progres_bar_current += 1
            #sg.one_line_progress_meter("Progress", progres_bar_current, progres_bar_max, key='key')

    return


def login_and_report(web_driver: webdriver.Chrome, username: str, password: str, acc_to_report: str, wait_time: float):
    
    web_driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(wait_time)

    username_input_xpath = "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input"
    password_input_xpath = "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input"

    ## Input username
    try: # Try for username input
        WebDriverWait(web_driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, username_input_xpath))
        )
    except:
        print("Username input not found")
        return -1
    username_input_element = web_driver.find_element_by_xpath(username_input_xpath)
    username_input_element.send_keys(username)

    ## Input password
    try: # Try for password input
        WebDriverWait(web_driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, password_input_xpath))
        )
    except:
        print("Password input not found")
        return -1
    password_input_element = web_driver.find_element_by_xpath(password_input_xpath)
    password_input_element.send_keys(password)
    password_input_element.send_keys(Keys.RETURN)

    time.sleep(wait_time)

    ## Save Login Info
    not_now_save_info_xpath = "//*[@id=\"react-root\"]/section/main/div/div/div/div/button"
    is_not_now_save_prompt = bool()
    try:
        WebDriverWait(web_driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, not_now_save_info_xpath))
        )
        is_not_now_save_prompt = True
    except:
        is_not_now_save_prompt = False
    if (is_not_now_save_prompt):
        web_driver.find_element_by_xpath(not_now_save_info_xpath).click()


    ## Go to the page to report
    acc_to_report_url = "https://www.instagram.com/" + acc_to_report
    web_driver.get(acc_to_report_url)

    ## Run reporting process
    report_spam_process_xpath_list = list()
    report_spam_process_xpath_list.append("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[2]/button")
    report_spam_process_xpath_list.append("/html/body/div[5]/div/div/div/div/button[3]")
    report_spam_process_xpath_list.append("/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]")
    report_spam_process_xpath_list.append("/html/body/div[5]/div/div/div/div/div/div/div[2]/button")

    # Loop through process
    for element_path in report_spam_process_xpath_list:
        try:
            WebDriverWait(web_driver, 3.0).until(
                EC.presence_of_all_elements_located((By.XPATH, element_path))
            )
        except:
            return -1
        element_to_click = web_driver.find_element_by_xpath(element_path)
        element_to_click.click()

    ## Log out process
    log_out_process_xpath_list = list()
    log_out_process_xpath_list.append("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
    log_out_process_xpath_list.append("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div/div")

    for element_path in log_out_process_xpath_list:
        try:
            WebDriverWait(web_driver, 3.0).until(
                EC.presence_of_all_elements_located((By.XPATH, element_path))
            )
        except:
            return -1
        element_to_click = web_driver.find_element_by_xpath(element_path)
        element_to_click.click()

    return 1



    
if __name__ == "__main__":
    main()
    pass