from csv_action import Files
from settings import Settings
from selenium.webdriver.common.keys import Keys


def word_count(string):
    count = len(string.split())
    print(count, " words in ", string)
    return count


class Comment_user_page:
    def __init__(self):
        self.settings: Settings = Settings()
        self.file: Files = Files()

    def header_parsser(self, driver):
        elem_header = driver.find_elements_by_tag_name('header')[0]
        elem_section = elem_header.find_elements_by_tag_name('section')[0]
        counts_of_following = elem_section.find_elements_by_tag_name('li')[2].find_elements_by_tag_name('span')[0]
        counts_of_following = counts_of_following.text.strip()
        counts_of_follower = elem_section.find_elements_by_tag_name('li')[1].find_elements_by_tag_name('span')[0]
        counts_of_follower = counts_of_follower.text.strip()
        counts_of_posts = elem_section.find_elements_by_tag_name('li')[0].find_elements_by_tag_name('span')[0]
        counts_of_posts = counts_of_posts.text.strip()
        nick_name: str
        if len(elem_section.find_elements_by_tag_name('h2')) == 1:
            nick_name = elem_section.find_elements_by_tag_name('h2')[0].text
        elif len(elem_section.find_elements_by_tag_name('h1')) == 1:
            nick_name = elem_section.find_elements_by_tag_name('h1')[0].text
        user_info = elem_section.find_elements_by_tag_name('div')[6].text
        #          0              1               2                    4                5
        return nick_name, counts_of_posts, counts_of_following, counts_of_follower, user_info

    def check_if_user_right(self, driver):
        print('check if right user')
        counts_of_following = self.header_parsser(driver)[2]
        if word_count(counts_of_following) == 1:
            if 30 < int(counts_of_following) < 500:
                return True
            else:
                return False
        else:
            return False

    def last_post_action(self, driver):
        # Go to last post
        header = self.header_parsser(driver)
        if len(driver.find_elements_by_tag_name('article')[0].find_elements_by_tag_name('h1')) == 0:
            articles = driver.find_elements_by_tag_name('article')[0].find_elements_by_tag_name('a')
            # TODO: список постов пользователя который оставил коментарий
            last_post_link = articles[0]
            last_post_link.click()
            self.settings.random_paus_interval(3, 7, "looking for last post")
            last_post = driver.find_elements_by_tag_name('article')[1]
            like_button = last_post.find_elements_by_tag_name('section')[0]
            like_button = like_button.find_elements_by_tag_name('button')[0]
            like_button.click()
            self.settings.random_paus_interval(2, 3, "pause between action")
            like_button.send_keys(Keys.ESCAPE)
            self.go_back(driver)
            self.go_back(driver)
            self.file.save_to_target_list(header[0], header[1], header[2], header[3], header[4])
        else:
            no_posts = driver.find_elements_by_tag_name('article')[0].find_elements_by_tag_name('h1')[0].text
            self.file.save_to_target_list(header[0], header[1], header[2], header[3], no_posts)
            self.go_back(driver)

    def go_back(self, driver):
        print("Go back")
        self.settings.random_paus_interval(2, 3, "pause before goBack")
        driver.back()
        self.settings.random_paus_interval(8, 11, "pause after goBack")

    def action_on_comment_user_page(self, driver):
        self.settings.random_paus_interval(4, 7, "looking on comments user page")
        header = self.header_parsser(driver)
        if self.check_if_user_right(driver):
            # return , , , ,
            self.last_post_action(driver)
        else:
            self.file.save_to_target_list(header[0], header[1], header[2], header[3], "#####")
            self.go_back(driver)
