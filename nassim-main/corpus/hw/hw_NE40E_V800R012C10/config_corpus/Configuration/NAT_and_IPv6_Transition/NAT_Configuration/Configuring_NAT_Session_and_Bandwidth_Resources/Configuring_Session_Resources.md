Configuring Session Resources
=============================

Session resources are essential for dedicated NAT.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active nat session-table size**](cmdqueryname=active+nat+session-table+size) *table-size* [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   Session resources are configured for the CPU of a specified dedicated board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.