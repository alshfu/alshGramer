import csv
import re


class Files:
    def save_to_target_list(self, user, a, b, c, d):
        with open(r'user_list.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            user_name = csv.writer(csvfile, delimiter='|')
            user_name.writerow([user, a, b, c, re.sub('\n', ' ', d)])
            csvfile.close()

    def cheak_user_list(self, username):
        with open(r"user_list.csv", "r", encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="|")
            for i, line in enumerate(reader):
                try:
                #    print("check if ", username, " same as ", line[0])
                    if username == line[0]:
                        return False
                except IndexError:
                    return True
                    break
        return True
