Configuring Smart-discover
==========================

After Smart-discover is configured, when the neighbor status changes or the DR or BDR on the multiple-access network (broadcast network or NBMA network) changes, the local router sends Hello packets to its neighbor immediately without waiting for the Hello timer to expire.

#### Context

Without Smart-discover, when the neighbor status of the Router changes or the DR/BDR on the multiple-access network (broadcast or NBMA network) changes, the Router does not send Hello packets to its neighbor until the Hello timer expires; after Smart-discover is configured, the Router sends Hello packets to its neighbor immediately without waiting for the Hello timer to expire, which speeds up the neighbor relationship establishment and OSPF network convergence.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run [**ospf smart-discover**](cmdqueryname=ospf+smart-discover)
   
   
   
   Smart-discover is configured on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.