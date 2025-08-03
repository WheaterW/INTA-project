Configuring a PW APS Instance and Bind a PW Protection Group to the PW APS Instance
===================================================================================

The state machine of a PW APS instance determines the protection switching in PW protection groups associated with the instance.

#### Context

After a PW protection group is associated with a PW APS instance, the state machine of the PW APS instance determines the protection switching in the PW protection group. The PW APS protocol enables the two endpoints of a PW to switch traffic simultaneously by negotiating the hold time or WTR time.

In a PW APS scenario, perform the following configurations on PE1 and PE2.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pw-aps**](cmdqueryname=pw-aps) *apsId* [ **frr** ]
   
   
   
   A PW APS instance is created.
3. (Optional) Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the PW APS instance.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The AC interface view is displayed.
6. Run [**mpls l2vpn pw-aps**](cmdqueryname=mpls+l2vpn+pw-aps) *apsId* { **admin** | **reference** }
   
   
   
   The PW protection group is bound to the PW APS instance.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   In a scenario in which traffic travels along the secondary PW, after the board on which the secondary PW's outbound interface resides fails or is removed, run the [**undo mpls l2vpn pw-aps**](cmdqueryname=undo+mpls+l2vpn+pw-aps) command to disassociate the secondary PW from the PW APS instance. If you do not run this command, traffic cannot be switched back to the primary PW for transmission.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.