def send(*args, **kwargs):
    print("Library Management: override_email_send hook executed")

def get_sender_details(*args, **kwargs):
    print("Library Management: get_sender_details hook executed")
    return {}