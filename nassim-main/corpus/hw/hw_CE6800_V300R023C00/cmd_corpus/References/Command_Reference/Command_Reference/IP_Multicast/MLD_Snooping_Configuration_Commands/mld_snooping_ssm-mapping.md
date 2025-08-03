mld snooping ssm-mapping
========================

mld snooping ssm-mapping

Function
--------



The **mld snooping ssm-mapping** command configures the mapping between an any-source multicast group address in the source-specific multicast (SSM) range and a multicast source address.

The **undo mld snooping ssm-mapping** command deletes a configured mapping.



By default, no mapping is configured between an any-source multicast group address in the SSM range and a multicast source address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping ssm-mapping** *group-address* *mask-length* *source-address*

**undo mld snooping ssm-mapping** *group-address* *mask-length* *source-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies an IPv6 multicast group address in the SSM range. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. And the value must be within the group address range defined in the SSM policy. |
| *mask-length* | Specifies the mask length of an IPv6 multicast group address. | The value is an integer ranging from 8 to 128. |
| *source-address* | Specifies an IPv6 multicast source address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The SSM mapping mechanism is used to convert MLDv1 Report messages into messages with (S, G) information. This mechanism enables hosts that do not support MLDv2 to enjoy SSM services. After a mapping is configured between a multicast group G and multicast source addresses such as S1 and S2, the device checks the group addresses of received MLDv1 Report messages. If the group addresses are in the SSM group address range, the device converts the messages into one or multiple MLDv2 IS\_IN (S1, S2......) messages with the group address being G.


Example
-------

# Map the multicast group address FF33::1 in VLAN 10 to the multicast source address 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping ssm-mapping ff33::1 64 2001:db8:1::1

```