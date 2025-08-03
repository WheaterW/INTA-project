Configuring a VRRP6 Status Recovery Delay
=========================================

Configuring a VRRP6 Status Recovery Delay

#### Context

Frequent changes to the status of the interface on which a VRRP6 group resides result in the VRRP6 status frequently flapping. To resolve this problem, configure a VRRP6 status recovery delay. Once set, the VRRP6 group only responds to a VRRP6 interface up event after the specified status recovery delay expires, preventing frequent VRRP6 status flapping caused by frequent interface status changes.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the view of the interface where a VRRP6 group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Configure a VRRP6 status recovery delay.
   ```
   [vrrp6 recover-delay](cmdqueryname=vrrp6+recover-delay) delay-value
   ```
   
   The default VRRP6 status recovery delay is 0 seconds, indicating that VRRP6 status flapping is not suppressed.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.