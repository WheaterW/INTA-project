NetStream Flow Sampling and Creation
====================================

The NetStream module on a device samples service traffic and creates NetStream flows for the sampled traffic.

#### NetStream Sampling

The NetStream module on the device samples service traffic based on a certain sampling rate (sampling only one out of every *n* packets). For example, if the sampling rate is set to 100, one packet out of every 100 packets is sampled randomly.

NetStream analyzes flow information of only sampled packets, which can basically reflect the real network traffic conditions. This reduces the number of packets for which statistics are collected and the impact on device performance.


#### NetStream Flow Creation

NetStream is a technology that collects packet statistics based on flows. The NetStream module analyzes sampled packets and creates flows based on the following key information in the packets:

* For IPv4 original flow statistics collection: Packets with identical 7-tuple information are considered to be part of the same flow. The 7-tuple information refers to the destination IP address, source IP address, destination port number, source port number, protocol type, ToS, and inbound or outbound interface.
* For IPv6 original flow statistics collection, the IPv6 packets with identical 8-tuple information are considered to be part of the same flow. The 8-tuple information refers to the destination IPv6 address, source IPv6 address, destination port number, source port number, protocol type, ToS, flow label, and inbound or outbound interface.
* For IPv4 flexible flow statistics collection, the IPv4 packets with identical 11-tuple information are considered to be part of the same flow. The 11-tuple information refers to the destination IP address, source IP address, destination port number, source port number, protocol type, ToS, inbound or outbound interface, source MAC address, destination MAC address, Ethernet type, and VLAN.
* For IPv6 flexible flow statistics collection, the IPv6 packets with identical 12-tuple information are considered to be part of the same flow. The 12-tuple information refers to the destination IPv6 address, source IPv6 address, destination port number, source port number, protocol type, ToS, flow label, inbound or outbound interface, source MAC address, destination MAC address, Ethernet type, and VLAN.

For details about original flows and flexible flows, see [Flow Statistics Export Modes](galaxy_netstream_cfg_0007.html#EN-US_CONCEPT_0000001563881217__section995357633175343).