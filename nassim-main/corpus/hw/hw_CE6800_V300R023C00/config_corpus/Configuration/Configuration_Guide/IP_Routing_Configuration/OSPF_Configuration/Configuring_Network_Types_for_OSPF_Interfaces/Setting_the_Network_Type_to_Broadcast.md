Setting the Network Type to Broadcast
=====================================

Setting the Network Type to Broadcast

#### Prerequisites

Before setting the network type to broadcast, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the network type of the OSPF interface to broadcast.
   
   
   ```
   [ospf network-type](cmdqueryname=ospf+network-type) broadcast
   ```
   
   By default, the network type of an Ethernet interface is broadcast.
   
   If a network is fully meshed (any two devices on the network are directly reachable) and all devices on the network support multicast, you can change the network type of a non-Ethernet interface to broadcast, thereby eliminating the need to manually specify neighbors.
5. (Optional) Set a DR priority for the interface.
   
   
   ```
   [ospf dr-priority](cmdqueryname=ospf+dr-priority) priovalue
   ```
   
   By default, the DR priority of an interface is 1. A larger value indicates a higher priority.
   
   The priority of an interface determines whether the interface is qualified to be a DR or BDR. The interface with the highest priority is elected as the DR. However, if the priority of an interface on a device is 0, the device cannot be elected as a DR or BDR. On a broadcast network, you can set the DR priority of an interface to control the DR or BDR election. When the DR and BDR are elected on a network segment, they send DD packets to all neighboring nodes and set up adjacencies with all neighboring nodes.
6. (Optional) Set a wait interval for the OSPF interface.
   
   
   ```
   [ospf timer wait](cmdqueryname=ospf+timer+wait) interval
   ```
   
   By default, the wait interval is 40 seconds.
   
   If no Backup Seen event is received within the specified interval, the DR election starts. Setting a proper interval for the wait timer can slow down changes of the DR and BDR on the network, reducing network flapping. The interval of the wait timer cannot be greater than that of the Dead timer (set using the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command).
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.