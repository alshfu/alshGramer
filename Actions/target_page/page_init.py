from Actions.commet_user_page.page_init import Page_c
from Actions.target_page.post_action import Posts
from proffile import Target
from settings import Settings


class Page:
    def __init__(self):
        self.target_list = Target().target_list
        self.target = self.target_list[0]
        self.url = Settings().get_url() + self.target
        self.url_posts_list = []
        self.url_comment_user = []


    # Переход на страничку таргета
    def open(self, driver):
        Settings().random_paus_interval(4, 15, "Переход на страничку " + self.target)
        driver.get(self.url)
        Posts().read_page(driver)
        url_posts_list = Posts().get_posts_list(driver)
        for url_to_post in url_posts_list:
            Posts().open(driver, url_to_post)
            coment_user_list = Posts().get_all_comments_user(driver)
            for url_to_user in coment_user_list:
                self.url_comment_user.append(url_to_user)
                print('Ссылка на пользователя  ', url_to_user, ' добавлена в список')
            break
        for url_user in self.url_comment_user:
            user = url_user.strip("https://www.instagram.com/")
            user = user.strip("/")
            print(user, " из списка коментаторв")
            if Page_c().cheak_if_user_exist(user):
                Page_c().open(driver,url_user,user)
                pass
