from scrapper import Scrapper
from database import Database,Post
from tqdm import tqdm

class MainApp:
    def __init__(self):
        self.scrapper = Scrapper()
        Post.create_table()

    def run(self):
        items_list = self.scrapper.scrape()
        for item in tqdm(items_list):
            post = Post()
            post.description = item['description']
            post.img_src = item.get('img_src','')
            post.snippets = item['snippets']
            post.title = item['title']
            post.raw_html = item['raw_html']
            post.save()


if __name__ == "__main__":
    app = MainApp()
    app.run()