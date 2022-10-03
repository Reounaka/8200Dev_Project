import os, shutil
import paramiko
from paramiko import SSHClient
ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#.env variable package
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Get the current working directory
cwd = (os.path.dirname(os.path.realpath(__file__)))

# Make new directory for csv_files downloaded
path = os.path.join(cwd, 'csv_files_temp')
if os.path.exists(path):
    shutil.rmtree(path) # remove if exist 
    os.makedirs(path)
else: 
    os.makedirs(path)

""" transport = paramiko.Transport((os.getenv('HOSTNAME'), 22))
transport.connect(username=os.getenv('SFTP_USERNAME'),password=os.getenv('SFTP_PASSWORD'),look_for_keys=False, allow_agent=False)
 """
transport = paramiko.Transport('185.164.16.144', 22)
transport.connect(username='reouvenn',password='Relinor9912')
sftp = paramiko.SFTPClient.from_transport(transport)
print("connection established successfully")

# Downloads csv files using SFTP connection
for file in sftp.listdir(path='/var/tmp/csv_files'):
		sftp.get(os.path.join('/var/tmp/csv_files',file),
			 os.path.join(path, file))

sftp.close()
transport.close()
new_path = os.path.join(cwd, "csv_files_temp")

def get_path():
    print(new_path)
    return new_path

   
   

