Interface Classification
========================

Interfaces of a device are used to exchange data and interact with other network devices. Interfaces are classified as physical or logical interfaces.

#### Physical Interfaces

Physical interfaces exist on interface cards and are classified into management interfaces and service interfaces.

**Management interfaces**

Management interfaces are used to log in to devices for configuration and management purposes. They are not used for service transmission. For details about how to configure a management interface, see "First Login to a Device" in *Configuration Guide > Basic Configuration*.

[Table 1](#EN-US_CONCEPT_0000001130622202__table1018913125213) describes the management interfaces that the device supports.

**Table 1** Management interfaces
| Interface | Description | Application |
| --- | --- | --- |
| Console interface | A data connection equipment (DCE) interface that complies with the EIA/TIA-232 standard. | The console interface is connected to the COM serial interface of a configuration terminal to set up an on-site configuration environment. |
| MEth interface | Complies with the 10/100/1000BASE-TX standard. | The MEth interface can be connected to a network interface of a configuration terminal or network management workstation to set up an on-site or remote configuration environment. |


**Service interfaces**

Service interfaces are used for service transmission. Service interfaces are also referred to as ports. This document uses the term interface.

[Table 2](#EN-US_CONCEPT_0000001130622202__table4190113119528) describes the service interfaces that the device supports.

**Table 2** Service interfaces
| Interface Type | Description |
| --- | --- |
| Layer 3 Ethernet interfaces | Layer 3 Ethernet interfaces work at the network layer. They can be configured with IPv4 or IPv6 addresses, process Layer 3 protocol packets, and provide the routing function. |
| Layer 2 Ethernet interfaces | Layer 2 Ethernet interfaces work at the data link layer, process Layer 2 protocol packets, and implement rapid Layer 2 forwarding. |




#### Logical Interfaces

Logical interfaces are manually configured and do not physically exist. They are responsible for transmitting service data.

[Table 3](#EN-US_CONCEPT_0000001130622202__logical_01) describes the logical interfaces that the device supports.

**Table 3** Logical interfaces
| Interface Type | Interface Description | Application Scenario |
| --- | --- | --- |
| VLANIF interface | This is a Layer 3 logical interface that is created on a per VLAN basis. | Due to their simple configuration, VLANIF interfaces are most commonly used to implement Layer 3 communication between users in different VLANs and network segments. After a VLANIF interface is allocated an IP address, it functions as the gateway for the user hosts within that VLAN and forwards packets across network segments at Layer 3. If users on multiple network segments all need to communicate with each other, a primary IP address and multiple secondary IP addresses need to be configured on a VLANIF interface. |
| Eth-Trunk interface | This is a Layer 2 or Layer 3 logical interface that bundles multiple Ethernet interfaces. Each of the Ethernet interfaces is called a member interface. | Eth-Trunk interfaces are used in link aggregation scenarios and offer higher bandwidth and reliability by combining individual Ethernet interfaces. |
| Layer 2 Ethernet sub-interface | This is a Layer 2 logical interface configured on a physical interface. One or more can be configured on one physical interface. This is not supported by the CE6820H, CE6820S, and CE6885-LL (low latency mode). | Layer 2 Ethernet sub-interfaces are used for service access on VXLAN networks and can transmit various types of data packets depending on the configured encapsulation types. |
| Layer 3 Ethernet sub-interface | This is a Layer 3 logical interface configured on a physical interface. One or more can be configured on one physical interface. This is not supported by the CE6885-LL (low latency mode). | Layer 3 Ethernet sub-interfaces are used to implement Layer 3 communication between users in different VLANs and network segments. Unlike VLANIF interfaces, which require multiple physical interfaces for inter-VLAN communication, Layer 3 Ethernet sub-interfaces â each corresponding to one VLAN â require only one physical interface to achieve the same purpose. |
| Layer 2 Eth-Trunk sub-interface | This is a Layer 2 logical interface configured on an Eth-Trunk interface. One or more can be configured on one Eth-Trunk interface. This is not supported by the CE6820H, CE6820S, and CE6885-LL (low latency mode). | Layer 2 Eth-Trunk sub-interfaces are used for service access on VXLAN networks and can transmit various types of data packets depending on the configured encapsulation types. |
| Layer 3 Eth-Trunk sub-interface | This is a Layer 3 logical interface configured on an Eth-Trunk interface. One or more can be configured on one Eth-Trunk interface. This is not supported by the CE6885-LL (low latency mode). | Layer 3 Eth-Trunk sub-interfaces are used to implement Layer 3 communication between users in different VLANs and network segments. If interfaces on a downstream Layer 2 network device are assigned to different VLANs and a Layer 3 device connects to this device through a Layer 3 Eth-Trunk interface, Layer 3 Eth-Trunk sub-interfaces need to be created on the Eth-Trunk interface. This enables the Layer 3 Eth-Trunk interface to correctly identify the VLAN packets, enabling users in these VLANs to communicate with each other. |
| NVE interface | This is a logical interface that implements network virtualization. This is not supported by the CE6820H, CE6820S, and CE6885-LL (low latency mode). | NVE interfaces are used to implement Layer 2 connectivity on a VXLAN by establishing VXLAN tunnels between NVEs and encapsulating/decapsulating VXLAN packets. |
| VBDIF interface | This is a Layer 3 logical interface created on a per BD basis. This is not supported by the CE6820H, CE6820S. | A BD is a Layer 2 broadcast domain used to forward VXLAN data packets. VBDIF interfaces can be used to implement communication between different VXLAN networks and between VXLAN and non-VXLAN networks, and connect a Layer 2 network to a Layer 3 network. |
| Loopback interface | This is a logical interface. Any data packet sent to a loopback interface is considered to be sent to the device itself. A loopback interface has the following characteristics:  * Once created, its physical status and link protocol status remain up until it is deleted, even if the interface has no IP address configured. A loopback IP address can be used if you need an IP address of an interface that is usually up. * The IP address of a loopback interface can be advertised immediately after being configured. A loopback interface can be assigned an IP address with a 32-bit mask, which reduces address consumption. * A device directly discards a packet if the outbound interface of the packet that needs to be sent out is a local loopback interface. * A loopback interface cannot be encapsulated with any link layer protocol. Therefore, negotiation is not performed at the data link layer, and the data link protocol status is usually up.  InLoopback0 is a special and fixed loopback interface, which is automatically created on device startup. This interface uses the fixed loopback address 127.0.0.1/8 to receive all data packets destined for the device where the InLoopback0 interface resides. This IP address cannot be advertised using routing protocols. | Loopback interfaces can be used to:  * Improve network reliability when their IP addresses are specified as the source IP addresses of packets. * Control access interfaces and filter logs to simplify displayed information. |
| Null0 interface | This interface is automatically created on device startup. It is always up but cannot forward packets. Packets sent to a Null0 interface are all discarded. A Null0 interface cannot be configured with any IP address or encapsulated with any link layer protocol. | Null0 interfaces can be used to:  * Prevent routing loops (most typical usage). For example, a route to a Null0 interface is always created during route summarization. * Filter traffic. Undesired packets can be sent to Null0 interfaces to avoid the need for an access control list (ACL). For example, a Null0 interface can be specified as the next hop of a static route to a network segment, thereby filtering out all the data packets destined for that network segment. |
| Tunnel interface | This is a Layer 3 logical interface that is used by devices on the two ends of a tunnel to process tunnel packets. This is not supported by the CE6885-LL (low latency mode). | Tunnel interfaces with a specific tunnel mode configured are used in that tunneling scenario. |