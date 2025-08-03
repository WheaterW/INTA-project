(Optional) Configuring a Port Priority in an MSTI
=================================================

The lower the numerical value, the more likely the port on a device becomes a designated port; the higher the numerical value, the more likely the port is to be blocked.

#### Context

In spanning tree calculation, priorities of ports on devices in Multiple Spanning Tree Instances (MSTIs) determine designated port selection.

If the root path costs and the bridge IDs (BID) of the sending devices are the same and you expect to block a port on a device in a Multiple Spanning Tree Instance (MSTI) to eliminate loops, set the port priority value to be larger than the default value. This port will be blocked in designated port selection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp**](cmdqueryname=stp) **instance** *instance-id* **port priority** *priority*
   
   
   
   A port priority is set in an MSTI.
   
   
   
   The value range of the priority is from 0 to 240, with the step 16. That is, the port priority can be 0, 16, or 32.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.