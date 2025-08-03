(Optional) Configuring the Revertive Switchover
===============================================

The revertive switching policies can be classified into three modes: immediate revertive mode, delayed revertive mode, and non-revertive mode.

#### Context

When primary and secondary PWs are configured, if the primary PW fails, traffic is switched to the secondary PW to prevent traffic interruption. If the primary PW recovers, traffic is switched back to the primary PW after a period of time. To flexibly adjust the switching time, configure a revertive switching policy.

When CEs are connected to PEs asymmetrically, do as follows on the PE (where traffic is switched) to which a CE is connected through a single link:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
3. Run [**mpls l2vpn reroute**](cmdqueryname=mpls+l2vpn+reroute) { { **delay** *delayTime* | **immediately** } [ **resume** *resumeTime* ] | **never** }
   
   
   
   The revertive switchover policy is configured.
   
   The types of the revertive switchover on PEs are as follows:
   
   * Immediate revertive switchover: The local PE immediately switches traffic to the primary PW and notifies the fault to the remote PE of the secondary PW. The PE notifies the rectification of the fault to the remote PE of the secondary PW after the period of *resumeTime*.
   * Delayed revertive switchover: The PE switches traffic to the primary PW after the period of *delayTime*.
   * None revertive switchover: The PE does not switch traffic to the primary PW until the secondary PW is faulty.
   
   For an asymmetric networking, in which ACs are of the Ethernet type, note the following:
   
   * If the remote shutdown function is configured on the interface of a PE that connects a CE, you are recommended not to use the policy of immediate revertive switchover, which may lead to network flapping and traffic loss. On the other hand, you can use the policy of delayed revertive switchover to set *delayTime* equal to or more than 30 seconds.
   * If the Ethernet OAM function is configured on the interface of a PE that connects a CE, and a revertive switchover policy is also configured, you cannot set *resumeTime* to be 0 seconds, but be equal to or longer than one second.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**manual-set pw-ac-fault**](cmdqueryname=manual-set+pw-ac-fault) command to simulate a PW fault to check whether a primary/secondary PW switchover is performed or not. The result is saved in the log file.

Run the [**manual-set pw-ac-fault**](cmdqueryname=manual-set+pw-ac-fault) command on the AC interface of the primary PW, the following situations occur:

* The status of the primary PW is **Down**.
* **VC** **status** of the primary PW is **InActive**, and that of the secondary PW is **Active.**
* L2VPN data is switched to the secondary PW.

Run the [**undo manual-set pw-ac-fault**](cmdqueryname=undo+manual-set+pw-ac-fault) command on the AC interface of the primary PW to rectify the fault on the PW, the following situations occur:

* The status of the primary PW is **up**.
* **VC** **status** of the primary PW is **Active**, and **VC** **status** of the secondary PW is **InActive.**
* L2VPN data is switched to the primary PW.