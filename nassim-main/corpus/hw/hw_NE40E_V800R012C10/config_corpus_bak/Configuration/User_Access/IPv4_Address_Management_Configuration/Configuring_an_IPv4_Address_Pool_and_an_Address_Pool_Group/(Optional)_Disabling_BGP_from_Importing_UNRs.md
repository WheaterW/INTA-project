(Optional) Disabling BGP from Importing UNRs
============================================

(Optional)_Disabling_BGP_from_Importing_UNRs

#### Context

In BRAS access scenarios, you can disable BGP from importing UNRs in the NoAdv state to reduce memory resources occupied by such UNRs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access no-advertise-unr import disable**](cmdqueryname=access+no-advertise-unr+import+disable)
   
   
   
   BGP is disabled from importing UNRs in the NoAdv state.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.