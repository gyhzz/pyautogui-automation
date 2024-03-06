import pyautogui
import time
import random
from data import mail_data, dmail_coordinates


def reset_task(coordinates: dict) -> None:
    
    pyautogui.click(coordinates['dmail_logo'])
    time.sleep(0.5)
    pyautogui.click(coordinates['main_blank'])
    time.sleep(0.5)


def approve_transaction(coordinates: dict) -> None:

    pyautogui.click(coordinates['mm_blank'])
    pyautogui.click(coordinates['mm_edit_gas'])
    time.sleep(0.5)
    pyautogui.click(coordinates['mm_low_gas'])
    time.sleep(0.5)
    pyautogui.scroll(-1000)
    time.sleep(0.5)
    pyautogui.click(coordinates['mm_approve'])
    time.sleep(10)


def compose_email(coordinates: dict, recipient: str, subject: str, body: str) -> None:

    pyautogui.click(coordinates['compose'])
    time.sleep(0.5)
    pyautogui.click(coordinates['recipient'])
    pyautogui.write(recipient)
    time.sleep(0.5)
    pyautogui.click(coordinates['subject'])
    pyautogui.write(subject)
    time.sleep(0.5)
    pyautogui.click(coordinates['body'])
    pyautogui.write(body)
    time.sleep(0.5)
    pyautogui.click(coordinates['send'])
    time.sleep(7)


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

        time.sleep(0.5)
        pyautogui.moveTo(v)


def main() -> None:
    
    print('Log - Testing coordinates...')
    test_coordinates(dmail_coordinates)

    count = 0

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

            compose_email(dmail_coordinates, email_address, subject, body)
            approve_transaction(dmail_coordinates)

            print(f"Log - Email #{count} sent to {email_address} with subject: {subject}")

            if high_frq:
                wait_time = random.randint(1, 10)
            else:
                wait_time = random.randint(60, 3600)

            print(f'Waiting for {wait_time}')
            time.sleep(wait_time)


if __name__ == '__main__':

    email_addresses = mail_data['email_addresses']['group_1']
    subjects = mail_data['subjects']['group_1']
    bodies = mail_data['bodies']['group_1']

    main()
