Understanding the Association Between Direct Routes and a VRRP Group
====================================================================

Understanding the Association Between Direct Routes and a VRRP Group

#### Context

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662319__fig157721130503), DeviceA and DeviceB form a Virtual Router Redundancy Protocol (VRRP) group and function as user gateways. DeviceA is the master device in the VRRP group, and DeviceB is the backup device. User-to-network traffic travels through DeviceA. However, network-to-user traffic may travel through DeviceA, DeviceB, or both of them over a path determined by a dynamic routing protocol. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662319__fig157721130503) (a), network-to-user traffic is load-balanced. In this case, the user-to-network and network-to-user traffic paths may be different, which causes services to be interrupted because firewalls configured on VRRP devices in the VRRP group block such service. In addition, the path inconsistency complicates traffic monitoring and statistics collection, increasing costs.

To address the preceding problem, a dynamic routing protocol is expected to select a path passing through the master device for both the user-to-network and network-to-user traffic, ensuring path consistency. Association between direct routes and a VRRP group can be configured so that the VRRP group status affects route selection of the dynamic routing protocol on the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662319__fig157721130503) (b). User-to-network traffic and network-to-user traffic are transmitted along the same path.

**Figure 1** VRRP networking diagram  
![](figure/en-us_image_0000001261359664.png "Click to enlarge")

#### Related Concepts

VRRP is a widely used fault-tolerant protocol that groups multiple routing devices into a backup group, improving network reliability. A VRRP group consists of a master device and one or more backup devices. If the master device fails, the VRRP group switches services to a backup device to ensure communication continuity and reliability.

A device in a VRRP group operates in one of three states:

* Master: If a network is working properly, the master device transmits all services.
* Backup: If the master device fails, the VRRP group selects a backup device as a new master device to take over traffic, ensuring service continuity.
* Initialize: After receiving a message indicating that the interface goes up, a device changes from the Initialize state to the Master or Backup state.

#### Implementation

The association between direct routes and the VRRP group enables the adjustment of the costs of direct network segment routes based on the VRRP status and helps a dynamic routing protocol to import the direct routes. The dynamic routing protocol selects the direct route with the lowest cost. For example, on the network shown in [Figure 1](#EN-US_CONCEPT_0000001176662319__fig157721130503), an association between direct routes and the VRRP group is configured on VRRP interfaces on DeviceA and DeviceB. The implementation is as follows:

* DeviceA in the Master state sets the cost of its route destined for the directly connected virtual IP network segment to 0 (default value).
* DeviceB in the Backup state increases the cost of its direct route destined for the network segment to which the VRRP virtual IP address belongs.

A dynamic routing protocol selects the route with DeviceA as a next hop because this route has a smaller cost value than the other one with DeviceB as a next hop. In this way, the user-to-network and network-to-user traffic paths keep consistent.


#### Application Scenario

When a data center is used, firewalls are configured on devices in a VRRP group to improve network security. Network-to-user traffic cannot pass through a firewall if traffic travels over a path different than the one used by user-to-network traffic.

On an IP radio access network (RAN), VRRP is configured to determine the master/backup status of aggregation site gateways (ASGs) and radio service gateways (RSGs) that are working in redundancy mode. Network-to-user and user-to-network traffic may pass through different paths, complicating network O&M and management.

The association between direct routes and a VRRP group can address the preceding problem by ensuring that the user-to-network traffic and network-to-user traffic travel along the same path.