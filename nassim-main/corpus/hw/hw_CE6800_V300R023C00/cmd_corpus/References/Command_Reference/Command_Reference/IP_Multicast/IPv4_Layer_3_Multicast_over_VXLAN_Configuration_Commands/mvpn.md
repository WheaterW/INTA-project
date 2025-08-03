mvpn
====

mvpn

Function
--------



The **mvpn** command enables multicast virtual private network (MVPN) and displays the VPN instance IPv4 address family MVPN view.

The **undo mvpn** command deletes all VPN instance IPv4 address family MVPN configurations.



By default, MVPN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mvpn**

**undo mvpn**


Parameters
----------

None

Views
-----

VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NG MVPN is a new framework designed to transmit IP multicast traffic across a BGP VPN. It uses BGP to transmit signaling information and uses PIM SM/PIM SSM/P2MP TE/mLDP to transmit data. NG MVPN enables unicast and multicast services to be transmitted using the same VPN architecture.NG MVPN configurations are performed in the VPN instance IPv4 address family MVPN view. Before deploying an NG MVPN, run the **mvpn** command to enable MVPN and enter the VPN instance IPv4 address family MVPN view.

**Prerequisites**

An MVPN ID has been configured using the **multicast mvpn** command. The **mvpn** command cannot be executed if an MVPN ID has not been configured.

**Precautions**

Running the **undo mvpn** command deletes all configurations in the VPN instance IPv4 address family MVPN view. Exercise caution when running the command.If MVPN has been enabled using the **mvpn** command, the **undo multicast mvpn** command cannot be executed. Before running the **undo multicast mvpn** command, run the **undo mvpn** command to disable MVPN in all VPN instances.


Example
-------

# Enable MVPN and enter the VPN instance IPv4 address family MVPN view.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 10:10
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn

```