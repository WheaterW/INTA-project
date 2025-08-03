NetStream Flow Export
=====================

The NDE exports statistics about aged flows from the NetStream cache to a specified NSC for further analysis.

#### Flow Statistics Export Modes

**Original flow statistics export**

In this mode, statistics about each flow are exported to the NSC when the flow aging time expires, enabling the NSC to obtain details about each flow.

**Flexible flow statistics export**

In this mode, the NDE creates flexible flows based on a customized template, and exports flow statistics to the NSC. This mode allows you to collect flow statistics based on the protocol type, source IP address, destination IP address, source port number, destination port number, source MAC address, destination MAC address, Ethernet type, VLAN, flow label, and ToS. Compared with original flow statistics export, flexible flow statistics export consumes fewer system resources, and allows you to collect NetStream flow statistics more flexibly.

When outbound or inbound flexible flow sampling is configured on an interface, only the interface information of the corresponding direction is contained in the flexible flow statistics.


#### Versions of Exported Packets

The NDE exports NetStream flow statistics to the NSC. In order for the NSC to parse the exported packets, the version of exported packets carrying these statistics must be the same as that configured on the NSC. NetStream packets can be exported in V5 or V9 format, and packets in both formats are transmitted using UDP.

* V5: The packet format is fixed. NetStream packets in this format contain the original flow statistics collected based on 7-tuple information.
* V9: The packet format is defined in a template. It allows NetStream flow statistics to be exported more flexibly through combinations of various data formats.

Due to its advantages of being template-based and highly extendable, V9 is supported by most NSCs. As such, you are advised to set the version of exported packets to V9.


#### Length of Interface Indexes in Exported Packets

A NetStream server obtains interface information in flow statistics according to the length of interface indexes (16 or 32 bits) in exported NetStream packets carrying the flow statistics. The NetStream servers of different vendors may use different interface index lengths. As such, the NDE must use an interface index length that is supported by the NetStream server. For example, if the NetStream server can parse 32-bit interface indexes, you need to set the length of interface indexes contained in exported NetStream packets to 32 bits on the NDE.

The interface index length configured on the NDE must be the same as that supported by the NSC; otherwise, the NSC cannot properly receive or parse the NetStream packets sent from the NDE.