route-distinguisher (VPN instance view)
=======================================

route-distinguisher (VPN instance view)

Function
--------



The **route-distinguisher** command configures an RD for a VPN instance.

The **undo route-distinguisher** command deletes the RD configuration in a specified VPN instance.



By default, no RD is configured for a VPN instance.


Format
------

**route-distinguisher** *route-distinguisher*

**undo route-distinguisher** *route-distinguisher*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-distinguisher* | Route distinguisher (RD). | An RD has the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535, and a user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. That is, an RD cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0-255.255.255.255, and the user-defined number ranges from 0 to 65535. |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Conventional BGP cannot process the routes of VPNs with overlapped address spaces. To solve this problem, BGP/MPLS IP VPN uses the VPN-IPv4 address family. A VPN-IPv4 address has 12 bytes, including an 8-byte RD and a 4-byte IPv4 address prefix. RDs are used to distinguish IPv4 prefixes that use the same address space. The structure of RDs enables each service provider to allocate RDs independently. An IPv4 address with an RD is called a VPN-IPv4 address. After receiving IPv4 routes from a CE, a PE converts the routes to globally unique VPN-IPv4 routes and advertises these routes over the public network.



**Precautions**



Configuring a unique RD for a VPN instance IPv4 address family is recommended; otherwise, route overlapping may occur.If you run the **undo route-distinguisher** command to delete the RD configuration in a specified VPN instance IPv4 address family, the configurations in the address family and the **peer default-originate vpn-instance** command configuration in the VPNv4 address family will be deleted. Exercise caution when running this command.




Example
-------

# Configure an RD for the VPN instance named vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] route-distinguisher 22:1

```