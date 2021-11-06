from scraper.chrome_driver_setup import driver
import time
import json


def get_data() -> list:
    url_list = []

    a_herf = driver.find_element_by_class_name(
        'serp-list serp-list_type_search serp-list_unique_yes serp-list_rum_yes serp-list_justifier_yes serp-controller__list counter__reqid clearfix i-bem serp-list_js_inited'.replace(
            ' ', '.'))

    div_list = a_herf.find_elements_by_tag_name('div')
    data_list = []
    for div in div_list:
        if div.get_attribute('data-bem') is not None:
            data_list.append(div.get_attribute('data-bem'))

    for data in data_list:
        json_data = json.loads(data)
        if 'serp-item' in json_data:
            if 'img_href' in json_data['serp-item']:
                url_list.append(json_data['serp-item']['img_href'])
    print(f'Url count:{len(url_list)}')
    return url_list


def scroll_down(size):
    scroll_pause_time = 3

    for i in range(0, size):
        # Get scroll height
        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            pass
