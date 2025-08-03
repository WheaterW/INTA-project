mld snooping querier enable
===========================

mld snooping querier enable

Function
--------



The **mld snooping querier enable** command enables the querier function for a VLAN.

The **undo mld snooping querier enable** disables the querier function for a VLAN.



By default, the querier is disabled for a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping querier enable**

**undo mld snooping querier enable**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the querier function is enabled using the mld snooping querier enable command on a Layer 2 device, this device will send MLD Query messages, freeing its interworking upstream device from doing this. The Layer 2 device will then also create and maintain multicast forwarding entries to forward data at the link layer.Before running themld snooping querier enable command, note the following points:

* Static multicast groups have been configured on the upstream device. Otherwise, user join messages cannot be sent to the upstream device, and multicast data flows cannot be sent to receivers.
* If the links from a multicast source to user hosts are on the same Layer 2 network, the querier function can be enabled on a Layer 2 device. This does not affect the normal receiving of multicast data packets.

Example
-------

# Enable the querier function for VLAN 10.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping querier enable

```