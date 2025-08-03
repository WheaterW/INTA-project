(Optional) Configuring a Mode for a FlexE Card
==============================================

FlexE cards support timeslot and bandwidth modes. The bandwidth mode is recommended.

#### Context

* Timeslot mode: A timeslot number to be allocated to a FlexE client is statically specified when the client is configured.
* Bandwidth mode: Only the needed bandwidth is specified when a FlexE client is configured, and the device automatically allocates the corresponding timeslot.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**flexe config-mode**](cmdqueryname=flexe+config-mode) **card** *cardID* { **bandwidth** | **timeslot** } The bandwidth or timeslot mode is configured for a specified FlexE card.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is not supported on the NE40E-M2E or NE40E-M2F.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.