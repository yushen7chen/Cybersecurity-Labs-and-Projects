"""This Program detects active ARP Spoofing attacks on host machines."""

import os, re, datetime, time

#The function accesses the ARP table and extracts its entries
def get_ARP():
    #Read the ARP table and save it in a list form
    try:
        with os.popen('arp -a') as f:
            data = f.read()
            arp_list = []
            mac_list = []

        #Iterating over the ARP entries list, filtering unnecessary data
        for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)', data):
            if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
                pass
            else:
                arp_list.append(line)
        #Adds the mac and ip as a tuple to the list
        for item in arp_list:
            mac_list.append((item[0], item[1]))

        return mac_list

    except Exception as e:
        print("An error occurred, ", e)

    ##print(data)

#The function examins the IP & Mac addresses and checks it for MAC duplication
def check_duplicate(mac_list, saved_list):
    for item in saved_list:
        for i in mac_list:
            if i[1] == item[1]:
                if i[0] != item[0]:
                    logging(item)

#This function creates a file and append into it a log of the ARP spoofing events
def logging(mac_tuple):
    try:
        stream = open('arp_spoof_log.txt', 'a+')
        stream.write("Arp Spoofed!\n")
        stream.write(f"The address is: {mac_tuple[1]}\n")
        stream.write(f"Date: {datetime.datetime.now()}\n\n")
    except Exception as e:
        print("An error occurred, ", e)
    finally:
        stream.close()

#This function clears the log
def clear_log():
    try:
        stream = open('arp_spoof_log.txt', 'w')
        stream.write('')
    except Exception as e:
        print("An error occurred, ", e)
    finally:
        stream.close()

def main():
    clear_log()
    saved_arp = get_ARP()
    time.sleep(10)
    check_duplicate(get_ARP(), saved_arp)


if __name__ == '__main__':
    main()
