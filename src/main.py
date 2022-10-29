from utils import get_config
from worker.CredentialWorker import CredentialWorker
import pwinput

from worker.GrowwWorker import GrowwWorker
from worker.IciciWorker import IciciWorker
from worker.WebWorker import WebWorker

config = get_config()

pwd = pwinput.pwinput()
cw = CredentialWorker(pwd, config.creds.encrypted_file_path, config.creds.decrypted_file_path)
creds = cw.get_encrypted_file_content()

ww = WebWorker(config.web)

# gw = GrowwWorker(config.groww, ww, creds.groww)
# mfs = gw.get_mf_portfolio()
# print(mfs)

iw = IciciWorker(config.icici, ww, creds.icici)
iw.login()

# w = WebWorker()
# w.login("https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&ITM=nli_personalb_personal_login_btn&_gl=1*8swtn9*_ga*OTMzNTEzOTU5LjE2NDIzOTg4MTQ.*_ga_SKB78GHTFV*MTY2MDM2OTg5NC4xMS4xLjE2NjAzNzA4OTQuNjA.", None, pwd)