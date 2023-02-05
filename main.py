from ftplib import FTP
import os
import re

# initialize the list
connect_params: list = ["a", "b", "c", "d", 1, "f"]
# params.txt contains 6 parameters necessary for connection and download
# here I read from this file
f = open('params.txt', 'r')
for x in range(6):
    temp_param: list = f.readline()
    connect_params[x] = temp_param
f.close()

username = re.sub("\n", "", connect_params[0])
password = re.sub("\n", "", connect_params[1])
site_url = re.sub("\n", "", connect_params[2])
# the path in the remote server where the files are located
site_directory = re.sub("\n", "", connect_params[3])
# these are the filename, tha last x position  that contain
# only the name and not all the other file attributes.
jpa_position = int(re.sub("\n", "", connect_params[4]))
string_to_search: str = re.sub("\n", "", connect_params[5])


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
    returned_value_get = os.system(cmd)  # returns a list of all jpa files containing string_to_search
    cmd = "del *" + string_to_search + "*.jpa"  # delete all jpa files containing string_to_search
    returned_value_del = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value_del)
    ftp = FTP(site_url)  # connect to host, default port
    ftp.login(username, password)
    ftp.cwd(site_directory)  # changing to the directory akeeba saves.
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    ftp.retrlines('LIST')
    files = ftp.dir("*.jpa", dirCallback)
    ftp.quit()
    print('TELOS')