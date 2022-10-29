import time
from Constant import ERROR_VALUE, MF_CATEGORY_DEBT
from model.config.groww.GrowwApp import GrowwApp
from model.creds.AppCreds import AppCreds
from worker.CredentialWorker import CredentialWorker
from worker.WebWorker import WebWorker
from model.holding.MfFund import MfFund
from model.holding.Portfolio import Portfolio

class GrowwWorker:

    def __init__(self, config: GrowwApp, web_worker: WebWorker, creds: AppCreds):
        self.web_worker = web_worker
        self.config = config
        self.creds = creds

    def __parse_mf_investments(self, dict: dict) -> Portfolio:
        return Portfolio(
            "Groww Mutual Fund Portfolio",
            dict['investedAmount'],
            dict['currentValue'],
            dict['xirr'],
            [
                MfFund(
                    fund.get('schemeName', ERROR_VALUE),
                    fund.get('amountInvested', float('inf')),
                    fund.get('currentValue', float('inf')),
                    fund.get('xirr', float('inf')),
                    fund.get('units', -1),
                    fund.get('category', MF_CATEGORY_DEBT),
                    str(fund.get('sipDetails', {'hasActiveSip': ERROR_VALUE}).get('hasActiveSip'))
                )
                for fund in dict['holdings']
            ]
        )

    def login(self):
        self.web_worker.open_url(self.config.landing_page)
        username_tag = self.config.login_html_tags.username
        username_continue_tag = self.config.login_html_tags.username_continue
        password_tag = self.config.login_html_tags.password
        submit_tag = self.config.login_html_tags.submit
        pin_tag = self.config.login_html_tags.pin
        while(True):
            self.web_worker.enter_input(username_tag, self.creds.username)
            self.web_worker.perform_click(username_continue_tag)
            if(self.web_worker.wait_on(password_tag, time_out=1, raise_exp=False)):
                break
        self.web_worker.enter_input(password_tag, self.creds.password)
        self.web_worker.perform_click(submit_tag)
        self.web_worker.enter_pin(pin_tag, self.creds.pin)

    def get_mf_portfolio(self) -> Portfolio:
        self.login()
        while(True):
            self.web_worker.perform_click(self.config.mf_tags.mf_nav_bar)
            if(self.web_worker.wait_on(self.config.mf_tags.mf_investments, time_out=1, raise_exp=False)):
                break
        mf_data = self.web_worker.get_network_request_data(self.config.mf_network_data_uri)
        return self.__parse_mf_investments(mf_data)

    
