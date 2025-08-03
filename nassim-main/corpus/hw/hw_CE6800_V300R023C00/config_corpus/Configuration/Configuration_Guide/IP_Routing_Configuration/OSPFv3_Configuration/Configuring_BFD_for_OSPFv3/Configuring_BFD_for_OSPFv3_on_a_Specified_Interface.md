Configuring BFD for OSPFv3 on a Specified Interface
===================================================

Configuring BFD for OSPFv3 on a Specified Interface

#### Prerequisites

Before configuring BFD for OSPFv3 on a specified interface, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

After BFD for OSPFv3 is configured on an interface, BFD quickly detects link faults on the interface and instructs OSPFv3 to immediately recalculate routes, speeding up OSPFv3 convergence. If the neighbor relationship goes down, the BFD session will be deleted dynamically. Perform the following steps on the device where the specified interface resides.


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
5. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
6. Enable OSPFv3 on the interface.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) process-id area area-id [ instance instance-id ]
   ```
   
   
   
   The specified area ID can be a decimal integer or in the IPv4 address format. Regardless of the specified format, the area ID is displayed as an IPv4 address.
7. Configure BFD on the interface to trigger the creation of a BFD session.
   
   
   ```
   [ospfv3 bfd](cmdqueryname=ospfv3+bfd) enable
   ```
   
   After this step is performed, when the neighbor relationship on the specified interface is in the Full state, OSPFv3 creates a BFD session with default parameter values for this interface.
   
   If BFD for OSPFv3 is configured for an Eth-Trunk with multiple physical interfaces added in a VLAN, and [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) is not specified, the BFD session may go down even if only one of the physical interfaces goes down. As a result, the OSPFv3 neighbor relationship also goes down. If [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) is specified in this case, the BFD session goes down only if all the physical interfaces are down, which ensures that the OSPFv3 neighbor relationship can be established normally.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BFD on an interface takes precedence over that in a process.
   
   The [**per-link one-arm-echo**](cmdqueryname=per-link+one-arm-echo) parameter can be specified only in the VLANIF interface view.
8. (Optional) Modify the session parameters of BFD for OSPFv3.
   
   
   ```
   [ospfv3 bfd](cmdqueryname=ospfv3+bfd) { min-transmit-interval min-transmit-value | min-receive-interval min-receive-value | detect-multiplier detect-multiplier-value | frr-binding } * [ instance instance-id ] 
   ```
   
   The default interval at which BFD packets are transmitted and the default detection multiplier are recommended. As such, this step can be skipped.
   
   The parameters need to be configured based on network conditions and requirements on network reliability. A short transmission interval for BFD packets can be set for a link that requires high reliability, and a long transmission interval can be used for a link that has low reliability requirements.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local device = Max { *min-transmit-value* (interval at which BFD packets are transmitted) set on the local device, *min-receive-value* (interval at which BFD packets are received) set on the peer device }
   * Actual interval at which BFD packets are received on the local device = Max { *min-transmit-value* (interval at which BFD packets are transmitted) set on the peer device, *min-receive-value* (interval at which BFD packets are received) set on the local device }
   * Actual period for BFD detection on the local device = Actual interval at which BFD packets are received on the local device x Detection multiplier specified by *detect-multiplier-value* on the peer device
   
   For example:
   
   * On the local device, the interval at which BFD packets are transmitted is set to 200 ms, the interval at which BFD packets are received is set to 300 ms, and the detection multiplier is set to 4.
   * On the peer device, the interval at which BFD packets are transmitted is set to 100 ms, the interval at which BFD packets are received is set to 600 ms, and the detection multiplier is set to 5.
   
   Then:
   
   * On the local device, the actual interval at which BFD packets are transmitted is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual interval at which BFD packets are received is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual detection period is 1500 ms (calculated by 300 ms x 5).
   * On the peer device, the actual interval at which BFD packets are transmitted is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual interval at which BFD packets are received is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual detection period is 2400 ms (calculated by 600 ms x 4).
9. (Optional) Enable the OSPFv3 interface to adjust its cost based on the status of an associated BFD session.
   
   
   ```
   [ospfv3 bfd incr-cost](cmdqueryname=ospfv3+bfd+incr-cost) { cost | max-reachable } [ instance instance-id ]
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [*process-id* ] **bfd** **session** [ *interface-type* *interface-number* ] [ *neighbor-id* ] [ **verbose** ] command to check information about BFD for OSPFv3 sessions.