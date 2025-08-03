ping arp mac
============

ping arp mac

Function
--------



The **ping arp mac** command configures a device on a LAN to send ICMP packets to check whether a MAC address is in use and displays the IP address corresponding to the MAC address.




Format
------

**ping arp mac** *mac-address* { { *ip-address* [ **vpn-instance** *vpn-instance-name* ] } | { **interface** { *interface-name* | *interface-type* *interface-number* } } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a destination MAC address. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be a multicast or broadcast address or the virtual MAC address of the device. |
| *ip-address* | Specifies an IPv4 address. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **interface** *interface-name* | Specifies the name of the interface that sends and receives ICMP packets. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface that sends and receives ICMP packets. | - |



Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**



When you know a MAC address on a network segment but do not know the corresponding IP address, run this command to configure a device to broadcast Layer 3 ICMP packets to obtain the IP address corresponding to the MAC address.



**Prerequisites**



ICMP has been enabled, and ICMP packets can be properly sent and received.



**Precautions**



**ping arp mac** command cannot be used to detect a local MAC address.




Example
-------

# Run the ping arp mac command to configure a device to send ICMP packets to check whether a MAC address is in use on the network segment 192.168.1.0.
```
<HUAWEI> ping arp mac 00e0-fca6-a45d 192.168.1.0
  LANIP: 192.168.1.0 MAC[00-E0-FC-A6-A4-5D], press CTRL_C to break
----- ARP-Ping MAC statistics -----
    1 packet(s) transmitted
    1 packet(s) received
    IP ADDRESS                MAC ADDRESS
    192.168.1.122             00-E0-FC-A6-A4-5D

```

# Run the ping arp mac command to configure an outbound interface to send ICMP packets to check whether a MAC address is in use.
```
<HUAWEI> ping arp mac 00e0-fca6-a45d interface 100GE1/0/1
  OutInterface: 100GE1/0/1 MAC[00-E0-FC-A6-A4-5D], press CTRL_C to break
----- ARP-Ping MAC statistics -----
    1 packet(s) transmitted
    1 packet(s) received
    IP ADDRESS                MAC ADDRESS
    192.168.1.122             00-E0-FC-A6-A4-5D

```

**Table 1** Description of the **ping arp mac** command output
| Item | Description |
| --- | --- |
| ARP-Ping MAC statistics | Statistics about ARP MAC ping test results. |
| MAC ADDRESS | MAC address specified in the test. |
| IP ADDRESS | IP address corresponding to the MAC address specified in the test. |
| LANIP | IP address of the tested network segment. |