lacp port-id-extension enable
=============================

lacp port-id-extension enable

Function
--------



The **lacp port-id-extension enable** command increases the ID of each member interface in an Eth-Trunk interface in LACP mode by 32768.

The **undo lacp port-id-extension enable** command restores the ID of each member interface in an Eth-Trunk interface in LACP mode.



By default, the system automatically allocates a number to each member interface in an Eth-Trunk interface.


Format
------

**lacp port-id-extension enable**

**undo lacp port-id-extension enable**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, the ID of each Eth-Trunk member interface on DeviceB and DeviceC is assigned by the system. When DeviceA is dual-homed to DeviceB and DeviceC through an Eth-Trunk interface in LACP mode, the IDs of Eth-Trunk member interfaces on DeviceB and DeviceC may be the same, causing LACP negotiation failure or the failure in locating forwarding interfaces. To ensure that the dual-homed Eth-Trunk interface in LACP mode can forward traffic and implement load balancing, run the **lacp port-id-extension enable** command on either DeviceB or DeviceC to increase the ID of each member interface of the Eth-Trunk interface in LACP mode by 32768. As a result, the IDs of Eth-Trunk member interfaces on DeviceB and DeviceC are not the same.



**Prerequisites**



Before running the **lacp port-id-extension enable** command, you must ensure that the **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in LACP mode.



**Follow-up Procedure**



Run the **display eth-trunk** command to check the LACP member interfaces ID.




Example
-------

# Increase the ID of each member interface in an Eth-Trunk interface in LACP mode by 32768.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] lacp port-id-extension enable

```