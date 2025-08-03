Overview of BGP Flow Specification
==================================

The device configured with BGP Flow Specification sent
a BGP Flow Specification route carrying a filtering rule to BGP Flow
Specification peers so that the traffic that consumes a lot of network
resources or aims to attack servers can be filtered or controlled
on the peers.

#### Definition

BGP flow specification is used to guard against denial of service (DoS) and distributed denial of service (DDoS) attacks, improving network security and availability.


#### Purpose

DoS and DDoS attacks pose a grave threat to network security. A DoS/DDoS attacker can control thousands of devices through multiple control ends to launch traffic attacks on the same destination address, subnet, or server. Such attacks cause network congestion and may even cause a server to fail to provide services due to excessive CPU usage.

Traditionally, there are two techniques for preventing DoS/DDoS attacks: traffic classification and traffic redirection. However, these two techniques have their own defects, as shown in [Table 1](#EN-US_CONCEPT_0172372311__en-us_concept_0172357159_tab_dc_vrp_flow_spec_feature_000201).

**Table 1** Comparison between the two traditional techniques for preventing DoS or DDoS attacks
| Preventative Technique | Technique Description | Defects |
| --- | --- | --- |
| Traffic classification | Traffic filtering rules and quality of service (QoS) policies are manually configured to reduce the impact of DoS and DDoS attacks on the network. | The technique has the following defects:  * It fails to guarantee real-time attack defense. Coordination among network service providers is needed to identify attack sources. * Traffic filtering policies need to be manually modified, thereby complicating maintenance. |
| Traffic redirection | The next hop of the route destined for the attack target is modified based on a routing policy.  * The next hop of the route is set to a blackhole, and attack traffic is then discarded. * The next hop of the route is set to a traffic cleaning device which cleans the attack traffic to ensure normal service traffic. | The technique has the following defects:  * The traffic filtering rule is simplistic. Only destination addresses can be used as a basis for traffic filtering. * Traffic filtering information and routing information are transmitted together, which complicates maintenance. |


BGP Flow Specification helps correct the preceding defects:

* It uses BGP Network Layer Reachability Information (NLRI) defined in standard protocols to transmit traffic filtering information. This allows traffic filtering information and routing information to be separately transmitted, improving maintainability.
* It provides various filtering conditions and actions to control traffic.

BGP Flow Specification supports BGP public network Flow Specification, BGP VPN Flow Specification, BGP VPNv4 Flow Specification, and BGP VPNv6 Flow Specification. [Table 2](#EN-US_CONCEPT_0172372311__en-us_concept_0172357159_tab_dc_vrp_flow_spec_feature_000202) lists their differences.

**Table 2** Comparison between BGP public network Flow Specification, BGP VPN Flow Specification, BGP VPNv4 Flow Specification, and BGP VPNv6 Flow Specification
| BGP Flow Specification Classification | Usage Scenario | Address Family |
| --- | --- | --- |
| BGP public network Flow Specification | Applies to public-network scenarios. | BGP-Flow address family and BGP-Flow IPv6 address family |
| BGP VPN Flow Specification | Applies to VPN scenarios where BGP Flow Specification routes cannot be transmitted over the public network between VPNs. | BGP-Flow VPN instance IPv4 address family and BGP-Flow VPN instance IPv6 address family |
| BGP VPNv4 Flow Specification | Applies to VPN scenarios where BGP Flow Specification routes are transmitted over the public network between VPNs. | BGP-Flow VPN instance IPv4 address family and BGP-Flow VPNv4 address family |
| BGP VPNv6 Flow Specification | Applies to VPN scenarios where BGP Flow Specification routes are transmitted over the public network between VPNs. | BGP-Flow VPN instance IPv6 address family and BGP-Flow VPNv6 address family |




#### Benefits

BGP flow specification can improve the reliability and security of user networks. Details are as follows:

* Real-time monitoring: BGP flow specification rapidly responds to attack traffic through scheduled sampling, keeping attack traffic under control.
* Preemptive defense: Defense policies are configured manually in advance based on the characteristics of common attack traffic to prevent common attack traffic from damaging user networks.
* Reduced costs: You do not need to create a traffic control policy on each device, improving maintainability.
* Minimized attack scope: BGP flow specification routes can be transmitted across domains so that attack traffic can be filtered out of the device nearest to the attack source. This significantly reduces the impact of attack traffic on networks.