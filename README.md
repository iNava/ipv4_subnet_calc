Python IPv4 Subnet Calculator 
============================

IPv4 Subnet Calculator for subnet mask and other classless (CIDR) network information. 
This is a useful feature for service providers and network operators who frequently allocate and work with subnets. 
CIDR stands for Classless Inter-Domain Routing, and refers to the standard of dividing the entire IP address space 
into smaller networks of variable size.


Features
--------
Given an IP address and CIDR network size, it calculates the network information and provides all-in-one aggregated 
JSON file report.

### Calculations
 * IP address
 * Network Address
 * Broadcast Address 
 * Total Number of Hosts
 * Number of Usable Hosts
 * Usable Host IP Range
 * Subnet Mask
 * Wildcard Mask
 * Binary Subnet Mask
 * IP Class
 * CIDR Notation
 * IP Type
 * Short
 * Binary ID
 * Integer ID
 * Hex ID
 * in-addr.arpa
 * IPv4 Mapped Address
 * 6to4 Prefix
 
Provides each data in dotted decimal, hexadecimal and binary formats.

### Aggregated Network Calculation Reports
 * JSON
 * Printed to STDOUT


### Minimum Requirements
 * Python 3.4

Usage
-----

```
$ python3 ipv4_subnet_calc

IPv4 Subnet Calculator

Please input IPv4 network address (e.g. 192.233.164.138):
192.168.25.49

Please input subnet using prefix (e.g. /24):
/28  
```


### Reports

#### Printed Report
```
IP Address:                 192.168.25.49
Network Address:            192.168.25.48
Broadcast Address:          192.168.25.63
Total Number of Hosts:      16
Number of Usable Hosts:     14
Usable Host IP Rang:        192.168.25.49 - 192.168.25.62"
Subnet Mask:                255.255.255.240
Wildcard Mask:              0.0.0.15
Binary Subnet Mask:         11111111.11111111.11111111.11110000
IP Class:                   C
CIDR Notation:              /28
IP Type:                    Private
Short:                      192.168.25.49 /28
Binary ID:                  11000000101010000001100100110001
Integer ID:                 3232241969
Hex ID:                     0xC0A81931
in-addr.arpa:               49.25.168.192.in-addr.arpa
IPv4 Mapped Address:        :FFFF:C0A8.1931
6to4 Prefix:                2002:C0A8.1931::/48
```


#### JSON Report
```
{
    "IP Address": "192.168.25.49",
    "Network Address": "192.168.25.48",
    "Broadcast Address": "192.168.25.63",
    "Total Number of Hosts": 16,
    "Number of Usable Hosts": 14,
    "Usable Host IP Rang": "192.168.25.49 - 192.168.25.62",
    "Subnet Mask": "255.255.255.240",
    "Wildcard Mask": "0.0.0.15",
    "Binary Subnet Mask": "11111111.11111111.11111111.11110000",
    "IP Class": "C",
    "CIDR Notation": "/28",
    "IP Type": "Private",
    "Short": "192.168.25.49 /28",
    "Binary ID": "11000000101010000001100100110001",
    "Integer ID": 3232241969,
    "Hex ID": "0xC0A81931",
    "in-addr.arpa": "49.25.168.192.in-addr.arpa",
    "IPv4 Mapped Address": ":FFFF:C0A8.1931",
    "6to4 Prefix": "2002:C0A8.1931::/48"
}
```
