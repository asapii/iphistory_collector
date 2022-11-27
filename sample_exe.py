if __name__ == '__main__':
    import subprocess
    res = subprocess.run('netsh trace convert input=\"C:\Windows\System32\LogFiles\WMI\LwtNetLog.etl\" output=\"lwtnetlog.txt\" dump=txt',stdout=subprocess.PIPE,shell=True)
    #res = subprocess.run("netsh trace convert input=\"C:\Windows\System32\LogFiles\WMI\LwtNetLog.etl\" output=\"lwtnetlog.txt\" dump = txt",stdout=subprocess.PIPE, shell=True)