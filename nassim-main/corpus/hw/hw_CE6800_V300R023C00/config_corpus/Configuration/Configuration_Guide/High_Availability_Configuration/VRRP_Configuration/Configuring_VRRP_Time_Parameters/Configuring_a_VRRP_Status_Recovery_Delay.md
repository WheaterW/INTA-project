Configuring a VRRP Status Recovery Delay
========================================

Configuring a VRRP Status Recovery Delay

#### Context

Frequent changes to the status of the interface on which a VRRP group resides result in the VRRP status frequently flapping. To resolve this problem, configure a VRRP status recovery delay. Once set, the VRRP group only responds to a Startup event after the specified status recovery delay expires, preventing frequent VRRP status flapping caused by frequent interface status changes.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure a VRRP status recovery delay.
   ```
   [vrrp recover-delay](cmdqueryname=vrrp+recover-delay) delay-value
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command run in the system view takes effect for all VRRP groups configured on this device.
   
   The [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command run in the interface view takes effect for all VRRP groups configured on this interface. If the [**vrrp recover-delay**](cmdqueryname=vrrp+recover-delay) command is run in both the system and interface views, the configuration in the interface view takes effect.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.