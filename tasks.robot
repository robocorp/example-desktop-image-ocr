*** Settings ***
Documentation       Gnucash automation example.
...                 Showcases different methods of utilizing
...                 image/character recognition based automation.

Variables           settings.py
Library             RPA.Desktop
Library             GnucashLibrary
Resource            gnucash.robot

Suite Setup         Open Gnucash
Suite Teardown      Close Gnucash


*** Tasks ***
Create Account
    Open Create New Account Form
    Fill Data
    Click Cancel

Get Assets Sum
    ${sum}=    Get Net Assets
    Log    Net assets are: ${sum}
