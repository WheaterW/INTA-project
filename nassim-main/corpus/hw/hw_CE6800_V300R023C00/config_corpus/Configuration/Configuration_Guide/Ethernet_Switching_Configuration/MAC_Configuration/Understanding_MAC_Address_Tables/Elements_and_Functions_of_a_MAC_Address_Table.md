Elements and Functions of a MAC Address Table
=============================================

Elements and Functions of a MAC Address Table

#### Elements

Each entry in a MAC address table is uniquely identified by a MAC address and a VLAN ID. If a destination host is added to multiple VLANs, one MAC address corresponds to multiple VLAN IDs in the MAC address table. [Table 1](#EN-US_CONCEPT_0000001130624942__table_01) lists MAC address entries, which specify the outbound interfaces for packets with specified destination MAC addresses and VLAN IDs. For example, the first MAC address entry is used to forward the packets with destination MAC address 00e0-fc12-1234 and VLAN ID 10 through the outbound interface, interface 1.

**Table 1** MAC address entries
| MAC Address | VLAN ID | Outbound Interface |
| --- | --- | --- |
| 00e0-fc12-1234 | 10 | Interface 1 |
| 00e0-fc12-5678 | 20 | Interface 2 |



#### Functions

A MAC address table is used for forwarding unicast packets. In [Figure 1](#EN-US_CONCEPT_0000001130624942__fig_01), when packets sent from PC1 to PC3 reach DeviceA, DeviceA searches its MAC address table for the outbound interface (interface 3) that matches the destination MAC address MAC 3 and VLAN 10 in the packets. DeviceA then forwards packets to PC3 from interface 3.

**Figure 1** Forwarding based on the MAC address table  
![](figure/en-us_image_0000001130784750.png)