Configuring Route Advertisement on DC GWs
=========================================

Route advertisement allows DC GWs to construct their own forwarding entries based on received EVPN routes.

#### Procedure

1. Configure DC GWs to advertise the VPN loopback and UE routes received from VNFs through EVPN.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) **Loopback** *interface-number*
      
      
      
      The loopback interface view is displayed.
   3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The loopback interface is bound to an L3VPN instance.
   4. (Optional) Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
      
      
      
      IPv6 is enabled on the loopback interface. This step is mandatory when the loopback interface is configured with an IPv6 address.
   5. Configure an IPv4 or IPv6 address for the loopback interface.
      
      
      * Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IPv4 address for the loopback interface.
      * Run the [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* } command to configure an IPv6 address for the loopback interface.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the loopback interface view.
   7. Create a route-policy to filter and modify the advertised and received routes. For configuration details, see [Configuring a Route-Policy](dc_vrp_route-policy_cfg_0007.html). A route-policy must support the following functions:
      
      
      * Export route-policy: An if-match clause configured in the route-policy can be used to filter VPN loopback routes and UE routes in the L3VPN instance. You can run the [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** | *ipv4-address* } or [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *ipv6-address* } command to configure the original next hop address of UE routes as a gateway address.
      * Import route-policy: You can run the [**apply gateway-ip none**](cmdqueryname=apply+gateway-ip+none) or [**apply ipv6 gateway-ip none**](cmdqueryname=apply+ipv6+gateway-ip+none) command to delete gateway IP addresses from the routes received from L2GWs/L3GWs, so that the BGP VPN packets sent by DC GWs to VNFs can recurse to SR tunnels instead of being forwarded through VBDIF interfaces based on gateway IP addresses (DC GWs do not have VBDIF interfaces).
   8. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   9. Enter the VPN instance IPv4 or IPv6 address family view.
      
      
      * Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
      * Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   10. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
       
       
       
       An export route-policy is applied to the L3VPN instance, so that the L3VPN instance can filter routes to be advertised to EVPN. This ensures that the L3VPN instance advertises only UE service routes and loopback VPN routes to EVPN.
   11. Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
       
       
       
       An import route-policy is applied to the L3VPN instance, so that the L3VPN instance can filter received EVPN routes and delete gateway IP addresses from the routes received from L2GWs/L3GWs.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance IPv4 or IPv6 address family view.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the VPN instance view.
   14. Create a route-policy to filter the UE routes received by the DC GW from the L2GW/L3GW and prohibit the advertisement of such UE routes. For details about how to create a route-policy, see [Configuring a Route-Policy](dc_vrp_route-policy_cfg_0007.html).
   15. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       
       
       The BGP view is displayed.
   16. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
       
       
       
       The BGP-EVPN address family view is displayed.
   17. Run [**peer**](cmdqueryname=peer+route-policy+export) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* **export**
       
       
       
       The route-policy is applied to prohibit the DC GW from advertising UE routes to other DC GWs.
   18. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-EVPN address family view.
   19. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
       
       
       * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
       * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   20. Run [**import-route**](cmdqueryname=import-route) **direct** [ **med** *med* | **route-policy** *route-policy-name* ] \*
       
       
       
       VPN loopback routes are imported into the BGP-VPN instance IPv4 or IPv6 address family.
   21. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
       
       
       
       The function to advertise IP routes from the VPN instance to the EVPN instance is enabled.
   22. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-VPN instance IPv4 or IPv6 address family view.
   23. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
2. Establish BGP VPN peer relationships between DC GWs and VNFs.
   1. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **deny** **node** *node*
      
      
      
      A route-policy that denies all routes is created.
   2. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the route-policy view.
   3. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   4. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
      
      
      * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
      * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   5. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *ipv6-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      A BGP VPN peer relationship is established.
   6. Run [**peer**](cmdqueryname=peer+connect-interface) { *ipv4-address* | *ipv6-address* | *group-name* } **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ]
      
      
      
      The source interface and source IP address are specified for the TCP connection to be set up between BGP peers.
   7. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *ipv6-address* | *group-name* } **route-policy** *route-policy-name* **export**
      
      
      
      The route-policy is applied so that the DC GW does not advertise BGP VPN routes to VNFs. This prevents routing loops.
   8. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *ipv6-address* | *group-name* } **reflect-client**
      
      
      
      The RR function is configured to reflect BGP VPN routes. This function allows VNFs to share UE routes.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv4 or IPv6 address family view.
3. Configure BGP EVPN RRs, so that EVPN routes can be synchronized between L2GWs/L3GWs and the EVPN routes sent by L2GWs/L3GWs can be reflected to PEs.
   1. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   2. Run [**peer**](cmdqueryname=peer+reflect-client) { *group-name* | *ipv4-address* } **reflect-client**
      
      
      
      The L2GW/L3GW and PE are configured as RR clients.
   3. Run [**peer**](cmdqueryname=peer+next-hop-invariable) { *group-name* | *ipv4-address* } **next-hop-invariable**
      
      
      
      DC GWs are configured not to modify the next hops of routes advertised to PEs and L2GWs/L3GWs. This ensures that the next hop addresses of routes received by a PE from a VNF are the IP addresses of L2GWs/L3GWs, and the next hop addresses of default routes received by an L2GW/L3GW are the IP addresses of PEs. These routes can then recurse to E2E SR-MPLS TE tunnels.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.