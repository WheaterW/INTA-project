Overview of IGMP
================

Overview of IGMP

#### Definition

In the TCP/IP protocol suite, the Internet Group Management Protocol (IGMP) manages IPv4 multicast members. It sets up and maintains multicast group memberships between IP hosts and their directly connected multicast devices.


#### Purpose

In IP multicast communication, packets are sent from a source and forwarded to a group of receivers. In the multicast communication model, a sender does not need to know the locations of receivers. As shown in [Figure 1](#EN-US_CONCEPT_0000001176663959__fig_01), to ensure that multicast packets can reach receiver hosts, a mechanism is required to enable the multicast devices connected to the network segment of receivers to know which multicast receivers exist on the network segment and ensure that the receivers can join the corresponding multicast group. IGMP implements this by setting up and maintaining multicast group memberships between receiver hosts and their directly connected multicast device.

**Figure 1** IGMP deployment on a multicast network  
![](figure/en-us_image_0000001176743889.png)