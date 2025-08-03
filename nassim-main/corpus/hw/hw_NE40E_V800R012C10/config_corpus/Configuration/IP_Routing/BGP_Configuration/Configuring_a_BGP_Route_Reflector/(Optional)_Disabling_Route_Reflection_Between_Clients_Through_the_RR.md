(Optional) Disabling Route Reflection Between Clients Through the RR
====================================================================

If the clients of a route reflector are fully connected, you need to disable route reflection among them through the RR to reduce bandwidth consumption.

#### Context

On some networks, if fully meshed IBGP connections have been established between clients, they can directly exchange routing information. Therefore, route reflection between clients through the RR is unnecessary and also consumes bandwidth resources. In this case, disable route reflection among them through the RR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients)
   
   
   
   Route reflection is disabled among clients through the RR.
   
   
   
   If the clients of an RR are fully connected, you can use the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection among the clients through the RR. This command is applicable to only RRs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.