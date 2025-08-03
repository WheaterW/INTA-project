Understanding BGP Auto FRR
==========================

As a protection measure against link failures, BGP Auto fast reroute (FRR) is applicable to networks with primary and backup links. With BGP Auto FRR, traffic can be switched between two BGP peers or two next hops within sub-seconds.

If a peer has multiple routes with the same prefix that are learned from different peers, it uses the optimal route as the primary link to forward packets and the sub-optimal route as a backup link. If the primary link fails, the peer rapidly notifies other peers that the BGP route has become unreachable and then switches traffic from the primary link to the backup link.

#### Application Scenarios

As shown in [Figure 1](#EN-US_CONCEPT_0000001130783942__fig_dc_vrp_bgp_feature_001701), DeviceD sends the learned BGP routes to DeviceB and DeviceC in AS 100. DeviceB and DeviceC then send the routes to DeviceA through an RR. DeviceA receives two routes with the next hops being the IP addresses of DeviceB and Device C, respectively. A route-policy is configured to preferentially select the routes received from one link. In this example, DeviceA preferentially selects the routes sent from DeviceB, and the backup link is link B.

**Figure 1** Network diagram of BGP Auto FRR  
![](figure/en-us_image_0000001130624238.png "Click to enlarge")

If a node along link A becomes faulty or if link A fails, the next hop of the route from DeviceA to DeviceB becomes unavailable. If BGP Auto FRR is enabled on DeviceA, the forwarding plane then quickly switches DeviceA-to-DeviceD traffic to link B, which ensures uninterrupted traffic forwarding. In addition, DeviceA re-selects the route sent by DeviceC based on the prefixes and then updates the FIB.