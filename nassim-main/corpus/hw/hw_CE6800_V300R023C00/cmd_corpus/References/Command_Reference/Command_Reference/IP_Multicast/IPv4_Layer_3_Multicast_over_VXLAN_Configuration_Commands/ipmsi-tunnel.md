ipmsi-tunnel
============

ipmsi-tunnel

Function
--------



The **ipmsi-tunnel** command displays the Multicast Virtual Private Network (MVPN) Inclusive-Provider Multicast Service Interface (I-PMSI) view.

The **undo ipmsi-tunnel** command deletes all MVPN I-PMSI configurations.



By default, no I-PMSI view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipmsi-tunnel**

**undo ipmsi-tunnel**


Parameters
----------

None

Views
-----

VPN instance IPv4 address family MVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PMSI tunnels are the logical tunnels used by the public network to transmit VPN multicast data, and P-tunnels are the actual tunnels used by the public network to transmit VPN multicast data. A sender PE uses PMSI tunnels to send specific VPN multicast data to receiver PEs. The receiver PEs determine whether to accept the VPN multicast traffic based on PMSI tunnel information.In an IPv4 Layer 3 multicast over VXLAN scenario where I-PMSI tunnels are VXLAN tunnels, you can run the **vxlan static** command to configure VXLAN as the I-PMSI tunnel establishment mode.

**Follow-up Procedure**

Run the **vxlan static** command to configure VXLAN as the protocol used to establish I-PMSI tunnels.

**Precautions**

Running the **undo ipmsi-tunnel** command deletes all configurations in the MVPN I-PMSI view. Exercise caution when running the command.


Example
-------

# Enter the I-PMSI view and specify VXLAN to establish an I-PMSI tunnel.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 100:100
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 12
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static

```