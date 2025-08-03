Disabling Automatic Recovery of Default DCN Interfaces
======================================================

The DCN plug-and-play function is implemented through automatic creation and recovery of default DCN interfaces. If a default E1 channel of a CPOS or E1 subcard does not require DCN plug-and-play, disable automatic recovery of the corresponding default DCN interface so that the interface can be reserved for other purposes.

#### Context

After DCN is enabled on a CPOS or E1 subcard, default DCN E1 channels are created automatically, DCN is enabled on the serial interfaces formed by E1 channels' timeslots, and DCN tunnels are established. If DCN tunnels are not required on a CPOS or E1 subcard, disable automatic recovery of corresponding default DCN interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN function is enabled globally, and the DCN view is displayed.
3. Run **auto-restore e1-channel-set disable**
   
   
   
   Automatic recovery is disabled for the default DCN interfaces formed by E1 channels' timeslots on a CPOS or E1 subcard.
   
   After automatic recovery is disabled:
   
   * If you delete the default DCN E1 channels that were created automatically, save the configuration, and restart the device, automatic recovery is disabled.
   * If you install a new CPOS or E1 subcard, the default DCN E1 channels will not be created automatically.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.