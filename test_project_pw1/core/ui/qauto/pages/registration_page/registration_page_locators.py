class RegistrationPageLocators:

    # css selectors
    user_name  = '#signupName'
    last_name = '#signupLastName'
    email = '#signupEmail'
    user_pwd ='#signupPassword'
    user_reenter_pwd ='#signupRepeatPassword'
    registering_button = "//button[@class='btn btn-primary' and text()='Register']"

    registration_locator = "//h4[@class='modal-title' and text()='Registration']"

    name_visible_field = "//input[@id='signupName']"
    last_name_visible_field = "//input[@id='signupLastName']"
    email_visible_field = "//input[@id='signupEmail']"
    user_pwd_visible_field = "//input[@id='signupPassword']"
    user_reenter_pwd_visible_field = "//label[text()='Re-enter password']"
    registering_button_visible = "//button[text()='Register']"

    name_error_message = "//p[text()='Name required']"
    last_name_error_message = "//p[text()='Last name required']"
    email_error_message = "//p[text()='Email required']"
    password_error_message = "//p[text()='Password required']"
    reenter_password_error_message = "//p[text()='Re-enter password required']"

    length_name_not_valid_message = "//p[text()='Name has to be from 2 to 20 characters long']"

    symbols_name_not_valid_message = "//p[text()='Name is invalid']"

    password_identically_message = "//p[text()='Passwords do not match']"
