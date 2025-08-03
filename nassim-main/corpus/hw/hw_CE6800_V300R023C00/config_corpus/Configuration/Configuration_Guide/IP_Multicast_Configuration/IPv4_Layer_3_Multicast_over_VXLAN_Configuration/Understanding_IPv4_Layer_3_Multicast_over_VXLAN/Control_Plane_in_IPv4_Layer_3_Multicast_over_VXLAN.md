Control Plane in IPv4 Layer 3 Multicast over VXLAN
==================================================

A VXLAN network with distributed gateways uses BGP EVPN routes to dynamically establish VXLAN tunnels and transmit host MAC routes or host IP routes, thereby implementing Layer 2 and Layer 3 communication between devices of the same tenant. To implement Layer 3 multicast in this scenario, some NG MVPN mechanisms must be introduced on the control plane so that multicast routing information can be transmitted on the VXLAN network. Multicast entries can then be established on the VXLAN network to guide multicast data forwarding.

#### Introduction to NG MVPN

[Figure 1](#EN-US_CONCEPT_0000001182173007__fig_dc_vrp_mc-over-vxlan_feature_000601) shows the basic network model of NG MVPN in a distributed VXLAN gateway scenario. [Table 1](#EN-US_CONCEPT_0000001182173007__table_01) describes the basic concepts involved in this model.

**Figure 1** Basic NG MVPN network model  
![](figure/en-us_image_0000001182465323.png)

**Table 1** Basic concepts
| Concept | Description |
| --- | --- |
| Leaf | It is a gateway device on a VXLAN network and logically functions as a VXLAN tunnel endpoint (VTEP). A leaf node is functionally equivalent to a provider edge (PE) on an NG MVPN. All VPN processing is performed on this device. |
| Spine | A transparent transmission device that focuses on IP forwarding on a VXLAN network. A spine is functionally equivalent to a provider (P) on an NG MVPN. This device has the BGP EVPN and basic IP forwarding capabilities but does not maintain VPN information. |
| Customer edge (CE) | A CE has an interface directly connected to a leaf node and is unaware of the existence of VPNs. A PIM network is deployed between a leaf and a CE so that multicast receivers can access a VXLAN-based NG MVPN. |
| BGP MVPN peer | NG MVPNs use BGP to transmit C-multicast routing information. That is, NG MVPN peers exchange BGP MVPN routes to transmit user join information and guide the generation of multicast entries. To enable different leaf nodes on the same NG MVPN to exchange BGP MVPN routes, a BGP MVPN peer relationship must be established between these leaf nodes. |
| Inclusive-Provider Multicast Service Interface (I-PMSI) tunnel | On an NG MVPN, information used by leaf nodes to establish public network tunnels is carried in a new BGP route attribute called PMSI. PMSI tunnels are logical channels used to transmit C-multicast data over the public network, and an I-PMSI tunnel connects to all PEs on the same NG MVPN. This means that multicast data sent over an I-PMSI tunnel can be received by all PEs on the NG MVPN.  The VXLAN tunnel between leaf nodes is an I-PMSI tunnel on the NG MVPN. |
| PIM Join (multicast member join) | PIM Join messages are converted into BGP MVPN routes on leaf nodes and sent to the leaf node or RP on the multicast source side, guiding the generation of multicast entries. PIM Join messages are classified into the following types:   * PIM (S, G) Join message: If a multicast source is specified when a multicast member joins a multicast group, a PIM (S, G) Join message is used. * PIM (\*, G) Join message: If no multicast source is specified when a multicast member joins a multicast group, a PIM (\*, G) Join message is used. |



#### BGP MVPN Peer Establishment and Route Transmission

**MVPN member auto-discovery**

On a VXLAN-based NG MVPN, each leaf node discovers other leaf nodes on the same MVPN through a process called MVPN member auto-discovery (A-D). An NG MVPN uses BGP to implement this process. To support MVPN member auto-discovery, BGP defines the BGP-MVPN address family. After the BGP-MVPN address family is enabled on leaf nodes, they can automatically negotiate to establish BGP peer relationships in the BGP-MVPN address family (as BGP MVPN peers). The implementation is as follows:

Leaf nodes on the same MVPN send BGP Update messages to each other to exchange MVPN information, which is carried in the network layer reachability information (NLRI) field of the BGP Update messages. The NLRI carrying MVPN information is also called MVPN NLRI. [Figure 2](#EN-US_CONCEPT_0000001182173007__fig_dc_vrp_mc-over-vxlan_feature_000602) describes the NLRI format.

**Figure 2** MVPN NLRI format  
![](figure/en-us_image_0000001136066038.png)

**Table 2** Fields in MVPN NLRI
| Field | Description |
| --- | --- |
| Route type | Type of an MVPN route. For details, see [Table 3](#EN-US_CONCEPT_0000001182173007__table_03). |
| Length | Length of the Route Type Specific field in the MVPN NLRI. |
| Route type specific | Information about an MVPN route. The length of this field is variable due to different types of MVPN routes containing different information. For details, see [Table 3](#EN-US_CONCEPT_0000001182173007__table_03). |

[Table 3](#EN-US_CONCEPT_0000001182173007__table_03) describes MVPN NLRI types and functions.

**Table 3** MVPN NLRI types and functions
| Type | Name | Function | Route Type Specific Field Format | Remarks |
| --- | --- | --- | --- | --- |
| 1 | Intra-AS I-PMSI A-D route | It is mainly used for intra-AS MVPN member auto-discovery and is initiated by each leaf node with MVPN enabled. | Field description:   * RD: route distinguisher, an 8-byte field in a VPN-IPv4 address. An RD and a 4-byte IPv4 address prefix form a VPN-IPv4 address, which is used to differentiate the IPv4 prefixes using the same address space in different VPN instances. * Originating router's IP address: IP address of the source device that sends the A-D route. In application, this field is the MVPN ID of the device that sends the BGP A-D route. | Type 1 and Type 5 routes are called MVPN A-D routes, which are used to automatically discover MVPN members. After leaf nodes on the same MVPN exchange Type 1 routes, they automatically establish a BGP MVPN peer relationship. |
| 5 | Source Active A-D route | It is used by a leaf node to notify other leaf nodes on the MVPN of multicast source information when it discovers new C-multicast (S, G) information. | Field description:   * RD: RD of the VPN instance on the leaf node connected to the multicast source. * Multicast source length: length of a multicast source address. The value is 32 if the address is an IPv4 address. * Multicast source: multicast source address. * Multicast group length: length of the multicast group address. The value is 32 if the address is an IPv4 address. * Multicast group: multicast group address. |
| 6 | Shared Tree Join route | It is used in the (\*, G) scenario. The (\*, G) PIM-SM join initiated by a VPN is also called (C-\*, C-G) PIM join, where C is short for customer.  When a receiver-side leaf node receives a (C-\*, C-G) PIM Join message, it converts the Join message into a Shared Tree Join route and then sends the route to the BGP MVPN peers (other leaf nodes through which the RP can be reached). | Field description:   * RD: RD of the VPN instance on the leaf node connected to the multicast source. * Source AS: Source AS Extended Community of the unicast route to the multicast source. * Multicast source length: length of a multicast source address. The value is 32 if the address is an IPv4 address. * Multicast source: multicast source address. * Multicast group length: length of the multicast group address. The value is 32 if the address is an IPv4 address. * Multicast group: multicast group address.   NOTE:  Shared Tree Join routes and Source Tree Join routes have the same NLRI format. But for the (C-\*, C-G) join, a multicast source address is an RP address. | Type 6 and Type 7 routes are called C-multicast routes, which are used to initiate VPN user join requests and guide the generation of multicast entries. |
| 7 | Source Tree Join route | It is used in the (S, G) scenario. The (S, G) PIM-SSM join initiated by a VPN is also called (C-S, C-G) PIM join, where C is short for customer.  When a receiver-side leaf node receives a (C-S, C-G) PIM Join message, it converts the Join message into a Source Tree Join route and then sends the route to the leaf node on the multicast source side through the BGP MVPN peer relationship. |

**MVPN Target**

MVPN targets are mainly used to control MVPN A-D route advertisement and function similarly as VPN targets on unicast VPNs. MVPN targets are classified into two types:

* Export MVPN target: After an export MVPN target is configured for an MVPN instance on a local leaf node, the export MVPN target is advertised along with an MVPN A-D route.
* Import MVPN Target: After receiving an MVPN A-D route from another leaf node, the local leaf node checks the export MVPN target of the route. If the export MVPN target matches the import MVPN target of a VPN instance on the local leaf node, the local leaf node accepts the MVPN A-D route and records the sender leaf node as an MVPN member. If the export MVPN target does not match the import MVPN target of any VPN instance, the local leaf node discards the route.

![](public_sys-resources/note_3.0-en-us.png) 

If no MVPN target is configured, the MVPN uses the VPN target of the unicast VPN by default. If an MVPN and a unicast VPN share the same network topology, an MVPN target does not need to be configured. Otherwise, configuring an MVPN target is required.