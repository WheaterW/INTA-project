Configuring the 1588v2 Synchronization Function on the Device Where an Atom GPS Module Resides
==============================================================================================

Configuring 1588v2 globally involves operations such as enabling 1588v2 in the system view and setting the device type to BC. After enabling 1588v2 in the system view, enable it in the interface view.

#### Context

Perform the following steps on the BC:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable 1588v2 on the device.
3. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) **bc** command to set the device type to BC.
4. (Optional) Run the [**ptp domain**](cmdqueryname=ptp+domain) **domain-value** command to configure the clock domain where the 1588v2 device resides.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The devices that implement time synchronization through 1588v2 messages must reside in the same 1588v2 domain.
5. (Optional) Run the [**ptp passive-measure enable**](cmdqueryname=ptp+passive-measure+enable) command to enable performance monitoring on the passive interface.
6. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
7. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable 1588v2 on the interface.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.