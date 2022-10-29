from model.config.icici.IciciApp import IciciApp
from model.creds.AppCreds import AppCreds
from worker.WebWorker import WebWorker

class IciciWorker:

    def __init__(self, config: IciciApp, web_worker: WebWorker, creds: AppCreds):
        self.web_worker = web_worker
        self.config = config
        self.creds = creds

    def login(self):
        self.web_worker.open_url(self.config.landing_page)
        while(True):
            try:
                self.web_worker.perform_click(self.config.icici_tags.username_dummy)
                break
            except:
                pass
        username_tag = self.config.login_html_tags.username
        password_tag = self.config.login_html_tags.password
        submit_tag = self.config.login_html_tags.submit
        self.web_worker.enter_input(username_tag, self.creds.username)
        self.web_worker.enter_input(password_tag, self.creds.password)
        self.web_worker.perform_click(submit_tag)