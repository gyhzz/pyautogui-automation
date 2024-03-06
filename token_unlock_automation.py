import pyautogui
import time
import random
from data import token_unlock_coordinates


def reset_unlock_task(coordinates: dict) -> None:

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

    pyautogui.click(coordinates['main_blank'])
    time.sleep(1)
    pyautogui.click(coordinates['main_blank'])
    time.sleep(1)
    for i in range(11):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(coordinates['mm_blank'])
    pyautogui.scroll(1000)

    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('1')
    
    pyautogui.scroll(-1000)
    time.sleep(3)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(3)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(20)


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


def main() -> None:

    token_positions = {1: (2680, 396), 2: (2680, 466), 3: (2680, 536), 4: (2680, 606)}
    current_token = 1
    count = 0

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
            wait_time = random.randint(1, 3600)

            print(f"Log - Waiting for {wait_time} seconds")

            time.sleep(wait_time)


if __name__ == "__main__":

    coordinates = token_unlock_coordinates

    # Test coordinates
    test_coords(coordinates)

    main()
