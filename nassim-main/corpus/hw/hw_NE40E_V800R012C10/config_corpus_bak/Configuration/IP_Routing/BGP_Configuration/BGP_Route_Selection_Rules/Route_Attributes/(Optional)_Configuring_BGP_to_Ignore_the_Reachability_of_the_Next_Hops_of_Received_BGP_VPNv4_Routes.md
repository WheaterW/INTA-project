(Optional) Configuring BGP to Ignore the Reachability of the Next Hops of Received BGP VPNv4 Routes
===================================================================================================

Configuring BGP to ignore the reachability of the next hops of received BGP VPNv4 routes ensures that the BGP routes remain active even if their next hops are unreachable.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0294514890__fig_dc_vrp_bgp_cfg_410401), an IGP runs between PE1 and ABR1, and between PE2 and ABR2. All the devices run IBGP. ABR1 and ABR2 are route reflectors (RRs). PE1 and ABR2 are the clients of ABR1, and PE2 and ABR1 are the clients of ABR2. A tunnel is deployed between PE1 and PE2. When ABR2 receives a BGP VPNv4 route with PE1 as the original next hop from ABR1, ABR2 cannot find the IP routing entry corresponding to PE1 and does not have a tunnel to PE1. As a result, ABR2 considers the received BGP VPNv4 route to be invalid, and this route cannot be advertised to PE2. As PE2 does not receive the BGP VPNv4 route originating from PE1, route recursion to the tunnel between PE1 and PE2 cannot be performed, and traffic cannot be forwarded through the tunnel. To address this, configure BGP on ABR2 to ignore the reachability of the next hops of received BGP VPNv4 routes. In this way, PE2 can learn the BGP VPNv4 route originating from PE1 through ABR2 properly, and the route can recurse to the tunnel for traffic forwarding.

**Figure 1** Configuring BGP not to verify next hop reachability  
![](figure/en-us_image_0294532409.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpnv4) **vpnv4**
   
   
   
   The BGP-VPNv4 address family view is displayed.
4. Run [**bestroute nexthop-resolved none**](cmdqueryname=bestroute+nexthop-resolved+none)
   
   
   
   BGP on the local device is configured to ignore the reachability of the next hops of received BGP VPNv4 routes.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table)*network* command to check the next-hop IP address obtained through route recursion and the outbound interface of the recursive tunnel.