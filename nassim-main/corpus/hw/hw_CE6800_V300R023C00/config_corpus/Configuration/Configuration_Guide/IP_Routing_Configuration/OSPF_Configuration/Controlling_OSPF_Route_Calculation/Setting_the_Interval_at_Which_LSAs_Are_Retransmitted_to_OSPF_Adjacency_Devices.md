Setting the Interval at Which LSAs Are Retransmitted to OSPF Adjacency Devices
==============================================================================

Setting the Interval at Which LSAs Are Retransmitted to OSPF Adjacency Devices

#### Prerequisites

Before setting the interval at which LSAs are retransmitted to OSPF adjacency devices, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

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
3. Set the interval at which LSAs are retransmitted to OSPF adjacency devices.
   
   
   ```
   [ospf timer retransmit](cmdqueryname=ospf+timer+retransmit) interval
   ```
   
   Setting the interval to a proper value is recommended. An excessively short interval will cause unnecessary retransmission. Generally, the interval should be longer than the round trip of a packet that is transmitted between two devices.
   
   The default retransmission interval is 5 seconds, which is recommended.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **retrans-queue** [ *interface-type* *interface-number* ] [ *neighbor-id* ] command to check information about the LSA retransmission list.