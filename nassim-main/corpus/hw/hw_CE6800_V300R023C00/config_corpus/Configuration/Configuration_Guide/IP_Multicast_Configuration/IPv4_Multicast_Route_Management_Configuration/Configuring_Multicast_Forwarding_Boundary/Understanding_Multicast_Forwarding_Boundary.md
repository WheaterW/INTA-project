Understanding Multicast Forwarding Boundary
===========================================

Understanding Multicast Forwarding Boundary

#### Definition

Multicast boundary allows multicast information of each multicast group to be transmitted within a specified scope. After multicast boundary is configured for a multicast group on an interface, a closed multicast forwarding area is formed, and the interface can no longer send or receive packets of the multicast group.


#### Application Scenarios

In [Figure 1](#EN-US_CONCEPT_0000001176742439__fig_dc_vrp_multicast_feature_204001), DeviceA, DeviceB, and DeviceC form multicast domain 1. DeviceD, DeviceE, and DeviceF form multicast domain 2. The two multicast domains communicate through DeviceB and DeviceD.

**Figure 1** Network diagram of configuring multicast boundary  
![](figure/en-us_image_0000001176742469.png)

To isolate data of multicast group G in the two multicast domains, you only need to configure multicast group G as the multicast forwarding boundary on either interface1 or interface2. After that, the interface no longer forwards or receives packets of multicast group G.