vpn-target evpn (VPN instance view)
===================================

vpn-target evpn (VPN instance view)

Function
--------



The **vpn-target evpn** command configures the VPN target extended community attribute for EVPN routes in the VPN instance.

The **undo vpn-target evpn** command deletes the VPN target extended community attribute of EVPN routes in the VPN instance.



By default, no VPN target extended community list is configured for EVPN routes in the VPN instance.

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
| *vpn-target* | Specifies a VPN target to be configured for a VPN instance. | The format of a VPN target can be as follows:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535. |
| *vrfRtType* | Adds a VPN target to the VPN target list of a VPN instance. | The value is an enumerated type:   * both: adds a VPN target to both the import and export VPN target lists of a VPN instance. If both, export-extcommunity, and import-extcommunity are not configured in the vpn-target command, a VPN target is added to both lists by default. * export-extcommunity: adds a VPN target to the export VPN target list of a VPN instance. * import-extcommunity: adds a VPN target to the import VPN target list of a VPN instance. |
| **all** | Deletes all the VPN targets of a VPN instance. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When advertising EVPN IP prefix routes to other PE peers, the local PE must carry all VPN targets in the export VPN target list configured for EVPN routes in the local VPN instance. If the VPN targets carried in received IRB routes or IP prefix routes overlap with those in the import VPN targets list of EVPN routes in the local VPN instance, only the IRB route or IP prefix route can be added to the routing table of the local VPN instance.


Example
-------

# Add 3:3 to the export VPN target list and 4:4 to the import VPN target list of EVPN routes in the VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] vpn-target 3:3 export-extcommunity evpn
[*HUAWEI-vpn-instance-vrf1] vpn-target 4:4 import-extcommunity evpn

```