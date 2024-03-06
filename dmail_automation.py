import pyautogui
import time
import random


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
    test_coordinates(coordinates)

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

            compose_email(coordinates, email_address, subject, body)
            approve_transaction(coordinates)

            print(f"Log - Email #{count} sent to {email_address} with subject: {subject}")

            if high_frq:
                wait_time = random.randint(1, 10)
            else:
                wait_time = random.randint(60, 3600)

            print(f'Waiting for {wait_time}')
            time.sleep(wait_time)


if __name__ == '__main__':

    coordinates = {
        'dmail_logo': (2054, 130),
        'main_blank': (1950, 130),
        'inbox': (2030, 261),
        'sent': (2030, 333),
        'compose': (2050, 198),
        'first_email': (2422, 282),
        'reply': (2670, 246),
        'recipient': (2317, 258),
        'subject': (2338, 298),
        'body': (2330, 429),
        'send': (2257, 763),
        'mm_blank': (3330, 210),
        'mm_edit_gas': (3363, 322),
        'mm_low_gas': (3342, 195),
        'mm_approve': (3350, 560)
    }

    email_addresses = [
    'member0hd6k@demo.edu',
    'servicedhk8f@demo.edu',
    'service4jrxr@demo.edu',
    'contactahewb@sample.net',
    'servicebg20u@example.com',
    'info2q1w2@test.org',
    'servicewpskd@test.org',
    'memberl262w@mail.com',
    'service7o2b1@sample.net',
    'memberhys96@mail.com'
    ]

    subjects = [
    'Urgent: Account Verification Required',
    'Welcome to Our Newsletter',
    'Your Order Has Been Shipped',
    'Action Required: Confirm Your Subscription',
    'Thank You for Your Purchase!',
    'Invitation: Exclusive Webinar for Subscribers',
    'Survey: Share Your Feedback With Us',
    'Reminder: Upcoming Payment Due',
    'Special Offer: Limited Time Discount Inside',
    'Important Update Regarding Your Account'
    ]

    bodies = [
    'Dear Customer, we need you to verify your account to continue using our services securely.',
    "Thank you for subscribing to our newsletter. We're excited to bring you weekly updates and insights.",
    "Good news! Your recent order has been dispatched, and it's on its way to you.",
    "Please confirm your subscription by clicking the link below. We're thrilled to have you!",
    "We appreciate your recent purchase. Here's everything you need to know about your order.",
    "Join us for an exclusive webinar where we'll dive deep into the latest industry trends.",
    'Your opinion matters to us. Could you spare a few minutes to fill out our customer satisfaction survey?',
    'This is a friendly reminder about the upcoming payment due on your account. Avoid late fees by paying now.',
    "As a valued customer, we're offering you an exclusive discount. Don't miss out on this limited-time offer!",
    "We've made some important updates to our terms of service. Please review the changes to stay informed."
    ]

    main()
