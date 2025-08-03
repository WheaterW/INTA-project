Configuring Basic FR Functions on a DCE
=======================================

Before deploying FR access links, configure basic FR functions on the DCE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The FR interface view is displayed.
3. Run [**link-protocol fr**](cmdqueryname=link-protocol+fr) [ **ietf** | **nonstandard** ]
   
   
   
   An FR encapsulation type is configured on the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the FR encapsulation type on an interface is changed, the system automatically deletes all the FR configurations on the interface. Therefore, you need to re-configure the interface.
4. Run [**fr interface-type**](cmdqueryname=fr+interface-type) **dce**
   
   
   
   The FR interface type is set to DCE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The DLCI on the DTE must be the same as that on the DCE.
   * After the FR interface type is changed, LMI parameters are deleted automatically.
5. (Optional) Run [**fr lmi type**](cmdqueryname=fr+lmi+type) { **ansi** | **nonstandard** | **q933a** }
   
   
   
   The LMI protocol type is set.
6. (Optional) Configure basic parameters on the DCE.
   
   
   1. Run the [**fr lmi t392dce**](cmdqueryname=fr+lmi+t392dce) *t392dcevalue* command to configure the maximum period (determined by T392) for the DCE to wait for a status enquiry message from the DTE.
   2. Run the [**fr lmi n392dce**](cmdqueryname=fr+lmi+n392dce) *n392dcevalue* command to configure the N392 parameter on the DCE.
   3. Run the [**fr lmi n393dce**](cmdqueryname=fr+lmi+n393dce) *n393dcevalue* command to configure the N393 parameter on the DCE.
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