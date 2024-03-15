import pyautogui
import time
import random
import csv
import datetime
from data import mail_data, dmail_coordinates, dmail_networks


def log_action(wallet_address: str, action_description: str, wait_time: int) -> None:
    with open('dmail_log.csv', 'a', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        log_writer.writerow([current_date, current_time, wallet_address, action_description, wait_time])

    print("Log - Action logged to dmail_log.csv")


def reset_task(coordinates: dict) -> None:
    
    pyautogui.click(coordinates['dmail_logo'])
    time.sleep(0.5)
    pyautogui.click(coordinates['main_blank'])
    time.sleep(0.5)


def change_network(coordinates: dict, current_network: int, force: bool) -> int:

    remaining_networks = list(dmail_coordinates['networks'].keys())
    remaining_networks.remove(current_network)
    select_network = remaining_networks[random.randint(0, len(remaining_networks)-1)]

    if force:
        select_network = 3

    print(f"Log - Selected network {select_network}")

    pyautogui.click(coordinates['change_network'])
    time.sleep(0.5)
    pyautogui.click(coordinates['networks'][select_network])
    time.sleep(7)
    pyautogui.click(coordinates['mm_network_agree'])
    time.sleep(0.5)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(3)
    print(f"Log - Changed network from {current_network} to {select_network}")

    return select_network


def approve_transaction(coordinates: dict, low_gas: bool) -> None:

    pyautogui.click(coordinates['mm_blank'])

    if low_gas:
        # pyautogui.click(coordinates['mm_edit_gas'])
        # time.sleep(0.5)
        # pyautogui.click(coordinates['mm_low_gas'])
        # time.sleep(0.5)

        for i in range(6):
            pyautogui.press('tab')
        pyautogui.press('enter')
        for i in range(5):
            pyautogui.press('tab')
        pyautogui.press('enter')

    pyautogui.scroll(-1000)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(10)


def compose_email(coordinates: dict, recipient: str, subject: str, body: str, current_network: int, switch: bool) -> None:

    pyautogui.click(coordinates['compose'])
    time.sleep(1)

    if switch:
        if current_network != 3 and random.randint(1,100) >= 50:
            current_network = change_network(dmail_coordinates, current_network, True)
        else:
            current_network = change_network(dmail_coordinates, current_network, False)

    pyautogui.click(coordinates['recipient'], clicks=3)
    pyautogui.press('backspace')
    pyautogui.write(recipient)
    time.sleep(0.5)
    pyautogui.click(coordinates['subject'], clicks=3)
    pyautogui.press('backspace')
    pyautogui.write(subject)
    time.sleep(0.5)
    pyautogui.click(coordinates['body'], clicks=3)
    pyautogui.press('backspace')
    pyautogui.write(body)
    time.sleep(0.5)
    pyautogui.click(coordinates['send'])
    time.sleep(7)

    return current_network


def toggle_high_frq() -> bool:

    if random.randint(1, 10) >= 8:
        print('Log - High frequency: ON')
        return True
    else:
        print('Log - High frequency: OFF')
        return False


def test_coordinates(coordinates: dict) -> None:

    print('Log - Testing coordinates...')

    for k,v in coordinates.items():

        if type(v) != type(dict()):
            time.sleep(0.1)
            pyautogui.moveTo(v)
        else:
            for k1,v1 in v.items():
                time.sleep(0.1)
                pyautogui.moveTo(v1)


def launch_dmail_job(wallet: str = "No wallet details", switch: bool = False, low_gas: bool = True) -> None:
    
    test_coordinates(dmail_coordinates)
    reset_task(dmail_coordinates)

    email_addresses = mail_data['email_addresses']['group_1']
    subjects = mail_data['subjects']['group_1']
    bodies = mail_data['bodies']['group_1']

    count = 0
    current_network = 3

    # Ensure the CSV has the headers if the file doesn't exist yet
    try:
        with open('dmail_log.csv', 'x', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow(["Date", "Time", "Wallet Address", "Action Description", "Wait Time"])
    except FileExistsError:
        pass  # File already exists, no need to add headers

    while True:

        print('Log - Begin task')

        high_frq = toggle_high_frq()

        if high_frq:
            execution_count = random.randint(3, 10)
        else:
            execution_count = random.randint(1, 5)

        for i in range(execution_count):

            count += 1
            print(f"Log - Composing email {count}/{execution_count}")

            email_address = email_addresses[random.randint(0, len(email_addresses)-1)]
            subject = subjects[random.randint(0, len(subjects)-1)]
            body = bodies[random.randint(0, len(bodies)-1)]

            current_network = compose_email(dmail_coordinates, email_address, subject, body, current_network, switch)
            approve_transaction(dmail_coordinates, low_gas)

            print(f"Log - Email #{count} sent to {email_address} with subject: {subject} on {dmail_networks[current_network]} network")

            if high_frq:
                wait_time = random.randint(5, 20)
            else:
                wait_time = random.randint(5, 20)

            log_action(wallet, f"Email #{count} sent to {email_address} with subject: {subject} on {dmail_networks[current_network]} network", wait_time)
            print(f'Log - Waiting for {wait_time}')

            time.sleep(wait_time)


if __name__ == '__main__':

    launch_dmail_job()
