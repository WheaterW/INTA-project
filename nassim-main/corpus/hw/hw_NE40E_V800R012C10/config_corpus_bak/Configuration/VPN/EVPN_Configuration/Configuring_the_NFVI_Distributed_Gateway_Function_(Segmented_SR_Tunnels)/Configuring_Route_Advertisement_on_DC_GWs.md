Configuring Route Advertisement on DC GWs
=========================================

Route advertisement can be configured on DC GWs for them to construct their own forwarding entries based on received EVPN or BGP routes.

#### Procedure

1. Configure DC GWs to advertise default static VPN routes and VPN loopback routes through EVPN.
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
   7. Configure default static VPN routes.
      
      
      * Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** { **0.0.0.0** | **0** } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv4 route.
      * Run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **::** **0** { *nexthop-ipv6âaddress* | *interface-type* *interface-number* [ *nexthop-ipv6-address* ] } [ **tag** *tag* ] command to create a default static VPN IPv6 route.
   8. Create a route-policy so that default static VPN routes and VPN loopback routes of the L3VPN instance can be filtered out. For details about how to create a route-policy, see [Configuring a Route-Policy](dc_vrp_route-policy_cfg_0007.html).
   9. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   10. Enter the VPN instance IPv4 or IPv6 address family view.
       
       
       * Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
       * Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
   11. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
       
       
       
       An export route-policy is applied to the L3VPN instance, so that the L3VPN instance can filter routes to be advertised to EVPN. This ensures that the L3VPN instance advertises only its default static VPN routes and loopback VPN routes to EVPN.
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
   21. Run [**network**](cmdqueryname=network) { **0.0.0.0** **0** | **::** **0** }
       
       
       
       Default static VPN routes are imported into the BGP-VPN instance IPv4 or IPv6 address family.
   22. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
       
       
       
       The function to advertise IP routes from the VPN instance to the EVPN instance is enabled.
   23. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-VPN instance IPv4 or IPv6 address family view.
   24. Run [**quit**](cmdqueryname=quit)
       
       
       
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
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv4 or IPv6 address family view.
3. Configure DC GWs to generate ARP or ND entries for Layer 2 forwarding based on the ARP or ND information in EVPN routes.
   1. Run [**interface**](cmdqueryname=interface) **vbdif** *bd-id*
      
      
      
      The VBDIF interface view is displayed.
   2. Run [**anycast-gateway enable**](cmdqueryname=anycast-gateway+enable)
      
      
      
      The distributed gateway function is enabled.
   3. Configure DC GWs to generate ARP or ND entries for Layer 2 forwarding based on the ARP or ND information in EVPN routes.
      
      
      * Run the [**arp generate-rd-table enable**](cmdqueryname=arp+generate-rd-table+enable) command to configure the DC GW to generate ARP entries for Layer 2 forwarding based on the ARP information in EVPN routes.
      * Run the [**ipv6 nd generate-rd-table enable**](cmdqueryname=ipv6+nd+generate-rd-table+enable) command to configure the DC GW to generate ND entries for Layer 2 forwarding based on the ND information in EVPN routes.
   4. (Optional) Run [**ipv6 nd dad attempts**](cmdqueryname=ipv6+nd+dad+attempts) **0**
      
      
      
      DAD is prohibited. This command is mandatory in IPv6 scenarios to prevent service interruptions occurred because the system detects that the IPv6 address of another device is the same as the VBDIF interface's IP address.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VBDIF interface view.
4. (Optional) Configure the asymmetric mode for IRB routes. If L2GWs/L3GWs are configured to advertise IRB or IRBv6 routes to DC GWs, the asymmetric IRB function needs to be configured on DC GWs.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Enter the BGP-VPN instance IPv4 or IPv6 address family view.
      
      
      * Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 address family view.
      * Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
   3. Run [**irb asymmetric**](cmdqueryname=irb+asymmetric)
      
      
      
      The asymmetric mode is enabled for IRB routes.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-VPN instance IPv4 or IPv6 address family view.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.