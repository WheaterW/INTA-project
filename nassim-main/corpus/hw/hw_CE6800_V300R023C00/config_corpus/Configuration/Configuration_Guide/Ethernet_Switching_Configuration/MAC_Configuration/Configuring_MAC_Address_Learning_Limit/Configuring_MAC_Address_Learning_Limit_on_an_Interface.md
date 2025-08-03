Configuring MAC Address Learning Limit on an Interface
======================================================

Configuring MAC Address Learning Limit on an Interface

#### Context

After MAC address learning limit is configured on an interface, a device does not learn new MAC addresses from the interface when the configured limit is reached. You can also configure an action for the device to take in this situation. This action determines whether the device discards the packets with source MAC addresses out of the MAC address table.

![](public_sys-resources/note_3.0-en-us.png) 

Before configuring a MAC address learning limit rule, run the [**reset mac-address**](cmdqueryname=reset+mac-address) command to clear the learned MAC address entries. This will ensure the optimum effect of the configured rule.

If you run the [**mac-address limit**](cmdqueryname=mac-address+limit) command for the first time, you must configure the [**mac-address limit**](cmdqueryname=mac-address+limit) **maximum** command before configuring the **action** and **alarm** parameters. Then, there is no requirement on the configuration sequence of the parameters when you run the [**mac-address limit**](cmdqueryname=mac-address+limit) command.


![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported by the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2. Determine whether to perform this step based on the current interface working mode.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
4. Limit the number of learned MAC addresses on the interface.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) maximum max
   ```
   
   By default, the number of MAC addresses that can be learned on an interface is not limited.
5. Configure an action for the device to take when the number of learned MAC addresses reaches the limit.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) action { discard | forward }
   ```
   
   When the number of learned MAC addresses reaches the limit, the device takes an action according to the configuration. If the action is set to **discard**, the device discards the packets with source MAC addresses out of the MAC address table. If the action is set to **forward**, the device forwards packets with new source MAC addresses but does not add the new MAC addresses to the MAC address table.
6. Configure whether to generate an alarm when the number of learned MAC addresses reaches the limit.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) alarm { disable | enable }
   ```
   
   By default, an alarm is generated when the number of learned MAC addresses reaches the limit.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address limit**](cmdqueryname=display+mac-address+limit) [ *interface-type interface-number* ] command to check the MAC address learning limit rule.