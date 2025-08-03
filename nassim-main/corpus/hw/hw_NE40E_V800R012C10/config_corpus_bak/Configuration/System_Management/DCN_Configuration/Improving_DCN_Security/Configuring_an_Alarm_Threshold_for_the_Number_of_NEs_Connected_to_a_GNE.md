Configuring an Alarm Threshold for the Number of NEs Connected to a GNE
=======================================================================

To prevent a GNE from being overloaded with NEs, configure an alarm threshold for the number of NEs connected to the GNE. When the number of NEs connected to the GNE reaches the alarm threshold, the GNE will send a trap to its interworking NMSs.

#### Background Information

On a DCN, NMSs use GNEs to manage all common NEs. To prevent a GNE from being overloaded with NEs, configure an alarm threshold for the number of NEs connected to the GNE. When the number of NEs connected to the GNE reaches the alarm threshold, the GNE will send a trap to its interworking NMSs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**ne-number alarm threshold**](cmdqueryname=ne-number+alarm+threshold) *threshold*
   
   
   
   An alarm threshold is configured for the number of NEs connected to the GNE.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.