*** Settings ***
Library    lib.py
Library       DataDriver
Test Template  Direct Geocoding

*** Keywords ***
Direct Geocoding
    [Arguments]    ${name}   ${lat}   ${lon}
    ${result} =   dir_geocoding   ${name}
    Should Be Equal    ${result[0]['lat']}    ${lat}
    Should Be Equal    ${result[0]['lon']}    ${lon}


*** Test Cases ***
Direct search for lat: ${lat} and lon: ${lon} by name: ${name}