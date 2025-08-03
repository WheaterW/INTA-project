Associating a BFD Session with an Interface
===========================================

This section describes how to associate a BFD session with an interface to trigger rapid route convergence if a fault occurs. It can be used only in multicast IP single-hop BFD sessions and link-bundle single-hop BFD sessions.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172361661__fig_dc_vrp_bfd_cfg_200001), two devices are directly connected at the network layer but are segmented physically by transmission devices. If the link fails, the devices take a long time to detect the fault and age the direct route. As a result, the network interruption lasts for a long time.

**Figure 1** Link with transmission devices between two ends  
![](images/fig_dc_vrp_bfd_cfg_200001.png)  

To speed up route convergence, associate the BFD status with the interface status so that a change in the BFD session status will trigger the protocol status change on the interface rapidly, triggering fast route convergence. When BFD detects a fault, it enters the down state, and then the bound interface also enters the BFD down state.


#### Pre-configuration Tasks

Before associating a BFD session with an interface, complete the following tasks:

* Enable BFD globally.
* Create a multicast IP single-hop BFD session or a link-bundle single-hop BFD session.
* Set up a BFD session and ensure that the BFD session is up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**process-interface-status**](cmdqueryname=process-interface-status) [ **sub-if** ] [ **reboot-no-impact** ]
   
   
   
   The association is configured between the BFD session status and the status of the bound interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) After the [**process-interface-status**](cmdqueryname=process-interface-status) command is run, the following situations occur:
   * If a BFD session detects a fault and goes down, the associated interface status becomes BFD\_Down. As a result, the direct route of the interface is removed from the routing table on the control plane, but BFD packets can still be sent.
   * The BFD status will not be reported to the interface if the BFD status changes while the [**commit**](cmdqueryname=commit) command is being executed. This prevents an incorrect BFD status message (when the BFD session is not established or does not go up) from causing an incorrect interface status change. When the [**commit**](cmdqueryname=commit) command is run and the BFD status changes, a BFD session reports the BFD status to the interface to trigger the status of the associated interface change.
   * If multiple single-hop BFD sessions with a multicast IP address configured as the peer address are bound to the same interface, the [**process-interface-status**](cmdqueryname=process-interface-status) command can be configured only for one BFD session. In other words, the interface status is affected by only one BFD session. Between link-bundle sessions and multicast sessions, and between link-bundle sessions, one interface can be bound to multiple BFD sessions enabled with the [**process-interface-status**](cmdqueryname=process-interface-status) command. When an interface is bound to multiple BFD sessions that are associated with the interface status, the protocol status of the associated interface goes down as long as one BFD session is down. After the protocol status of the associated interface goes down, the protocol status of the associated interface goes up as long as one BFD session is up.
   * Before you associate the BFD status with the interface status, ensure that the BFD configurations on two devices are correct and consistent. If the local BFD session is in the down state, check whether the BFD configuration on the peer device is correct and whether the remote BFD session is shut down.
   * If the BFD session status must be synchronized to the interface status immediately, ensure that the BFD configurations on the two routers are correct, and then run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands to shut down and start the BFD session. When the [**undo shutdown**](cmdqueryname=undo+shutdown) command is run, a detection timer is initiated. If the BFD session goes up through negotiation before the timer expires, the BFD session notifies the bound interface of a BFD up event. Otherwise, the BFD session considers the link faulty and notifies the bound interface of a BFD down event. This way, the BFD session status is synchronized with the interface status in real time.
   * After the [**shutdown**](cmdqueryname=shutdown) command is run, the BFD session status will not be reported to the bound interface.
   * If the [**process-interface-status**](cmdqueryname=process-interface-status) [ **sub-if** ] command configured for a BFD session exists in the configuration file, after the device is restarted, the BFD session reports a BFD down event to the interface so that the interface sets its protocol state to down. This prevents traffic loss when the BFD session is up but the interface is down during initialization of the device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configuration

Run the following commands to check the configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) command to check information about BFD sessions.

After completing the configurations, run the [**display bfd session**](cmdqueryname=display+bfd+session) command. The command output shows that **Proc Interface Status** is **Enable**.