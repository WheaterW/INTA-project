Configuring Session Resources
=============================

Configuring session resources is a prerequisite for configuring DS-Lite functions on a service board. If no session resources are configured, DS-Lite services become unavailable.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
3. Run [**active nat session-table size**](cmdqueryname=active+nat+session-table+size) *table-size* [**slot**](cmdqueryname=slot) *slot-id* 
   
   
   
   The number of session resources on the CPU of the service board is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.