Configure Load Balancing.
=========================

Configure Load Balancing.

#### Context

In the NFVI distributed gateway scenario, the traffic forwarded between the UE and Internet through the VNF is called north-south traffic, and the traffic forwarded between VNF1 and VNF2 is called east-west traffic. To balance both types of traffic, you need to configure load balancing on L2GWs/L3GWs.


#### Procedure

1. Run the [**ip route-static**](cmdqueryname=ip+route-static)**vpn-instance** or [**ipv6 route-static**](cmdqueryname=ipv6+route-static) **vpn-instance** command on each L2GW/L3GW to configure static routes destined for VNF1 and VNF2. When running the command, specify the **inter-protocol-ecmp** keyword to allow hybrid load balancing between static routes and dynamic protocol routes.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * To implement load balancing between static routes and dynamic protocol routes on an L2GW/L3GW, you need to configure the preference of static routes or configure a route-policy to adjust the preference of dynamic routes, so that the preference of static routes is the same as that of dynamic protocol routes.
   * Static routes on an L2GW/L3GW need to be bound to BFD sessions for the gateway to quickly detect the connectivity between VNFs.
2. To configure BGP EVPN hybrid load balancing, perform the following steps:
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   3. Enter the BGP VPN instance IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name or [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
   4. Configure the maximum number of BGP equal-cost routes that can participate in load balancing.
      
      
      ```
      [maximum load-balancing](cmdqueryname=maximum+load-balancing) [ ebgp | ibgp ] number [ ecmp-nexthop-changed ]
      ```
      
      
      
      By default, the maximum number of equal-cost routes for load balancing is 1. That is, load balancing is not performed.
   5. Return to the BGP view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Enter the BGP-EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
   7. Enable BGP Add-Path and set the number of preferred routes that the RR can select.
      
      
      ```
      [bestroute add-path](cmdqueryname=bestroute+add-path) path-number path-number
      ```
      
      By default, BGP Add-Path is not enabled.
   8. Enable the function to receive Add-Path routes from or send Add-Path routes to a DC gateway or both.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } capability-advertise add-path { send | receive | both }
      ```
      
      By default, a device is disabled from sending Add-Path routes to or receiving Add-Path routes from a specified peer.
   9. Configure the number of preferred routes to be advertised to the DC gateway.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } advertise add-path path-number path-number
      ```
      
      By default, BGP advertises only one optimal route to a peer.
   10. Return to the BGP view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   11. Return to the system view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   12. Commit the configuration.
       
       
       ```
       [commit](cmdqueryname=commit)
       ```