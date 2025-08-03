vpn-target (VPN instance view)
==============================

vpn-target (VPN instance view)

Function
--------



The **vpn-target** command configures VPN targets for a VPN instance IPv4 address family.

The **undo vpn-target** command deletes the VPN targets of a VPN instance IPv4 address family.



By default, no VPN target is configured for a VPN instance IPv4 address family.


Format
------

**vpn-target** { *vpn-target* } &<1-8> [ *vrfRtType* ]

**undo vpn-target** { *vpn-target* } &<1-8> [ *vrfRtType* ]

**undo vpn-target all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-target* | Specifies a VPN target to be configured for a VPN instance IPv4 address family. | The format of a VPN target can be as follows:   * 2-byte AS number: 4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0:0. * Integral 4-byte AS number: 2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in dotted notation: 2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that a VPN target cannot be 0.0:0. * 32-bit IP address: 2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535. |
| *vrfRtType* | Adds a VPN target to the VPN target list of a VPN instance IPv4 address family. | The value is an enumerated type:   * both: adds a VPN target to both the import and export VPN target lists of a VPN instance IPv4 address family. If both, export-extcommunity, and import-extcommunity are not configured in the vpn-target command, a VPN target is added to both lists by default. * export-extcommunity: adds a VPN target to the export VPN target list of a VPN instance IPv4 address family. * import-extcommunity: adds a VPN target to the import VPN target list of a VPN instance IPv4 address family. |
| **all** | Deletes all the VPN targets of a VPN instance IPv4 address family. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a local PE advertises VPNv4 routes to peer PEs, the VPNv4 routes carry all the export VPN targets of the local VPN instance IPv4 address family. The received VPNv4 routes can be added to the routing table of the local VPN instance IPv4 address family only when their VPN targets belong to the list of import VPN targets of the local VPN instance IPv4 address family. To configure VPN targets for a VPN instance IPv4 address family, run the **vpn-target** command.A maximum of eight VPN targets can be specified in the **vpn-target** command. If you want to configure more VPN targets in a VPN instance IPv4 address family view, run the **vpn-target** command more than once.

**Prerequisites**



A route distinguisher (RD) has been configured for the VPN instance IPv4 address family using the **route-distinguisher** command.



**Configuration Impact**



If the **vpn-target** command is not used, a PE does not install received VPNv4 routes into the routing table of its VPN instance IPv4 address family.If all the VPN targets of the IPv4 address family of a VPN instance are deleted using the **undo vpn-target** command, all routes learned by the IPv4 address family of the VPN instance from other VPN instances will be deleted.



**Follow-up Procedure**



Run the **ipv4-family vpn-instance** command in the BGP view to synchronize the VPN targets of the VPN instance IPv4 address family to the BGP VPN instance IPv4 address family.



**Precautions**

Adding, modifying, or deleting VPN targets may cause BGP peers in a BGP VPN instance to update large numbers of sent, received, locally leaked, and remotely leaked routes.


Example
-------

# Add 3:3 to the export VPN target list and 4:4 to the import VPN target list of VPN instance vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] vpn-target 3:3 export-extcommunity
[*HUAWEI-vpn-instance-vrf1] vpn-target 4:4 import-extcommunity

```