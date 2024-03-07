'''
This module contains coordinates and data for the automation scripts
'''

mail_data = {
    'email_addresses': {
        'group_1': [
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
        ],
        'group_2': [
            'queries98kj@business.com', 
            'updates45gv@service.net', 
            'notifications32xz@platform.org',
            'responses76yh@community.edu', 
            'inquiries24fd@info.co', 
            'feedback60pl@responses.com',
            'subscriptions22kd@newsletters.net', 
            'accounts33kl@finance.org', 
            'assistance88mn@help.co',
            'orders99op@purchases.com', 
            'returns77qr@ecommerce.net', 
            'shipping44ws@logistics.org',
            'events66nt@invites.co', 
            'training55pr@education.com', 
            'projects44dw@collaborations.net',
            'research22ba@studies.org', 
            'development77vc@innovation.co', 
            'partners33rf@ventures.com',
            'solutions99sg@tech.net', 
            'career66nd@opportunities.org'
        ]
    },
    'subjects': {
        'group_1': [
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
        ],
        'group_2': [
            'Your Inquiry Has Been Received', 
            'Weekly Update: Latest Trends', 
            'Notification of Service Change',
            'Response to Your Recent Query', 
            'Thank You for Your Inquiry', 
            'We Value Your Feedback',
            'Your Subscription Has Been Confirmed', 
            'Account Statement Update', 
            'How May We Assist You Further?',
            'Confirmation of Your Order', 
            'Return Process Initiated', 
            'Shipping Update on Your Order',
            'Exclusive Event Invitation', 
            'Upcoming Training Sessions', 
            'New Project Announcements',
            'Latest Research Findings', 
            'Innovation in Development', 
            'New Partnership Opportunities',
            'Tech Solutions for Your Business', 
            'Join Our Growing Team'
        ]
    },
    'bodies': {
        'group_1': [
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
        ],
        'group_2': [
            "We've received your inquiry and our team will get back to you shortly.",
            "Stay updated with the latest trends in our weekly roundup.",
            "We're making some changes to our service. Here's what you need to know.",
            "Here's the response to your recent query. Let us know if you have further questions.",
            "Thank you for reaching out to us. We're here to assist you with your needs.",
            "Your feedback is crucial for us. Let us know how we can serve you better.",
            "Thank you for subscribing to our newsletter. Stay tuned for more updates.",
            "Here's your latest account statement. Review your transactions at your convenience.",
            "Our support team is ready to assist you. How can we help you today?",
            "Your order has been confirmed. Thank you for shopping with us.",
            "We've initiated the return process for your order. Here's what to expect next.",
            "Your order is on its way. Track the shipping details inside.",
            "You're invited to our exclusive event. Secure your spot today.",
            "Join our upcoming training sessions to enhance your skills.",
            "We're excited to announce new projects. Discover collaboration opportunities.",
            "Check out our latest research findings in the attached document.",
            "Discover the innovation happening in development. Read more inside.",
            "Explore new partnership opportunities with us. Let's create something great together.",
            "Find out how our tech solutions can transform your business.",
            "We're hiring! Explore career opportunities with us and join our team."
        ]
    }
}

# networks = {
#     'networks':{
#     1: (3000, 357),
#     2: (3000, 385),
#     3: (3000, 412),
#     4: (3000, 440),
#     5: (3000, 467),
#     6: (3000, 495),
#     7: (3000, 522),
#     8: (3000, 550),
#     9: (3000, 577),
#     10: (3000, 605),
#     11: (3000, 632),
#     12: (3000, 660),
#     13: (3000, 687),
#     14: (3000, 715)
#     }
# }

networks = {
    1: (3000, 357),
    3: (3000, 412),
    4: (3000, 440),
    6: (3000, 495),
    7: (3000, 522),
    8: (3000, 550),
    9: (3000, 577)
}

dmail_coordinates = {
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
        'mm_approve': (3350, 560),
        'mm_network_agree': (3282, 532),
        'change_network': (3050, 765),
        'networks': networks
    }

dmail_networks = {
    1: 'Ethereum',
    2: 'BNB',
    3: 'zkSync',
    4: 'Linea',
    5: 'opBNB',
    6: 'Manta',
    7: 'Scroll',
    8: 'Base',
    9: 'ZKFair',
    10: 'ZetaChain',
    11: 'Polygon',
    12: 'KCC',
    13: 'Conflux',
    14: 'IoTeX'
}

token_unlock_coordinates = {'token_top': (2854, 322),
                   'token_bottom': (2854, 482),
                   'main_tab': (1994, 20),
                   'main_blank': (2118, 359),
                   'main_unlock': (2680, 716),
                   'main_safe': (2680, 660),
                   'mm_taskbar': (3086, 841),
                   'mm_reject': (3194, 561),
                   'mm_blank': (3300, 60),
                   'mm_approve': (3353, 559),
                   'token_1_reset_usdc': (2600, 228),
                   'token_2_reset_eth': (2507, 230),
                   'token_positions': {1: (2680, 396),
                                       2: (2680, 466),
                                       3: (2680, 536),
                                       4: (2680, 606)}
    }


# Test coordinates using the below code

if __name__ == '__main__':

    import pyautogui
    import time 


    def test_coordinates(coordinates: dict) -> None:

        print('Log - Testing coordinates...')

        for k,v in coordinates.items():

            if type(v) != type(dict()):
                time.sleep(0.3)
                pyautogui.moveTo(v)
            else:
                for k1,v1 in v.items():
                    time.sleep(0.3)
                    pyautogui.moveTo(v1)


    time.sleep(3)
    print(pyautogui.position())

    #test_coordinates(dmail_coordinates)

    # time.sleep(3)
    # pyautogui.moveTo((2680, 716))
    # time.sleep(1)
    # pyautogui.moveTo((2680, 659))

    # # Token unlock top token position (low): (2850, 322)
    # # Token unlock bottom token position (low): (2850, 482)
    # time.sleep(3)
    # pyautogui.moveTo((2850, 322))
    # time.sleep(1)
    # pyautogui.moveTo((2850, 482))

    # # Token unlock top token position (high): (2850, 222)
    # # Token unlock bottom token position (high): (2850, 380)
    # time.sleep(3)
    # pyautogui.moveTo((2850, 222))
    # time.sleep(1)
    # pyautogui.moveTo((2850, 380))
