from selenium.webdriver.common.keys import Keys

from settings import Settings


class Post_c():
    def open_post(self, driver, user, post):
        driver.get(post)
        Settings().random_paus_interval(4, 7, "Переход  пост пользователя " + user)
        self.last_post_action(driver)

    def last_post_action(self, driver):
        Settings().random_paus_interval(3, 7, "Читаем пост ")
        last_post = driver.find_elements_by_tag_name('article')[0]
        like_button = last_post.find_elements_by_tag_name('section')[0]
        like_button = like_button.find_elements_by_tag_name('button')[0]
        like_button.click()
