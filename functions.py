def textfile_encode_detector(file_path):
    from chardet.universaldetector import UniversalDetector
    detector = UniversalDetector()
    encode_type = ""
    with open(file_path,'rb') as f:
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        encode_type = detector.result['encoding']
    return encode_type

def text_encode(src_path,src_codec,dest_path,dest_codec):
    """
    Change Text encode src_codec to dest_codec
    delete "space"
    delete column without keep_str
    """
    import codecs
    src = codecs.open(src_path, "r", src_codec)
    dest = codecs.open(dest_path, "w", dest_codec)
    keep_str = ["Address addition. Address","Address DAD successful. Address"]
    for row in src:
        if keep_str[0] in row or keep_str[1] in row:
            """delete(space)"""
            dest.write(row.replace(" ",""))
    src.close()
    dest.close()

"""BOTSU
def text_parse(src_path,dest_path):
    src = open(src_path,"r")
    dest = open(dest_path,"w")
    keep_str = ["Addressaddition.Address","AddressDADsuccessful.Address"]
    for row in src:
        if keep_str[0] in row or keep_str[1] in row:
            dest.write(row)
    src.close()
    dest.close()
"""

def get_listforcsv(line_text):
    import re
    from datetime import datetime
    if "IgnoreIPv4address" not in line_text:
        """IPv4"""
        print("v4")
        re_date = re.findall(r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}',line_text)
        re_time = re.findall(r'[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{8,10}', line_text)
        re_interface = re.findall(r'Interface=([0-9]{1,2})\,',line_text)
        re_trigger = re.findall(r'IP:(.*?).Address',line_text)
        re_ipv4 = re.findall(r'Address=(.*?)\,',line_text)
        #return_time = re_date[0]+" "+re_time[0]
        #return_time = datetime.strptime(return_time[:-3],"%Y-%m-%d %H:%M:%S.%f")
        re_time_tmp = re_time[0]
        re_time[0] = re_time_tmp[:-3]
        list = [re_date[0],re_time[0],re_interface[0],re_trigger[0],re_ipv4[0],""]
        return list
    else:
        """IPv6"""
        print("v6")
        re_date = re.findall(r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}',line_text)
        re_time = re.findall(r'[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{8,10}', line_text)
        re_interface = re.findall(r'Interface=([0-9]{1,2})\,',line_text)
        re_trigger = re.findall(r'IP:(.*?).Address',line_text)
        re_ipv6 = re.findall(r'IPv6address=(.*?)\,',line_text)
        #return_time = re_date[0]+" "+re_time[0]
        #return_time = datetime.strptime(return_time[:-3],"%Y-%m-%d %H:%M:%S.%f")
        re_time_tmp = re_time[0]
        re_time[0] = re_time_tmp[:-3]
        list = [re_date[0],re_time[0],re_interface[0],re_trigger[0],"",re_ipv6[0]]
        return list



if __name__ == '__main__':
    ret = get_listforcsv("[6]0000.0000::2022-11-1722:44:26.532957800[Microsoft-Windows-TCPIP]IP:AddressDADsuccessful.Address=192.168.56.1,Interface=11,Compartment=1,Protocol=IPv4.")
    print(ret)

    #text_parse("utf8_lwtnetlog.txt","parsed_lwtnetlog.txt")
    #f = open("lwtnetlog.txt")
    #print(textfile_encode_detector("lwtnetlog.txt"))


    #for line in f:
    #    print(line)
    #f.close()
