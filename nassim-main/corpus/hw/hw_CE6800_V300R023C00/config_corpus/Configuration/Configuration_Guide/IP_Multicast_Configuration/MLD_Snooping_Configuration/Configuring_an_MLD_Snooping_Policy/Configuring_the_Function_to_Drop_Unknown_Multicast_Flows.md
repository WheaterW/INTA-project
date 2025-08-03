Configuring the Function to Drop Unknown Multicast Flows
========================================================

Configuring the Function to Drop Unknown Multicast Flows

#### Context

A multicast flow is considered unknown if it does not match any entry in the multicast forwarding table. By default, a device broadcasts unknown multicast flows in the corresponding VLAN. To reduce the instantaneous bandwidth usage involved in this case, you can configure the device to drop unknown multicast flows.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the function to drop unknown multicast flows.
   
   
   ```
   [unknown-multicast discard](cmdqueryname=unknown-multicast+discard)
   ```
   
   To prevent multicast traffic forwarding failures, you are advised not to perform this configuration in the VLAN if the corresponding VLANIF interface has Layer 3 multicast configured and functions as a multicast traffic inbound interface.
   
   After this configuration is performed, the device discards received unknown multicast data packets. As a result, multicast traffic may fail to be forwarded.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```