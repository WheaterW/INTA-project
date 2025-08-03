Configuring Layer 3 Port Isolation
==================================

Configuring Layer 3 Port Isolation

#### Context

After Layer 3 port isolation is configured, Layer 3 traffic whose outbound and inbound interfaces are the same is discarded on the outbound interface to prevent loops. After Layer 3 port isolation is enabled, only Layer 3 traffic is isolated.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable Layer 3 port isolation.
   
   
   ```
   [port-isolate l3 enable](cmdqueryname=port-isolate+l3+enable)
   ```
   
   By default, Layer 3 port isolation is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```