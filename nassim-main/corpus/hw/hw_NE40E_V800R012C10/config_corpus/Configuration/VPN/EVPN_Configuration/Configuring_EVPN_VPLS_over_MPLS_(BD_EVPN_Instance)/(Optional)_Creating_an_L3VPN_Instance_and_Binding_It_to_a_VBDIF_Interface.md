(Optional) Creating an L3VPN Instance and Binding It to a VBDIF Interface
=========================================================================

To enable an EVPN to transmit Layer 3 services, configure an L3VPN instance and bind it to a VBDIF interface.

#### Context

The L3VPN instance can then manage host routes received from the VBDIF interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Create an L3VPN instance on each device.
   
   
   
   For IPv4 services, configure an IPv4 L3VPN instance.
   
   1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to create the VPN instance IPv4 address family and enter its view.
   3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance IPv4 address family.
   4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn** command to set one or multiple VPN targets of the VPN instance IPv4 address family.
   5. Run the [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) command to enable the device to generate and advertise EVPN IP prefix routes and IRB routes.
   6. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn** command to apply a specified tunnel policy to the VPN instance IPv4 address family to associate the tunnel policy with the EVPN routes leaked to the VPN instance IPv4 address family.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv4 address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   
   For IPv6 services, configure an IPv6 L3VPN instance.
   
   1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   2. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to create the VPN instance IPv6 address family and enter its view.
   3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance IPv6 address family.
   4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn** command to set one or multiple VPN targets for the VPN instance IPv6 address family.
   5. Run the [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) command to enable the device to generate and advertise EVPN IP prefix routes and IRB routes.
   6. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn** command to apply a specified tunnel policy to the VPN instance IPv6 address family to associate the tunnel policy with the EVPN routes leaked to the VPN instance IPv6 address family.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
3. Run [**interface vbdif**](cmdqueryname=interface) *bd-id*
   
   
   
   A VBDIF interface is created, and its view is displayed.
4. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The VBDIF interface is bound to a VPN instance.
5. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
6. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* }
   
   
   
   An IPv4/IPv6 address is set for the VBDIF interface for Layer 3 communication.
7. (Optional) Run [**mac-address**](cmdqueryname=mac-address) *mac-address*
   
   
   
   A MAC address is configured for the VBDIF interface.
8. Run [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) or [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable)
   
   
   
   The device is enabled to advertise host ARP/ND routes and IRB/IRBv6 routes.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.