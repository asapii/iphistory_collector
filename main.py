
if __name__ == '__main__':
    import functions as func
    import chardet
    import csv
    import datetime
    import subprocess

    now = datetime.datetime.now()
    output_dir ="iphistory_output_" + now.strftime('%Y%m%d_%H%M%S')
    parsed_etl = output_dir + "\\lwtnetlog.txt"
    output_csv = output_dir + "\\output.csv"
    headline_csv = ["Time","InterfaceNo","Trigger","IPv4","IPv6"]

    subprocess.run('mkdir ' + output_dir, stdout=subprocess.PIPE, shell=True)
    res = subprocess.run('netsh trace convert input=\"C:\Windows\System32\LogFiles\WMI\LwtNetLog.etl\" output=\"'
                         + parsed_etl + '" dump=txt',
                         stdout=subprocess.PIPE,shell=True)
    func.text_encode(parsed_etl,func.textfile_encode_detector(parsed_etl),output_dir + "\\parsed_lwtnetlog_utf8.txt","utf-8")
    with open(output_csv,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headline_csv)
        with open(output_dir + "\\parsed_lwtnetlog_utf8.txt","r") as txt:
            for row in txt:
                writer.writerow(func.get_listforcsv(row))

    subprocess.run('echo >netsh interface ip show interfaces > ' + output_dir + "\\interfaces.txt", stdout=subprocess.PIPE, shell=True)
    subprocess.run('netsh interface ip show interfaces >> ' + output_dir + "\\interfaces.txt", stdout=subprocess.PIPE, shell=True)
    subprocess.run('del ' + output_dir + "\\parsed_lwtnetlog_utf8.txt", stdout=subprocess.PIPE, shell=True)
    func.msgbox("IpHistoryCollector finished!!\n\nOutputDirectory:\n"+output_dir)