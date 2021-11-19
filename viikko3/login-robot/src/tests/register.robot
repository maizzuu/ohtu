*** Settings ***
Resource  resource.robot
Test Setup  Run Application And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input  maija
    Input  salasana2
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  maija
    Input  salasana2
    Input  new
    Input  maija
    Input  salasana3
    Run Application
    Output Should Contain  User with username maija already exists

Register With Too Short Username And Valid Password
    Input  f
    Input  salasana2
    Run Application
    Output Should Contain  Username or password does not meet requirements

Register With Valid Username And Too Short Password
    Input  maija
    Input  salis3
    Run Application
    Output Should Contain  Username or password does not meet requirements

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  maija
    Input  salasana
    Run Application
    Output Should Contain  Username or password does not meet requirements

*** Keywords ***
Run Application And Input New Command
    Run Application
    Input New Command