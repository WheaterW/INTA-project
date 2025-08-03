mld snooping static-router-port vlan
====================================

mld snooping static-router-port vlan

Function
--------



The **mld snooping static-router-port vlan** command configures an interface as a static router interface in a VLAN.

The **undo mld snooping static-router-port vlan** command cancels the configuration.



By default, an interface is a dynamic router interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping static-router-port vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo mld snooping static-router-port vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **to** *vlan-id2* | Specifies the ending VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **all** | Indicates all VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If user hosts need to receive multicast data packets from an interface for a long period of time, run the mld snooping static-router-port command to configure the interface as a static router interface.


Example
-------

# Configure 100GE 1/0/1 as a static router interface of VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] mld snooping static-router-port vlan 2

```