external-path (BGP-VPN-Target address family view)
==================================================

external-path (BGP-VPN-Target address family view)

Function
--------



The **external-path** command sets the maximum number of EBGP peers to which VPN routes that match a VPN-Target are advertised.

The **undo external-path** command restores the default value.



By default, an EBGP peer selects a route from multiple VPN ORF routes with the same prefix as the preferred route.


Format
------

**external-path** *number*

**undo external-path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of EBGP peers to which VPN routes that match a VPN-Target are advertised. | The value is an integer ranging from 1 to 64. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, when an EBGP peer receives the same VPN ORF route from multiple peers, the EBGP peer selects one route from the multiple VPN ORF routes with the same prefix as the preferred route and advertises only the VPN ORF route to the preferred peer. As a result, fast reroute (FRR) and load balancing cannot be implemented.To implement FRR and load balancing between ASBRs, run the **external-path** command to set the maximum number of EBGP peers in the BGP-VPN-Target address family to increase the number of VPN routes that match the VPN targets advertised by the peers.




Example
-------

# Set the maximum number of EBGP peers to which VPN routes that match a VPN-Target are advertised to 5.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] external-path 5

```