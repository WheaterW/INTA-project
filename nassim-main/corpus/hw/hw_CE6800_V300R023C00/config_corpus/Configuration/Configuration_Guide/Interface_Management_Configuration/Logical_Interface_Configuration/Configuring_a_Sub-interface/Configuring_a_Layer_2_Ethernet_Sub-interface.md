Configuring a Layer 2 Ethernet Sub-interface
============================================

Configuring a Layer 2 Ethernet Sub-interface

#### Context

When a device connects to a Layer 2 network, you can configure Layer 2 Ethernet sub-interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a Layer 2 Ethernet sub-interface and enter its view.
   
   
   ```
   interface interface-type interface-number.subnumber mode [l2](cmdqueryname=interface+l2)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```