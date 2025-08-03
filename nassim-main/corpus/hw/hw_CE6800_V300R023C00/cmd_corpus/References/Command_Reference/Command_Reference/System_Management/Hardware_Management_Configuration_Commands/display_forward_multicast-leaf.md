display forward multicast-leaf
==============================

display forward multicast-leaf

Function
--------



The **display forward multicast-leaf** command displays the number of multicast leaf resources.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display forward multicast-leaf**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The AIB table and ELB table share the internal forwarding table resources of the chip. The AIB table resources include ARP, ND, VXLAN, and IP tunnel services. The ELB table resources include various multicast services such as VLAN, L3MC, and VXLAN, and you can run this command to check the number of ELBs configured for multicast leaf nodes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of resource number of multicast leaf.
```
<HUAWEI> display forward multicast-leaf
Current system multicast-leaf number   : 64
Configured system multicast-leaf number: 96

```

**Table 1** Description of the **display forward multicast-leaf** command output
| Item | Description |
| --- | --- |
| Current system multicast-leaf number | Current system multicast-leaf number:   * 64: 64K(65536). * 80: 80K(81920). * 96: 96K(98304). * 112: 112K(114688). * 128: 128K(131072). |
| Configured system multicast-leaf number | Number of configured multicast leaf resources, which takes effect after the next restart. The value can be:   * 64: 64K(65536). * 80: 80K(81920). * 96: 96K(98304). * 112: 112K(114688). * 128: 128K(131072). |