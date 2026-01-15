from gmaillib import get_gmail_service, build_message, send_message

service = get_gmail_service()
sender = 'James Kirk <testuser3@hua.gr>'
recipient = 'thkam@hua.gr'
body_html = """
<p> This is me! </p>
"""
subject = 'Test2'
message = build_message(sender, recipient , subject, body_html)
draft = send_message(service, message)