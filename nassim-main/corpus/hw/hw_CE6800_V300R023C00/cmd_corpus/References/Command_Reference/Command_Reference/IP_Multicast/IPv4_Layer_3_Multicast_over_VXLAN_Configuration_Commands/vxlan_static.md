vxlan static
============

vxlan static

Function
--------



The **vxlan static** command configures VXLAN as the protocol for establishing an Inclusive-Provider Multicast Service Interface (I-PMSI) tunnel.

The **undo vxlan static** command deletes the I-PMSI VXLAN configuration.



By default, no protocol is specified for establishing an I-PMSI tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan static**

**undo vxlan static**


Parameters
----------

None

Views
-----

MVPN-IPMSI view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PMSI tunnels are the logical tunnels used by the public network to send VPN-based multicast data, and P-tunnels are the actual tunnels used by the public network to transmit VPN-based multicast data. An I-PMSI tunnel connects all PEs on the same MVPN. Therefore, all PEs on the same MVPN can receive multicast data traffic from the I-PMSI tunnel.In an IPv4 Layer 3 multicast over VXLAN scenario, I-PMSI uses VXLAN tunnels. To specify VXLAN as the protocol for establishing an I-PMSI tunnel, run the **vxlan static** command.

**Precautions**

If the **vtep-src** command has been run in the VPN view, the **vxlan static** command cannot be run in the MVPN view.


Example
-------

# Configure VXLAN as the protocol for establishing an I-PMSI tunnel.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 2
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static

```