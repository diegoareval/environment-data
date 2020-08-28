from uuid import getnode as get_mac

def format_mac_adress(mac):
  return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

mac = get_mac()

print(format_mac_adress(mac))