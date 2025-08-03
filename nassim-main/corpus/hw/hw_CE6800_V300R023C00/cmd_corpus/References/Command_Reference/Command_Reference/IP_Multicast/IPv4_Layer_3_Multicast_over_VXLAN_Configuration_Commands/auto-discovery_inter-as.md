auto-discovery inter-as
=======================

auto-discovery inter-as

Function
--------



The **auto-discovery inter-as** command enables the auto-discovery mode for inter autonomous system (inter-AS).

The **undo auto-discovery inter-as** command disables the auto-discovery mode for inter-AS.



By default, the A-D mode for inter-AS is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**auto-discovery inter-as**

**undo auto-discovery inter-as**


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

On a network with multiple autonomous systems (ASs), run the auto-discovery inter-as command to enable the auto-discovery function for inter-AS.For the scenario configured with inter-AS Option C, the auto-discovery inter-as command is not influenced by the **peer advertise-community** command.

* After the auto-discovery inter-as command is deployed to a PE, the local attribute of the PE does not have the no-export limit, which means the routes are established to EBGP peers. The network can be properly connected.
* When the auto-discovery inter-as command is not configured on a PE, then the local attribute of the PE has the no-export limit, which means the routers cannot be established to EBGP peers. The network cannot work properly.For the scenario configured with inter-AS Option B, the auto-discovery inter-as command is influenced by the **peer advertise-community** command.
* If the **peer advertise-community** command is not configured, the peer ASBRs receive routes information without the no-export attribute, so the network can be properly connected, no matter whether the auto-discovery inter-as command is configured or not.
* After the auto-discovery inter-as command is deployed to a PE, the local attribute of the PE does not have the no-export limit, and the routes established to peer ASBRs do not contain the no-export attribute. The ASBRs can send the received routes to other EBGP peers, so the network can be properly connected.
* When the auto-discovery inter-as command is not configured on a PE, then the local attribute of the PE has the no-export limit, but the routers established to peer ASBRs do not contain the no-export attribute. The ASBRs can send the received routes to other EBGP peers, so the network can work properly.
* If the **peer advertise-community** command is configured, the auto-discovery inter-as command determines whether the routes established to ASBRs contain the no-export attribute or not.
* After the auto-discovery inter-as command is deployed to a PE, the local attribute of the PE does not have the no-export limit, and the routes established to peer ASBRs do not contain the no-export attribute. The ASBRs can send the received routes to other EBGP peers, so the network can be properly connected.
* When the auto-discovery inter-as command is not configured on a PE, then the local attribute of the PE has the no-export limit, the routers established to peer ASBRs also contain the no-export attribute. The ASBRs cannot send the received routes to other EBGP peers, so the network cannot work properly.

**Prerequisites**

Before running this command in the public network MVPN view, you must enable the multicast function in the system view.Before running this command in the VPN MVPN view, you must enable the multicast function in the VPN.

**Precautions**

After the auto-discovery inter-as command is deployed, the intra-AD routes and SPMSI-AD routes sent to BGP do not contain the no-export attribute, so that the routes can be sent to inter-AS network to perform auto discovery.


Example
-------

# Enable the inter-AS auto discovery function on a PE.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 4.4.4.4
[*HUAWEI] ip vpn-instance 1
[*HUAWEI-vpn-instance-1] route-distinguisher 4:4
[*HUAWEI-vpn-instance-1] multicast routing-enable
[*HUAWEI-vpn-instance-1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-1-af-ipv4-mvpn] auto-discovery inter-as

```