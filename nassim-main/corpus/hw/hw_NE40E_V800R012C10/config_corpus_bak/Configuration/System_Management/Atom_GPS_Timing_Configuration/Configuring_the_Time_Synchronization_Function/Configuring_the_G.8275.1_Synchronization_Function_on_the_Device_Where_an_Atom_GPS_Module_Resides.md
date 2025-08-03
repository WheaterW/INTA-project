Configuring the G.8275.1 Synchronization Function on the Device Where an Atom GPS Module Resides
================================================================================================

To ensure G.8275.1 for time synchronization, you need to globally enable G.8275.1 in the system view, set the device type to T-BC, and configure basic information such as the domain value. After enabling G.8275.1 in the system view, you need to enable G.8275.1 in the interface view.

#### Context

Perform the following operations on the T-BC:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
3. Run the [**ptp profile g-8275-1 enable**](cmdqueryname=ptp+profile+g-8275-1+enable) command to enable G.8275.1 on the device.
4. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) **t-bc** command to set the device type to T-BC.
5. (Optional) Run the [**ptp domain**](cmdqueryname=ptp+domain) *domain-value* command to configure the clock domain where the device resides.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When G.8275.1 is used to perform time synchronization, T-BCs must reside in the same clock domain.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
7. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
8. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the interface.
9. Run the [**ptp notslave disable**](cmdqueryname=ptp+notslave+disable) command to configure the notSlave attribute of the interface as FALSE.
10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.