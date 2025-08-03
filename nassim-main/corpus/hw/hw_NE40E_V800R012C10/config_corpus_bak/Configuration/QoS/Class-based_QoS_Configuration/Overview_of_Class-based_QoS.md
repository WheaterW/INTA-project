Overview of Class-based QoS
===========================

Overview_of_Class-based_QoS

#### Definition

Traffic classification technology allows a device to classify packets that enter a DiffServ domain in order for the device to identify the packet service type and to apply any appropriate action upon the packet.

A traffic classifier is configured to provide differentiated services and must be associated with a certain traffic control or resource allocation behavior, which is called a traffic behavior.


#### Traffic Classification Techniques

Packets can be classified based on QoS priorities (for details, see section [QoS Priority Fields](feature_0021577555.html)), or packet information such as the source IP address, destination IP address, MAC address, IP protocol, and port number, or specifications in an SLA.

After packets are classified at the DiffServ domain edge, internal nodes provide differentiated services for classified packets. A downstream node can accept and continue the upstream classification or classify packets based on its own criteria.

Therefore, traffic classification can be classified as behavior aggregate classification or multi-field classification. For details, see section [BA Classification](feature_0021577556.html) and [MF Classification](feature_0021577559.html).


#### BA Classification

Behavior Aggregate (BA) classification allows the
device to classify packets based on related values as follows:

* DSCP value of IPv4 packets
* TC value of IPv6 packets
* EXP value of MPLS packets
* 802.1p value of VLAN packets

It is used to simply identify the traffic that
has the specific priority or class of service (CoS) for mapping between
external and internal priorities.

BA classification confirms that the priority of
incoming packets on a device is trusted and mapped to the service-class
and color based on a priority mapping table. The service-class and
color of outgoing packets are then mapped back to the priority. For
details about priority mapping, see section [QoS Priority Mapping](feature_0021577558.html).

To configure BA classification on a NE40E, configure a DiffServ (DS) domain, define a priority mapping
table for the DS domain, and bind the DS domain to a trusted interface.

BA classification applies to the DS internal nodes.


#### Multi-Field Classification

As networks rapidly develop, services on the Internet become increasingly diversified. Various services share limited network resources, especially when multiple services use port number 80. Because of this increasing demand, network devices are required to possess a high degree of sensitivity for services, including an in-depth parsing of packets and a comprehensive understanding of any packet field at any layer. This level of sensitivity rises far beyond what behavior aggregate (BA) classification can offer. Multi-field (MF) classification can be deployed to help address this sensitivity deficit.

MF classification allows a device to elaborately classify packets based on certain conditions, such as 5-tuple (source IP address, source port number, protocol number, destination address, and destination port number). To simplify configurations and facilitate batch modification, MF classification commands are designed based on a template. For details, see section [Traffic Policy Based on MF Classification](feature_0021577561.html).


#### Traffic Behaviors Techniques

The following table describes traffic behaviors that can be implemented individually or jointly for classified packets on a NE40E.

| Traffic Behavior | | Description |
| --- | --- | --- |
| Marking/Re- marking | External marking | Sets or modifies the priority of packets to relay QoS information to the next device. |
| Internal marking | Sets the class of service (CoS) and drop precedence of packets for internal processing on a device so that packets can be placed directly in specific queues.  Setting the drop precedence of packets is also called coloring packets. When traffic congestion occurs, packets in the same queue are provided with differentiated buffer services based on colors. |
| Traffic policing | | Restricts the traffic rate to a specific value. When traffic exceeds the specified rate, excess traffic is dropped. |
| Congestion management | | Places packets in queues for buffering. When traffic congestion occurs, the device determines the forwarding order based on a specific scheduling algorithm and performs traffic shaping for outgoing traffic to meet users' requirements on the network performance. |
| Congestion avoidance | | Monitors network resources. When network congestion intensifies, the device drops packets to prevent overloading the network. |
| Packet filtering | | Functions as the basic traffic control method. The device determines whether to drop or forward packets based on traffic classification results. |
| Policy-based routing (also called redirection) | | Determines whether packets will be dropped or forwarded based on the following policies:   * Drop PBR states that a specific IP address must be matched against the forwarding table. If an outbound interface is matched, packets are forwarded; otherwise, packets are dropped. * Forward PBR states that a specific IP address must be matched against the forwarding table. If an outbound interface is matched, packets are forwarded; otherwise, packets are forwarded based on the destination IP addresses. |
| Load balancing | | Load balancing is configured to be session-by-session or packet-by-packet.  Load balancing applies only to packets that have multiple forwarding paths available. There are two possible scenarios:   * Multiple forwarding entries exist. * Only one forwarding entry exists, but a trunk interface that has multiple member interfaces functions as the outbound interface in the forwarding entry. |
| Packet fragmentation | | Modifies the Don't Fragment (DF) field of packets.  NOTE:  Some packets sent from user terminals are 1500 bytes long. PCs generally set the DF value to 1 in the packets. When packets traverse network devices at various layers, such as the access, aggregation, or core network layer, additional information is added so that the packet length will exceed the maximum transmission unit (MTU) of 1500 bytes. If such a packet carries the DF value of 1 in the header, the packet will be dropped. A DF value of 1 specifies that a datagram not be fragmented in transit. To prevent such packet loss and to keep users unaware of any change, the device involved is allowed to set the DF field in an IP header. |
| URPF (Unicast Reverse Path Forwarding) | | Prevents the source address spoofing attack. URPF obtains the source IP address and the inbound interface of a packet and checks them against the forwarding table. If the source IP address is not found, URPF considers the source IP address as a pseudo address and drops the packet. |
| Flow mirroring | | Allows a device to copy an original packet from a mirrored port and to send the copy to the observing port. |
| Flow sampling | | Collects information about specific data flow, such as timestamps, source address, destination address, source port number, destination port number, ToS value, protocol number, packet length, and inbound interface information, to monitor specific users. |
| Modifying the TTL value | | Modifies the Time To Live (TTL) value of IP packet headers. |