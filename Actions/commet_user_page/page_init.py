from Actions.commet_user_page.page_action import Comment_user_page
from csv_action import Files
from proffile import Target
from settings import Settings


class Page_c():

    def __init__(self):
        self.target_user = Target().target_list[0]
        self.settings: Settings = Settings()
        self.file: Files = Files()

    def cheak_if_user_exist(self, user):
        if self.target_user != user:
            if self.file.cheak_user_list(user):
                print(user, "не найден в списке")
                return True
            else:
                print(user, "был найден в списке")
                return False

    def open(self, driver, url, user):
        driver.get(url)
        Settings().random_paus_interval(4, 7, "Переход на страничку " + user)
        Comment_user_page().read_page(driver, user)
