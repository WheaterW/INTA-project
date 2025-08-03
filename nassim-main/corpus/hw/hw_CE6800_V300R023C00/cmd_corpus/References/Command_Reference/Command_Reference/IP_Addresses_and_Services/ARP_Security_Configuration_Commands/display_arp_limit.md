display arp limit
=================

display arp limit

Function
--------



The **display arp limit** command displays the maximum number of ARP entries that an interface can learn and the corresponding alarm threshold.




Format
------

**display arp limit** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **vlan** *vlan-id*  ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies an interface. | - |
| **vlan** *vlan-id* | Specifies a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If the number of ARP entries that the device learns has reached the upper limit, it will cause some users unable to use the network normally, you can run this command to view the maximum number of ARP entries that each interface can learn and the number of ARP entries that each interface has learned.

**Precautions**

If you use this command on a Layer 2 or Layer 3 interface, both the maximum number of ARP entries that the Layer 2 or Layer 3 interface can learn and the number of ARP entries that the device has learnt are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about ARP entry learned on the device.
```
<HUAWEI> display arp limit
 Interface                         VLAN       Limit      Learnt     Threshold
-----------------------------------------------------------------------------------------
 Vlanif10                             0          10           0             -
-----------------------------------------------------------------------------------------
Total:1

```

**Table 1** Description of the **display arp limit** command output
| Item | Description |
| --- | --- |
| Interface | Interface type. |
| VLAN | ID of the VLAN to which the interface belongs. |
| Limit | Maximum number of ARP entries that the interface can learn. |
| Learnt | Number of ARP entries that the interface has learnt. |
| Threshold | Alarm threshold for the maximum number of ARP entries that the interface can learn, in percentage. |
| Total | Total number of interfaces. |