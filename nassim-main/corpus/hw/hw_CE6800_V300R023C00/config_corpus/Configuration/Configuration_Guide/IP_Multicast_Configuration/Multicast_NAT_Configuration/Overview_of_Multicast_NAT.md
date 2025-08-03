Overview of Multicast NAT
=========================

Overview of Multicast NAT

#### Definition

Multicast network address translation (NAT) translates the characteristics of multicast streams, such as the source IP address, destination IP address, source UDP port number, and destination UDP port number. Multicast NAT allows you to configure traffic policies on inbound interfaces to match input multicast streams. It also allows you to configure translation rules on outbound interfaces, so that a multicast stream can be replicated to multiple outbound interfaces and multicast stream characteristics can be modified according to the rules. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001193909855__fig_feature_image_multicast_nat_01), after multicast NAT is deployed on the Device, the Device uses traffic policies to match the input multicast stream StreamIn, translates stream characteristics, and outputs the post-translation multicast streams StreamOut1 and StreamOut2.

**Figure 1** Multicast NAT networking  
![](figure/en-us_image_0000001187073918.png)

#### Purpose

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001193909855__fig_feature_image_multicast_nat_01), users A and B receive the input multicast stream StreamIn from different multicast groups. However, traditional multicast technologies cannot meet the requirement for sending the same multicast stream to different multicast groups. To resolve this issue, deploy multicast NAT on the Device so that the Device can translate the characteristics of the input multicast stream StreamIn and output multicast streams that meet the characteristics of users A and B.


#### Benefits

Multicast NAT offers the following benefits:

* Multicast stream characteristics can be translated as needed to meet the requirements of different downstream users for receiving multicast streams.
* The matrixes of multicast streams can be conveniently switched to replace traditional serial digital interface (SDI) switching matrixes.