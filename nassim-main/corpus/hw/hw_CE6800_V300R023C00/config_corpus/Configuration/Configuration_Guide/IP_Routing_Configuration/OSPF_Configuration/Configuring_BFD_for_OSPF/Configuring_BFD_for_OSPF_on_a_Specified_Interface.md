Configuring BFD for OSPF on a Specified Interface
=================================================

Configuring BFD for OSPF on a Specified Interface

#### Prerequisites

Before configuring BFD for OSPF on a specified interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

After BFD for OSPF is configured on a device interface, BFD quickly detects link faults on the interface and instructs OSPF to immediately recalculate routes, maximizing the speed of OSPF convergence. When the OSPF neighbor relationship goes Down, the BFD session will be dynamically deleted. Perform the following steps on the device where a BFD session needs to be configured on a specified interface:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
6. Configure BFD for OSPF.
   
   
   ```
   [ospf bfd](cmdqueryname=ospf+bfd) enable [ per-link one-arm-echo ]
   ```
   
   After this step is performed, when the neighbor relationship on the specified interface is in the Full state, OSPF creates a BFD session with default parameter values for this interface.
   
   If BFD for OSPF is configured for an Eth-Trunk with multiple physical interfaces added in a VLAN, and [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) is not specified, the BFD session may go down even if only one of the physical interfaces goes down. As a result, the OSPF neighbor relationship also goes down. If [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) is specified in this case, the BFD session goes down only if all the physical interfaces are down, which prevents the OSPF neighbor relationship from going down.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BFD for OSPF on an interface takes precedence over that in the OSPF process.
   
   The [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) parameter can be specified only in the VLANIF interface view.
7. (Optional) Modify BFD session parameters.
   
   
   ```
   [ospf bfd](cmdqueryname=ospf+bfd) { min-tx-interval transmit-interval | min-rx-interval receive-interval | detect-multiplier multiplier-value | frr-binding } *
   ```
   
   The default interval at which BFD packets are transmitted and the default detection multiplier are recommended. As such, this step can be skipped.
   
   The parameters need to be configured based on network conditions and requirements on network reliability. A short transmission interval for BFD packets can be set for a link that requires high reliability, and a long transmission interval can be used when reliability is not as critical.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local device = Max { *transmit-interval* (interval at which BFD packets are transmitted) set on the local device, *receive-interval* (interval at which BFD packets are received) set on the peer device }
   * Actual interval at which BFD packets are received on the local device = Max { *transmit-interval* (interval at which BFD packets are transmitted) set on the peer device, *receive-interval* (interval at which BFD packets are received) set on the local device }
   * Actual period for BFD detection on the local device = Actual interval at which BFD packets are received on the local device x Detection multiplier specified by *multiplier-value* on the peer device
   
   For example, if the following conditions are met:
   
   * On the local device, the interval at which BFD packets are transmitted is set to 200 ms, the interval at which BFD packets are received is set to 300 ms, and the detection multiplier is set to 4.
   * On the peer device, the interval at which BFD packets are transmitted is set to 100 ms, the interval at which BFD packets are received is set to 600 ms, and the detection multiplier is set to 5.
   
   The following results are then obtained:
   
   * On the local device, the actual interval at which BFD packets are transmitted is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual interval at which BFD packets are received is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual detection period is 1500 ms (calculated by 300 ms x 5).
   * On the peer device, the actual interval at which BFD packets are transmitted is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual interval at which BFD packets are received is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual detection period is 2400 ms (calculated by 600 ms x 4).
8. (Optional) Enable the OSPF interface to adjust its cost based on the status of an associated BFD session.
   
   
   ```
   [ospf bfd incr-cost](cmdqueryname=ospf+bfd+incr-cost) { cost | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [*process-id* ] **bfd** **session** *interface-type* *interface-number* [ *router-id* ] command to check information about the session of BFD for OSPF on the specified interface.