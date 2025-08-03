Understanding NQA for IPv4 Static Route
=======================================

Understanding NQA for IPv4 Static Route

#### Definition

Static routes do not have a dedicated detection mechanism. If a link fails, a network administrator must manually delete the corresponding static route from the IP routing table. This process delays link switchovers and can cause lengthy service interruptions.

BFD for IPv4 static route allows BFD sessions to monitor the link status of IPv4 static routes. However, BFD for IPv4 static route requires that both ends of a link support BFD. As a result, it cannot be implemented in some scenarios. NQA for IPv4 static route is applicable to networks where BFD for IPv4 static route cannot be deployed due to device limitations. NQA for IPv4 static route monitors the status of IPv4 static routes and rapidly implements a primary/backup link switchover, preventing lengthy service traffic interruptions.

[Table 1](#EN-US_CONCEPT_0000001130782750__table_01) compares BFD and NQA that monitor IPv4 static routes.

**Table 1** Comparison between BFD and NQA that monitor IPv4 static routes
| Item | BFD for IPv4 Static Route | NQA for IPv4 Static Route |
| --- | --- | --- |
| Detection method | Bidirectional session | Unidirectional detection |
| Requirements for communicating devices | Both ends of a BFD session must support BFD. | Only one end of an NQA test link supports NQA. |
| Detection speed | Millisecond-level | Second-level |



#### Related Concepts

NQA monitors network quality of service (QoS) in real time, and can be used to diagnose the fault if a network fails.

NQA relies on a test instance to monitor the link status. Two ends of an NQA test are called the NQA client and NQA server. The NQA client initiates an NQA test that can return any of the following results:

* Success: The test is successful. NQA instructs the routing management module to set a static route to active and add the static route to the routing table.
* Failed: The test fails. NQA instructs the routing management module to set the static route to inactive and delete the static route from the routing table.
* No result: The test is running and no result has been obtained. In this case, the status of the static route is unchanged.


#### Fundamentals

NQA for IPv4 static route associates an NQA test instance with an IPv4 static route and uses the NQA test instance to monitor the corresponding link status. The routing management module determines whether an IPv4 static route is active based on the test result of the NQA test instance. If the static route is inactive, the routing management module deletes it from the IP routing table and selects a backup link for data forwarding, which prevents lengthy service interruptions.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130782750__fig178699441714), 10 users are connected to the switch. Because dynamic routing protocols are not available for communication between DeviceB and users, IPv4 static routes are configured on DeviceB. To ensure network stability, perform the same configuration on DeviceC as the backup.

DeviceA, DeviceB, and DeviceC run a dynamic routing protocol and learn routes from one another. DeviceB and DeviceC are configured to import IPv4 static routes to the routing table of the dynamic routing protocol, and different costs are set for the routes. In this case, DeviceA can learn user routes from DeviceB and DeviceC through the dynamic routing protocol. DeviceA determines the primary and backup links based on link costs.

NQA for IPv4 static route, configured on DeviceB, uses an NQA test instance to monitor the status of the primary link. If the primary link fails, the corresponding IPv4 static route is deleted and downstream traffic switches to the backup link. When both the links are running properly, downstream traffic is preferentially transmitted along the primary link.

**Figure 1** Network diagram of NQA for IPv4 static route  
![](figure/en-us_image_0000001189654573.png)
![](public_sys-resources/note_3.0-en-us.png) 

Each IPv4 static route can be associated with only one NQA test instance.