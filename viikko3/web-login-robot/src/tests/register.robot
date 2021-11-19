*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Registration
    Registration Should Fail With Message  Username or password does not meet requirements

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  salis
    Set Password Confirmation  salis
    Submit Registration
    Registration Should Fail With Message  Username or password does not meet requirements

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  salasana2
    Set Password Confirmation  salis
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  maijap
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Set Username  maijap
    Set Password  salasana2
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  maija2
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Registration
    Registration Should Fail With Message  Username or password does not meet requirements
    Go To Login Page
    Set Username  maija2
    Set Password  salasana2
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}