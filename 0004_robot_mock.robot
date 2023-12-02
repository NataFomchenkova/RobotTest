*** Settings ***
Library    lib.py

*** Keywords ***
my logging function
    log    hello

*** Test Cases ***
Real test
    ${result} =  test_api  Собор Василия Блаженного  1  json
    Should Be Equal As Strings       ${result[0]['name']}    Собор Василия Блаженного

Mock test
    ${result} =  mock_test  Собор Василия Блаженного  1  json
    Should Be Equal As Strings       ${result[0]['name']}    https://www.youtube.com/watch?v=dQw4w9WgXcQ