import selenium
from selenium.webdriver.common.keys import Keys

from Actions.target_page.page_action import Target_page
from csv_action import Files
from settings import Settings


class Posts(Target_page):
    def __init__(self):
        self.post_index = 0

    def open(self, driver, url_to_post):
        # Переход на пост
        driver.get(url_to_post)
        Settings().random_paus_interval(5, 10, "Читаем пост " + url_to_post)
        self.get_all_comments(driver)

    def get_all_comments(self, driver):
        elem_b = driver.find_elements_by_tag_name('article')[0]
        elem_a = elem_b.find_elements_by_tag_name('ul')[0]
        elem_a = elem_a.find_elements_by_tag_name('ul')[0]
        comments_count = 0
        for _ in range(300):
            try:
                elem_a.find_elements_by_tag_name('h3')[0].find_elements_by_tag_name('a')[0].send_keys(Keys.END)
                Settings().random_paus_interval(2, 3, "pause between post action")
                elem_b.find_element_by_xpath('//span[@aria-label="Load more comments"]').click()
                Settings().random_paus_interval(2, 3, "pause between post action")
                comments_elem = driver.find_elements_by_tag_name('article')[0]
                comments_elem = comments_elem.find_elements_by_tag_name('ul')[0]
                comments_elem = comments_elem.find_elements_by_tag_name('ul')
                if comments_count == len(comments_elem):
                    print("No more comments")
                    break
                comments_count = len(comments_elem)
                print("comments_count = ", comments_count)
            except selenium.common.exceptions.NoSuchElementException:
                break

    def get_all_comments_user(self, driver):
        users_list = []
        comments_elem = driver.find_elements_by_tag_name('article')[0]
        comments_elem = comments_elem.find_elements_by_tag_name('ul')[0]
        comments_elem = comments_elem.find_elements_by_tag_name('ul')

        for comment_elem in comments_elem:
            try:
                comment_h3_elem = comment_elem.find_elements_by_tag_name('h3')[0]
                comment_user = comment_h3_elem.find_elements_by_tag_name('a')[0].get_attribute('href')
                users_list.append(comment_user)
            except IndexError:
                pass
        return users_list

    def read_page_secondary(self, driver, target_name):
        self.get_all_comments(driver)
        last_post = driver.find_elements_by_tag_name('article')[self.artile_index]
        comments_ul = last_post.find_elements_by_tag_name('ul')[0]
        comments_ul = comments_ul.find_elements_by_tag_name('ul')
        print("comments_ul = ", comments_ul)
        print("comments_ul = ", len(comments_ul))
        last_user = comments_ul[len(comments_ul) - 1].find_elements_by_tag_name('h3')[0].text.strip()
        print("Last user name :", last_user)
        for comment in comments_ul:
            comment_h3 = comment.find_elements_by_tag_name('h3')
            if len(comment_h3) == 1:
                comment_user = comment_h3[0].text.strip()
                if comment_user != target_name and Files().cheak_user_list(comment_user):
                    self.comment_user_list.append(comment_user)
                    print(comment_user)
                    comment_user_link = comment_h3[0].find_elements_by_tag_name('a')[0]
                    comment_user_link.click()
                    Settings().random_paus_interval(4, 7, "pause between post action")
                    # Comment_user_page().action_on_comment_user_page(driver)
                    if comment_user == last_user:
                        print("last user find")
                        break
                    self.artile_index = 0
                    self.read_page(driver, target_name)
