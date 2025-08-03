Enabling IP Multicast Routing
=============================

Enabling IP multicast routing for the public network instance and VPN instance is the first step in configuring multicast VPNs.

#### Context

Enabling IP multicast routing for the public network instance and VPN instance is the first step in configuring multicast VPNs. IP multicast routing needs to be enabled on every PE on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled in the public network instance.
3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VPN instance IPv4 address family.
6. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled for the VPN instance IPv4 address family.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.