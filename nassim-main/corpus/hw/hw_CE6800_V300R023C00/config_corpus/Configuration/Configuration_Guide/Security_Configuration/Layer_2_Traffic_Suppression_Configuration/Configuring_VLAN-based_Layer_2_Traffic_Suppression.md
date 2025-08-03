Configuring VLAN-based Layer 2 Traffic Suppression
==================================================

VLAN-based traffic suppression prevents excessive traffic from burdening the network.

#### Context

Traffic suppression can be implemented only on a Layer 2 interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Create a specified VLAN.
   
   
   ```
   [vlan batch](cmdqueryname=vlan+batch) { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
6. Add interfaces to the VLAN.
   
   
   ```
   [port](cmdqueryname=port) interface-type { interface-number1 [ to interface-number2 ] } &<1-10>
   ```
7. Disable interfaces in the VLAN from forwarding unknown multicast packets.
   
   
   ```
   unknown-multicast discard
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```