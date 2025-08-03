(Optional) Configuring MAP Translation for ICMP/ICMPv6 Error Packets
====================================================================

In a MAP-T scenario, the MAP conversion of ICMP error packets can be performed only after the MAP conversion function is configured for ICMP error packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-t instance**](cmdqueryname=map-t+instance) *map-t-instance-name* [ **id** *id* ]
   
   
   
   The MAP-T instance view is displayed.
3. Run [**map icmp-tranfer enable**](cmdqueryname=map+icmp-tranfer+enable)
   
   
   
   The MAP conversion function is enabled for ICMP/ICMPv6 error packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.