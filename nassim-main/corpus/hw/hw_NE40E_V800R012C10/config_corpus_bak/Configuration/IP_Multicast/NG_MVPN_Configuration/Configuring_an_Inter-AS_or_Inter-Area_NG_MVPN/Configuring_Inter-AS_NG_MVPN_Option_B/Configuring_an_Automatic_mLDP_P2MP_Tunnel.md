Configuring an Automatic mLDP P2MP Tunnel
=========================================

Automatic mLDP P2MP tunnels can only transmit NG MVPN and multicast VPLS traffic.

#### Context

There is no need to manually specify leaf nodes before automatic mLDP P2MP tunnels are triggered.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP is enabled globally.
4. (Only for ASBRs and receiver PEs) Run [**mldp recursive-fec**](cmdqueryname=mldp+recursive-fec)
   
   
   
   mLDP P2MP services are enabled to span BGP ASs.
   
   
   
   In a BGP native IP scenario (the route from the current node to the root node is a BGP unicast route, the original next hop of which is directly connected to the current node, and the IGP routes between the current node and the original next hop are reachable), if the upstream node does not support recursive FEC resolution, run the [**mldp bgp native-ip**](cmdqueryname=mldp+bgp+native-ip) command so that LDP selects the original BGP next hop as the upstream node to establish an mLDP P2MP tunnel.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.