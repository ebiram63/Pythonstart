import struct
import socket


def main(data):
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_data,addr = conn.recvfrom(65535)
        dest_mac, src_mac, ether_proto, data = ethernet_frame(raw_data)
        print('\n Ethernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, ether_proto))

        # 8 for ipv4
        if ether_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            print('\t IPv4 Packet: ')


#unpaking ethernet frames
def ethernet_frame(data):
    src_mac, dest_mac, proto = struct.unpack('! 6s 6s H', data[14:])
    return get_mac_addr(src_mac), get_mac_addr(dest_mac), socket.htons(proto), data[14:]

#formated mac address 
def get_mac_addr(byte_addr):
    byte_str = map('{:02x}'.format,byte_addr)
    return ':'.join(byte_str).upper()


def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) *4
    ttl,proto,src,target = struct.unpack('! 8x B B 2x 4s 4s'.format,data[0,20])
    return version, header_length, ttl,proto, ipv4(src), ipv4(target), data[header_length:]

# formatted ipv4 ex 127.0.0.1
def ipv4(addr):
    return '.' . join(map(str,addr))

# unpack ICMP
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack(from.data[:4])
    return icmp_type, code, checksum, data[4:]

# unpack TCP segment
def tcp_segment(data):
    src_port, dest_port, seguence, acknoledge, offset_reserve_flag = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserve_flag >> 12)*4
    return(src_port, dest_port, seguence, acknoledge, offset_reserve_flag)





main()