# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ftplib import FTP
import os

username = "xxxxxxxxxxxxxxx"
password = "xxxxxxxxxxxxxxx"
site_url = "abcde.domain.com"
site_directory = "folder1/folder2/folder3/"
# jpa_position = -59 # The last N characters of the string which contains the file name
jpa_position = -42
string_to_search: str = "panch"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def dirCallback(line):
    line = "%s" % line
    line = line[jpa_position:]
    ftpfunc = FTP(site_url)  # connect to host, default port
    ftpfunc.login(username, password)  # user anonymous, passwd anonymous@
    ftpfunc.cwd(site_directory)  # changing directory
    print(line)
    ftpfunc.retrbinary("RETR " + line, open(line, 'wb').write)  # downloads the file


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = "dir *.jpa | findstr " + string_to_search
    returned_value_get = os.system(cmd)  # returns a list of all jpa files containing panch
    cmd = "del *panch*.jpa" # delete all jpa files containing panch
    returned_value_del = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value_del)
    ftp = FTP(site_url)  # connect to host, default port
    ftp.login(username, password)
    ftp.cwd(site_directory)  # changing to the directory akeeba saves.
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    ftp.retrlines('LIST')
    files = ftp.dir("*.jpa", dirCallback)
    ftp.quit()
    print('TELOS')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
