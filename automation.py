import pyautogui
import time
import random


'''
Positions
Outside Swap Box: (2118, 359)
Select Token: (2846, 321)
Token 1 Pos: (2680, 396)
Token 2 Pos: (2680, 466)
Token 3 Pos: (2680, 536)
Token 4 Pos: (2680, 606)
Unlock Token: (2687, 704)
Inside MM Box: (3142, 257)
Spending Cap: (3260, 405)
MM Next/Approve: (3353, 559)
'''

token_top = (2845, 288)
token_bottom = (2840, 437)


def reset_unlock_task() -> None:

    pyautogui.click(2118, 359)
    pyautogui.scroll(1000)
    pyautogui.click(token_top)
    time.sleep(1)
    pyautogui.click(2600, 228)
    pyautogui.click(2118, 359)
    time.sleep(1)
    pyautogui.click(token_bottom)
    time.sleep(1)
    pyautogui.click(2507, 230)
    pyautogui.click(2118, 359)
    time.sleep(1)


def perform_unlock_task() -> None:

    pyautogui.click(2118, 359)
    time.sleep(1)
    pyautogui.click(2118, 359)
    time.sleep(1)
    for i in range(11):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.click(3142, 257)
    pyautogui.scroll(1000)

    for i in range(7):
        pyautogui.press('tab')

    pyautogui.press('1')
    
    pyautogui.scroll(-1000)
    time.sleep(3)
    pyautogui.click(3353, 559)
    time.sleep(3)
    pyautogui.click(3353, 559)
    time.sleep(20)


def perform_change_token_task(token_pos: tuple) -> None:

    reset_unlock_task()
    pyautogui.click(token_top)
    time.sleep(1)
    pyautogui.scroll(1000)
    pyautogui.click(token_pos)
    time.sleep(1)
    pyautogui.click(2118, 359)
    for i in range(4):
        pyautogui.press('tab')
    pyautogui.write('1.001')
    pyautogui.click(2118, 359)
    time.sleep(1)


def countdown(seconds: int) -> None:

    for i in range(seconds):
        print(f"Log - Waiting {i+1}/{seconds} seconds")


def main() -> None:

    token_positions = {1: (2680, 396), 2: (2680, 466), 3: (2680, 536), 4: (2680, 606)}
    current_token = 1

    while True:

        # Select random token and update current token with selected token
        token_list = [1, 2, 3, 4]
        current_token = 1
        token_list.remove(current_token)
        select_token = token_list[random.randint(0, 2)]
        current_token = select_token

        print(f"Log - Selected Token {select_token}")

        # Change token on app to selected token
        perform_change_token_task(token_positions[select_token])

        print(f"Log - Changed to token {select_token}")

        # Define number of times to perform token unlock task
        execution_count = random.randint(1, 5)

        print(f"Log - Unlock task will be executed {execution_count} times")

        for i in range(execution_count):

            perform_unlock_task()

            print(f"Log - Unlocked token {select_token} {i+1}/{execution_count} time(s)")

            # Define random wait time between tasks
            wait_time = random.randint(1, 10)

            print(f"Log - Waiting for {wait_time} seconds")

            time.sleep(wait_time)


if __name__ == "__main__":

    main()
    #pass
