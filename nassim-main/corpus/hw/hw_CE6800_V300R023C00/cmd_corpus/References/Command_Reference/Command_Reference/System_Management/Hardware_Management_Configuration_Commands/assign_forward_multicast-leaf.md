assign forward multicast-leaf
=============================

assign forward multicast-leaf

Function
--------



The **assign forward multicast-leaf** command configures the number of multicast service leaf resources.

The **undo assign forward multicast-leaf** command restores the default number of multicast leaf resources.



By default, the number of multicast leaf resources is 64K.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**assign forward multicast-leaf** { **64** | **80** | **96** | **112** | **128** }

**undo assign forward multicast-leaf** [ **80** | **96** | **112** | **128** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **64** | Indicates that the number of multicast leaf resources is 64K (65536). | - |
| **80** | Indicates that the number of multicast leaf resources is 80K (81920). | - |
| **96** | Indicates that the number of multicast leaf resources to 96K (98304). | - |
| **112** | Indicates that the number of multicast leaf resources is 112K (114688). | - |
| **128** | Indicates that the number of multicast leaf resources is 128K (131072). | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The AIB table and ELB table share forwarding table resources inside the chip. The AIB table resources include ARP, ND, VXLAN and IP tunnel services and the ELB table resources include VLAN, L3MC and VXLAN multicast services. You can run this command to set the number of multicast leaf ELB resources to meet the requirements of different scenarios on multicast leaf specifications.

**Precautions**

This function takes effect only after the device is restarted.


Example
-------

# Set the number of multicast leaf resources.
```
<HUAWEI> system-view
[~HUAWEI] assign forward multicast-leaf 96
Info: Please save configuration before restart. The new resource mode will take effect after the system reboot.

```