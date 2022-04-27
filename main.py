from scrapper import Scrapper
from database import Database,Post
from tqdm import tqdm

class MainApp:
    def __init__(self):
        self.scrapper = Scrapper()
        Post.create_table()

    def run(self):
        items_list = self.scrapper.scrape()


if __name__ == "__main__":
    app = MainApp()
    app.run()