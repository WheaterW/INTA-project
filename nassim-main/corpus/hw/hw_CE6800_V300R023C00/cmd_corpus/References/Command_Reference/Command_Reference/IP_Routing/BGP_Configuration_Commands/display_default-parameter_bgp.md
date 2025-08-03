display default-parameter bgp
=============================

display default-parameter bgp

Function
--------



The **display default-parameter bgp** command displays the default configurations in BGP initialization.




Format
------

**display default-parameter bgp**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the default configurations in BGP initialization, run the display default-parameter bgp command. The command output remains unchanged even when the BGP configurations are modified. Before you run this command, BGP must have been enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the default configurations in BGP initialization.
```
<HUAWEI> display default-parameter bgp
 BGP version               : 4
 EBGP preference           : 255
 IBGP preference           : 255
 Local preference          : 255
 BGP connect-retry         : 32s
 BGP holdtime              : 180s
 BGP keepAlive             : 60s
 BGP sendHoldTime          : 86400s
 EBGP route-update-interval: 30s
 IBGP route-update-interval: 15s
 Default local-preference  : 100
 Default MED               : 0
 IPv4-family unicast       : enable
 EBGP-interface-sensitive  : enable
 IBGP-interface-sensitive  : disable
 Reflect between-clients   : enable
 Check-first-as            : enable
 Synchronization           : disable
 Private-4-byte-as         : enable
 Nexthop-resolved rules    :
     IPv4-family           : unicast(ip)
                             vpn-instance(tunnel)
                             link-state unicast(ip)
     IPv6-family           : unicast(ip)
                             vpn-instance(tunnel)
 BGP L2VPN-family EVPN     :
     BUM Flow Forward Mode : Ingress Replication
     Tunnel Type           : VXLAN

```

**Table 1** Description of the **display default-parameter bgp** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP connect-retry | ConnectRetry interval. |
| BGP holdtime | Hold time. |
| BGP keepAlive | Keepalive interval. |
| BGP sendHoldTime | Session hold time. |
| BGP L2VPN-family EVPN | Default values of BGP EVPN parameters. |
| EBGP preference | Protocol preference of an EBGP route. |
| EBGP route-update-interval | Minimum interval for sending EBGP Update messages. |
| IBGP preference | Protocol preference of an IBGP route. |
| IBGP route-update-interval | Minimum interval for sending IBGP Update messages. |
| Local preference | Protocol preference of the local route. |
| Default local-preference | Local preference of a BGP route. |
| Default MED | MED value of a BGP route. |
| IPv4-family unicast | BGP IPv4 unicast address family view:   * enable. * disable. |
| EBGP-interface-sensitive | When an interface goes Down, the BGP session between the interface and its directly connected external peer is immediately cleared.   * enable. * disable. |
| IBGP-interface-sensitive | Enables a device to immediately delete the directly connected IBGP peer relationship established on an interface if the local interface that directly connects the IBGP peer relationship fails. |
| Reflect between-clients | Route reflection between clients through the RR:   * enable. * disable. |
| Check-first-as | When the check on the first AS number in the AS\_Path attribute carried in the Update message sent by the EBGP peer is enabled:   * enable. * disable. |
| Synchronization | Synchronization between IBGP and IGP:   * enable. * disable. |
| Private-4-byte-as | Whether the 4-byte private AS number function is enabled.   * enable. * disable. |
| Nexthop-resolved rules | Next hop recursion rule. |
| BUM Flow Forward Mode | BUM traffic transmission mode. The default mode is ingress replication. |
| Tunnel Type | Network-side tunnel type. The default type is VXLAN tunnel. |