Overview of ARP Security
========================

Address Resolution Protocol (ARP) security protects devices
from attacks that tamper with or forge ARP packets. ARP security implementation
enhances device and network security.

#### ARP Security Background

The Address Resolution Protocol (ARP) is an Internet protocol used to map IP addresses to MAC addresses.

If two hosts need to communicate, the sender must know the network-layer IP address of the receiver. IP datagrams, however, must be encapsulated with MAC addresses before they can be transmitted over the physical network. Therefore, ARP is needed to map IP addresses to MAC addresses to ensure the transmission of datagrams.


#### ARP Attack Type

ARP is easy to use but lacks security protection mechanisms. Attackers may use ARP to attack network devices. The following ARP attacks exist on networks:

* ARP spoofing attack
  
  Attackers send bogus ARP messages to modify ARP entries on gateways or valid hosts, interrupting the transmission of valid ARP messages.
* ARP flooding attack (also called DoS attack)
  
  Attackers forge and send to a device excessive ARP request messages and gratuitous ARP messages with IP addresses that cannot be mapped to MAC addresses. As a result, the device's ARP buffer overflows, and the device is incapable of caching valid ARP entries. In this case, valid ARP messages cannot be transmitted.


#### ARP Security Application

These ARP attacks pose a serious threat to the network security. ARP security offers various technologies to detect and protect against ARP attacks. [Table 1](#EN-US_CONCEPT_0172371856__en-us_concept_0172357123_tab_dc_vrp_arp-sec_feature_000101) describes ARP security implementation in defense against ARP attacks.

**Table 1** ARP security solutions
| Attack Type | ARP Defense | Function Description | Benefits |
| --- | --- | --- | --- |
| ARP spoofing | [Validity Check of ARP Packets](feature_0003992329.html) | After receiving an ARP message, the device checks whether the source and destination MAC addresses in the Ethernet header are the same as those in the data field of the ARP message. If the source and destination MAC addresses in the Ethernet packet header are different from those in the Data field of the ARP message, the device discards the ARP message. Otherwise, the ARP message is allowed to pass through. | The ARP anti-spoofing function can effectively defend against attacks initiated using ARP messages, ensuring the security and reliability of network communication. |
| ARP flooding | [Strict ARP Learning](feature_0003997073.html) | A device learns only the ARP Response messages in response to the ARP Request messages sent by itself. This prevents attacks from ARP Request messages and ARP Response messages in response to the ARP Request messages sent by other devices. | The ARP anti-flooding function can effectively reduce the CPU load and prevent ARP entry overflow, ensuring the normal running of network devices. |
| [ARP Entry Limit](feature_0003994266.html) | The device limits the maximum number of ARP entries that an interface can learn to prevent ARP entry overflow and implement ARP entry security. |
| [ARP Message Rate Limiting](feature_0003993346.html) | The device counts the number of ARP messages received within a specified period. If the number of received ARP messages exceeds the threshold, the device ignores the excess ARP messages and does not process them, preventing ARP entry overflow. |
| [Rate Limiting on ARP Miss Messages](feature_0003992973.html) | The device counts the number of ARP Miss messages received within a specified period. If the number of received ARP Miss messages exceeds the configured threshold, the device ignores the excess ARP Miss messages. This reduces the CPU load. |
| [Gratuitous ARP Packet Discarding](feature_0003996159_1.html) | After the function of discarding gratuitous ARP messages is enabled, the device directly discards gratuitous ARP messages to prevent ARP entry overflow. |