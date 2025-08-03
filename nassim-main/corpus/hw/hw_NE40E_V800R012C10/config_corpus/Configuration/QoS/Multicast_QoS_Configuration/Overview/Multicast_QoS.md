Multicast QoS
=============

Multicast QoS ensures smooth broadcast of multicast programs, preventing multicast traffic bursts.

#### Multicast Virtual Scheduling

With the development of BTV services, the quality of video services on TVs is now a key issue that has a direct impact on the experience of users. Therefore, how to ensure that users can watch smooth TV programs and how to differentiate and manage user bandwidth in a refined manner become urgent tasks for carriers.

**Figure 1** Multicast virtual scheduling networking  
![](images/fig_dc_ne_cfg_01384701.png)

As shown in [Figure 1](#EN-US_CONCEPT_0172371616__en-us_concept_0172357053_fig_dc_ne_cfg_01384701), a family views multicast programs (multicast data) through a Set Top Box (STB) and browses the Internet (unicast data) through a PC. The maximum bandwidth for the family is 3 Mbit/s. The Internet service consumes all the 3 Mbit/s bandwidth, and then the family demands a multicast program requiring the bandwidth of 2 Mbit/s through the STB. As the multicast data and unicast data require the bandwidth of 5 Mbit/s in total, data congestion will occur on the access network, and some packets will be discarded. As a result, the quality of multicast programs cannot be ensured.

The multicast virtual scheduling technology is developed to solve this problem. The multicast virtual scheduling technology is the user-level scheduling. It adjusts the bandwidth for the unicast traffic and multicast traffic of a user in a coordinated manner without changing the total bandwidth of the user, thus ensuring the quality of BTV services of the user. To address this problem, the Router in [Figure 1](#EN-US_CONCEPT_0172371616__en-us_concept_0172357053_fig_dc_ne_cfg_01384701) is configured with multicast virtual scheduling. When the sum of the multicast traffic and unicast traffic received by a user is greater than the bandwidth assigned to the user, the router reduces the bandwidth for unicast traffic of the user to 1 Mbit/s to meet the requirement of bandwidth for multicast traffic. Therefore, the user can watch multicast programs normally. After the IPTV multicast service is deployed, the multicast source may jitter when the multicast traffic is heavy and the multicast source is busy. The NE40E can shape the multicast traffic so that the jitter of the multicast source can be limited to an acceptable degree. If the NE40E is configured with multicast shaping, the NE40E can control the multicast traffic of users. Multicast shaping prevents multicast traffic from bursting, ensures that multicast packets are sent smoothly, and controls the jitter of the multicast source to an acceptable degree.