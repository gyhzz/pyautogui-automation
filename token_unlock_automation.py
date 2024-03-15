import pyautogui
import time
import random
import csv
import datetime
from data import token_unlock_coordinates


def log_action(wallet_address: str, action_description: str, wait_time: int) -> None:
    with open('token_unlock_log.csv', 'a', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_writer.writerow([current_date, current_time, wallet_address, action_description, wait_time])

    print("Log - Action logged to token_unlock_log.csv")


def reset_unlock_task(coordinates: dict) -> None:

    pyautogui.click(coordinates['mm_taskbar'])
    time.sleep(0.5)
    pyautogui.click(coordinates['mm_reject'])
    time.sleep(0.5)
    pyautogui.click(coordinates['main_tab'])
    time.sleep(0.5)
    pyautogui.click(coordinates['main_blank'])
    pyautogui.scroll(1000)
    pyautogui.click(coordinates['token_top'])
    time.sleep(1)
    pyautogui.click(coordinates['token_1_reset_usdc'])
    pyautogui.click(coordinates['main_blank'])
    time.sleep(1)
    pyautogui.click(coordinates['token_bottom'])
    time.sleep(1)
    pyautogui.click(coordinates['token_2_reset_eth'])
    pyautogui.click(coordinates['main_blank'])
    time.sleep(1)


def perform_unlock_task(coordinates: dict) -> None:

    # pyautogui.click(coordinates['main_tab'])
    # time.sleep(1)
    # pyautogui.click(coordinates['main_blank'])
    # time.sleep(1)

    # for i in range(11):
    #     pyautogui.press('tab')
    # pyautogui.press('enter')

    # pyautogui.click(coordinates['main_unlock'])
    # pyautogui.click(coordinates['main_safe'])

    pyautogui.click(coordinates['mm_taskbar'])
    time.sleep(15)
    pyautogui.click(coordinates['main_unlock'])

    time.sleep(12)
    pyautogui.click(coordinates['mm_blank'])
    time.sleep(1)
    pyautogui.scroll(1000)

    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('1')
    time.sleep(0.5)
    pyautogui.scroll(-1000)
    time.sleep(3)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(3)
    pyautogui.click(coordinates['mm_approve'])
    print("Note - Action has not been locked yet, please wait for action logged message")
    time.sleep(20)
    pyautogui.click(coordinates['main_blank'])


def perform_change_token_task(coordinates: dict, select_token: 1) -> None:

    reset_unlock_task(coordinates)

    pyautogui.click(coordinates['token_top'])
    time.sleep(1)
    pyautogui.scroll(1000)
    pyautogui.click(coordinates['token_positions'][select_token])
    time.sleep(1)
    pyautogui.click(coordinates['main_blank'])

    for i in range(4):
        pyautogui.press('tab')
        
    pyautogui.write('1.001')
    pyautogui.click(coordinates['main_blank'])
    time.sleep(1)


def countdown(seconds: int) -> None:

    for i in range(seconds):
        print(f"Log - Waiting {i+1}/{seconds} seconds")


def test_coords(coordinates: dict) -> None:

    for k,v in coordinates.items():
        if type(v) != type(dict()):
            time.sleep(0.1)
            pyautogui.moveTo(v)

        else:
            for k1,v1 in v.items():
                time.sleep(0.1)
                pyautogui.moveTo(v1)


def launch_unlock_job(wallet: str = "No wallet details", wait_max: int = 10) -> None:

    coordinates = token_unlock_coordinates

    test_coords(coordinates)

    current_token = 1
    count = 0

    # Ensure the CSV has the headers if the file doesn't exist yet
    try:
        with open('token_unlock_log.csv', 'x', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow(["Date", "Time", "Wallet Address", "Action Description", "Wait Time"])
    except FileExistsError:
        pass  # File already exists, no need to add headers

    # Give a few seconds of buffer before starting
    time.sleep(5)

    while True:

        # Select random token and update current token with selected token
        token_list = [1, 2, 3, 4]
        token_list.remove(current_token)
        select_token = token_list[random.randint(0, 2)]
        current_token = select_token

        print(f"Log - Selected Token {select_token}")

        # Change token on app to selected token
        perform_change_token_task(coordinates, select_token)

        print(f"Log - Changed to token {select_token}")

        # Define number of times to perform token unlock task
        execution_count = random.randint(1, 5)

        print(f"Log - Unlock task will be executed {execution_count} times")

        for i in range(execution_count):

            count += 1
            print(f"Log - Performing transaction {count}")

            perform_unlock_task(coordinates)

            print(f"Log - Unlocked token {select_token} {i+1}/{execution_count} time(s)")

            # Define random wait time between tasks
            wait_time = random.randint(1, wait_max)

            log_action(wallet, f"Unlocked token {select_token} {i+1}/{execution_count} time(s)", wait_time)
            print(f"Log - Waiting for {wait_time} seconds")

            time.sleep(wait_time)


if __name__ == "__main__":

    launch_unlock_job()
