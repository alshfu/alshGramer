from random import random, randint

from Actions.commet_user_page.post_action import Post_c
from csv_action import Files
from settings import Settings


def word_count(string):
    count = len(string.split())
    print(count, " words in ", string)
    return count


class Comment_user_page():
    def __init__(self):
        self.file: Files = Files()
        self.comment_user_list = []
        self.head_info = []

    def read_page(self, driver, user):
        Settings().random_paus_interval(4, 7, "Читаем страничку пользователя "+ user)
        self.check_if_user_right(driver)


    def get_random_post(self, driver):
        elem_artikle = driver.find_elements_by_tag_name('article')[0]
        posts_links = elem_artikle.find_elements_by_tag_name('a')
        url_posts_list = []
        for post_link in posts_links:
            print('Ссылка на пост ', post_link.get_attribute('href'), ' добавлена в список')
            url_posts_list.append(post_link.get_attribute('href'))
        random_post = randint(0, 4)
        print('Пост под номером ', random_post, "был выбран рандом")
        Post_c().open_post(driver,self.head_info[0],url_posts_list[random_post])

    def set_header_info(self, nick_name, counts_of_posts, counts_of_following, counts_of_follower, user_info):
        self.head_info.append(nick_name)
        self.head_info.append(counts_of_posts)
        self.head_info.append(counts_of_following)
        self.head_info.append(counts_of_follower)
        self.head_info.append(user_info)

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
        user_info: str
        if len(elem_section.find_elements_by_tag_name('h2')) == 1:
            nick_name = elem_section.find_elements_by_tag_name('h2')[0].text
            user_info = "################"
        elif len(elem_section.find_elements_by_tag_name('h1')) == 1:
            nick_name = elem_section.find_elements_by_tag_name('h1')[0].text
            user_info = elem_section.find_elements_by_tag_name('div')[6].text
        self.set_header_info(nick_name,counts_of_posts,counts_of_following,counts_of_follower,user_info)
        Files().save_to_target_list(nick_name,counts_of_posts,counts_of_following,counts_of_follower,user_info)

    def check_if_user_right(self, driver):
        print('Проверка если пользователь подходит')
        self.header_parsser(driver)
        counts_of_following = self.head_info[2]
        if word_count(counts_of_following) == 1:
            if 5 < int(counts_of_following) < 500:
                print('Пользователь подходит')
                self.get_random_post(driver)

