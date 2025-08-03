mld snooping send-query source-address
======================================

mld snooping send-query source-address

Function
--------



The **mld snooping send-query source-address** command sets a source IP address for MLD Query messages.

The **undo mld snooping send-query source-address** command restores the source IP address to FE80::.



By default, the source IP address of an MLD Query message is FE80::.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping send-query source-address** *ip-address*

**undo mld snooping send-query source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a source IP address for MLD general Query messages. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the topology of a Layer 2 ring network changes, interfaces in a relevant VLAN will receive a link change event. After the mld snooping send-query source-address command is run on a device on the ring network, the device will send MLD general Query messages with the default source address FE80:: to all non-router interfaces in the VLAN, so that the other devices can quickly update router interface information.If FE80:: is being used by other devices, run the mld snooping send-query source-address command to set a new source IP address for MLD General Query messages.


Example
-------

# Set the source IP address to FE80:1::1 for MLD general Query messages.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping send-query source-address fe80::1

```