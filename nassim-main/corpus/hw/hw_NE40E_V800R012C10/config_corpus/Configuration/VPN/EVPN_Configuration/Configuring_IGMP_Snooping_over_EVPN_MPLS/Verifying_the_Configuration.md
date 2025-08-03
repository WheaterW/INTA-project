Verifying the Configuration
===========================

After configuring IGMP snooping over EVPN, verify the received EVPN routes and VPN routes on devices.

#### Prerequisites

IGMP snooping over EVPN has been configured.


#### Procedure

* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **vpn-instance** *evpn-name* | **route-distinguisher** *route-distinguisher* } **routing-table** { **smet-route** | **join-route** } [ *prefix* ] or [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** [ **peer** *peer-address* **advertised-routes** ] { **smet-route** | **join-route** } [ *prefix* ] command to check information about BGP EVPN SMET or IGMP Join routes.