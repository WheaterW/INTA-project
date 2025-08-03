spt-only mode
=============

spt-only mode

Function
--------



The **spt-only mode** command configures PIM-SM RPTs to be set up not across MVPN tunnels.

The **undo spt-only mode** command restores the default configuration.



By default, PIM-SM RPTs cannot be set up.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**spt-only mode**

**undo spt-only mode**


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

In NG MVPN, PIM-SM RPTs can be set up in either of the following modes:

* PIM-SM RPT setup over inter-AS MVPN tunnels: PIM-SM RPT data is transmitted to remote PEs over MVPN tunnels. The advantage of PIM-SM RPT setup over MVPN tunnels is that Rendezvous Points (RPs) can be deployed on PEs or CEs, but the disadvantage of PIM-SM RPT setup over MVPN tunnels is that Rendezvous Point Trees (RPTs) can be deployed on PEs or CEs. The switchover from the RPT to the shortest path tree (SPT) may occur on the MVPN tunnel. Therefore, the PE needs to maintain many states, and the RP can only be a static RP.
* PIM-SM RPT not across MVPN tunnels: PIM-SM RPTs are not transmitted to remote PEs through MVPN tunnels. The advantage is that PIM-SM RPTs are not transmitted through MVPN tunnels. Therefore, RPT-to-SPT switching does not occur on MVPN tunnels. This feature simplifies PE processing and reduces the number of states maintained by PEs. An RP can be a static RP or a dynamic RP. The disadvantage is that if an RP is deployed on a CE, an MSDP peer relationship needs to be established between the PE and CE.By default, PIM-SM RPTs cannot be set up.
* To set up PIM-SM RPTs not across MVPN tunnels, run the **spt-only mode** command.

**Precautions**

PEs in the same MVPN instance must use the same PIM-SM RPT setup mode.


Example
-------

# Configure PIM-SM RPTs to be set up not across MVPN tunnels.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] spt-only mode

```