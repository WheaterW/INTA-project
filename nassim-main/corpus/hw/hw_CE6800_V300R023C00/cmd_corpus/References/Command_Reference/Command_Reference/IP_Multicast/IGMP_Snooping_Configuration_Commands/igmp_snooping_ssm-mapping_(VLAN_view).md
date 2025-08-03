igmp snooping ssm-mapping (VLAN view)
=====================================

igmp snooping ssm-mapping (VLAN view)

Function
--------



The **igmp snooping ssm-mapping** command configures a mapping between a multicast group address within the Source Specific Multicast Mapping (SSM) group address range and a multicast source address.

The **undo igmp snooping ssm-mapping** command cancels the configuration.



By default, there is no mapping between a group address within the SSM group address range and a multicast source address.


Format
------

**igmp snooping ssm-mapping** *group-address* { *group-mask* | *mask-length* } *source-address*

**undo igmp snooping ssm-mapping** *group-address* { *group-mask* | *mask-length* } *source-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies a multicast group address. | The value is in dotted decimal notation and must be within the group address range defined in an SSM policy. |
| *group-mask* | Specifies the mask of a multicast group address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast group address. | The value is an integer ranging from 4 to 32. |
| *source-address* | Specifies a multicast source address to be mapped to a multicast group. | The value is in dotted decimal notation. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The SSM mapping mechanism is used to convert IGMPv1 and IGMPv2 Report messages into (S, G) Report messages. This mechanism enables hosts that do not support IGMPv3 to enjoy SSM services. After a mapping between a multicast group G and multicast source addresses such as S1 and S2 is configured on a device, the device checks the group addresses of received IGMPv1 and IGMPv2 messages. If the group addresses are in the SSM group address range, the device converts the messages into an IGMPv3 IS\_IN (S1, S2......) messages with the group address being G.

**Prerequisites**

The igmp ssm mapping enable command has been run to enable SSM mapping.

**Precautions**

After an SSM mapping policy is configured using the igmp snooping ssm-mapping enable [ policy policy-name ] command, the command cannot be run to configure SSM source/group address mapping entries.


Example
-------

# Configure a mapping between the multicast group address 238.0.0.1 to the multicast source address 10.1.1.1 in VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] igmp snooping ssm-mapping 238.0.0.1 24 10.1.1.1

```