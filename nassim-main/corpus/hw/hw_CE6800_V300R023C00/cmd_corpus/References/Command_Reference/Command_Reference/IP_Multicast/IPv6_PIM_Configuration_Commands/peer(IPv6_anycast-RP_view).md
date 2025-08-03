peer(IPv6 anycast-RP view)
==========================

peer(IPv6 anycast-RP view)

Function
--------



The **peer** command configures Anycast Rendezvous Point (RP) peers.

The **undo peer** command removes the configurations of Anycast RPs.



By default, no Anycast RP peer is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *RpPeerAddress*

**undo peer** *RpPeerAddress*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *RpPeerAddress* | Specifies the address of an Anycast RP peer. | The value is in hexadecimal notation. |



Views
-----

IPv6 anycast-RP view,VPN instance IPv6 anycast-RP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If PIM Anycast RP is configured, after an RP receives a Register message, it checks the source address in the Register message. If the Register message is sent by the source's designated router (DR), the RP forwards the Register message to Anycast RP peers. If the Register message is sent by an Anycast RP peer, it does not forward the Register message.When forwarding a PIM Register message to other Anycast RP peers, the local RP needs to use its own IP address (called the local address) as the source address of the Register message and use the addresses of Anycast RP peers as the destination addresses of the Register message. In such a manner, Anycast RP peers can learn source/group information from each other. This command is used to configure an address for an Anycast RP peer. This address is used as the destination address of the Register message to be sent by the local RP.

**Precautions**

You can specify a maximum of 16 Anycast RP peers for each Anycast RP.In a PIM-SM domain, all the devices deployed with Anycast RP must be fully connected logically. Anycast RP peer relationships need to be configured between every two devices deployed with the Anycast RP.


Example
-------

# In the public network instance view, set the Anycast RP address to 2001:DB8::1 and the peer address to 2001:DB8::2.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] anycast-rp 2001:DB8::1
[*HUAWEI-pim6-anycast-rp-2001:DB8::1] peer 2001:DB8::2

```