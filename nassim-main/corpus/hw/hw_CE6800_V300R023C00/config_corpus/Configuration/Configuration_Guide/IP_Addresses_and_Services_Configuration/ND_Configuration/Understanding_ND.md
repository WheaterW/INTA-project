Understanding ND
================

Understanding ND

#### IPv6 Address Resolution

To communicate with a destination host, a source host needs to first obtain the destination host's link-layer address (MAC address). In IPv4, this is achieved through ARP, whereas in IPv6, this is achieved through NDP.

ARP is defined as a protocol that runs between Layer 2 and Layer 3. Its messages are encapsulated in Ethernet packets, with the Ethernet type value set to 0x0806. ND is implemented through ICMPv6 messages, with the Ethernet type value set to 0x86DD. To signify that the messages are ICMPv6 messages, the Next Header value in the IPv6 header is set to 58. NDP, which is a Layer 3 protocol, uses ICMPv6-encapsulated messages. Layer 3 address resolution has the following advantages:

* Layer 3 address resolution enables Layer 2 devices to use the same address resolution protocol.
* Layer 3 security mechanisms are used to prevent address resolution attacks.
* Request messages can be multicast, reducing loads on Layer 2 networks.

Address resolution uses ICMPv6 Neighbor Solicitation (NS) and Neighbor Advertisement (NA) messages.

* In NS messages, the Type and Code field values are 135 and 0, respectively. These messages are similar to IPv4 ARP Request messages.
* In NA messages, the Type and Code field values are 136 and 0, respectively. These messages are similar to IPv4 ARP Reply messages.

[Figure 1](#EN-US_CONCEPT_0000001130622526__fig647113313815) shows the IPv6 address resolution process.

**Figure 1** IPv6 address resolution  
![](figure/en-us_image_0000001176742005.png)

Before sending messages to HostB, HostA must obtain HostB's link-layer address. To accomplish this, HostA sends an NS message with its IPv6 address as the source address and the solicited-node multicast address of HostB as the destination address. The Options field in the NS message carries the link-layer address of HostA.

After receiving the NS message, HostB replies with an NA message. In the NA message, the source address is HostB's IPv6 address, and the destination address is HostA's IPv6 address. The Options field carries HostB's link-layer address. This address resolution process enables HostA to obtain HostB's link-layer address.


#### Checking Neighbor Cache Entry States

Hardware faults and hot swapping of interface cards interrupt communication with neighboring devices. Communication cannot be restored if the destination of a neighboring device becomes invalid, but it can be restored if the path fails. To monitor the state of each neighboring device, nodes therefore need to maintain a neighbor table.

RFC standards define five neighbor cache entry states: Incomplete, Reachable, Stale, Delay, and Probe.

[Figure 2](#EN-US_CONCEPT_0000001130622526__fig5966164321313) shows the transition of neighbor cache entry states. The Empty state indicates that the neighbor table is empty.

**Figure 2** Neighbor state transition  
![](figure/en-us_image_0000001176742003.png)

The following example describes changes in neighbor cache entry state of node A during its first communication with node B.

1. Node A sends an NS message and generates a cache entry. The neighbor cache entry state is Incomplete.
2. If node B replies with an NA message, the neighbor cache entry state changes from Incomplete to Reachable. Otherwise, the neighbor cache entry state changes from Incomplete to Empty after a certain period of time, and node A deletes this entry.
3. After the neighbor reachable time expires, the neighbor cache entry state changes from Reachable to Stale, indicating that the neighbor reachable state is unknown.
4. If node A receives an unsolicited NA message from node B in the Reachable state, and the link-layer address of node B carried in the message is different from that learned by node A, the neighbor cache entry state changes to Stale.
5. After the aging time of ND entries in the Stale state expires, the neighbor cache entry state changes to Delay.
6. After a period of time (5s), the neighbor cache entry state changes from Delay to Probe. During this time, if node A receives an NA message, the neighbor cache entry state changes to Reachable.
7. Node A sends three unicast NS messages at the configured interval (1s) while node B is in the Probe state. If node A receives an NA message, the neighbor cache entry state changes from Probe to Reachable. Otherwise, the state changes to Empty and node A deletes the entry.