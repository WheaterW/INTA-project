ipv6-family (VPN instance view)
===============================

ipv6-family (VPN instance view)

Function
--------



The **ipv6-family** command enables the IPv6 address family for a VPN instance.

The **undo ipv6-family** command disables the IPv6 address family for a VPN instance.



By default, the IPv6 address family is disabled for a VPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6-family** [ **unicast** ]

**undo ipv6-family** [ **unicast** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unicast** | Displays the unicast address family view. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In L3VPNv6 networking, after you run the **ip vpn-instance** command to create a VPN instance, you can run the ipv6-family command to enable the IPv6 address family for the VPN instance and perform VPN configurations in the address family view if you want to have IPv6 VPN routes advertised and IPv6 VPN data forwarded.

**Follow-up Procedure**



Run the **route-distinguisher** command to configure an RD for the IPv6 address family of the VPN instance. VPN configurations can be performed in the IPv6 address family view only after an RD is configured for the IPv6 address family of the VPN instance.



**Precautions**



After the IPv6 address family for a VPN instance is disabled using the **undo ipv6-family** command, configurations in the IPv6 address family as well as the IPv6 address family-related configurations in the BGP view will be deleted. Therefore, exercise caution when you run this command.




Example
-------

# Enable the IPv6 address family for a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6]

```