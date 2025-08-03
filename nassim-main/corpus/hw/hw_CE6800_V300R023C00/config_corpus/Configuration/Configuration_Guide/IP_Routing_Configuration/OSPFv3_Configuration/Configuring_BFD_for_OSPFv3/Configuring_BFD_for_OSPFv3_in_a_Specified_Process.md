Configuring BFD for OSPFv3 in a Specified Process
=================================================

Configuring BFD for OSPFv3 in a Specified Process

#### Prerequisites

Before configuring BFD for OSPFv3 in a specified process, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

After BFD for OSPFv3 is configured, upon detection of a link fault, BFD immediately notifies the devices at both ends of the link, triggering rapid OSPFv3 convergence. If the neighbor relationship goes down, the BFD session will be deleted dynamically. If you want to configure BFD for all interfaces in a specified OSPFv3 process and trigger BFD session creation, perform the following steps on the devices between which a BFD session is to be created.


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
4. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
5. Enable BFD in the OSPFv3 process to trigger the creation of BFD sessions for OSPFv3.
   
   
   ```
   [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) enable
   ```
   
   By default, BFD is disabled in an OSPFv3 process.
6. (Optional) Modify the session parameters of BFD for OSPFv3.
   
   
   ```
   [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) { min-transmit-interval Tx-Value | min-receive-interval Rx-Value | detect-multiplier Mul-Value | frr-binding } *
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
7. (Optional) Enable an OSPFv3 process to adjust the cost based on the status of an associated BFD session.
   
   
   ```
   [bfd all-interfaces incr-cost](cmdqueryname=bfd+all-interfaces+incr-cost) { cost | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
8. (Optional) Disable a specified interface from dynamically creating a BFD for OSPFv3 session.
   1. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
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
   4. Disable the interface from dynamically creating a BFD session.
      
      
      ```
      [ospfv3 bfd block](cmdqueryname=ospfv3+bfd+block)
      ```
      
      After BFD for OSPFv3 is configured using the [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **enable** command, all interfaces on which neighbor relationships are Full in the OSPFv3 process will create BFD sessions. If BFD is not required on specific interfaces, disable these interfaces from creating BFD sessions.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [*process-id* ] **bfd** **session** [ *interface-type* *interface-number* ] [ *neighbor-id* ] [ **verbose** ] command to check information about BFD for OSPFv3 sessions.