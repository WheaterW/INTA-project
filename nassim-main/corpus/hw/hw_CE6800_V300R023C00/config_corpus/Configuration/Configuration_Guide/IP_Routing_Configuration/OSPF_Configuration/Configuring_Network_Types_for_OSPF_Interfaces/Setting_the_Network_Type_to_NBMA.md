Setting the Network Type to NBMA
================================

Setting the Network Type to NBMA

#### Prerequisites

Before setting the network type to NBMA, you have completed the following task:

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
4. Set the network type of the OSPF interface to NBMA.
   
   
   ```
   [ospf network-type](cmdqueryname=ospf+network-type) nbma
   ```
   The default network type of an Ethernet interface is broadcast. If a device that does not support multicast exists on the broadcast network, you can change the network type of the device interface to NBMA.![](../public_sys-resources/note_3.0-en-us.png) 
   
   The NBMA network must be fully meshed. That is, any two devices on the NBMA network must be directly reachable. In most cases, however, this requirement cannot be met. To address this issue, [change the network type to P2MP](vrp_ospf_cfg_0025.html).
5. (Optional) Set the interval at which Hello packets for polling are sent by the NBMA interface.
   
   
   ```
   [ospf timer poll](cmdqueryname=ospf+timer+poll) interval
   ```
   
   The default interval is 120 seconds.
   
   After the neighbor relationship on the NBMA network becomes invalid, the device sends Hello packets at the interval set using this command.
6. (Optional) Set a DR priority for the interface.
   
   
   ```
   [ospf dr-priority](cmdqueryname=ospf+dr-priority) priovalue
   ```
   
   By default, the DR priority of an interface is 1. A larger value indicates a higher priority.
   
   The priority of an interface determines whether the interface is qualified to be a DR or BDR. The interface with the highest priority is elected as the DR. However, if the priority of an interface on a device is 0, the device cannot be elected as a DR or BDR. On an NBMA network, you can set the DR priority of an interface to control the DR or BDR election. When the DR and BDR are elected on a network segment, they send DD packets to all neighboring nodes and set up adjacencies with all neighboring nodes.
7. (Optional) Set a wait interval for the OSPF interface.
   
   
   ```
   [ospf timer wait](cmdqueryname=ospf+timer+wait) interval
   ```
   
   By default, the wait interval is 120 seconds.
   
   If no Backup Seen event is received within the specified interval, the DR election starts. Setting a proper interval for the wait timer can slow down changes of the DR and BDR on the network, reducing network flapping. The interval of the wait timer cannot be greater than that of the Dead timer (set using the [**ospf timer dead**](cmdqueryname=ospf+timer+dead) command).
8. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
10. Set an IP address and a DR priority for a neighbor on the NBMA network.
    
    
    ```
    [peer](cmdqueryname=peer) ip-address [ dr-priority priority ]
    ```
    
    An NBMA interface cannot broadcast Hello packets to discover neighboring devices. Therefore, the IP address of a neighboring device must be configured in the OSPF process, and a DR priority must be set to determine whether the neighboring device can participate in DR election.
    
    If **dr-priority** *priority* is not specified in the command, the default DR priority 1 is used.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check information about OSPF interfaces.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **peer** command to check information about OSPF neighbors.
* Run the [**display ospf brief**](cmdqueryname=display+ospf+brief) command to check the interval at which Hello packets for polling are sent on the NBMA network.