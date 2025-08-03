display mac-address forward-engine
==================================

display mac-address forward-engine

Function
--------



The **display mac-address forward-engine** command displays MAC address entries in the chip.




Format
------

**display mac-address** *mac-address* **vlan** *vlan-id* **slot** *slot-id* **forward-engine**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies the destination MAC address in an entry. | The value is in the format of H-H-H, in which each H is a hexadecimal number of 1 to 4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **vlan** *vlan-id* | Displays MAC address entries in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **slot** *slot-id* | Displays MAC address entries in a specified slot. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The MAC address table of the device stores MAC addresses of other devices. When forwarding an Ethernet frame, the device searches the MAC address table for the outbound interface according to the destination MAC address and VLAN ID in the Ethernet frame.If packets are forwarded in unicast mode and MAC address entries cannot be queried using the display mac-address or display mac-address dynamic command, you can use this command to check whether there are MAC address entries in the chip.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the MAC address entry with MAC address 00e0-fc12-3456 and VLAN 1 in the specified slot.
```
<HUAWEI> display mac-address 00e0-fc12-3456 vlan 1 slot 1 forward-engine
---- Flags: * - Backup
-------------------------------------------------------------------------------
MAC Address    VLAN         Learned-From        Type         Age
-------------------------------------------------------------------------------
00e0-fc12-3456  1           10GE1/0/1           dynamic      -
-------------------------------------------------------------------------------
Total items on chip 0: 1

```

**Table 1** Description of the **display mac-address forward-engine** command output
| Item | Description |
| --- | --- |
| Backup | Backup way. |
| MAC Address | Destination MAC address in a MAC address entry. |
| VLAN | ID of the VLAN that a MAC address belongs to. |
| Learned-From | Interface that learns a MAC address. |
| Type | Type of a MAC address entry.   * static: indicates a static MAC address entry, which is manually configured and will not be aged out. * blackhole: indicates a blackhole MAC address entry, which is manually configured and will not be aged out. * dynamic: indicates a MAC address entry learned by the switch, which will be aged out when the aging time expires. |
| Age | No value is displayed if dynamic MAC entries are queried. |
| Total items on chip 0 | Number of MAC address entries in chip 0. |