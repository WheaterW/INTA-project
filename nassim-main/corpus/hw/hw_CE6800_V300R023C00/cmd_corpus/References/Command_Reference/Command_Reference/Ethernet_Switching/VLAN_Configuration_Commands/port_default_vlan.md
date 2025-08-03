port default vlan
=================

port default vlan

Function
--------



The **port default vlan** command sets a default VLAN for interfaces and adds interfaces to the VLAN.

The **undo port default vlan** command deletes the interfaces from the default VLAN and restores the default VLAN ID.



By default, the VLAN ID of all interfaces is 1.


Format
------

**port default vlan** *vlan-id*

**undo port default vlan** [ *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Frames sent from user hosts are untagged and those sent from a remote device may also be untagged. However, a switching device only processes and forwards tagged frames. Therefore, tags need to be added to the untagged frames on the switching device. To implement this function, run the port default vlan command to configure a default VLAN on an interface of the switching device. After this function is enabled, the interface adds the default VLAN ID to received untagged frames.

**Prerequisites**

A VLAN has been created.The link type of the interface has been configured as access using the **port link-type** command.

**Precautions**



A super VLAN cannot be configured as a default VLAN.The port default vlan command has the same function as the **port** command in the VLAN view.The interface to be added to a VLAN must be a Layer 2 interface. If the interface is a Layer 3 interface, run the **portswitch** command to switch the interface to Layer 2.The port default vlan command cannot be configured on physical interfaces that are added to an Eth-Trunk.




Example
-------

# Add 100GE1/0/1 into VLAN 3.
```
<HUAWEI> system-view
[~HUAWEI] vlan 3
[*HUAWEI-vlan3] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port default vlan 3

```