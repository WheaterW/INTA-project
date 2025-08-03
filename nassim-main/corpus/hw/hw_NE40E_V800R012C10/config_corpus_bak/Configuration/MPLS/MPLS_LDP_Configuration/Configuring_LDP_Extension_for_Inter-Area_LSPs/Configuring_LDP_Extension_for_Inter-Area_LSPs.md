Configuring LDP Extension for Inter-Area LSPs
=============================================

LDP extension for inter-area LSPs can be configured on the ingress and transit nodes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**longest-match**](cmdqueryname=longest-match)
   
   
   
   LDP is configured to search for routes based on the longest match rule to establish LSPs.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command cannot be run during LDP GR.