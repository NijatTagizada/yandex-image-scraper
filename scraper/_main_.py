from scraper.chrome_driver_setup import driver
from scraper.export_failed_url import export_failed_urls
from scraper.save_image import save_image, failed_url_list
from scraper.scraping_data import scroll_down, get_data

url = 'https://yandex.ru/images/search?text=gopro&isize=large'

if __name__ == '__main__':
    try:
        # Open Chrome and navigate to Url
        driver.get(url)

        # Scroll down for more image
        scroll_down(1)

        # Get data from yandex
        url_list = get_data()

        # Close driver
        driver.quit()

        # Save image from exported url
        save_image(url_list)

        # Export failed url
        export_failed_urls(failed_url_list)
    except Exception as ex:
        print(ex)
        driver.quit()
