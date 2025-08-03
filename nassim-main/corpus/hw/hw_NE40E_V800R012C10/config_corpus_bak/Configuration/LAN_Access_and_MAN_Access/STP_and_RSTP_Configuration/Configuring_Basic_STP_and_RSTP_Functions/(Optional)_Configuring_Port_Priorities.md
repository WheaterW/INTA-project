(Optional) Configuring Port Priorities
======================================

Select a designated port for each connection based on the root path cost, bridge ID (BID), and port ID of each port. The lower the port priority value, the more likely the port on a device becomes a designated port; the higher the port priority value, the more likely the port is to be blocked.

#### Context

In STP/RSTP calculation, whether a port on a device will be selected as a designated port is determined by its priority. For details, see [Overview of STP and RSTP](dc_vrp_stp_cfg_0002.html).

If the root path costs and the BIDs of the sending devices are the same and you expect to block a port on a device to eliminate loops, set the port priority value to be larger than the default value when the devices have the same bridge ID and the cost of path. This port will be blocked in designated port selection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp port priority**](cmdqueryname=stp+port+priority) *priority*
   
   
   
   The port priority is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.