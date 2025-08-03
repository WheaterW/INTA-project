Configuring a Level 1 Carrier CE to Access Level 1 Carrier PEs
==============================================================

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 2 carrier functions as the VPN user of the Level 1 carrier, the same as the CE of the PE in the basic BGP/MPLS IP VPN.

#### Procedure

1. Create a VPN instance on a Level 1 carrier PE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enable the VPN instance IPv4 address family and enter its view.
   4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance IPv4 address family.
   5. Run the [**apply-label**](cmdqueryname=apply-label) **per-route** command to set the label distribution mode to one-label-per-route.
   6. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv4 address family.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the Level 1 carrier CE.
   9. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to associate the interface with the VPN instance.
   10. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
   11. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS on the interface.
   12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure labeled BGP on the Level 1 carrier PE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *node* command to create a route-policy for the Level 1 carrier CE.
   3. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the device to allocate labels to IPv4 routes.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**bgp**](cmdqueryname=bgp) *as-number1* command to enter the BGP view.
   6. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
   7. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the Level 1 carrier CE as an EBGP peer of the device.
   8. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to enable the capability of exchanging labeled IPv4 routes.
   9. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export** command to configure the device to allocate labels to routes to be advertised to the Level 1 carrier CE.
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Configure labeled BGP on the Level 1 carrier CE between it and the Level 1 carrier PE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the Level 1 carrier PE.
   3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the interface.
   4. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS on the interface.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   6. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name1* **permit** **node** *node* command to create a route-policy for the Level 1 carrier PE.
   7. Run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command to configure the device to allocate labels to IPv4 routes.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   9. Run the [**bgp**](cmdqueryname=bgp) *as-number2* command to enter the BGP view.
   10. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the Level 1 carrier PE as an EBGP peer of the device.
   11. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability** command to enable the capability of exchanging labeled IPv4 routes.
   12. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export** command to configure the device to allocate labels to routes to be advertised to the Level 1 carrier PE.
   13. (Optional) Run the [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ] command to permit routing loops.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Perform this step if the Level 1 carrier and Level 2 carriers belong to different ASs and Level 2 carriers belong to the same AS.
   14. Run the [**import-route**](cmdqueryname=import-route) { **rip** | **isis** | **ospf** } *processId* command to import the internal routes of the Level 2 carrier network.
   15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.