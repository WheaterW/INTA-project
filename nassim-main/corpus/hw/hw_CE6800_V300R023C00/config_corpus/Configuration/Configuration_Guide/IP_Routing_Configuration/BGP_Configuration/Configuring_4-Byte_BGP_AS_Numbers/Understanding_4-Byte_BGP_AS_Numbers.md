Understanding 4-Byte BGP AS Numbers
===================================

Understanding 4-Byte BGP AS Numbers

#### Purpose

2-byte AS numbers used on networks range from 1 to 65535, and the available AS numbers verge on exhaustion as networks expand. Therefore, 4-byte AS numbers ranging from 1 to 4294967295 are used to extend the AS number range. In addition, new speakers that support 4-byte AS numbers can co-exist with old speakers that support only 2-byte AS numbers.


#### Definition

4-byte AS numbers are extended from 2-byte AS numbers. BGP peers use a new capability code and new optional transitive attributes to negotiate the 4-byte AS number capability and transmit 4-byte AS numbers. This mechanism enables communication between new speakers as well as between old speakers and new speakers.

To support 4-byte AS numbers, an open capability code 0x41 is defined in a standard protocol for BGP connection negotiation. 0x41 indicates that the BGP speaker supports 4-byte AS numbers.

In addition, two new optional transitive attributes AS4\_Path (code 0x11) and AS4\_Aggregator (code 0x12) are defined to transmit 4-byte AS numbers over old sessions.

If a new speaker with an AS number greater than 65535 sets up a BGP connection with an old speaker, the old speaker needs to set the peer AS number to be the same as AS\_TRANS. The value of AS\_TRANS is fixed at 23456 and reserved.


#### Related Concepts

BGP 4-byte AS numbers involve the following concepts:

* New speaker: a BGP speaker that supports the new 4-byte AS number extensions.
* Old speaker: a BGP speaker that does not support the new 4-byte AS number extensions.
* New session: a BGP connection established between new speakers.
* Old session: a BGP connection established either between a new speaker and an old speaker or between old speakers.


#### Fundamentals

BGP speakers negotiate capabilities by exchanging Open messages. [Figure 1](#EN-US_CONCEPT_0000001176743547__fig_dc_vrp_bgp_feature_003602) shows the format of Open messages exchanged between new speakers. The header of a BGP Open message is fixed, in which My AS Number is supposed to be the local AS number. However, My AS Number carries only 2-byte AS numbers, and does not support 4-byte AS numbers. Therefore, a new speaker adds the AS\_TRANS 23456 to My AS Number and its local AS number to Optional Parameters before it sends an Open message to a peer. After the peer receives the message, it can determine whether the new speaker supports 4-byte AS numbers by checking Optional Parameters in the message.**Figure 1** Format of Open messages sent by new speakers  
![](figure/en-us_image_0000001130783968.png)

[Figure 2](#EN-US_CONCEPT_0000001176743547__fig_dc_vrp_bgp_feature_003603) shows how peer relationships are established between new speakers, and between an old speaker and a new speaker. BGP speakers notify each other of whether they support 4-byte AS numbers by exchanging Open messages. After the capability negotiation, new sessions are established between new speakers, and old sessions are established between a new speaker and an old speaker.**Figure 2** Process of establishing a BGP peer relationship  
![](figure/en-us_image_0000001176663717.png "Click to enlarge")

The AS\_Path and AS\_Aggregator attributes in Update messages exchanged between new speakers carry 4-byte AS numbers, whereas the two attributes in Update messages sent by an old speaker carry 2-byte AS numbers.

* When a new speaker sends an Update message carrying an AS number greater than 65535 to an old speaker, the new speaker uses AS4\_Path and AS4\_Aggregator to assist AS\_Path and AS\_Aggregator in transferring 4-byte AS numbers, as both AS4\_Path and AS4\_Aggregator are unrecognizable by the old speaker. On the network shown in [Figure 3](#EN-US_CONCEPT_0000001176743547__fig_dc_vrp_bgp_feature_003604), before the new speaker in AS 2.2 sends an Update message to the old speaker in AS 65002, the new speaker replaces each 4-byte AS number (1.1 and 2.2) with 23456 in AS\_Path; therefore, the AS\_Path carried in the Update message is (23456, 23456, 65001), and the carried AS4\_Path is (2.2, 1.1, 65001). Upon receiving the Update message, the old speaker in AS 65002 transparently transmits the message to other ASs.
* When a new speaker receives an Update message carrying AS\_Path, AS4\_Path, AS\_Aggregator, and AS4\_Aggregator from the old speaker, the new speaker uses the reconstruction algorithm to reconstruct the actual AS\_Path and AS\_Aggregator. On the network shown in [Figure 3](#EN-US_CONCEPT_0000001176743547__fig_dc_vrp_bgp_feature_003604), after the new speaker in AS 65003 receives an Update message carrying AS\_Path (65002, 23456, 23456, 65001) and AS4\_Path (2.2, 1.1, 65001) from the old speaker in AS 65002, the new speaker reconstructs the actual AS\_Path (65002, 2.2, 1.1, 65001).

**Figure 3** Process of transmitting a BGP Update message  
![](figure/en-us_image_0000001176663719.png "Click to enlarge")


#### Formats of 4-byte AS numbers

A 4-byte AS number can be either an integer or in dotted notation. 4-byte AS numbers are stored as unsigned integers, regardless of their formats. 4-byte AS numbers in dotted notation are in the format of *x*.*y*. A 4-byte AS number is switched between the integer and dotted notation formats as follows: 4-byte AS integer = *x* x 65536 + *y*. For example, if a 4-byte AS number in dotted notation is 2.3, it can be converted into the integer 131075 (2 x 65536 + 3).

BGP supports 4-byte AS numbers in both formats. The formats of 4-byte AS numbers displayed in the configuration scripts are the same as those configured by users.

By default, 4-byte AS numbers are displayed in dotted notation in the outputs of commands such as display and debugging commands, regardless of their configured formats. If the default display format of 4-byte AS numbers is changed from dotted notation to integer using a command, the 4-byte AS numbers will be displayed as integers automatically.

![](public_sys-resources/notice_3.0-en-us.png) 

If you adjust the display format of 4-byte AS numbers, the matching results of AS\_Path regular expressions and extended community filters are affected. Specifically, if the display format of 4-byte AS numbers is changed when an AS\_Path regular expression or extended community filter is used as an export or import policy, the AS\_Path regular expression or extended community filter needs to be reconfigured. If reconfiguration is not performed, routes cannot match the export or import policy, and a network fault occurs.



#### Benefits

4-byte AS numbers alleviate AS number exhaustion; therefore, they are beneficial to carriers who need to expand the network scale.