Configuring Basic FR Functions on a DTE
=======================================

Before deploying FR access links, configure basic FR functions on the DTE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The FR interface view is displayed.
3. Run [**link-protocol fr**](cmdqueryname=link-protocol+fr) [ **ietf** | **nonstandard** ]
   
   
   
   An FR encapsulation type is configured on the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the FR encapsulation type on an interface is changed, the system automatically deletes all the FR configurations on the interface. Therefore, you need to re-configure the interface.
4. (Optional) Run [**fr interface-type**](cmdqueryname=fr+interface-type) **dte**
   
   
   
   The FR interface type is set to DTE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the FR interface type is changed, LMI parameters are deleted automatically.
5. (Optional) Run [**fr lmi type**](cmdqueryname=fr+lmi+type) { **ansi** | **nonstandard** | **q933a** }
   
   
   
   The LMI protocol type is set.
6. (Optional) Configure basic parameters on the DTE.
   
   
   1. Run the [**fr lmi n391dte**](cmdqueryname=fr+lmi+n391dte) *n391value* command to configure the N391 parameter on the DTE.
   2. Run the [**fr lmi n392dte**](cmdqueryname=fr+lmi+n392dte) *n392dtevalue* command to configure the N392 parameter on the DTE.
   3. Run the [**fr lmi n393dte**](cmdqueryname=fr+lmi+n393dte) *n393dtevalue* command to configure the N393 parameter on the DTE.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the interface view.
8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subnumber* [ **p2p** ]
   
   
   
   The FR sub-interface view is displayed.
9. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the FR sub-interface.
10. Run [**fr dlci**](cmdqueryname=fr+dlci) *dlci-value*
    
    A DLCI is configured for the VC.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    * The DLCI on the DTE must be the same as that on the DCE.
    * If you want to change a configured DLCI, run the **shutdown** command to shut down the sub-interface or delete the original DLCI.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.