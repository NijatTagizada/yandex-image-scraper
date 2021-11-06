from scraper.chrome_driver_setup import driver
from scraper.export_failed_url import export_failed_links
from scraper.save_image import save_image, failed_url_list
from scraper.scraping_data import scroll_down, get_data

url = 'https://yandex.ru/images/search?text=gopro&isize=large'

if __name__ == '__main__':
    try:
        driver.get(url)
        scroll_down(1)
        url_list = get_data()
        driver.quit()

        save_image(url_list)
        export_failed_links(failed_url_list)
    except Exception as ex:
        print(ex)
        driver.quit()
