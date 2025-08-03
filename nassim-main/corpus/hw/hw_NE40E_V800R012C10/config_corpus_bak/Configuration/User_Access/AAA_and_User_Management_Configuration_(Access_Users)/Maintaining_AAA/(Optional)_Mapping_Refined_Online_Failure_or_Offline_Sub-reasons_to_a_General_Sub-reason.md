(Optional) Mapping Refined Online Failure or Offline Sub-reasons to a General Sub-reason
========================================================================================

If you want to learn only general login failure
or logout sub-reasons, not refined sub-reasons, you can map some refined
sub-reasons to a general sub-reason. The device will then display
information only about the mapping general sub-reason.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa) 
   
   
   
   The AAA view is displayed.
3. Run [**sub-reason**](cmdqueryname=sub-reason) *start-reason* [ *end-reason* ] **mapping** *mapping-reason*
   
   
   
   Refined login failure or logout sub-reasons are mapped to
   a general sub-reason.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.