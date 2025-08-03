Configuring an Inter-AS E2E SR-MPLS TE Tunnel (Explicit Path Used)
==================================================================

An inter-AS E2E SR-MPLS TE tunnel can connect SR-MPLS TE tunnels in multiple AS domains to build a large-scale TE network.

#### Usage Scenario

SR-MPLS TE, a new MPLS TE tunneling technology, has unique advantages in label distribution, protocol simplification, large-scale expansion, and fast path adjustment. SR-MPLS TE can better cooperate with SDN.

The SR that is extended through an IGP can implement SR-MPLS TE only within an AS domain. To implement inter-AS E2E SR-MPLS TE tunnels, BGP EPE needs to be used to allocate peer SIDs to the adjacencies and nodes between AS domains. The controller uses the explicit paths to orchestrate IGP SIDs and BGP peer SIDs to implement inter-AS optimal path forwarding on the network shown in [Figure 1](#EN-US_TASK_0172368819__fig-dc_vrp_sr_all_cfg_004101).

In addition, the label depth supported by an ordinary forwarder is limited, whereas the depth of the label stack of an inter-AS SR-MPLS TE tunnel may exceed the maximum depth supported by a forwarder. To reduce the number of label stack layers encapsulated by the forwarder, use binding SIDs. When configuring an intra-AS SR-MPLS TE tunnel, set a binding SID for the tunnel. The binding SID identifies an SR-MPLS TE tunnel and replaces the label stack of an SR-MPLS TE tunnel.

**Figure 1** Inter-AS E2E SR-MPLS TE tunnel networking  
![](images/fig-dc_vrp_sr_all_cfg_004101.png "Click to enlarge")

#### Pre-configuration Tasks

Before configuring an inter-AS E2E SR-MPLS TE tunnel, complete the following tasks:

* Configure an intra-AS SR-MPLS TE tunnel.
* Configure BGP EPE between ASBRs. For details, see [Configuring BGP SR](dc_vrp_sr_all_cfg_0033.html).


[Setting a Binding SID](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0042.html)

Using binding SIDs reduces the number of labels in a label stack on an NE, which helps build a large-scale network.

[Configuring an SR-MPLS TE Explicit Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0043.html)

An explicit path over which an SR-MPLS TE tunnel is to be established is configured on the ingress. You can specify node or link labels for the explicit path.

[Configuring an E2E SR-MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0044.html)

A tunnel interface must be configured on an ingress so that the interface is used to establish and manage an E2E SR-MPLS TE tunnel.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0045.html)

After configuring an inter-AS E2E SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.