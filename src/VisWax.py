import requests
from bs4 import BeautifulSoup


class VisWax:

    def __init__(self):
        self.URL = "https://secure.runescape.com/m=forum/forums?75,76,331,66006366"
        self.resp = None
        self.soup = None

        print("A001: Initializing Viswax")

        self.result = {}

    def __fetch_webpage__(self):

        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        # }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.31 SmartTV/6.0"
        }
        # headers = {
        #     # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     # "Accept-Encoding": "gzip, deflate, br",
        #     # "Cache - Control": "max - age = 0",
        #     # "Connection": "keep-alive",
        #     # "Accept-Language": "en-US,en;q=0.9",
        #     # "DNT": "1",
        #     # "Host": "secure.runescape.com",
        #     # "Upgrade-Insecure-Requests": "1",
        #     # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        # }

        # headers = {
        #
        # }

        print("A002: Fetching webpage")
        resp = requests.get(self.URL, headers=headers)
        print("A003: webpage response has been fetched")
        if resp.ok:
            self.resp = resp
            print("A004: Response is ok")
            print(str(resp.text))
        else:
            print("A005: Something went wrong.")

        print(str(resp.headers))
        # print(str(resp.text))

    def __parse__webpage__(self):
        if self.resp is not None:
            print("A006: Attempting to parse response")
            soup = BeautifulSoup(self.resp.text, "html.parser")
            print("A015: created a html parser from BeautifulSoup")

            forum_posts = soup.find("span", attrs={"class": "forum-post__body"})
            print("A016: Found the forum posts")
            print("A021: Forum post string")
            print(str(forum_posts))
            print("A022: Forum post contents")
            print(str(forum_posts.contents))

            main_content = str(forum_posts.text)[136:344]
            date_parts = main_content.split("Slot 1:")
            print("A017: split the date parts")

            # Sets the date of the viswax command being run
            self.result["date"] = date_parts[0].strip()
            print("A018: Stripped the date part")

            slot_1_parts = date_parts[1].split("Slot 2:")
            print("A019: Got the Slot 1 runes")

            # Sets the primary rune (Slot 1)
            self.result["primary_rune"] = slot_1_parts[0].strip()

            slot_2_parts = slot_1_parts[1].split("Slot 3")
            print("A020: Got the Slot 2 runes")

            # Sets the secondary runes
            self.result["secondary_rune"] = slot_2_parts[0].strip().replace("-", "\n- ")
            print("A008: Successfully parsed the response")

        else:
            print("A007: Website fetch has failed. Unable to parse.")

        print("A013: Self at the end of parsing: " + str(self.result))

    def get_viswax_combo(self, speech_format=True):
        try:
            self.__fetch_webpage__()
            self.__parse__webpage__()

            if speech_format:
                return self.__speechify__()
            else:
                return self.result

        except Exception as err:
            print("A010: Exception occurred when getting Viswax Combo")
            print(str(err))
            self.result["error"] = 'A009: An exception occurred: {}'.format(err)
            return "A014: There has been an error trying to fetch VisWax runes. Please contact Alan."

    def __speechify__(self):
        print("A011: Attempting to speechify the result")
        if "error" not in self.result:
            date = self.result["date"]
            primary_rune = self.result["primary_rune"]
            secondary_rune = self.result["secondary_rune"]
            self.result["message"] = f"**{date}**\n**Slot 1:** \n{primary_rune} \n**Slot 2:** {secondary_rune}"
            return self.result["message"]

        print("A012: Error during speechify")
        return self.result["error"]
