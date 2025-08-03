(Optional) Configuring Access Control for 1588v2 Clock Source Selection
=======================================================================

(Optional) Configuring Access Control for 1588v2 Clock Source Selection

#### Context

As many devices may participate in dynamic BMC selection on a large 1588v2 network, clock attacks or unintended configuration errors may cause clock flapping on the entire network. To address this issue, you can limit the range of clock sources that are allowed to participate in dynamic BMC selection by configuring access control for clock source selection.

Perform the following steps on each 1588v2 device:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable access control for 1588v2 clock source selection.
   
   
   ```
   [ptp acl enable](cmdqueryname=ptp+acl+enable)
   ```
   
   
   
   By default, access control is not enabled for clock source selection.
3. Configure the ID of another 1588v2 device to be allowed to participate in BMC selection.
   
   
   ```
   [ptp acl-permit-clockid](cmdqueryname=ptp+acl-permit-clockid) clockid-value
   ```
   
   
   
   By default, if no clock ID range is specified for clock devices that are allowed to participate in dynamic BMC selection after access control is enabled for clock source selection, no clock source participates in dynamic BMC selection.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To cancel the configuration of the slave clock, run the [**undo ptp enable**](cmdqueryname=undo+ptp+enable) command on the interface, and then run the [**undo ptp acl enable**](cmdqueryname=undo+ptp+acl+enable) and [**ptp acl-permit-clockid**](cmdqueryname=ptp+acl-permit-clockid) *clockid-value* commands.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```