port hybrid pvid vlan
=====================

port hybrid pvid vlan

Function
--------



The **port hybrid pvid vlan** command sets a default VLAN ID for a hybrid interface.

The **undo port hybrid pvid vlan** command restores the default VLAN ID of a hybrid interface.



By default, the VLAN ID of all interfaces is 1.


Format
------

**port hybrid pvid vlan** *vlan-id*

**undo port hybrid pvid vlan** [ *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies a default VLAN ID of a hybrid interface. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

All Ethernet frames are forwarded in tagged forms on a switching device. A device must add tags to received untagged frames. To implement this, run the **port hybrid pvid vlan** command to configure a default VLAN ID for an interface. If the interface receives untagged frames, it adds a default VLAN ID to the frames.After a default VLAN ID is set on a hybrid interface:

* When the interface receives untagged packets, it adds the default VLAN ID to the packets. If the default VLAN is in the list of VLANs whose packets are allowed to pass, the interface accepts the packets and adds the default VLAN ID to the packets; if the default VLAN is not in the list, the interface discards the packets.
* When the interface receives tagged packets, if the default VLAN is in the list of VLANs whose packets are allowed to pass, the interface accepts the packets; if the default VLAN is not in the list, the interface discards the packets.
* When the interface sends packets, if the default VLAN is in the list of VLANs whose packets are allowed to pass, the interface sends the packets. You can configure whether the packets carry the tag when the interface sends the packets.

**Prerequisites**



Before running the **port hybrid pvid vlan** command to configure the default VLAN of an interface, ensure that the VLAN has been created.



**Configuration Impact**



If the **port hybrid pvid vlan** command is run more than once on the same interface, the latest configuration overrides the previous one.



**Precautions**



This command cannot be configured on a physical interface that has been added to an Eth-Trunk interface.The **port hybrid pvid vlan** command only configures a default VLAN ID for an interface, not adds the interface to the VLAN.




Example
-------

# Set the default VLAN to VLAN 5 for interfaces.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] port link-type hybrid
[*HUAWEI-100GE1/0/1] port hybrid pvid vlan 5

```