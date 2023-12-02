*** Settings ***
Library    lib.py

*** Variables ***
${KEK}  1

*** Keywords ***
my logging function
    log    hello

*** Test Cases ***
мой первый тест
    my logging function

    
limit val
    ${limit} =  get_limit  3
    Should Be Equal As Integers    3   ${limit}
    
    
search location
    ${result} =  test_api  Собор Василия Блаженного  1  json
    LOG   ${result}
    LOG   ${result[0]['lat']}
    LOG   ${result[0]['lon']}
    Should Be Equal As Strings       ${result[0]['display_name']}    Собор Василия Блаженного, 2, Красная площадь, 2, Китай-город, Тверской район, Москва, Центральный федеральный округ, 109012, Россия


поиск магнитов
    ${count} =  get_limit_magnit   locations
    Should Be Equal As Integers    3   ${count}
    
    
rick and morty
    ${count} =  rick_and_mor_api
    Should Be Equal As Integers    826   ${count}


rick and morty 2
    ${count} =  rick_and_mor_api_counter
    Should Be Equal As Integers    826   ${count}


