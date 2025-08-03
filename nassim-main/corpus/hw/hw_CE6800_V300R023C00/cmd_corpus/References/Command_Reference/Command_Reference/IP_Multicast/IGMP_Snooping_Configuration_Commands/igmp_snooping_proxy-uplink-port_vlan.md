igmp snooping proxy-uplink-port vlan
====================================

igmp snooping proxy-uplink-port vlan

Function
--------



The **igmp snooping proxy-uplink-port vlan** command configures an interface as an IGMP snooping proxy uplink interface. No IGMP Query message can be sent to this interface.

The **undo igmp snooping proxy-uplink-port vlan** command cancels the configuration.



By default, no IGMP snooping proxy uplink interface exists in a VLAN.


Format
------

**igmp snooping proxy-uplink-port vlan** *vlan-id*

**undo igmp snooping proxy-uplink-port vlan** *vlan-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Indicates a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the IGMP snooping proxy or querier function is enabled on a Layer 2 device, the Layer 2 device broadcasts IGMP Query messages to all interfaces (including router interfaces) in a VLAN periodically, which may trigger IGMP querier reelection. To prevent IGMP querier reelection, run the igmp snooping proxy-uplink-port command on the router interface to disable the Layer 2 device from sending IGMP Query messages to the router interface in a VLAN.

**Prerequisites**

IGMP snooping proxy has been enabled using the **igmp snooping proxy** command in the VLAN view, or IGMP snooping querier has been enabled using the **igmp snooping querier enable** command in the VLAN view.

**Precautions**

Only one IGMP snooping proxy unlink interface can be configured in a VLAN.


Example
-------

# Configure a 100GE 1/0/1 in VLAN 10 as an IGMP snooping proxy uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] igmp snooping proxy-uplink-port vlan 10

```