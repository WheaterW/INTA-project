Setting the Network Type to NBMA
================================

Setting the Network Type to NBMA

#### Prerequisites

Before setting the network type to NBMA, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the network type of the OSPFv3 interface to NBMA.
   
   
   ```
   [ospfv3 network-type](cmdqueryname=ospfv3+network-type) nbma [ instance instance-id ]
   ```
   
   The default network type of an Ethernet interface is broadcast. If a device that does not support multicast exists on the broadcast network, you can change the network type of the device interface to NBMA.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The NBMA network must be fully meshed. That is, any two devices on the NBMA network must be directly reachable. In most cases, however, this requirement cannot be met. To address this issue, [change the network type to P2MP](vrp_ospfv3_cfg_0024.html).
5. Configure a neighbor on the NBMA network.
   
   
   ```
   [ospfv3 peer router-id](cmdqueryname=ospfv3+peer+router-id) router-id-value prefix [ dr-eligible | cost cost-value | instance instance-id | poll poll-interval ] *
   ```
   
   An NBMA interface cannot broadcast Hello packets to discover neighboring devices. Therefore, you need to specify the IP address of a neighboring device in the process, and determine whether the neighboring device can participate in DR election. You can also set other parameters such as the cost.
   
   By default, no IP address is configured for the neighboring device on an NBMA network, and whether the neighboring device can participate in DR election is not specified.
6. (Optional) Set the interval at which polling packets are sent by the NBMA interface.
   
   
   ```
   [ospfv3 timer poll](cmdqueryname=ospfv3+timer+poll) interval [ instance instance-id ]
   ```
   
   The default interval is 120 seconds.
   
   After the neighbor relationship on the NBMA network becomes invalid, the device sends Hello packets at the interval set using this command.
7. (Optional) Set a DR priority for the OSPFv3 interface.
   
   
   ```
   [ospfv3 dr-priority](cmdqueryname=ospfv3+dr-priority) priovalue [ instance instanceId ]
   ```
   
   By default, the DR priority of an interface is 1. A larger value indicates a higher priority.
   
   The priority of an interface determines whether the interface is qualified to be a DR or BDR. The interface with the highest priority is elected as the DR. However, if the priority of an interface on a device is 0, the device cannot be elected as a DR or BDR. On an NBMA network, you can set the DR priority of an interface to control the DR or BDR election. When the DR and BDR are elected on a network segment, they send DD packets to all neighboring nodes and set up adjacencies with all neighboring nodes.
8. (Optional) Set a wait interval for the OSPFv3 interface.
   
   
   ```
   [ospfv3 timer wait](cmdqueryname=ospfv3+timer+wait) interval [ instance instance-id ]
   ```
   
   By default, the wait interval is 40 seconds.
   
   If no Backup Seen event is received within the specified interval, the DR election starts. Setting a proper interval for the wait timer can slow down changes of the DR and BDR on the network, reducing network flapping. The interval of the wait timer cannot be greater than that of the Dead timer (set using the [**ospfv3 timer dead**](cmdqueryname=ospfv3+timer+dead) command).
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **peer** command to check information about OSPFv3 neighbors.

#### Follow-up Procedure

![](../public_sys-resources/notice_3.0-en-us.png) 

Changing the DR priority leads to DR/BDR re-election and terminates the OSPFv3 adjacency between devices. Therefore, changing the DR priority is typically not recommended.

You can use either of the following methods to trigger DR/BDR re-election:

* Restart all devices.
* Run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in sequence on each of the interfaces that are used to establish OSPFv3 neighbor relationships.