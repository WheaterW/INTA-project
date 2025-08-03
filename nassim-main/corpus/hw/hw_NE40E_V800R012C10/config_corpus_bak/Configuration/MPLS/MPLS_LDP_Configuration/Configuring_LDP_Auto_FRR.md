Configuring LDP Auto FRR
========================

LDP Auto Fast Reroute (FRR) can be configured to rapidly trigger a service switchover if a fault occurs, which improves network reliability.

#### Usage Scenario

On an MPLS network with a backup link, if a link fault occurs, Interior Gateway Protocol (IGP) routes converge and routes related to the backup link become available. Traffic on an LDP LSP can be switched to a backup path only after IGP routes are converged successfully. Before the switchover is complete, traffic is interrupted. To prevent traffic interruptions, LDP FRR can be configured.

LDP FRR uses the liberal label retention mode, obtains a liberal label, and applies for a forwarding entry associated with the label. It then forwards the forwarding entry to the forwarding plane as a backup forwarding entry used by the primary LSP. On the network enabled with LDP FRR, the interface can detect a fault that occurs on itself, and a BFD session associated with the interface can also detect a failure in the interface or the primary LSP established on the interface. If a fault occurs, LDP FRR is notified of the failure and rapidly forwards traffic to a backup LSP, protecting traffic on the primary LSP. The traffic switchover is performed within 50 milliseconds, which minimizes the traffic interruption time.

LDP Auto FRR depends on IGP FRR. When IGP FRR is enabled, LDP Auto FRR will be automatically enabled, and a backup LSP will be established based on a specific policy.

LFA Auto FRR cannot be used to calculate alternate links on large-scale networks, especially on ring networks. To address this problem, enable Remote LFA Auto FRR.


#### Pre-configuration Tasks

Before configuring LDP Auto FRR, complete the following tasks:

* Assign an IP address to each interface to implement IP connectivity.
* Configure an IGP to advertise the route to each network segment of each interface and to advertise the host route to each LSR ID.
* [Configure an LDP LSP](dc_vrp_ldp-p2p_cfg_0015.html) to establish a primary LDP LSP.
* Configure IGP Auto FRR ([IS-IS
  Auto FRR](dc_vrp_isis_cfg_0091.html) or [OSPF IP FRR](dc_vrp_ospf_cfg_2009.html)).
* Before you configure remote LFA FRR, configure LDP LSPs to perform recursion hop by hop between the source node and PQ node. That is, [configure a local LDP session](dc_vrp_ldp-p2p_cfg_0003.html) between each pair of directly connected nodes along the link from the source node to PQ node.


[Enabling LDP Auto FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0050.html)

If LDP auto FRR is needed, configure it on the ingress or a transit node of a tunnel.

[(Optional) Configuring Graceful Deletion for LDP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0052.html)

LDP graceful deletion can be configured to speed up LDP FRR traffic switching.

[(Optional) Enabling the Coexistence of ECMP and FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0213.html)

The coexistence of ECMP and FRR can be enabled so that protection paths can be established for ECMP paths, preventing traffic loss stemming from an ECMP path disconnection.

[(Optional) Configuring the Function to Report Remote LDP Session Down Traps Generated Due to RLFA Route Deletion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_rlfa_trap.html)

In a remote LFA FRR scenario, enable the function to report remote LDP session down traps generated due to RLFA route deletion if the function is required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0051.html)

After configuring LDP Auto FRR, you can view information about the LDP Auto FRR LSP.