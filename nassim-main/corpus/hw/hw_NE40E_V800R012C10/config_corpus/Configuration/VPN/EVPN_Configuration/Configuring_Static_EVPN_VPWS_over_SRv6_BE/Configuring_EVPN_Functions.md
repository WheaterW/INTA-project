Configuring EVPN Functions
==========================

EVPN VPWS is deployed based on the EVPN service architecture. Before configuring EVPN VPWS over SRv6 BE, you need to configure EVPN functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
   
   
   
   A VPWS EVPN instance is created, and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description is configured for the EVPN instance.
   
   
   
   Similar to a hostname or an interface description, an EVPN instance description helps you memorize the EVPN instance.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the EVPN instance.
   
   
   
   An EVPN instance takes effect only after an RD is configured for it. The RDs of different EVPN instances on the same PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you need to create a large number of EVPN instances and plan a large number of RDs, you can run the **evpn route-distinguisher auto** *rd-ip* command in the system view to enable automatic RD allocation, thereby avoiding RD conflicts. The *rd-ip* parameter specifies an IPv4 address, enabling a device to allocate RDs in the format of *X.X.X.X*:*index* to all EVPN instances that are not allocated RDs. *X.X.X.X* indicates a user-defined RD-IP value, and *index* indicates a 2-byte number ranging from 1 to 65535 automatically allocated by the system.
5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured for the EVPN instance.
   
   
   
   VPN targets are BGP extended community attributes used to control the import and export of EVPN routes. A maximum of eight import VPN targets and eight export VPN targets can be configured each time the [**vpn-target**](cmdqueryname=vpn-target) command is run. To configure more VPN targets for an EVPN instance address family, run the [**vpn-target**](cmdqueryname=vpn-target) command several times.
6. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   The EVPN instance is associated with a tunnel policy.
   
   
   
   This configuration enables PEs to use TE tunnels to transmit data packets.
7. (Optional) Run [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value*
   
   
   
   A switchback delay is configured.
   
   
   
   In a dual-homing scenario, after a fault on the access-side link of the master PE or the master PE is rectified, the master PE generates Ethernet A-D per-EVI routes and then advertise these routes to the remote PE through the BGP EVPN peer relationship. Upon receipt of these routes, the remote PE generates forwarding entries accordingly and switches traffic from the path destined for the backup PE to one destined for the master PE. In this case, if the master PE fails to generate some forwarding entries in a timely manner, a few packets will be lost. To prevent this problem, run the [**timer revert delay**](cmdqueryname=timer+revert+delay) *delay-value* command on the remote PE to configure an appropriate switchback delay. Then, after the remote PE receives Ethernet A-D per-EVI routes, it delays generating forwarding entries. Specifically, the remote PE generates forwarding entries only after the forwarding entries on the master PE become stable. After the delay times out, the remote PE generates new forwarding entries and sends traffic to the master PE, preventing packet loss.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
10. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
    
    
    
    The BGP-EVPN address family view is displayed.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.