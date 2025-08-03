Configuring an L3VPN Instance
=============================

You can configure an L3VPN instance to store and manage received VPN routes or VM routes.

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
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*.*subinterface-number*
   
   
   
   An Ethernet sub-interface is created, and its view is displayed.
4. (Optional) Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   A VLAN to be associated with the Ethernet sub-interface is specified, and the VLAN encapsulation type is set.
5. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The sub-interface is bound to a VPN instance.
6. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
7. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* }
   
   
   
   An IPv4/IPv6 address is configured for the Ethernet sub-interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.