Configuring Load Balancing
==========================

Configuring Load Balancing

#### Context

In NFVI scenarios where distributed gateways are deployed, traffic forwarded between UEs and the Internet through VNFs is called north-south traffic, and traffic forwarded between VNFs is called east-west traffic. To balance both types of traffic, you need to configure load balancing on DC gateways and L2GWs/L3GWs.

You can use either of the following configuration methods as required:


#### Procedure

* Run the [**ip route-static**](cmdqueryname=ip+route-static) **vpn-instance** or [**ipv6 route-static**](cmdqueryname=ipv6+route-static) **vpn-instance** command on each L2GW/L3GW to configure static routes destined for VNF1 and VNF2. When running the command, specify the **inter-protocol-ecmp** keyword to allow hybrid load balancing between static routes and dynamic protocol routes. In addition, set the preference of static routes to 255, so that these routes have the same preference as BGP EVPN routes.
* To configure a VPN IGP route to a VNF on an L2GW/L3GW, perform the following steps:
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
  4. Configure the maximum number of equal-cost BGP routes for load balancing with routes of other protocols.
     
     
     ```
     [maximum load-balancing mixed](cmdqueryname=maximum+load-balancing+mixed) number
     ```
     
     
     
     By default, the maximum number of equal-cost BGP routes for load balancing with routes of other protocols is 0, indicating that load balancing is not performed.
     
     This step serves the following purposes:
     
     + Enables load balancing between different types of BGP routes (for example, between IBGP and EBGP routes or between leaked and non-leaked routes) and sets the maximum number of BGP equal-cost routes for load balancing.
     + Enables BGP routes to work in load-balancing mode with routes of other protocols. The route management module determines whether to select BGP routes for hybrid load balancing.
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
  9. Configure the number of preferred routes to be advertised to the DC gateway.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name | ipv6-address } advertise add-path path-number path-number
     ```
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

#### Follow-up Procedure

* By default, after finding that the next-hop outbound interfaces of received Layer 3 traffic are VXLAN and non-VXLAN interfaces working in hybrid load-balancing mode, the device load-balances this traffic among these interfaces. If local traffic does not need to enter VXLAN tunnels, perform the following configurations so that traffic is forwarded only to a local non-VXLAN outbound interface.
  ```
  [load-balance ecmp](cmdqueryname=load-balance+ecmp)
  [vxlan-overlay](cmdqueryname=vxlan-overlay) { network | all } local-preference enable
  ```
  
  If **network** is specified, traffic entering the local device from the VXLAN network side and matching a route is forwarded only to a local non-VXLAN outbound interface.
  
  If **all** is specified, all traffic that matches a route is forwarded only to a local non-VXLAN outbound interface.