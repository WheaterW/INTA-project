Configuring Dynamic BFD for RIP
===============================

Configuring Dynamic BFD for RIP

#### Prerequisites

Before configuring dynamic BFD for RIP, you have completed the following tasks:

* Assign an IP address to each interface to ensure reachability between neighboring nodes at the network layer.
* [Configure basic RIP functions](vrp_rip_cfg_0008.html).

#### Context

Generally, RIP uses timers to receive and send Update messages to maintain neighbor relationships. However, if a RIP routing device does not receive an Update message after the age timer expires, the RIP routing device will announce that this neighbor goes down. The default value of the age timer is 180s. If a link fails, RIP can only detect the failure after 180s. During this time, if high-rate data services are deployed on a network, a large amount of data will be lost.

BFD provides millisecond-level fault detection and can rapidly detect faults in protected links or nodes and report them to RIP. This speeds up RIP's response to network topology changes and achieves rapid RIP route convergence.

In BFD for RIP, BFD session establishment is triggered by RIP. When establishing a neighbor relationship, RIP sends detection parameters of the neighbor to BFD, and a BFD session will be established based on these parameters. If a link fault occurs, the local RIP process will receive a neighbor unreachable message within milliseconds, and the local RIP routing device will delete routing entries in which the neighbor relationship is down and use the backup path to transmit messages.

BFD for RIP can be configured using either of the following methods:

* [Enabling BFD in a RIP process](#EN-US_TASK_0000001130623188__step_dc_vrp_rip_cfg_005501): This method is recommended when BFD for RIP needs to be enabled on most RIP interfaces.
* [Enabling BFD on an RIP interface](#EN-US_TASK_0000001130623188__step_dc_vrp_rip_cfg_005502): This method is recommended when BFD for RIP needs to be enabled on a small number of RIP interfaces.



#### Procedure

* Enable BFD in a RIP process.
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
  4. Create a RIP process and enter the RIP view.
     
     
     ```
     [rip](cmdqueryname=rip) process-id
     ```
  5. Enable BFD in the RIP process and establish a BFD session.
     
     
     ```
     [bfd all-interfaces enable](cmdqueryname=bfd+all-interfaces+enable)
     ```
     
     
     
     If BFD is enabled globally, RIP will use the default BFD parameters to establish BFD sessions on all the interfaces where RIP neighbor relationships are up.
  6. (Optional) Configure the BFD parameters used to establish a BFD session.
     
     
     ```
     [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) { min-rx-interval min-receive-value | min-tx-interval min-transmit-value | detect-multiplier detect-multiplier-value }*
     ```
     
     
     
     By default, the minimum interval at which BFD packets are sent and the minimum interval at which BFD packets are received are 10 ms, and the detection multiplier is 3.
     
     The BFD parameters for establishing a BFD session are changed on all RIP interfaces after running this command. As such, you are advised to use the default detection multiplier and default effective intervals at which BFD packets are sent and received.![](public_sys-resources/note_3.0-en-us.png) 
     
     Configure BFD parameter values based on the reliability requirements of the live network.
     
     + If the live network requires high reliability, reduce the effective interval at which BFD packets are sent.
     + If the live network does not require high reliability, increase the effective interval at which BFD packets are sent.The BFD detection intervals are calculated as follows:
     + Effective interval at which BFD packets are sent from the local device = Max (**min-tx-interval** configured on the local device, **min-rx-interval** configured on the peer device)
     + Effective interval at which BFD packets are received by the local device = Max (**min-tx-interval** configured on the remote device, **min-rx-interval** configured on the local device)
     + Detection interval of the local device = Effective interval at which BFD packets are received by the local device x BFD detection multiplier configured on the remote device
  7. (Optional) Perform the following operations to prevent an interface in the RIP process from establishing a BFD session:
     
     
     1. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     2. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     3. Prevent the interface from creating a BFD session.
        ```
        [rip bfd block](cmdqueryname=rip+bfd+block)
        ```
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable BFD on a RIP interface.
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
  5. Enable BFD on the interface to establish a BFD session.
     
     
     ```
     [rip bfd enable](cmdqueryname=rip+bfd+enable)
     ```
  6. (Optional) Configure the BFD parameters used to establish a BFD session.
     
     
     ```
     [rip bfd](cmdqueryname=rip+bfd) { min-rx-interval min-receive-value | min-tx-interval min-transmit-value | detect-multiplier detect-multiplier-value } *
     ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

After enabling BFD for RIP at both ends of a link, run the [**display rip bfd session**](cmdqueryname=display+rip+bfd+session) { **interface** *interface-type* *interface-number* | *neighbor-id* | **all** } command. In the command output, if **BFDState** is displayed as **Up**, a BFD session has been established.