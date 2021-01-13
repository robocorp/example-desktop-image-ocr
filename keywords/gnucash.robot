*** Settings ***
Library   OperatingSystem

*** Variables ***
${GNUCASH_APP}   ${NONE}

*** Keywords ***
Fill Data
    Fill Name               OCR testing
    ${region}=              Fill Code And Get Region    1337
    Fill Description        ${region}    Found by OCR and region locators
    Fill Notes              Next we'll find the cancel button by image template

Open Gnucash
    Remove file             ${GNUCASH_DATABASE}.LCK
    ${app}=                 Open Application     ${GNUCASH_EXECUTABLE}  ${GNUCASH_DATABASE}
    Set suite variable      ${GNUCASH_APP}    ${app}
    Wait For Element        ocr:New    timeout=20

Close Gnucash
    [Documentation]         Close the application with internal
    ...                     hotkeys. This is better than calling
    ...                     `Close Application  <application>`.
    Close application       ${GNUCASH_APP}

Open Create New Account Form
    [Documentation]         Click button by label (OCR).
    Click                   ocr:New
    Wait For element        ocr:"New Account"

Fill Name
    [Documentation]         Type text. We know that the cursor is
    ...                     already in the right place here.
    [Arguments]             ${text}
    Type Text               ${text}

Fill Code and Get Region
    [Documentation]         Fill text by field label (OCR) and region,
    ...                     then return the region.
    [Arguments]             ${text}
    ${region}=              Find element    ocr:"Account code" + offset:200,0
    Click                   ${region}
    Type Text               ${text}
    [Return]                ${region}

Fill Description
    [Documentation]         Fill text by known region.
    [Arguments]             ${region}  ${text}
    Click                   ${region} + offset:0,40
    Type Text               ${text}

Fill Notes
    [Documentation]         Fill text by field label (OCR) and offset.
    [Arguments]             ${text}
    Click                   ocr:Notes + offset:200,0
    Type Text               ${text}

Click Cancel
    [Documentation]         Click Cancel by image template.
    Click                   image:resources/gnucash_newaccount_cancel_button.png
