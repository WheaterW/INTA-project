Configuring the SyncE Function on the Device Where an Atom GNSS Module Resides
==============================================================================

After the device where the Atom GNSS module resides synchronizes clock information from the Atom GNSS module, the device needs to transmit clock signals to downstream devices in order to achieve network-wide clock synchronization. Therefore, the SyncE function needs to be configured on the device.

#### Context

Perform the following steps on the device equipped with an Atom GNSS module (AE 905S B module):


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. Run the [**clock synchronization enable**](cmdqueryname=clock+synchronization+enable) command to enable clock synchronization on the interface.
4. Run the [**clock priority priority-value**](cmdqueryname=clock+priority+priority-value) command to configure a priority for the clock reference source of the interface.
5. Run the [**quit**](cmdqueryname=quit) command to exit the interface view and enter the system view.
6. Run the [**clock ssm-control**](cmdqueryname=clock+ssm-control) { **on** | **off** } command to enable or disable SSM control.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Specifying **on** to enable clock source selection based on SSM levels is recommended. If clock source selection based on SSM quality levels is not enabled, the system does not select a clock source based on SSM quality levels. If the SSM quality level decreases, the system does not perform source switching or send clock source signals that contain SSM quality level information.
   * If **off** is specified, the SSM quality level of sent clock source signals is dnu.
7. (Optional) Run the [**clock freq-deviation-detect enable**](cmdqueryname=clock+freq-deviation-detect+enable) command to enable frequency deviation detection.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.