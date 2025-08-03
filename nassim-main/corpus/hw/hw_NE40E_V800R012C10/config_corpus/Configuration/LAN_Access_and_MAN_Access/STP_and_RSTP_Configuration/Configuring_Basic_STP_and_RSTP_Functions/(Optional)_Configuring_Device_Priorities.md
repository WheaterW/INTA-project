(Optional) Configuring Device Priorities
========================================

Select a device (functioning as a root bridge) from devices for each spanning tree. You can configure the priorities of the devices to preferentially select a root bridge. The lower the numerical value is, the higher priority a device has and the more likely the device will be selected as a root bridge.

#### Context

On an STP/RSTP-capable network, there is only one root bridge and it is the logic center of the entire spanning tree. In root bridge selection, the device with high performance and network hierarchy is generally selected as a root bridge; however, the priority of such a device may be not that high. Thus setting a high priority for the device is necessary so that the device can function as a root bridge.

Other devices with low performance and network hierarchy are not fit to be a root bridge. Therefore, set low priorities for these devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp priority**](cmdqueryname=stp+priority) *priority*
   
   
   
   The priority of a device is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To configure a device as a primary root bridge, you can run the [**stp root primary**](cmdqueryname=stp+root+primary) command directly. The priority value of this device is 0.
   * To configure a device as a secondary root bridge, run the [**stp root secondary**](cmdqueryname=stp+root+secondary) command. The priority value of this device is 4096.
     
     A device cannot act as a primary root bridge and a secondary root bridge at the same time.
   * If you want to change the priority of a device after you run the [**stp root primary**](cmdqueryname=stp+root+primary) command or the [**stp root secondary**](cmdqueryname=stp+root+secondary) command to configure the device as a primary root bridge or a secondary root bridge, run the [**undo stp root**](cmdqueryname=undo+stp+root) command to disable the root bridge function or secondary root bridge function, and then run the [**stp priority**](cmdqueryname=stp+priority) *priority* command to re-set a priority.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.