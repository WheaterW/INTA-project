Setting the Interval at Which LSAs Are Retransmitted to OSPF Adjacency Devices
==============================================================================

Setting the Interval at Which LSAs Are Retransmitted to OSPF Adjacency Devices

#### Prerequisites

Before setting the interval at which LSAs are retransmitted to OSPF adjacency devices, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

After sending an LSA to an adjacency device (neighbor), a device waits for the neighbor to reply with an LSAck packet. If the device does not receive an LSAck packet after the retransmission interval elapses n times, it retransmits the LSA to its neighbor, the device retransmits the LSA to its neighbor. The retransmission interval is defined as follows:

First retransmission: Interval = User-configured retransmission interval (*interval*).

Second retransmission: Interval = User-configured retransmission interval (*interval*).

Third retransmission: Interval = User-configured retransmission interval (*interval*).

Fourth retransmission: Interval = User-configured retransmission interval (*interval*) x 2.

Fifth retransmission: Interval = User-configured retransmission interval (*interval*) x 2^2.

Nth retransmission: Interval = User-configured retransmission interval (*interval*) x 2^(n â 3).

If interval x 2^(n â 3) is greater than 30, the retransmission interval for the nth time is 30.

If the user-configured retransmission interval (*interval*) is greater than 30, the retransmission interval for the nth time is equal to this user-configured interval.

You can set an appropriate interval at which LSAs are retransmitted based on network conditions in order to accelerate convergence.


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
4. Set the interval at which LSAs are retransmitted to adjacency devices.
   
   
   ```
   [ospfv3 timer retransmit](cmdqueryname=ospfv3+timer+retransmit) interval [ instance instance-id ]
   ```
   
   The default retransmission interval is 5 seconds.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Setting the interval to a proper value is recommended. An excessively short interval will cause unnecessary retransmission. Generally, the interval should be longer than the round trip of a packet that is transmitted between two devices.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3+retrans-list)[ *process-id* ] **retrans-list** command to check information about the OSPFv3 LSA retransmission list.