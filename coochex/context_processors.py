from json import dump
import time

import requests
from selenium import webdriver


def check_link_cookie(links: dict[str: str]) -> None:
    """

    :param links:
    :return: None
    """
    # Запускается браузер Chrome
    driver = webdriver.Chrome()
    error_results = []
    run_results = []
    for login, af_link in links.items():
        driver.get(af_link)
        # Проверка доступности страницы
        response = requests.get(af_link)
        # Время на загрузку страницы
        time.sleep(2)
        cookie_t = driver.get_cookie('tagtag_aid')
        data = {
            'Status': response.status_code,
            'Login': login,
            'Redirect_link': driver.current_url,
            'Cookie': cookie_t,
            'admitad_uid': '',
            'Attribution': None
        }
        if cookie_t is None:
            tt_cookie = 'Error, tracking code not found'
            data['admitad_uid'] = tt_cookie
            # Собираются кампании без трекинг-кода
            error_results.append(data)
        else:
            tt_cookie = cookie_t.get('value', 'No cookie found')
        cookie_d = driver.get_cookie('deduplication_cookie')
        if cookie_d is None:
            dd_cookie = 'Error, deduplication code not found'
        else:
            dd_cookie = cookie_d.get('value', 'No deduplication cookie')
        data['Attribution'], data['admitad_uid'] = dd_cookie, tt_cookie
        # Собираются результаты всей проверки
        run_results.append(data)
        print(data)

    with open('results/error_results.json', 'w') as error_file:
        dump(error_results, error_file, indent=4)
    with open('results/run_results.json', 'w') as main_file:
        dump(run_results, main_file, indent=4)
    driver.quit()
