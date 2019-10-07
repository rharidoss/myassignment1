import re
from collections import Counter

def apache_log_reader(logfile):
#    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    myregex = r'\s\d{3}\s'

    with open(logfile) as f:
        log = f.read()
        http_code_list = re.findall(myregex,log)
        ipcount = Counter(http_code_list)
        for k, v in ipcount.items():
            print("http code " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))

# Create entry point of our code
if __name__ == '__main__':
    apache_log_reader("access.log")
