Configuring LDP-IGP Synchronization
===================================

LDP-IGP synchronization helps minimize traffic interruptions when the traffic is switched from the backup link to the primary link and implement millisecond-level switchovers.

#### Usage Scenario

You can configure LDP-IGP synchronization to prevent traffic loss after the primary LSP fails on the network where primary and backup links exist. The details are as follows:

* When the primary link is restored and an LDP session or an LDP adjacency between nodes along the primary link fails, LSP traffic is discarded because LSP traffic is switched from the primary link to the backup link, whereas IGP traffic is still transmitted through the primary link.
* When the primary link is restored and an LDP session between nodes along the primary link fails, LSP traffic is discarded because LSP traffic is switched from the primary link to the backup link, whereas IGP traffic is still transmitted through the primary link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Both OSPF and IS-IS support LDP-IGP synchronization.



#### Pre-configuration Tasks

Before configuring LDP-IGP synchronization, complete the following tasks:

* Configure basic IGP (OSPF or IS-IS) functions.
* Enable MPLS.
* Enable MPLS LDP globally and on each interface.


[Enabling LDP-IGP Synchronization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2004.html)

LDP-IGP synchronization needs to be enabled on interfaces on both ends of the link between the node where a primary LSP and a backup LSP diverge from each other and its LDP peer on the primary LSP. LDP-IGP synchronization can be enabled either on an interface or in an IGP process.

[(Optional) Blocking LDP-IGP Synchronization on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2005.html)

If you do not want to run LDP-IGP synchronization on some interfaces, you can block the function on these interfaces.

[(Optional) Setting a Value for the Hold-down Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0078.html)

This section describes how to set a value for the Hold-down timer. Before the timer expires, an interface waits for the establishment of an LDP session and an LDP adjacency without setting up an IGP neighbor relationship.

[(Optional) Setting a Value for the Hold-max-cost Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2006.html)

If the LDP session or LDP adjacency on the primary link fails, LSP traffic is switched to the backup link within the specified hold-max-cost period before the reestablishment of the LDP session and LDP adjacency on the primary link.

[(Optional) Setting the Delay Timer Value](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2009.html)

When a faulty link recovers and an LDP session is reestablished on the link, LDP starts the Delay timer to wait for the establishment of an LSP. After the Delay timer expires, LDP notifies the IGP that the synchronization process is complete.

[(Optional) Configuring Graceful Deletion for LDP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0053.html)

LDP graceful deletion can be configured to speed up traffic switching using LDP-IGP synchronization, improving network reliability.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2007.html)

After configuring LDP-IGP synchronization, you can check the synchronization states of interfaces on which LDP-IGP synchronization has been enabled.