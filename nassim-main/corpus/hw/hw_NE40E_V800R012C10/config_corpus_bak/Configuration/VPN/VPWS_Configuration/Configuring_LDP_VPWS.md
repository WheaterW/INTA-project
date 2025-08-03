Configuring LDP VPWS
====================

Configuring_LDP_VPWS

#### Usage Scenario

Carriers have constructed various types of backbone networks using different technologies. For example, they have constructed backbone public switched telephone networks (PSTNs) to carry voice services, FR backbone networks to carry FR data, and ATM backbone networks to transmit ATM data. As IP services develop rapidly, carriers have established IP backbone networks to meet this trend. In addition to backbone networks, diverse access networks are also constructed. As a result, poor interoperability exists between different types of networks. It is an urgent task for carriers to find a way to effectively integrate these networks, enhance network utilization, and provide more types of services for users.

By converging previous access modes with the current IP backbone network, VPWS prevents repetitious network construction and saves operational costs. With the VPWS technology, an IP backbone network can connect to various access networks, upgrading and enhancing the entire network. After an MPLS IP backbone network is constructed, the traditional datacom networks such as ATM and FR networks can be used as access networks. ATM and FR users are unaware of such network changes. With the VPWS technology, access networks of different protocols can interwork with each other. For example, ATM users and FR users can communicate with each other.

**Figure 1** Typical VPWS application  
![](images/fig_dc_vrp_vpws_cfg_300401.png)

[Figure 1](#EN-US_TASK_0172369791__fig_dc_vrp_vpws_cfg_300401) shows typical VPWS networking. The backbone network is an IP network accessed by LANs in different modes.

Assume that a carrier has established a nationwide backbone network to provide VPWS services. A customer has two branches: one in city A and one in city B. The branch in city A accesses the carrier's backbone network over an ATM network, and the branch in city B accesses the carrier's backbone network over an FR network. The carrier can set up a VPWS connection between access sites PE1 in city A and PE2 in city B.

In this manner, the carrier can provide point-to-point private network services over a WAN without taking special measures to address different access modes. In this solution, the customer does not need to modify the original enterprise network plan; the carrier can implement smooth migration to the IP backbone network without modifying existing access modes.


#### Pre-configuration Tasks

Before configuring LDP VPWS, complete the following tasks:

* Configure static routes or an IGP on PEs and Ps of the MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on PEs and Ps of the MPLS backbone network.
* Set up LDP sessions among PEs (if the PEs are indirectly connected, set up remote LDP sessions between them).
* Establish tunnels between PEs based on the tunnel policy (if no tunnel policy is configured, LDP tunnels are used by default).


[(Optional) Configuring Flow Label-based Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6014.html)

Flow label-based load balancing enables L2VPN data flows on a PW to be load-balanced over tunnels between P devices based on flow labels, improving forwarding efficiency.

[(Optional) Configuring an AC Interface to Transparently Transmit TDM Frames/ATM Cells](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6006.html)

A PW can be configured on an AC interface only after the AC interface has been configured to transparently transmit TDM frames/ATM cells.

[(Optional) Configuring a PW Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_3005.html)

A PW template is a collection of common PW attributes. Configuring PWs using a PW template helps save configuration workload.

[Configuring a VPWS PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_3006.html)

This section describes how to establish a P2P VPWS PW between two PEs for communication.

[Configuring VPWS Heterogeneous Interworking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_3007.html)

If AC types at the two ends of a VPWS PW are different, configure VPWS heterogeneous interworking for the two CEs to communicate.

[(Optional) Configuring a Secondary VPWS Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5002.html)

This section describes how to configure a secondary VPWS connection for VLL FRR, so that L2VPN traffic can be quickly switched to the backup path if the primary path fails. After the primary path recovers, the L2VPN traffic can be switched back to it according to the corresponding revertive switching policy.

[(Optional) Configuring the Revertive Switchover](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_5003.html)

The revertive switching policies can be classified into three modes: immediate revertive mode, delayed revertive mode, and non-revertive mode.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_3008.html)