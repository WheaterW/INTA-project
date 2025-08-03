Configuring G.8275.1 on an Interface
====================================

After enabling G.8275.1 in the system view, you need to enable G.8275.1 in the interface view.

#### Context

Perform the following steps on each T-BC/T-TC:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the interface.
4. (Optional) Run the [**ptp notslave disable**](cmdqueryname=ptp+notslave+disable) command on the T-BC to set the notslave attribute of the interface to FALSE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * By default, an interface does not participate in G.8275.1 clock source selection. After the [**ptp notslave disable**](cmdqueryname=ptp+notslave+disable) command is run on an interface, the interface can participate in G.8275.1 clock source selection.
   * This command needs to be configured for the upstream or horizontal interface, but not for the downstream interface.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.