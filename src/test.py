from worker.CredentialWorker import CredentialWorker

cw = CredentialWorker('hello','src/creds_lock.txt','src/creds.json')
cw.decrypt_file()