Enabling QinQ-based Layer 2 Protocol Tunneling on an Interface
==============================================================

Enabling QinQ-based Layer 2 Protocol Tunneling on an Interface

#### Context

Perform the following operations on a PE according to the type of the protocol whose packets need to be transparently transmitted.

![](public_sys-resources/note_3.0-en-us.png) 

Do not specify the same protocol type for the [**l2protocol-tunnel vlan**](cmdqueryname=l2protocol-tunnel+vlan) and [**l2protocol-tunnel enable**](cmdqueryname=l2protocol-tunnel+enable) commands on the same interface. Otherwise, the system displays a message indicating a configuration conflict.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a user-side interface on the PE.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Change the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the link type of the interface to dot1q-tunnel.
   
   
   ```
   [port link-type dot1q-tunnel](cmdqueryname=port+link-type+dot1q-tunnel)
   ```
5. Configure the interface to add an outer VLAN tag to Layer 2 protocol packets from users.
   
   
   ```
   [port default vlan](cmdqueryname=port+default+vlan) vlan-id
   ```
6. Enable QinQ-based Layer 2 protocol tunneling on the interface.
   
   
   ```
   [l2protocol-tunnel](cmdqueryname=l2protocol-tunnel) { all | user-defined-protocol protocol-name | protocol } [vlan](cmdqueryname=vlan) { low-vid [ to high-vid ] } &<1-10>
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The outer VLAN specified in step 5 must be included in the range of VLANs configured in step 6.
7. (Optional) Set a threshold above which an interface enabled with Layer 2 protocol tunneling drops protocol packets.
   
   
   ```
   [l2protocol-tunnel drop-threshold](cmdqueryname=l2protocol-tunnel+drop-threshold) rate [ user-defined-protocol protocol-name | { protocol } &<1-16> ]
   ```
   
   By default, the threshold is 0, indicating that the interface does not limit the rate of incoming Layer 2 protocol packets.
   
   Set this threshold to prevent malicious attacks caused by excessive Layer 2 protocol packets. When the number of such packets that an interface receives within 1s exceeds the configured threshold, the interface discards them.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```