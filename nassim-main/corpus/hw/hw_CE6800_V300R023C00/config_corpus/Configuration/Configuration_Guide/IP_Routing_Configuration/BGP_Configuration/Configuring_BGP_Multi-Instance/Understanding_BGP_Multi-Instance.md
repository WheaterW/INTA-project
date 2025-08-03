Understanding BGP Multi-Instance
================================

Understanding BGP Multi-Instance

#### Context

By default, all BGP routes are stored in the BGP base instance, meaning that it is impossible to implement separate route management and maintenance. BGP multi-instance can solve this problem. A device can run two types of BGP instances simultaneously: BGP base instance and BGP multi-instance. They are independent of each other and can have either the same or different AS numbers. You can deploy different address families for the BGP base instance and BGP multi-instance based on network deployment requirements to carry different routes and implement separate route management and maintenance.


#### Implementation

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130624110__fig_dc_vrp_bgp_feature_003301), to isolate private and public network services (by deploying public network services between DeviceA and DeviceB and private network services between DeviceB and DeviceC), configure BGP as follows:

* Configure BGP basic instance **bgp 100** on DeviceA.
* Configure BGP basic instance **bgp 100** and BGP multi-instance **bgp 200 instance a** on DeviceB.
* Configure BGP basic instance **bgp 200** on DeviceC.

Establish a public network BGP peer relationship in the BGP basic instance between DeviceA and DeviceB, and establish a BGP peer relationship in DeviceB's BGP multi-instance and DeviceC's BGP basic instance. Then, check route information on DeviceA, DeviceB, and DeviceC. If DeviceA has only the routes of DeviceB's BGP instance 100, DeviceB has all the routes, and DeviceC has only the routes of DeviceB's BGP instance 200, separate route management and maintenance have been achieved on DeviceB.
**Figure 1** Network diagram of BGP multi-instance for service isolation  
![](figure/en-us_image_0000001130783976.png)