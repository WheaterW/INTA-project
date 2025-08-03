local-address (IPv6 anycast-RP view)
====================================

local-address (IPv6 anycast-RP view)

Function
--------



The **local-address** command sets a local address for an Anycast Rendezvous Point (RP).

The **undo local-address** command deletes the local address set for an Anycast RP.



By default, no local address is set for an Anycast RP.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**local-address** *local-address*

**undo local-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-address* | Specifies the local address of Anycast RP. | The value must be a valid IPv6 unicast IP address in hexadecimal notation. |



Views
-----

IPv6 anycast-RP view,VPN instance IPv6 anycast-RP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the Anycast RP is configured in a multicast domain, after an RP receives a Register message, it checks the source address in the Register message. If the Register message is sent by the source's designated router (DR), the RP forwards the Register message to Anycast RP peers. If the Register message is sent by an Anycast RP peer, it does not forward the Register message.When forwarding a PIM Register message to other Anycast RP peers, the local RP needs to use its own IP address (called the local address) as the source address of the Register message and use the addresses of Anycast RP peers as the destination addresses of the Register message. In such a manner, Anycast RP peers can learn source/group information from each other. The local-address command is used to set a local address for an Anycast RP.

**Precautions**

The local address must be different from the Anycast RP address.Setting a Loopback interface address as the local address of the Anycast RP is recommended.


Example
-------

# Set the local address of Anycast RP to 2001:DB8:11::1 in the IPv6 Anycast-RP view.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] anycast-rp 2001:DB8:1::1
[*HUAWEI-pim6-anycast-rp-2001:DB8:1::1] local-address 2001:DB8:11::1

```