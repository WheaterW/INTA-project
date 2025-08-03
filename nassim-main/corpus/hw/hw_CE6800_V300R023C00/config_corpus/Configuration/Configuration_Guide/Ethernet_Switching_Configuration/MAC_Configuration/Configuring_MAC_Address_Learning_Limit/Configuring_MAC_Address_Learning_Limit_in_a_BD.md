Configuring MAC Address Learning Limit in a BD
==============================================

Configuring MAC Address Learning Limit in a BD

#### Context

After MAC address learning limit is configured in a BD, the device does not learn new MAC addresses on interfaces in the BD when the configured limit is reached. You can also configure an action for the device to take in this situation. This action determines whether the device discards the packets with source MAC addresses out of the MAC address table.

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
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Limit the number of learned MAC addresses.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) maximum max
   ```
   
   By default, the number of MAC addresses that can be learned is not set.
4. Configure an action for the device to take when the number of learned MAC addresses reaches the limit.
   
   
   ```
   [mac-address limit](cmdqueryname=mac-address+limit) action { discard | forward }
   ```
   
   By default, the device takes the **forward** action on packets when the number of learned MAC addresses reaches the limit. That is, the device forwards packets with new source MAC addresses but does not add the new MAC addresses to the MAC address table.
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

Run the [**display mac-address limit**](cmdqueryname=display+mac-address+limit) [ **bridge-domain** *bd-id* ] command to check the MAC address learning limit rule.