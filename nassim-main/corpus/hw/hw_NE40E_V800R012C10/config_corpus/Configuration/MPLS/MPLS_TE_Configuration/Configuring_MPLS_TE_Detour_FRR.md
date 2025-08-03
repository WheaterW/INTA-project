Configuring MPLS TE Detour FRR
==============================

MPLS TE detour FRR automatically creates a different backup LSP for the primary LSP on each eligible node to protect downstream links or nodes.

#### Context

TE FRR provides local link or node protection for TE tunnels. TE FRR works in either facility backup or one-to-one backup mode. [Table 1](#EN-US_TASK_0000001935677173__table_0000031705) compares the two modes.

**Table 1** Comparison between facility backup and one-to-one backup
| Mode | Advantage | Disadvantage |
| --- | --- | --- |
| Facility backup | Is extensible, resource efficient, and easy to implement. | Bypass tunnels must be manually planned and configured, which is time-consuming and laborious on a complex network. |
| One-to-one backup | Is easy to configure, eliminates manual network planning, and provides flexibility on a complex network. | Each node has to maintain the status of detour LSPs, which consumes additional bandwidth resources. |

TE FRR in one-to-one backup mode is also called MPLS detour FRR. Each eligible node automatically creates a detour LSP.

This section describes how to configure MPLS detour FRR. For information about how to configure TE FRR in facility backup mode, see [Configuring MPLS TE Manual FRR](dc_vrp_te-p2p_cfg_0048.html) and [Configuring MPLS TE Auto FRR](dc_vrp_te-p2p_cfg_0053.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The facility backup and one-to-one backup modes are mutually exclusive on the same TE tunnel interface. If both modes are configured, the latest configured mode overrides the previous one.
* After MPLS detour FRR is configured, nodes on a TE tunnel are automatically enabled to record routes and labels. Before you disable the route and label record functions, disable MPLS detour FRR.


#### Pre-configuration Tasks

Before configuring MPLS detour FRR, complete the following task:

[Configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

CSPF must be enabled on each node along both the primary and backup RSVP-TE tunnel paths.



[Enabling TE Detour FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0312.html)

TE detour FRR must be enabled on the ingress of a primary tunnel before TE Auto FRR is configured.

[(Optional) Disabling MPLS Detour FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0212b.html)

If MPLS detour FRR is disabled on a transit node or egress node, the ingress node excludes the node when calculating a detour LSP and does not occupy forwarding resources of the node.