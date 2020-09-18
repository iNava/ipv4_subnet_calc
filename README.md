Python IPv4 Subnet Calculator 
============================

IPv4 Subnet Calculator for subnet mask and other classless (CIDR) network information. 
This is a useful feature for service providers and network operators who frequently allocate and work with subnets. 
CIDR stands for Classless Inter-Domain Routing, and refers to the standard of dividing the entire IP address space 
into smaller networks of variable size.


Features
--------
Given an IP address and CIDR network size, it calculates the network information and provides all-in-one aggregated 
JSON file report and posiible Networks in text file.

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
 * Text file
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
----------------------------------------------------------------
IP Address                  192.168.25.49
Network Address             192.168.25.32
Broadcast Address           192.168.25.63
Total Number of Hosts       32
Number of Usable Hosts      30
Usable Host IP Range        192.168.25.33 - 192.168.25.62
Subnet Mask                 255.255.255.224
Wildcard Mask               0.0.0.31
Binary Subnet Mask          11111111.11111111.11111111.11100000
IP Class                    C
CIDR Notation               /27
IP Type                     Private
Short                       192.168.25.49 /27
Binary ID                   11000000101010000001100100110001
Integer ID                  3232241969
Hex ID                      0xC0A81931
in-addr.arpa                49.25.168.192.in-addr.arpa
IPv4 Mapped Address         :FFFF:C0A8.1931
6to4 Prefix                 2002:C0A8.1931::/48

All 8 of the possible /27 Networks for 192.168.25.*:

Network IP: 192.168.25.0
Usable Host IP Range: 192.168.25.1 - 192.168.25.30
Network Broadcast IP: 192.168.25.31
--------------------------------------------------

Network IP: 192.168.25.32
Usable Host IP Range: 192.168.25.33 - 192.168.25.62
Network Broadcast IP: 192.168.25.63
--------------------------------------------------

Network IP: 192.168.25.64
Usable Host IP Range: 192.168.25.65 - 192.168.25.94
Network Broadcast IP: 192.168.25.95
--------------------------------------------------

Network IP: 192.168.25.96
Usable Host IP Range: 192.168.25.97 - 192.168.25.126
Network Broadcast IP: 192.168.25.127
--------------------------------------------------

Network IP: 192.168.25.128
Usable Host IP Range: 192.168.25.129 - 192.168.25.158
Network Broadcast IP: 192.168.25.159
--------------------------------------------------

Network IP: 192.168.25.160
Usable Host IP Range: 192.168.25.161 - 192.168.25.190
Network Broadcast IP: 192.168.25.191
--------------------------------------------------

Network IP: 192.168.25.192
Usable Host IP Range: 192.168.25.193 - 192.168.25.222
Network Broadcast IP: 192.168.25.223
--------------------------------------------------

Network IP: 192.168.25.224
Usable Host IP Range: 192.168.25.225 - 192.168.25.254
Network Broadcast IP: 192.168.25.255
--------------------------------------------------
```


#### JSON Report (./reults/data.json)
```
{
    "IP Address": "192.168.25.49",
    "Network Address": "192.168.25.32",
    "Broadcast Address": "192.168.25.63",
    "Total Number of Hosts": 32,
    "Number of Usable Hosts": 30,
    "Usable Host IP Range": "192.168.25.33 - 192.168.25.62",
    "Subnet Mask": "255.255.255.224",
    "Wildcard Mask": "0.0.0.31",
    "Binary Subnet Mask": "11111111.11111111.11111111.11100000",
    "IP Class": "C",
    "CIDR Notation": "/27",
    "IP Type": "Private",
    "Short": "192.168.25.49 /27",
    "Binary ID": "11000000101010000001100100110001",
    "Integer ID": 3232241969,
    "Hex ID": "0xC0A81931",
    "in-addr.arpa": "49.25.168.192.in-addr.arpa",
    "IPv4 Mapped Address": ":FFFF:C0A8.1931",
    "6to4 Prefix": "2002:C0A8.1931::/48"
}
```

#### Possible Networks Report (./reults/possible_networks.txt)
```
All 8 of the possible /27 Networks for 192.168.25.*:

Network IP: 192.168.25.0
Usable Host IP Range: 192.168.25.1 - 192.168.25.30
Network Broadcast IP: 192.168.25.31
--------------------------------------------------

Network IP: 192.168.25.32
Usable Host IP Range: 192.168.25.33 - 192.168.25.62
Network Broadcast IP: 192.168.25.63
--------------------------------------------------

Network IP: 192.168.25.64
Usable Host IP Range: 192.168.25.65 - 192.168.25.94
Network Broadcast IP: 192.168.25.95
--------------------------------------------------

Network IP: 192.168.25.96
Usable Host IP Range: 192.168.25.97 - 192.168.25.126
Network Broadcast IP: 192.168.25.127
--------------------------------------------------

Network IP: 192.168.25.128
Usable Host IP Range: 192.168.25.129 - 192.168.25.158
Network Broadcast IP: 192.168.25.159
--------------------------------------------------

Network IP: 192.168.25.160
Usable Host IP Range: 192.168.25.161 - 192.168.25.190
Network Broadcast IP: 192.168.25.191
--------------------------------------------------

Network IP: 192.168.25.192
Usable Host IP Range: 192.168.25.193 - 192.168.25.222
Network Broadcast IP: 192.168.25.223
--------------------------------------------------

Network IP: 192.168.25.224
Usable Host IP Range: 192.168.25.225 - 192.168.25.254
Network Broadcast IP: 192.168.25.255
--------------------------------------------------
```