import requests
from bs4 import BeautifulSoup


class VisWax:

    def __init__(self):
        self.URL = "https://secure.runescape.com/m=forum/forums?75,76,331,66006366"
        self.resp = None
        self.soup = None

        self.result = {}

    def __fetch_webpage__(self):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        }

        resp = requests.get(self.URL, headers=headers)
        if resp.ok:
            self.resp = resp
            # print(resp.text)
        else:
            print("Something went wrong.")
            # print(resp.text)

    def __parse__webpage__(self):
        if self.resp is not None:
            soup = BeautifulSoup(self.resp.text, "html.parser")
            forum_posts = soup.find("span", attrs={"class": "forum-post__body"})

            main_content = str(forum_posts.text)[136:344]
            date_parts = main_content.split("Slot 1:")

            # Sets the date of the viswax command being run
            self.result["date"] = date_parts[0].strip()

            slot_1_parts = date_parts[1].split("Slot 2:")

            # Sets the primary rune (Slot 1)
            self.result["primary_rune"] = slot_1_parts[0].strip()

            slot_2_parts = slot_1_parts[1].split("Slot 3")

            # Sets the secondary runes
            self.result["secondary_rune"] = slot_2_parts[0].strip().replace("-", "\n- ")

        else:
            print("Website fetch has failed. Unable to parse.")

    def get_viswax_combo(self, speech_format=True):
        try:
            self.__fetch_webpage__()
            self.__parse__webpage__()

            if speech_format:
                return {
                    "data": self.__speechify__()
                }
            else:
                return self.result

        except Exception as err:
            self.result["error"] = 'An exception occurred: {}'.format(err)

            return self.result

    def __speechify__(self):
        if "error" not in self.result:
            date = self.result["date"]
            primary_rune = self.result["primary_rune"]
            secondary_rune = self.result["secondary_rune"]
            self.result["message"] = f"**{date}**\n**Slot 1:** \n{primary_rune} \n**Slot 2:** {secondary_rune}"
            return self.result["message"]

        return self.result["error"]
