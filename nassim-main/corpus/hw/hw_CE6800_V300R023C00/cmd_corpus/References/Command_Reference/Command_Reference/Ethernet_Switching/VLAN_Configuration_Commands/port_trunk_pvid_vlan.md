port trunk pvid vlan
====================

port trunk pvid vlan

Function
--------



The **port trunk pvid vlan** command sets a default VLAN ID for a trunk interface.

The **undo port trunk pvid vlan** command restores the default VLAN ID of a trunk interface.



By default, the default VLAN of a trunk interface is VLAN1.


Format
------

**port trunk pvid vlan** *vlan-id*

**undo port trunk pvid vlan** [ *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a default VLAN ID of a trunk interface. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

All Ethernet frames are forwarded in tagged form. A device must add tags to received untagged frames. To implement this, run the port trunk pvid vlan to configure a default VLAN for an interface. The interface adds the default VLAN ID to received untagged frames.

**Prerequisites**



A VLAN has been created.



**Configuration Impact**



If the **port trunk pvid vlan** command is run more than once, the last configuration overrides the previous one.



**Follow-up Procedure**



Add a trunk interface to the created VLAN or VLANs.



**Precautions**



Default VLAN packets may not be allowed to pass through an interface. To allow them to pass through the interface, run the **port trunk allow-pass** command to add the interface to the default VLAN .




Example
-------

# Set the default VLAN to VLAN 5 for interfaces.
```
<HUAWEI> system-view
[~HUAWEI] vlan 5
[*HUAWEI-vlan5] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk pvid vlan 5

```