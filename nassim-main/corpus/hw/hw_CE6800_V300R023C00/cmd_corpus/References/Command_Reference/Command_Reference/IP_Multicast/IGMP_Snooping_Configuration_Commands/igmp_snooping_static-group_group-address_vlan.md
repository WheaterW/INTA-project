igmp snooping static-group group-address vlan
=============================================

igmp snooping static-group group-address vlan

Function
--------



The **igmp snooping static-group group-address vlan** command configures a static member interface.

The **undo igmp snooping static-group group-address vlan** command cancels the configuration.



By default, a dynamic member interface is used.


Format
------

**igmp snooping static-group** [ **source-address** *source-address* ] **group-address** *group-address* **vlan** { *vid1* [ **to** *vid2* ] } &<1-10>

**undo igmp snooping static-group** [ **source-address** *source-address* ] **group-address** { **all** | *group-address* } **vlan** { **all** | { *vid1* [ **to** *vid2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-address** *source-address* | Specifies a multicast source address. | The value is a string of case-sensitive characters ranging from 1.0.0.0 to 223.255.255.255.255, spaces not supported. |
| *group-address* | Specifies a multicast group address. | The value is a string of case-sensitive characters ranging from 224.0.1.0 to 239.255.255.255, spaces not supported. |
| *vid1* | Specifies a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vid2* | Specifies a VLAN and the value is larger than vlan-id1. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Indicates all of multicast groups. | - |
| **all** | Indicates multicast groups in all VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If hosts connected to an interface need to regularly receive data for a multicast group or a source-specific multicast group, the igmp snooping static-group group-address vlan command can be used to configure the interface as a static member interface.Static member interfaces can be configured on different positions on a network to enable users to receive data for specific multicast groups or source-specific multicast groups regularly. The commands listed in the following table can be run in any order. Run one or more commands as required to configure static member interfaces. For details, see Table Description of the igmp snooping static-group group-address vlan command in different scenarios.

**Prerequisites**

IGMP snooping has been configured globally and in a VLAN.

**Configuration Impact**

A static member interface does not respond to IGMP Query messages. After the undo igmp snooping static-group group-address vlan command is run on a static member interface, the interface does not initiate an IGMP Leave message.If the igmp snooping static-group group-address vlan command is run more than once, all configurations take effect.

**Precautions**

If the number of (S, G) entries relevant to a group has reached the maximum value (128), no static entry will be created after the igmp snooping static-group group-address vlan command is run. This means that no entry relevant to a static multicast group will be generated even after the reset igmp snooping group all reset command is run in the system view to refresh entries.


Example
-------

# Configure 100GE 1/0/1 in a VLAN as a static member interface and configure the static member interface to join multicast group 224.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] igmp snooping static-group group-address 224.1.1.1 vlan 2

```