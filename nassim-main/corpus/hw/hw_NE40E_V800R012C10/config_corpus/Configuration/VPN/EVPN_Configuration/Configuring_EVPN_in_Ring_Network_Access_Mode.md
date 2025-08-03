Configuring EVPN in Ring Network Access Mode
============================================

If EVPN VPLS over MPLS or EVPN VPLS over SRv6 in ring network access mode needs to be deployed on a network, you need to configure EVPN in this mode and deploy a loop avoidance protocol to prevent loops.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001118104814__fig142211553144816), EVPN VPLS over MPLS or EVPN VPLS over SRv6 needs to be deployed between PEs, and a loop avoidance protocol (MSTP in this example) needs to be deployed on the ring network formed by PE1, PE2, CE1, and CE2. Currently, STP, ERPS, and MSTP can be deployed.

**Figure 1** EVPN in ring network access mode  
![](figure/en-us_image_0000001118724120.png)

#### Pre-configuration Tasks

Before configuring EVPN VPLS in ring network access mode, complete the following tasks:

* Configure [EVPN VPLS over SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html), [EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html), or EVPN VPLS over MPLS on PEs.
* Configure [EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html) on PEs.
* Configure [basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html) on PEs and CEs.
* Configure a loop avoidance protocol on PEs and CEs. For details, see [MSTP Configuration](dc_vrp_mstp_cfg_0001.html), [STP/RSTP Configuration](dc_vrp_stp_cfg_0000.html), and and [ERPS (G.8032) Configuration](dc_vrp_erps_cfg_0000.html).


[Configuring Ring Network Topology Isolation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0170.html)

In scenarios where multiple ring networks that belong to the same BD but different VLANs connect to an EVPN, you can configure ring network topology isolation on AC sub-interfaces. This configuration isolates the topologies of these ring networks and reduces the number of Layer 2 protocol packets transparently transmitted between the networks. In this way, the sub-interfaces transparently transmit Layer 2 protocol packets only after the packets pass the VLAN check on these sub-interfaces.

[Configuring Ring Network Access](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0171.html)

If MSTP is deployed on a ring network, run the [**evpn stp-ring-id**](cmdqueryname=evpn+stp-ring-id) command on dual-homing PEs to configure the same ring ID for them. The dual-homing PEs are then identified by the same ring ID.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0172.html)

After EVPN in ring network access mode is configured, you can check the spanning tree status of ports in the MSTP process on ring network devices and check EVPN route information on PEs.