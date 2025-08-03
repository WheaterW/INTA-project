(Optional) Disabling Route Reflection Between Clients Through the RR
====================================================================

If the clients of an RR are fully meshed, you can disable route reflection between the clients through the RR. This reduces the memory overhead.

#### Context

On some networks, if IBGP peer connections have already been established among clients of an RR, they can exchange routing information directly. In this case, route reflection between the clients through the RR is unnecessary and consumes bandwidth resources. In this case, you can disable route reflection between the clients through the RR. This reduces the memory overhead on the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
   
   
   
   Route reflection between clients through the RR is disabled.
   
   
   
   If the clients of an RR have been fully meshed, you can run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between the clients through the RR. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command is run only on RRs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.