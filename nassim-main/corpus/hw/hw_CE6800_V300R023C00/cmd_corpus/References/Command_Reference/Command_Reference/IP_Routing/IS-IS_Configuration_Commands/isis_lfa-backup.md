isis lfa-backup
===============

isis lfa-backup

Function
--------



The **isis lfa-backup** command enables an IS-IS interface to participate in Loop-Free Alternate (LFA) calculation.

The **undo isis lfa-backup** command disables an IS-IS interface from participating in LFA calculation.

The **isis lfa-backup disable** command disables an IS-IS interface from participating in LFA calculation.

The **undo isis lfa-backup disable** command enables an IS-IS interface to participate in LFA calculation.



By default, an IS-IS interface can participate in LFA calculation.


Format
------

**isis lfa-backup** [ **level-1** | **level-1-2** | **level-2** ]

**isis lfa-backup** [ **level-1** | **level-1-2** | **level-2** ] **disable**

**undo isis lfa-backup** [ **level-1** | **level-1-2** | **level-2** ]

**undo isis lfa-backup** [ **level-1** | **level-1-2** | **level-2** ] **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Adds an interface to a Level-1 area. | - |
| **level-1-2** | Adds an interface to a Level-1 and a Level-2 area. | - |
| **level-2** | Adds an interface to a Level-2 area. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, FRR calculates a backup link based on the LFA algorithm, and the backup link together with the active link is added to the forwarding table. If an error occurs on the network, FRR can fast switch traffic to the backup link before route convergence on the control plane. This feature ensures uninterrupted traffic forwarding and greatly improves the reliability of IS-IS networks.By default, an IS-IS interface can participate in LFA calculation. However, some backup links are uncertain when an active link is faulty. To prevent traffic from being transmitted along a link, you can run the **undo isis lfa-backup** command on the interface on the link to disable the interface from participating in the LFA calculation.

**Precautions**



To ensure that FRR can function properly, do not disable all interfaces from participating in the LFA calculation.




Example
-------

# Disable 100GE1/0/1 from becoming the backup interface of Auto FRR.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] undo isis lfa-backup

```