Overview of Microsegmentation
=============================

Overview of Microsegmentation

#### Definition

Microsegmentation, also called EPG-based security isolation, groups servers on a network based on rules. It applies traffic control policies based on EPGs to simplify O&M and implement security management and control.


#### Purpose

Enterprises face increasing security risks as stored data, applications, and internal traffic increase on networks. Using traditional network methods such as subnet assignment and ACLs to isolate services brings the following problems:

* Virtual Local Area Network (VLAN) IDs or VXLAN network identifiers (VNIs) can be used to divide subnets for service isolation (for example, isolating services in subnets A and B), but services on servers in the same subnet cannot be isolated. When different subnets share a gateway, servers in these subnets cannot be isolated because the gateway has a route to each subnet.
* ACLs can be configured to isolate servers. However, networks contain many servers, and many ACL rules need to be deployed to isolate servers. This makes configuration and maintenance complex. In addition, ACL resources of network devices are limited and cannot meet customer requirements.

Microsegmentation addresses the preceding problems. On a VXLAN network, microsegmentation provides grouping rules (for example, IP address or IP address range) with finer granularity than subnets, and features simple deployment. Service isolation between servers can be implemented by grouping servers on the VXLAN network into EPGs and deploying traffic control policies based on the EPGs.


#### Benefits

Microsegmentation implements service isolation between different servers of a VXLAN network and ensures secure management and control for the VXLAN network. In addition, the configuration and maintenance of microsegmentation are simple, significantly reducing the configuration and maintenance costs.