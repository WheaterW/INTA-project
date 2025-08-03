Configuring BGP VPWS FRR
========================

BGP VPWS FRR allows VPWS traffic to switch to the secondary PW when the primary PW fails.

#### Usage Scenario

VPN FRR is a technique that allows a device to fast switch VPN routes by presetting and using master and backup forwarding entries on the remote PE (which correspond to the master and backup PEs, respectively), in conjunction with fast detection of PE failures. VPN FRR prevents the issue where E2E service convergence caused by a PE failure lasts more than 1 second and the issue where the service restoration time for a faulty PE relies on the number of VPN routes in the routing table of the PE on an MPLS VPN where a CE is dual-homed to PEs. After VPN FRR is configured on PEs, E2E service convergence takes less than 1 second in the event of a PE failure.

VPN FRR provides fast service convergence after a node on a tunnel fails, irrespective of the number of VPN routes in the routing table of the node. In addition, VPN FRR is simple, reliable, and easy to deploy. Except for fast detection of PE failures, VPN FRR does not require assistance of adjacent devices.

VPWS FRR is a type of VPN FRR. VPWS FRR allows VPWS traffic to switch to the secondary PW when the primary PW fails.

Typical BGP VPWS FRR scenarios include:

* Symmetric access of CEs to PEs: The CEs at the two ends of a VC communicate over two paths, one as the primary path and the other the backup path.
* Asymmetric access of CEs to PEs: The CE on one end of the VC connects to a PE over a high-reliability link, and the CE on the other end is dual-homed to PEs over two lower-reliability links. The two CEs communicate over two paths. The high-reliability path serves as the primary path, and the low-reliability path serves as the secondary path.


#### Pre-configuration Tasks

Before configuring VPWS FRR, complete the following tasks:

* Configure static routes or an IGP on the PEs and Ps of the MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on the PEs and Ps of the MPLS backbone network.
* Establish LDP/BGP sessions among PEs. (If the PEs are indirectly connected, set up remote LDP sessions between them.)
* Establish tunnels between PEs based on tunnel policies.


[Configuring Primary and Secondary PWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6066.html)

Configuring the primary and secondary PWs is essential to configuring VPWS FRR.

[(Optional) Configuring BFD for PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6067.html)

BFD for PW helps quickly detect faults on public network links.

[(Optional) Configuring Fast Fault Notification](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6068.html)

OAM mapping and physical-layer fault notification can accelerate AC fault detection and notification.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6069.html)