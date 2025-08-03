netstream export host
=====================

netstream export host

Function
--------



The **netstream export host** command configures the destination IP address and destination UDP port number for the exported packets carrying flow statistics.

The **undo netstream export host** command deletes the configured destination IP address and destination UDP port number for the exported packets carrying flow statistics.



By default, no destination IP address or destination UDP port number is configured for the exported packets carrying flow statistics.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **host** { *ip-address* | **ipv6** *ipv6-address* } *port* [ **vpn-instance** *vpn-instance-name* ] **dscp** *dscp-value*

**undo netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **host** { *ip-address* | **ipv6** *ipv6-address* } *port* [ **vpn-instance** *vpn-instance-name* ] **dscp** *dscp-value*

For CE6885-LL (low latency mode):

**netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **host** *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] **dscp** *dscp-value*

**undo netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **host** *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] **dscp** *dscp-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the destination IP address of the exported packets carrying flow statistics. | The value is in dotted decimal notation. |
| *port* | Specifies the destination UDP port number of the exported packets carrying flow statistics. | The value is an integer ranging from 1 to 65535. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance of the exported packets carrying flow statistics. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **dscp** *dscp-value* | Specifies the DSCP priority of the exported packets carrying flow statistics. | The value is an integer that ranges from 0 to 63. |
| **ip** | Specifies destination information for the exported packets carrying IPv4 flow statistics. | - |
| **ipv6** *ipv6-address* | Specifies the destination IPv6 address of the exported packets carrying flow statistics.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **ipv6** | Specifies destination information for the exported packets carrying IPv6 flow statistics. | - |
| **vxlan** | Specifies destination information for the exported packets carrying VXLAN flexible flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After finishing data collection, the NDE sends the collected data to the NSC. This command specifies the destination address of the collected data, that is, the NSC IP address.

**Precautions**



You can configure two groups of destination addresses and destination port numbers for IPv4, IPv6, and VXLAN flexible flow statistics collection to implement NSC backup. Before configuring the third group of destination addresses and destination port numbers, run the undo netstream export { ip | ipv6 | vxlan inner-ip } host command to delete the original group of destination addresses and destination port numbers. Otherwise, the system displays a message indicating that the maximum number of destination addresses and port numbers are exceeded. As a result, the configuration fails.The addresses of the local and peer devices bound to a VPN instance must be different, and cannot be set to unspecified addresses, IPv6 link-local addresses, multicast addresses, or loopback addresses.The relationships between DSCP values and forwarding queues are as follows: Packets with DSCP values from 0 to 7 enter queue 0. Packets with DSCP values from 8 to 15 enter queue 1. Packets with DSCP values from 16 to 23 enter queue 2. Packets with DSCP values from 24 to 31 enter queue 3. Packets with DSCP values from 32 to 39 enter queue 4. Packets with DSCP values from 40 to 63 enter queue 5.




Example
-------

# Set the destination IP address for the exported packets carrying original flow statistics to 10.1.1.1, UDP port number to 222, and DSCP value to 0.
```
<HUAWEI> system-view
[~HUAWEI] netstream export ip host 10.1.1.1 222 dscp 0

```