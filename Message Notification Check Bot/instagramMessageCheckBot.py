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
                "3. Enter internet speed.\n"
                "4. Click \'Run\'\n"
                "6. Give the software time to scrape (this may take a while).\n"
                "\n\n\n"
                "Important:\n"
                "- The provided accounts should be in the format \'username:password\'\n"
                " with no new lines between each account\n"
                "- The accounts that received messages will be output to a text file \n"
                " the same directory as the \'acc.txt\' file."
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
            sg.Text("Internet Speed (value between 1(fast) and 3(slow))"),
            sg.In(size=(4, 1), enable_events=True, key="-SPEED-")
        ],

        [
            sg.Checkbox("Run in headless mode", enable_events=True, key="-HEADLESS-")
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

    window = sg.Window("Instagram Message Notification Checking Bot", layout)

    acc_file_path = str()
    acc_with_messages_file_path = str()
    internetSpeed = 2.0
    users = dict()
    users_with_messages = dict()

    # Create an event loop
    while True:
        event, values = window.read()

        # End program if user closes window or
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break

        # Folder name was filled in
        if event == "-ACCOUNTS FILE-":
            folder = values["-ACCOUNTS FILE-"]
            acc_file_path = folder + "/acc.txt"
            acc_with_messages_file_path = folder + "/acc_with_messages.txt"
        
        # Internet speed filled out
        if event == "-SPEED-":
            internetSpeed = values["-SPEED-"]

        if event == "RUN":
            run_bot(acc_file_path, acc_with_messages_file_path, users, users_with_messages, values["-HEADLESS-"], internetSpeed)
            break

    window.close()
    return

def run_bot(acc_file_path: str, acc_with_messages_file_path, users: dict, users_with_messages: dict, isHeadless: bool, wait_time: float):

    a = open(acc_file_path, "r").readlines()
    file = [s.rstrip()for s in a]
    file.reverse()

    for lines in file:
        file = lines.split(":")

        un = file[0]
        pw = file[1]
        users[un] = pw

    checkUsernameDict(users, users_with_messages, 1.5, isHeadless)

    out = open(acc_with_messages_file_path, "w")
    out.write("Accounts that have message notifications:\n")
    out.write("----------------------------------------\n\n")
    for key, value in users_with_messages.items():
        out.write("{}:{}\n".format(key, value))
    out.close()

    return



def checkUsernameDict(users: dict, users_with_messages: dict, wait_time: float, isHeadless: bool):

    options = Options()
    options.headless = isHeadless

    progres_bar_current = 0
    progres_bar_max = len(users)

    sg.one_line_progress_meter("Progress", 0, progres_bar_max, key='key', orientation='h')
    
    for key, value in users.items():

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)

        res = messageCheck(driver, key, value, wait_time)

        if (type(res) == bool):
            if (res):
                users_with_messages[key] = value
        elif (res == -1):
            print("{} could not be checked".format(key))
            
        driver.quit()

        progres_bar_current += 1
        sg.one_line_progress_meter("Progress", progres_bar_current, progres_bar_max, key='key')

    return

# Log in to Instragram and check if a notification has been received
# Return -1 if an element could not be located
# Return True if a message notification exists, else return False
def messageCheck(web_driver: webdriver.Chrome, username: str, password: str, wait_time: float):
    
    web_driver.get("https://www.instagram.com/accounts/login/?hl=en")
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

    time.sleep(wait_time)

    ## Recieve notifications prompt
    not_now__receive_notification_xpath = "/html/body/div[4]/div/div/div/div[3]/button[2]"
    is_not_now_receive_prompt = bool()
    try:
        WebDriverWait(web_driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, not_now__receive_notification_xpath))
        )
        is_not_now_receive_prompt = True
    except:
        is_not_now_receive_prompt = False
    if (is_not_now_receive_prompt):
        web_driver.find_element_by_xpath(not_now__receive_notification_xpath).click()

    ## Check for message notification icon
    message_notification_xpath = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div"
    try:
        WebDriverWait(web_driver, 1).until(
            EC.presence_of_all_elements_located((By.XPATH, message_notification_xpath))
        )
        return True
    except:
        return False
    


if __name__ == "__main__":
    main()
    pass