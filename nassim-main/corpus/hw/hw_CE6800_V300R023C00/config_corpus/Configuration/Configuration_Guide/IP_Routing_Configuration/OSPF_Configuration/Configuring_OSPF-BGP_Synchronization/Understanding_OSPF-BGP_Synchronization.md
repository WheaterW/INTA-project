Understanding OSPF-BGP Synchronization
======================================

Understanding OSPF-BGP Synchronization

#### Purpose

New device deployment or a device restart may lead to network traffic loss during BGP convergence. This is due to IGP convergence being faster than BGP convergence. OSPF-BGP synchronization can address this issue.


#### Fundamentals

If a backup link exists, BGP traffic may be lost during traffic switchback, as BGP routes converge more slowly than OSPF routes.

In [Figure 1](#EN-US_CONCEPT_0000001130783208__fig_dc_vrp_ospf_feature_001001), DeviceA, DeviceB, DeviceC, and DeviceD run OSPF and establish IBGP connections. DeviceC functions as a backup of DeviceB. When the network is stable, BGP and OSPF routes fully converge on the devices.

In normal cases, traffic from DeviceA to 10.3.1.0/30 passes through DeviceB. If DeviceB fails, traffic is switched to DeviceC. After DeviceB recovers, traffic is switched back to DeviceB, during which traffic loss occurs.

This is due to OSPF route convergence being complete, while BGP route convergence (which is slower than IGP route convergence) continues during the traffic switchback. As a result, DeviceB does not have the route to 10.3.1.0/30.

When traffic from DeviceA to 10.3.1.0/30 is forwarded to DeviceB, DeviceB discards the traffic because it does not have the route to 10.3.1.0/30.

**Figure 1** Networking for OSPF-BGP synchronization  
![](figure/en-us_image_0000001130783282.png)

If OSPF-BGP synchronization is configured on a device, the device remains as a stub device during the set synchronization period. During this period, the link metric in the LSAs advertised by the device is the maximum value (65535), which instructs other OSPF devices not to use it as a transit device for data forwarding.

In [Figure 1](#EN-US_CONCEPT_0000001130783208__fig_dc_vrp_ospf_feature_001001), OSPF-BGP synchronization is enabled on DeviceB. In this situation, before BGP route convergence is complete, DeviceA continues to forward data through DeviceC rather than DeviceB until BGP route convergence on the latter is complete.