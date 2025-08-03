Understanding Dynamic BGP Peer Groups
=====================================

A peer group is a set of peers with the same policies. When a peer is added to a peer group, it inherits the configurations of the peer group. If the configurations of the peer group change, the configurations of all the peers in the group change accordingly. A large number of BGP peers may exist on a large-scale BGP network, many of which need the same policies, and you can configure a static peer group to simplify configuration.

However, multiple BGP peers can change frequently on some BGP networks, causing the establishment of BGP peer relationships to change accordingly. If you configure peers in static mode, you must frequently add or delete peer configurations on the local device, increasing the maintenance workload. To address this problem, configure the dynamic BGP peer function to enable a BGP device to listen for BGP connection requests from a specified network segment, dynamically establish BGP peer relationships, and add these peers to the same dynamic peer group. As a result, manually adding or deleting BGP peer configurations in response to each dynamic peer change is no longer required.

#### Application Scenarios

As shown in [Figure 1](#EN-US_CONCEPT_0000001176663703__fig_dc_vrp_bgp_feature_001701), DeviceA establishes EBGP peer relationships with DeviceB and DeviceC, and establishes IBGP peer relationships with DeviceD and DeviceE.

**Figure 1** Network diagram of a dynamic BGP peer group  
![](figure/en-us_image_0000001130784014.png)

As DeviceB and DeviceC are on the same network segment, you can configure a dynamic BGP peer group on DeviceA to listen for the network segment 10.1.0.0/16. As a result, DeviceB and DeviceC are added to the dynamic BGP peer group. If other devices on the same network segment request the establishment of a BGP peer relationship with DeviceA, they will be added to the dynamic BGP peer group, reducing the network maintenance workload. The configuration on DeviceD is similar to the configuration on DeviceE.