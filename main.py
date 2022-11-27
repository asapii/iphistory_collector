# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import functions as func
    import chardet
    import csv
    import datetime
    import subprocess

    parsed_etl = "lwtnetlog.txt"
    now = datetime.datetime.now()
    output_csv = "output.csv"
    headline_csv = ["Date","Time","InterfaceNo","Trigger","IPv4","IPv6"]

    res = subprocess.run('netsh trace convert input=\"C:\Windows\System32\LogFiles\WMI\LwtNetLog.etl\" output=\"lwtnetlog.txt\" dump=txt',stdout=subprocess.PIPE,shell=True)
    func.text_encode(parsed_etl,func.textfile_encode_detector(parsed_etl),"parsed_lwtnetlog_utf8.txt","utf-8")
    #func.text_parse("utf8_lwtnetlog.txt","parsed_lwtnetlog.txt")
    #with open(parsed_etl_output) as f:
    with open(output_csv,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headline_csv)
        with open("parsed_lwtnetlog_utf8.txt","r") as txt:
            for row in txt:
                writer.writerow(func.get_listforcsv(row))
