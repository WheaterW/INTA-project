anycast-rp (VPN instance IPv6 PIM view)
=======================================

anycast-rp (VPN instance IPv6 PIM view)

Function
--------



The **anycast-rp** command configures an anycast-rendezvous point (Anycast-RP) and displays the IPv6 Anycast-RP view or displays an existing IPv6 Anycast-RP view.

The **undo anycast-rp** command deletes an Anycast-RP.



By default, no Anycast-RP is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**anycast-rp** *rp-address*

**undo anycast-rp** *rp-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rp-address* | Specifies an Anycast-RP address. | The value is in hexadecimal notation. This address must be a valid IPv6 unicast address |



Views
-----

VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a traditional Protocol Independent Multicast-Sparse Mode (PIM-SM) domain, all multicast groups map to one RP. When the network is overloaded or all traffic needs to be forwarded by only one RP, the RP may be overburdened. If the RP fails, routes are converged slowly or multicast packets are forwarded over non-optimal paths.To resolve this issue, run the anycast-rp command to configure an Anycast-RP in the PIM-SM domain, enabling the network to automatically select a topologically closest RP for each source and receiver. This function releases burdens on RPs, implements RP backup, and optimizes the forwarding paths.


Example
-------

# Set the Anycast-RP address to 2001:db8:2::2 and enter the IPv6 Anycast-RP view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] ipv6-family
[*HUAWEI-vpn-instance-abc-af-ipv6] route-distinguisher 1003:1
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 routing-enable
[*HUAWEI-vpn-instance-abc-af-ipv6] quit
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] pim ipv6 vpn-instance abc
[*HUAWEI-pim6-abc] anycast-rp 2001:db8:2::2
[*HUAWEI-pim6-abc-anycast-rp-2001:db8:2::2]

```