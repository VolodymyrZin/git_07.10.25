
import pytest
import logging

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logging.info(log_message)
    elif status == "expired":
        logging.warning(log_message)
    else:
        logging.error(log_message)

@pytest.mark.parametrize("username, status", [
    ('admin', 'success'),
    ('user', 'expired'),
    ('smb', 'failed'),
])
def test_log_event(username: str, status: str):

    log_event(username, status)
    expected_message = f"Login event - Username: {username}, Status: {status}"
    with open("login_system.log", "r") as log_file:
        messages = log_file.readlines()
    assert any(expected_message in message for message in messages)







