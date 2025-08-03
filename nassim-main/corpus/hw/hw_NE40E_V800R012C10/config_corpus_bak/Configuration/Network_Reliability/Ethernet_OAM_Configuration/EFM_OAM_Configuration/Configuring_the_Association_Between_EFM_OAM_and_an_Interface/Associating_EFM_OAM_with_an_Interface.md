Associating EFM OAM with an Interface
=====================================

You can associate EFM OAM with an interface to perform rapid service switchovers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm trigger if-down**](cmdqueryname=efm+trigger+if-down)
   
   
   
   EFM OAM is associated with the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.