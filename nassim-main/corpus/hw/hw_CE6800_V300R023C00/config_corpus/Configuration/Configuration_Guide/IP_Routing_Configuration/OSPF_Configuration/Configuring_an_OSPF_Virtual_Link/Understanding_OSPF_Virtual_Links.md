Understanding OSPF Virtual Links
================================

Understanding OSPF Virtual Links

#### Context

All non-backbone areas must be connected to the backbone area during OSPF deployment to ensure that all areas are reachable. However, in real-world applications, some areas may be unable to connect to the backbone area due to limitations.

For example, on the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662989__fig_feature_000422976901), area 2 is not connected to area 0 (backbone area), and DeviceB is not an ABR. Consequently, DeviceB does not generate routing information about network 1 in area 0, and DeviceC does not have a route to network 1.

**Figure 1** Non-backbone area not connected to the backbone area  
![](figure/en-us_image_0000001130783302.png)

In this case, you can configure an OSPF virtual link to resolve this issue.


#### Related Concepts

A virtual link refers to a logical channel established between two ABRs over a non-backbone area.

* A virtual link must be configured at both ends of the link.
* The area that provides a non-backbone area internal route for both ends of the virtual link is called transit area.

A virtual link is similar to a P2P connection established between two ABRs. As with physical interfaces, it is possible to configure interface parameters, such as the interval at which Hello packets are sent, at both ends of the virtual link.


#### Fundamentals

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001176662989__fig_feature_000422976902), two ABRs use a virtual link to directly transmit OSPF packets, while the OSPF device between them only forwards packets. Because the device is not the destination of the OSPF packets, it transparently transmits them as common IP packets.

**Figure 2** OSPF virtual link  
![](figure/en-us_image_0000001130783300.png)