vpn-target (VPN instance IPv4 address family MVPN view)
=======================================================

vpn-target (VPN instance IPv4 address family MVPN view)

Function
--------



The **vpn-target** command configures a multicast virtual private network (MVPN) target for the VPN instance MVPN address family.

The **undo vpn-target** command deletes the MVPN target of the VPN instance MVPN address family.



By default, no MVPN target is configured for the VPN instance MVPN address family. The VPN instance MVPN address family uses the VPN target configured in the VPN instance IPv4 address family view as the MVPN target.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vpn-target** { *vrfRT* } &<1-8> [ *vrfRTType* ]

**undo vpn-target** { *vrfRT* } &<1-8> [ *vrfRTType* ]

**undo vpn-target all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrfRT* | Specifies the MVPN target to be added to the import or export VPN target extended community list of the VPN instance MVPN address family. | The available MVPN target formats are as follows:   * 16-bit AS number: 32-bit user-defined number. For example, 1:3. An AS number ranges from 0 to 65535, and a user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot both be 0s. This means that the VPN target value cannot be 0:0. * 32-bit IP address: 16-bit user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number ranges from 0 to 65535. * Integral 4-byte AS number: 2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot both be 0s. This means that the VPN target value cannot be 0:0. * 4-byte AS number in dotted notation: 2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot both be 0s. This means that the VPN target value cannot be 0:0.0. |
| *vrfRTType* | vrfRT type. | The parameters are as follows:   * both: Adds a VPN target to both the import and export VPN target extended community lists of the VPN instance MVPN address family. * export-extcommunity: Indicates the export MVPN target. A maximum of 500 export MVPN targets can be configured. * import-extcommunity: Indicates the import MVPN target. A maximum of 4096 import MVPN targets can be configured. |
| **all** | Deletes all MVPN targets. | - |



Views
-----

VPN instance IPv4 address family MVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MVPN target controls route learning between MVPN sites. An MVPN target can be an import or export MVPN target. An export MVPN target is contained in an MVPN route to be advertised to a remote Multiprotocol Border Gateway Protocol (MP-BGP) peer. After receiving an MVPN route, an MP-BGP peer compares the received export MVPN target with the local import MVPN target to determine whether the MVPN route can be added to the MVPN routing table of the local VPN instance.

**Configuration Impact**

After an MVPN target is configured for the VPN instance MVPN address family, the VPN instance MVPN address family accepts only the MVPN routes that match the MVPN target. When MVPN routes are advertised between VPN instances, if one of the MVPN targets carried in the MVPN routes matches the import VPN target of the local VPN instance MVPN address family, the routes will be added to the MVPN routing table of the local VPN instance.If all MVPN targets of the VPN instance MVPN address family are deleted using the **undo vpn-target** command, all routes learned by the VPN instance MVPN address family from other VPN instances will be deleted.

**Precautions**

The command configuration does not overwrite the previously configured MVPN target. If the number of configured MVPN targets reaches the maximum value, no more MVPN target can be added.Multiple MVPN targets can be configured in the VPN instance MVPN address family. A maximum of eight MVPN targets can be configured using the target command. To configure more MVPN targets in the VPN instance MVPN address family view, run the **vpn-target** command multiple times.If the configured MVPN import target is the same as the MVPN import target configured for another VPN instance or the MVPN import address family target configured for another VPN instance, the MVPN corresponding to the tunnel may be incorrectly selected. As a result, multicast traffic cannot be forwarded.


Example
-------

# Configure the export and import MVPN targets for the VPN instance MVPN address family.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 2
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] vpn-target 1:1 2:2 3:3 both

```