vpn-target evpn (VPN instance IPv6 address family view)
=======================================================

vpn-target evpn (VPN instance IPv6 address family view)

Function
--------



The **vpn-target evpn** command configures the VPN target extended community attribute for EVPN routes in the VPN instance IPv6 address family.

The **undo vpn-target evpn** command deletes the VPN target extended community attribute of EVPN routes in the VPN instance IPv6 address family.



By default, no VPN target extended community list is configured for EVPN routes in the VPN instance IPv6 address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vpn-target** { *vpn-target* } &<1-8> [ *vrfRtType* ] **evpn**

**undo vpn-target** { *vpn-target* } &<1-8> [ *vrfRtType* ] **evpn**

**undo vpn-target all evpn**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-target* | Specifies the VPN target to be added to the VPN target list of a VPN instance IPv6 address family. | The three formats of a VPN target are as follows:   * 16-bit AS number:32-bit user-defined number. For example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. This means that a VPN target cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 0 to 4294967295. A user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. This means that a VPN target cannot be 0:0. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. The user-defined number also ranges from 0 to 65535. For example, a VPN target can be 0.0:3 or 0.1:0. The AS number and user-defined number cannot be both 0s. This means that a VPN target cannot be 0.0:0. * 32-bit IP address:16-bit user-defined number. For example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. |
| *vrfRtType* | Adds a VPN target to the VPN target list of a VPN instance IPv6 address family. | The value is an enumerated type:   * both: adds a VPN target to both the import and export VPN target lists of a VPN instance IPv6 address family. If both, export-extcommunity, and import-extcommunity are not configured in the vpn-target command, a VPN target is added to both lists by default. * export-extcommunity: adds a VPN target to the export VPN target list of a VPN instance IPv6 address family. * import-extcommunity: adds a VPN target to the import VPN target list of a VPN instance IPv6 address family. |
| **all** | Delete all the VPN targets of a VPN instance IPv6 address family. | - |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When advertising EVPN IPv6 prefix routes to other PE peers, the local PE must carry all VPN targets in the export VPN target list configured for EVPN routes in the local VPN instance IPv6 address family. If the VPN targets carried in received IRBv6 routes or IPv6 prefix routes overlap with those in the import VPN targets list of EVPN routes in the local VPN instance IPv6 address family, only the IRBv6 route or IPv6 prefix route can be added to the routing table of the local VPN instance IPv6 address family.

**Prerequisites**

The **ipv6-family** command has been run in the VPN instance view to enable the IPv6 address family, and the **route-distinguisher** command has been run in the VPN instance view to set an RD for the VPN instance IPv6 address family.

**Configuration Impact**

If the vpn-target evpn command is not used, a PE does not install received IRBv6 routes or IPv6 prefix routes into the routing table of its VPN instance IPv6 address family.After the **undo vpn-target evpn** command is run, all routes learned through IRBv6 routes or IPv6 prefix routes in the VPN instance address family are deleted.


Example
-------

# Add 5:5 to the VPN target list of EVPN routes in the VPN instance IPv6 address family.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv6] vpn-target 5:5 evpn

```