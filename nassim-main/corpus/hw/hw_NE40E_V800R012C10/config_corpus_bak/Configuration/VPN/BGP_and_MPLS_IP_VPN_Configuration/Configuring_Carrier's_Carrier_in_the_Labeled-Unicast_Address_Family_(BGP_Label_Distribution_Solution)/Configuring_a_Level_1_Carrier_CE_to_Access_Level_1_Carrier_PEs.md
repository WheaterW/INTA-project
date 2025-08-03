Configuring a Level 1 Carrier CE to Access Level 1 Carrier PEs
==============================================================

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user.

#### Procedure

* Create a VPN instance on the Level 1 carrier PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to configure the VPN instance IPv4 address family and enter its view.
  4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance IPv4 address family.
  5. Run the [**apply-label**](cmdqueryname=apply-label) **per-route** command to set the label distribution mode to one-label-per-route.
  6. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv4 address family.
  7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  8. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the Level 1 carrier CE.
  9. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the interface to the VPN instance.
  10. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
  11. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS on the interface.
  12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure labeled BGP on the Level 1 carrier PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain1* | *as-number-dot1* } command to enter the BGP view.
  3. Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to create a BGP VPN instance and enter its view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain2* | *as-number-dot2* } command to configure the Level 1 carrier CE as an EBGP peer in the BGP VPN instance view.
  5. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
  6. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  7. Run the [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } command to import labeled BGP VPN routes into the BGP VPN routing table.
  8. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
  9. Run the [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name* command to enter the BGP labeled VPN instance IPv4 address family view.
  10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the BGP peer relationship in the BGP-labeled-VPN instance IPv4 address family view, so that the Level 1 carrier PE and the Level 1 carrier CE can exchange labeled BGP routes.
  11. Run the [**import-rib**](cmdqueryname=import-rib) **vpn-instance** *vpn-instance-name* **include-label-route** [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] command to enable the device to import the labeled BGP routes that are imported from the VPN instance into the routing table of the BGP-labeled-VPN instance IPv4 address family.
  12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure labeled BGP on the Level 1 carrier CE between it and the Level 1 carrier PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the Level 1 carrier PE.
  3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
  4. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS on the interface.
  5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  6. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain2* | *as-number-dot2* } command to enter the BGP view.
  7. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain1* | *as-number-dot1* } command to configure the Level 1 carrier PE as an EBGP peer of the device.
  8. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP-labeled address family view.
  9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the BGP peer relationship in the BGP-labeled address family view, so that the Level 1 carrier CE and the Level 1 carrier PE can exchange labeled BGP routes.
  10. (Optional) Run the [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ] command to permit routing loops.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Perform this step if the Level 1 carrier and Level 2 carriers belong to different ASs and Level 2 carriers belong to the same AS.
  11. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
  12. Run the [**import-rib public**](cmdqueryname=import-rib+public) **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* } command to configure the device to import BGP VPN labeled routes into the BGP public network routing table.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure labeled BGP on the Level 1 carrier CE between it and the Level 2 carrier PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain2* | *as-number-dot2* } command to enter the BGP view.
  3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain2* | *as-number-dot2* } command to configure the Level 2 carrier PE as an IBGP peer of the device.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number* command to specify the interface for setting up a TCP connection.
  5. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP-labeled address family view.
  6. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the BGP peer relationship in the BGP-labeled address family view, so that the Level 1 carrier CE and the Level 2 carrier PE can exchange labeled BGP routes.
  7. Run the [**import-route**](cmdqueryname=import-route) { **rip** | **isis** | **ospf** } *processId* command to import the routes of the Level 2 carrier network.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure labeled BGP on the Level 2 carrier PE.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) { *as-number-plain2* | *as-number-dot2* } command to enter the BGP view.
  3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain2* | *as-number-dot2* } command to configure the Level 1 carrier CE as an IBGP peer of the device.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number* command to specify the interface for setting up a TCP connection.
  5. Run the [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast) command to enter the BGP-labeled address family view.
  6. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **enable** command to enable the BGP peer relationship in the BGP-labeled address family view, so that the Level 2 carrier PE and the Level 1 carrier CE can exchange labeled BGP routes.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.