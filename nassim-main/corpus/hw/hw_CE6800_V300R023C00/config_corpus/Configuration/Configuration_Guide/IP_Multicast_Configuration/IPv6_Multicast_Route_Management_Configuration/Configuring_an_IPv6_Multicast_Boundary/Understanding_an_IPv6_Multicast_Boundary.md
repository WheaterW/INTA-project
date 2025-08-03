Understanding an IPv6 Multicast Boundary
========================================

Understanding an IPv6 Multicast Boundary

#### Definition

A multicast boundary allows multicast information of each multicast group to be transmitted within a specified scope. After a multicast boundary is configured for a multicast group on an interface, a closed multicast forwarding area is formed, and the interface can no longer send or accept packets of the multicast group.


#### Application Scenarios

In [Figure 1](#EN-US_CONCEPT_0000001533400590__fig_dc_vrp_multicast_feature_204001), DeviceA, DeviceB, and DeviceC form multicast domain 1. DeviceD, DeviceE, and DeviceF form multicast domain 2. The two multicast domains communicate through DeviceB and DeviceD.

**Figure 1** Network diagram of configuring an IPv6 multicast boundary  
![](figure/en-us_image_0000001551264352.png)

To isolate data of multicast group G in the two multicast domains, you only need to configure multicast group G as the multicast forwarding boundary on either interface 1 or interface 2. After that, the interface no longer forwards or accepts packets of multicast group G.