Enabling the DS-Lite Function
=============================

DS-Lite must be enabled before DS-Lite functions are configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active ds-lite vsuf slot**](cmdqueryname=active+ds-lite+vsuf+slot) *slot-id*
   
   
   
   The DS-Lite function is enabled on a specified service board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.