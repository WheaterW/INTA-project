Enabling VLAN-based Layer 2 Protocol Tunneling on an Interface
==============================================================

Enabling VLAN-based Layer 2 Protocol Tunneling on an Interface

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
4. Configure the link type of an interface.
   
   Perform either of the following operations as required:
   * Set the link type of the interface to trunk.
     
     1. Set the link type of the interface to trunk.
        
        ```
        [port link-type trunk](cmdqueryname=port+link-type+trunk)
        ```
     2. Add the interface to a specified VLAN.
        ```
        [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-40> | all }
        ```
   * Set the link type of the interface to hybrid.
     
     1. Set the link type of the interface to hybrid.
        
        ```
        [port link-type hybrid](cmdqueryname=port+link-type+hybrid)
        ```
     2. Configure the interface to allow packets from the VLAN to pass through in tagged mode.
        
        ```
        [port hybrid tagged vlan](cmdqueryname=port+hybrid+tagged+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
        ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The range of VLANs allowed by the interface must contain the VLAN IDs of Layer 2 protocol packets.
5. Enable VLAN-based Layer 2 protocol tunneling on the interface.
   
   
   ```
   [l2protocol-tunnel](cmdqueryname=l2protocol-tunnel) { all | user-defined-protocol protocol-name | protocol } [vlan](cmdqueryname=vlan) { low-vid [ to high-vid ] } &<1-10>
   ```
6. (Optional) Set a threshold above which an interface enabled with Layer 2 protocol tunneling drops protocol packets.
   
   
   ```
   [l2protocol-tunnel drop-threshold](cmdqueryname=l2protocol-tunnel+drop-threshold) rate [ user-defined-protocol protocol-name | { protocol } &<1-16> ]
   ```
   
   By default, the threshold is 0, indicating that the interface does not limit the rate of incoming Layer 2 protocol packets.
   
   Set this threshold to prevent malicious attacks caused by excessive Layer 2 protocol packets. When the number of such packets that an interface receives within 1s exceeds the configured threshold, the interface discards them.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```