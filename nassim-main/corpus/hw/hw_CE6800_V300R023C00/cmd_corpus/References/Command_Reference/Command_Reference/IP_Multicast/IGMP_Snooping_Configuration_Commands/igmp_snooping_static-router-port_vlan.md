igmp snooping static-router-port vlan
=====================================

igmp snooping static-router-port vlan

Function
--------



The **igmp snooping static-router-port vlan** command configures a static router port.

The **undo igmp snooping static-router-port vlan** command cancels the configuration.



By default, a dynamic router port is used.


Format
------

**igmp snooping static-router-port vlan** { *vid1* [ **to** *vid2* ] } &<1-10>

**undo igmp snooping static-router-port vlan** { { *vid1* [ **to** *vid2* ] } &<1-10> | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vid1* | Specifies a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The vlan-id value ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value ranges from 1 to 1023. |
| **to** *vid2* | Specifies a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The vlan-id value ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value ranges from 1 to 1023. |
| **all** | Specifies all VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If user hosts need to receive multicast data packets from a port for a long period of time, the igmp snooping static-router-port vlan command can be used to configure the port as a static router port.Static router ports can be configured on different positions on a network to enable user hosts to regularly receive data for specific multicast groups or source-specific multicast groups. The commands listed in the following table can be run in any order. Run one or more commands as required to configure static router ports. For details, see Table Description of the igmp snooping static-router-port vlan command in different scenarios.

**Prerequisites**

IGMP snooping has been configured globally and in a VLAN.

**Configuration Impact**

A static router port does not age. To delete a static router port, you must run the **undo igmp snooping static-router-port vlan** command.If the igmp snooping static-router-port vlan command is run more than once, all configurations take effect.


Example
-------

# Configure 100GE1/0/1 as a static router port in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] igmp snooping static-router-port vlan 2

```