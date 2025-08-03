Overview of VLANs
=================

Overview of VLANs

#### Definition

Virtual Local Area Network (VLAN) technology logically divides a physical LAN into multiple broadcast domains, each of which is called a VLAN.


#### Purpose

VLAN was originally introduced to address the problems of conflicts, broadcast storms, data security risks that occurred on early Ethernet, which was itself originally intended for small and simple networks using bus technology and carrier-sense multiple access/collision detection (CSMA/CD). These problems have become even more prominent as Ethernet has expanded to larger and more complex networks, with LANs carrying such diversified data as graphics, voice, and video:

* Conflicts: Multiple hosts on the network send frames at the same time, causing a conflict. Additional hosts lead to increased conflicts.
* Broadcast storms: Frames sent by any host on the network are sent to all other hosts, causing broadcast storms. More hosts lead to more severe broadcast storms.
* Data security risks: As all hosts on the network share a single data transmission channel, data security cannot be ensured. Increasingly complex data leads to greater security risks.

Using Layer 2 devices for fast Layer 2 switching can restrict data transmission within a LAN. However, this resolves only the conflicts.

To reduce broadcast traffic, you can configure different network segments to isolate devices, but the drawbacks of this solution include high costs. As such, VLAN technology was introduced.

VLAN technology allows a physical LAN to be divided into multiple logical LANs (multiple VLANs). Each VLAN functions as a separate broadcast domain, with devices in the same VLAN able to directly communicate with one another, while those in different VLANs cannot. As a result, broadcast packets are confined within a single VLAN, thereby strengthening network security.


#### Benefits

VLAN technology offers the following benefits:

* Confines each broadcast domain to a single VLAN, conserving bandwidth and improving network processing capabilities.
* Enhances LAN security. Frames in different VLANs are separately transmitted, so that hosts in a VLAN cannot directly communicate with those in another VLAN.
* Improves network robustness. A fault in one VLAN does not affect hosts in another VLAN.
* Allows for flexible virtual groups. VLAN technology allows hosts to be divided into different groups, and hosts in different geographical locations can be grouped together, simplifying network construction and maintenance.