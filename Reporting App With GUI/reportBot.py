import time
from webbot import *
import pyautogui
import argparse
import sys
import PySimpleGUI as sg 
import os.path



# Bot Function
def reportBot(botFilePath, username_to_report, iSpeed):

    speed = float(iSpeed)

    a = open(botFilePath, "r").readlines()
    file = [s.rstrip()for s in a]
    file.reverse()

    user = []
    passw = []
    for lines in file:
        file = lines.split(":")

        un = file[0]
        pw = file[1]
        user.append(un)
        passw.append(pw)

    

    for line in range(len(user)):
        web = Browser(showWindow=True)
        web.go_to("https://www.instagram.com/accounts/login/")
        time.sleep(0.5*speed)

        web.type(user[line], into='Phone number, username, or email')
        time.sleep(0.5*speed)
        web.press(web.Key.TAB)
        time.sleep(0.5*speed)
        web.type(passw[line], into='Password')
        web.press(web.Key.ENTER)

        time.sleep(1.5*speed)
        web.click(text="Not Now")
        time.sleep(0.8*speed)
        web.click(text="Not Now")
        time.sleep(0.5*speed)

        reportPage = "https://www.instagram.com/" + username_to_report.strip() + "/"
        web.go_to(reportPage)

        time.sleep(1.5*speed)

        web.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')

        time.sleep(0.5*speed)

        web.click(text='Report User')

        time.sleep(1.5*speed)

        web.click(xpath="/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]")

        time.sleep(0.5*speed)

        web.click(text='Close')

        time.sleep(0.5*speed)

        web.click(xpath='/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')

        time.sleep(0.5*speed)

        web.click(xpath='/html/body/div[1]/section/main/div/header/section/div[1]/div/button')

        time.sleep(0.5*speed)

        web.click(text='Log Out')

        time.sleep(0.5*speed)

        pyautogui.keyDown('ctrl')
        time.sleep(0.25)
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('w')

    return


def main():
    instructions_column = [
        [
            sg.Text(
                "Instructions:\n"
                "1. Install Google Chrome - the bot will use it to access Instagram.\n"
                "2. Create a text file with the name \"acc.txt\".\n"
                "3. Enter the usernames and passwords of the bot account in the text file.\n"
                "4. The bot accounts should be entered in the following format: \"username:password\"\n"
                "5. Use the browse button to select the folder that the text file is located in.\n"
                "6. Enter the username of the account that you want to report.\n"
                "7. Specify your internet speed (this is because the report bot has to wait for the browser to load).\n"
                "8. Enter how many times each bot account should report (a value between 1 and 10).\n"
                "9. Click \'RUN\'.\n"
                "10. Don't run anything else or click around on your screen. The GUI will\n "
                "    fully close when all the bots are finished running.\n"
                "11. Sit back and enjoy.\n")
        ]
    ]

    # For now will only show the name of the file that was chosen
    user_input_column = [
        [
            sg.Text("Folder With Bot Accounts Text File"),
            sg.In(size=(25, 1), enable_events=True, key="-BOT ACCOUNTS FILE-"),
            sg.FolderBrowse()
        ],

        [
            sg.Text("Username To Report"),
            sg.In(size=(25, 1), enable_events=True, key="-USERNAME TO REPORT-")
        ],

        [
            sg.Text("Internet Speed (value between 1(fast) and 3(slow))"),
            sg.In(size=(4, 1), enable_events=True, key="-SPEED-")
        ],

        [
            sg.Text("Reports Per Bot Account (value between 1 and 10)"),
            sg.In(size=(4, 1), enable_events=True, key="-REPORTS-")
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

    window = sg.Window("Instagram Report Bot", layout)

    botFilePath = ""
    userNameToReport = ""
    internetSpeed = 1
    reportsPerBot = 1


    # Create an event loop
    while True:
        event, values = window.read()

        # End program if user closes window or
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break

        # Folder name was filled in
        if event == "-BOT ACCOUNTS FILE-":
            folder = values["-BOT ACCOUNTS FILE-"]
            botFilePath = folder + "/acc.txt"

        # Username was filled in
        if event == "-USERNAME TO REPORT-":
            userNameToReport = values["-USERNAME TO REPORT-"]
        
        # Internet speed filled out
        if event == "-SPEED-":
            internetSpeed = values["-SPEED-"]

        # Reports per bot filled out
        if event == "-REPORTS-":
            reportsPerBot = values["-REPORTS-"]

        if event == "RUN":
            for n in range(int(reportsPerBot)):
                reportBot(botFilePath, userNameToReport, internetSpeed)
            break

    window.close()
    return


if __name__ == "__main__":
    main()