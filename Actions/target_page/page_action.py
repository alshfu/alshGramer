from csv_action import Files
from settings import Settings


class Target_page():

    def __init__(self):
        self.file: Files = Files()
        self.comment_user_list = []

    def read_page(self, driver):
        Settings().random_paus_interval(4, 7, "Читаем страничку конкурента")

    def get_posts_list(self, driver):
        elem_artikle = driver.find_elements_by_tag_name('article')[0]
        posts_links = elem_artikle.find_elements_by_tag_name('a')
        url_posts_list = []
        for post_link in posts_links:
            print('Ссылка на пост ', post_link.get_attribute('href'), ' добавлена в список')
            url_posts_list.append(post_link.get_attribute('href'))
        return url_posts_list
