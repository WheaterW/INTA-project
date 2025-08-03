mld snooping proxy-uplink-port
==============================

mld snooping proxy-uplink-port

Function
--------



The **mld snooping proxy-uplink-port** command configures an interface as an MLD snooping proxy uplink interface, so that MLD Query messages are not sent to this interface.

The **undo mld snooping proxy-uplink-port** command cancels an interface as an MLD snooping proxy uplink interface.



By default, no MLD snooping proxy uplink interface is configured in a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping proxy-uplink-port vlan** *vlan-id*

**undo mld snooping proxy-uplink-port vlan** *vlan-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies a VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the MLD snooping proxy or querier function is enabled on a Layer 2 device, the Layer 2 device broadcasts MLD Query messages to all interfaces (including router interfaces) in a VLAN periodically, which may trigger MLD querier reelection. To prevent MLD querier reelection, run the mld snooping proxy-uplink-port command to configure an interface as an MLD snooping proxy uplink interface, so that MLD Query messages are not sent to this interface.


Example
-------

# Configure 100GE 1/0/1 in VLAN 10 as an MLD snooping proxy uplink interface.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] mld snooping proxy-uplink-port vlan 10

```