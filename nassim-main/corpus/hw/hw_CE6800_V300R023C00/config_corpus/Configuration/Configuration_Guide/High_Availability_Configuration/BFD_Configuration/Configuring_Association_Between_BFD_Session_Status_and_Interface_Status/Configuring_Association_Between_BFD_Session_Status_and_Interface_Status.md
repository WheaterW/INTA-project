Configuring Association Between BFD Session Status and Interface Status
=======================================================================

Configuring Association Between BFD Session Status and Interface Status

#### Prerequisites

Before associating the BFD session status with the interface status, you have completed the following tasks:

* Enable BFD globally.
* Create a single-hop BFD session with a multicast IP address configured as the peer address.
* Ensure that the BFD session is up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BFD session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) session-name
   ```
   
   The BFD session must be a single-hop BFD session with a multicast IP address configured as the peer address.
3. Associate the BFD session status with the status of the interface to which the BFD session is bound.
   
   
   ```
   [process-interface-status](cmdqueryname=process-interface-status) [ sub-if ] [ reboot-no-impact ]
   ```
   
   By default, a single-hop BFD session with a multicast IP address configured as the peer address is not associated with the status of the interface to which the BFD session is bound.
   
   After the [**process-interface-status**](cmdqueryname=process-interface-status) command is run:
   * If a BFD session detects a fault and goes down, the associated interface status becomes BFD Down. As a result, the direct route of the interface is removed from the routing table, but BFD packets can still be sent.
   * If multiple single-hop BFD sessions with a multicast IP address configured as the peer address are bound to the same interface, the [**process-interface-status**](cmdqueryname=process-interface-status) command can be configured only for one BFD session. In other words, the interface status is affected by only one BFD session.
   * Before you associate the BFD status with the interface status, ensure that the BFD configurations on two devices are correct and match each other. If the local BFD session is in the Down state, check whether the BFD configurations on both ends are correct.
   * If the BFD session status must be synchronized to the interface status immediately, ensure that the BFD configurations on the two devices are correct, and then run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands to shut down and start the BFD session. When the [**undo shutdown**](cmdqueryname=undo+shutdown) command is run in the BFD session view, a detection timer is initiated. If the BFD session goes up through negotiation before the timer expires, the BFD session notifies the bound interface of a BFD up event. Otherwise, the BFD session considers the link faulty and notifies the bound interface of a BFD down event. This way, the BFD session status is synchronized with the interface status in real time.
   * After the [**shutdown**](cmdqueryname=shutdown) command is run, the BFD session status will not be reported to the bound interface.
   * If the [**process-interface-status**](cmdqueryname=process-interface-status) command configured for a BFD session exists in the configuration file, after the device is restarted, the BFD session reports a BFD down event to the interface so that the interface sets its protocol state to Down. This prevents traffic loss when the BFD session is up but the interface is down during initialization of the device.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```