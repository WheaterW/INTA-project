(Optional) Configuring an Action to Process Packets That Do Not Match a GTSM Policy
===================================================================================

(Optional) Configuring an Action to Process Packets That Do Not Match a GTSM Policy

#### Context

After GTSM is enabled, you can enable a device either to allow the packets that do not match a GTSM policy to pass or to drop such packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device either to allow packets that do not match a GTSM policy to pass or to drop such packets.
   
   
   ```
   [gtsm default-action](cmdqueryname=gtsm+default-action) { drop | pass }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The configured action takes effect only if GTSM is enabled.
   * Check whether the granularity specified in the GTSM policy is too fine. If an over fine-grained policy is configured, you are not advised to set the action to **drop**, preventing a large number of unmatched packets from being incorrectly dropped.
   * If the action is set to **drop**, you can determine whether to log the dropped packet information. Enabling the log function facilitates fault locating.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```