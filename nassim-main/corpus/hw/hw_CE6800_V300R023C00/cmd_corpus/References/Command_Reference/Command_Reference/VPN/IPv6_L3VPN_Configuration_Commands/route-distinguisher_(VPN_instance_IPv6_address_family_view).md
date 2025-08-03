route-distinguisher (VPN instance IPv6 address family view)
===========================================================

route-distinguisher (VPN instance IPv6 address family view)

Function
--------



The **route-distinguisher** command configures an RD for a VPN instance IPv6 address family.

The **undo route-distinguisher** command deletes the RD configuration in a specified VPN instance IPv6 address family.



By default, no RD is configured for a VPN instance IPv6 address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**route-distinguisher** *route-distinguisher*

**undo route-distinguisher** *route-distinguisher*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-distinguisher* | Specifies an RD. | The three formats of an RD are as follows:   * 16-bit AS number: 32-bit user-defined number. For example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. This means that an RD cannot be 0:0. * Integral 4-byte AS number: 2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 0 to 4294967295. A user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. This means that an RD cannot be 0:0. * 4-byte AS number in dotted notation: 2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. The user-defined number also ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. This means that an RD cannot be 0.0:0. * 32-bit IP address: 16-bit user-defined number. For example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Conventional BGP cannot process the routes of VPNs with overlapped address spaces. To solve this problem, BGP/MPLS IP VPN uses the VPN-IPv6 address family. A VPN-IPv6 address has 24 bytes, including an 8-byte RD and a 16-byte IPv6 address prefix. RDs are used to distinguish IPv6 prefixes that use the same address space. The structure of RDs enables each service provider to allocate RDs independently. An IPv6 address with an RD is called a VPN-IPv6 address. After receiving IPv6 routes from a CE, a PE converts the routes to globally unique VPN-IPv6 routes and advertises these routes over the public network.

**Precautions**

An RD must be configured prior to other IPv6 VPN configurations. This means that an RD must be configured for a VPN instance IPv6 address family before other VPN configurations are performed.Configuring a unique RD for a VPN instance IPv6 address family is recommended; otherwise, route overlapping may occur.If you run the **undo route-distinguisher** command to delete the RD configuration in a specified VPN instance IPv6 address family, the configurations in the address family and the **peer default-originate vpn-instance** command configuration in the VPNv6 address family will be deleted. Exercise caution when running this command.


Example
-------

# Configure an RD for a VPN instance IPv6 address family.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 22:1

```