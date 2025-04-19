from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os

class MyLayout(BoxLayout):
    def download_video(self):
        url = self.ids.url_input.text
        os.system(f"yt-dlp {url}")

class YTApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    YTApp().run()
