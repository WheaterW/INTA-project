Disabling MAC Address Learning in a BD
======================================

Disabling MAC Address Learning in a BD

#### Context

If a network is not changed often, you can disable MAC address learning in a BD to improve device security. After MAC address learning is disabled in the BD, the device does not learn new MAC addresses from interfaces in the BD. In such cases, the device cannot communicate with other devices through the BD, improving network stability and security.

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
3. Disable MAC address learning.
   
   
   ```
   [mac-address learning disable](cmdqueryname=mac-address+learning+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | *bd-id* [ **verbose** | **brief** | **binding-info** ] ] command to check whether MAC address learning is successfully disabled in a BD.