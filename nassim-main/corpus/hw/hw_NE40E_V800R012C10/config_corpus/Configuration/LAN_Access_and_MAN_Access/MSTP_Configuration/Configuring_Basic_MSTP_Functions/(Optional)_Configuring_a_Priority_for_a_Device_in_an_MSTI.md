(Optional) Configuring a Priority for a Device in an MSTI
=========================================================

The lower the numerical value is, the higher priority a device has and the more likely the device will be selected as a root bridge. You can configure the cost of the path from a device to the root bridge to preferentially select a root port.

#### Context

In a Multiple Spanning Tree Instance (MSTI), there is only one root bridge and it is the logic center of the MSTI. In root bridge selection, the device with high performance and network hierarchy is generally selected as a root bridge; however, the priority of such a device may be not that high. Thus setting a high priority for the device is necessary so that the device can function as a root bridge.

Other devices with low performance and network hierarchy are not fit to be a root bridge. Therefore, set low priorities for these devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **priority** *priority*
   
   
   
   The priority of the device in a specified MSTI is set.
   
   
   
   If **instance** is not specified, the priority of the device is configured in MSTI 0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To configure the current device as a primary root bridge, directly run the [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **root** **primary** command. The priority of the device is automatically changed to 0 after the configuration.
   * To configure the current device as a secondary root bridge, run the [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **root** **secondary** command. The priority of the device is automatically changed to 4096 after the configuration.
     
     In an MSTI, a device cannot act as a primary root bridge and a secondary root bridge at the same time.
   * If the current device has been specified as a primary or secondary root bridge using the [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **root** **primary** or [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **root** **secondary** command and you want to change the priority of the device, run the **undo stp** [ **instance** *instance-id* ] **root** command to disable the root bridge or secondary root bridge function first. Then, run the [**stp**](cmdqueryname=stp) [ **instance** *instance-id* ] **priority** *priority* command to set a new priority.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.