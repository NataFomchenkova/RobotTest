*** Settings ***
Library    lib.py
Library       DataDriver
Test Template  Reverse Geocoding

*** Keywords ***
Reverse Geocoding
    [Arguments]    ${name}   ${lat}   ${lon}
    ${result} =   rev_geocoding   ${lat}   ${lon}
    Should Be Equal    ${result['name']}    ${name}


*** Test Cases ***
Reverse search for name: ${name} by lat: ${lat} and lon: ${lon}
