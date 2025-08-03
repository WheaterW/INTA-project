isis ipv6 lfa-backup
====================

isis ipv6 lfa-backup

Function
--------



The **isis ipv6 lfa-backup** command enables an IS-IS IPv6 interface to participate in Loop-Free Alternate (LFA) calculation.

The **undo isis ipv6 lfa-backup** command disables an IS-IS IPv6 interface from participating in LFA calculation.

The **isis ipv6 lfa-backup disable** command disables an IS-IS IPv6 interface from participating in LFA calculation.

The **undo isis ipv6 lfa-backup disable** command enables an IS-IS IPv6 interface to participate in LFA calculation.



By default, an IS-IS IPv6 interface can participate in LFA calculation.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 lfa-backup** [ **level-1** | **level-1-2** | **level-2** ]

**isis ipv6 lfa-backup** [ **level-1** | **level-1-2** | **level-2** ] **disable**

**undo isis ipv6 lfa-backup** [ **level-1** | **level-1-2** | **level-2** ]

**undo isis ipv6 lfa-backup** [ **level-1** | **level-1-2** | **level-2** ] **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Enables an IPv6 interface to participate in LFA calculation in a Level-1 area. | - |
| **level-1-2** | Enables an IPv6 interface to participate in LFA calculation in Level-1 and Level-2 areas. | - |
| **level-2** | Enables an interface to participate in LFA calculation in a Level-2 area. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, FRR calculates a backup link based on the LFA algorithm, and the backup link together with the active link is added to the forwarding table. If an error occurs on the network, FRR can fast switch traffic to the backup link before route convergence on the control plane. This feature ensures uninterrupted traffic forwarding and greatly improves the reliability of IS-IS networks.By default, an IS-IS IPv6 interface can participate in LFA calculation. However, some backup links are uncertain when an active link is faulty. To prevent traffic from being transmitted along a link, you can run the **undo isis ipv6 lfa-backup** command on the IPv6 interface on the link to disable the interface from participating in the LFA calculation.

**Prerequisites**

IPv6 IS-IS has been enabled running the **isis ipv6 enable** command on a specified interface.

**Precautions**

To ensure that FRR can function properly, do not disable all interfaces from participating in the LFA calculation.


Example
-------

# Disable 100GE1/0/1 from becoming a backup interface for IPv6 IS-IS auto FRR.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable
[*HUAWEI-100GE1/0/1] undo isis ipv6 lfa-backup

```