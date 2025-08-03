display mac-vlan
================

display mac-vlan

Function
--------



The **display mac-vlan** command displays MAC-VLAN entries when VLANs are classified based on MAC addresses.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mac-vlan** { **vlan** *vlan-id* | **mac-address** { *mac-address* | **all** } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays the MAC-VLAN entries of a specified VLAN. | The value is an integer ranging from 1 to 4094. |
| **mac-address** *mac-address* | Specifies the MAC address to be queried. | The format is H-H-H. H is a hexadecimal number ranging from 1 to 4, for example, 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **all** | Displays all MAC-VLAN entries. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After VLAN classification based on MAC addresses is configured, you can run **display mac-vlan** command to view MAC-VLAN entries.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View all MAC-VLAN entries.
```
<HUAWEI> display mac-vlan mac-address all
Total MAC VLAN address count: 1
---------------------------------------------------
MAC Address     Mask            VLAN    Priority   
---------------------------------------------------
00e0-fc12-3456  ffff-ffff-ffff  10      0

```

**Table 1** Description of the **display mac-vlan** command output
| Item | Description |
| --- | --- |
| Total MAC VLAN address count | Total number of MAC address entries displayed. |
| MAC Address | MAC address associated with the specified VLAN ID. |
| VLAN | VLAN ID associated with the MAC address. |
| Mask | Mask associated with the MAC-VLAN entry. |
| Priority | 802.1p priority of the VLAN for the MAC address. |