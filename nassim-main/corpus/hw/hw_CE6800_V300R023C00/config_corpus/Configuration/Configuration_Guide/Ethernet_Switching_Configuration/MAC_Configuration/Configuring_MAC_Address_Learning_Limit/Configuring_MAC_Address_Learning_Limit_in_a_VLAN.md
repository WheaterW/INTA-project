Configuring MAC Address Learning Limit in a VLAN
================================================

Configuring MAC Address Learning Limit in a VLAN

#### Context

After MAC address learning limit is configured in a VLAN, the device does not learn new MAC addresses on interfaces in the VLAN when the configured limit is reached. You can also configure an action for the device to take in this situation. This action determines whether the device discards the packets with source MAC addresses out of the MAC address table.

![](public_sys-resources/note_3.0-en-us.png) 

Before configuring a MAC address learning limit rule, run the [**reset mac-address**](cmdqueryname=reset+mac-address) command to clear the learned MAC address entries. This will ensure the optimum effect of the configured rule.

If you run the [**mac-address limit**](cmdqueryname=mac-address+limit) command for the first time, you must configure the [**mac-address limit**](cmdqueryname=mac-address+limit) **maximum** command before configuring the **action** and **alarm** parameters. Then, there is no requirement on the configuration sequence of the parameters when you run the [**mac-address limit**](cmdqueryname=mac-address+limit) command.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Limit the number of learned MAC addresses in the VLAN.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) maximum max
   ```
   
   By default, the number of MAC addresses that can be learned in a VLAN is not limited.
4. Configure an action for the device to take when the number of learned MAC addresses reaches the limit.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) action { discard | forward }
   ```
   
   When the number of learned MAC addresses reaches the limit, by default, a device forwards packets with new source MAC addresses but does not generate MAC address entries based on these MAC addresses.
5. Configure whether to generate an alarm when the number of learned MAC addresses reaches the limit.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) alarm { disable | enable }
   ```
   
   By default, an alarm is generated when the number of learned MAC addresses reaches the limit.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address limit**](cmdqueryname=display+mac-address+limit) [ **vlan** *vlan-id* ] command to check the MAC address learning limit rule.