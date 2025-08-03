Routing in IPv4 Layer 3 Multicast over VXLAN
============================================

Routing in IPv4 Layer 3 Multicast over VXLAN

#### MVPN Extended Community Attributes

MVPN extended community attributes are mainly used to control the advertisement and acceptance of BGP C-multicast routes. The attributes are classified into the following types:

* Source AS extended community: carried in the BGP EVPN routes advertised by leaf nodes. This attribute is an AS-type attribute and is mainly used in inter-AS scenarios.
* VRF Route Import extended community: carried in the BGP EVPN routes advertised by a leaf node to other leaf nodes. When a receiver leaf node sends a C-multicast route to the sender leaf node, the receiver leaf node attaches this attribute to the route. When there are multiple sender leaf nodes, each sender leaf node that receives a C-multicast route can determine, according to this attribute, whether the C-multicast route should be processed by itself and which VPN routing table that the C-multicast route should be installed into.
  
  The value of the VRF Route Import Extended Community is in the format of Administrator field:Local Administrator field, in which the value of the Administrator field is the local MVPN ID (IP address of the originator PE in the MVPN), and the value of the Local Administrator field is the local VPN instance ID of the sender leaf node. If no MVPN ID is configured, BGP EVPN routes and C-multicast routes sent by a PE cannot carry the VRF Route Import extended community attribute.


#### Multicast Member Join Process

After leaf nodes establish a BGP MVPN peer relationship, they can use BGP MVPN routes to transmit the join information of C-multicast members. The following example describes how a multicast member joins a multicast group in PIM (S, G) and PIM (\*, G) modes.

**PIM (S, G) Join**

[Figure 1](#EN-US_CONCEPT_0000001182172995__fig_dc_vrp_mc-over-vxlan_feature_000603) describes how a multicast member joins a multicast group in the scenario where Leaf 2 initiates a PIM (S, G) Join request to Leaf 1.

**Figure 1** Time sequence for a multicast member to join a multicast group  
![](figure/en-us_image_0000001182465321.png)

For details about the process of joining a multicast group, see [Table 1](#EN-US_CONCEPT_0000001182172995__table_04).

**Table 1** Procedure for joining a multicast group
| Step | Device | Key Action |
| --- | --- | --- |
| 1 | Leaf1 | Leaf 1 generates a host unicast route destined for the multicast source, converts this route to a BGP EVPN route carrying Source AS and VRF Route Import extended community attributes, and advertises this route to Leaf 2. |
| 2 | Leaf2 | After Leaf 2 receives the route, Leaf 2 matches the export RT of the route against its local import RT.  * If the two targets match, the BGP EVPN route sent by Leaf 1 is accepted, and the Source AS and VRF Route Import extended community attributes carried in this route are stored for C-multicast route generation. * If the two targets do not match, the BGP EVPN route is discarded. |
| 3 | Leaf2 | After Leaf 2 receives an IGMP join request, it generates a PIM-SSM Join message. |
| 4 | Leaf2 | After generating the PIM-SSM Join message, Leaf 2 constructs a C-multicast route based on the Source AS and VRF Route Import extended community attributes stored in Step 2, and sets RT-import of the C-multicast route to the VRF Route Import extended community value. |
| 5 | Leaf2 | It generates a multicast entry, in which the downstream interface is the interface that receives the PIM Join message. In addition, Leaf 2 searches for the VPN unicast route to the multicast source. Upon finding that the upstream device is Leaf 1, Leaf 2 sends the PIM-SSM Join message to Leaf 1 through the C-multicast route. |
| 6 | Leaf1 | After receiving the C-multicast route, Leaf 1 performs the following operations:  1. Checks the Administrator field and Local Administrator field values in the RT-import attribute of the C-multicast route. After confirming that the Administrator field value is the same as its local MVPN ID, it accepts the C-multicast route. 2. Determines the VPN instance to which the C-multicast route belongs based on the Local Administrator field value in the RT-import attribute of the route. 3. Processes the C-multicast route and adds it to the corresponding VPN instance routing table. 4. Converts the C-multicast route into a PIM-SSM Join message and creates a C-multicast entry to guide multicast data traffic forwarding. In the entry, the downstream interface is a Through-BGP interface (with the forwarding plane being a VXLAN tunnel).  Finally, the multicast receiver successfully joins the multicast group, and Leaf 1 can forward multicast traffic of the multicast group to Leaf 2. |

**PIM (\*, G) Join**

[Table 2](#EN-US_CONCEPT_0000001182172995__table_05) describes the PIM (\*, G) Join implementation.

**Table 2** PIM (\*, G) Join implementation
| Implementation Mode | Fundamentals | Advantage | Disadvantage |
| --- | --- | --- | --- |
| Not transmitting (\*, G) entries across the public network | (\*, G) entries are not transmitted to a remote leaf node through a VXLAN tunnel on the public network. Instead, the (\*, G) entries are converted into (S, G) entries and then transmitted to the remote leaf node across the public network.  In this mode, if different PIM-SM BSR domains are available, there must be a reachable VPN route between each device and the RP in each domain. If only one BSR domain is available, there must be a reachable VPN route between each device and the RP. | * PIM (\*, G) entries are not transmitted across the public network. Therefore, the RPT-to-SPT switchover does not occur on the public network, which simplifies processing on PEs and reduces state information maintained on leaf nodes. * VPN RPs can be either static or dynamic. | Leaf nodes alone can function as VPN RPs, or both CEs and leaf nodes function as VPN RPs. However, if CEs function as VPN RPs, each of them needs to establish an MSDP peer relationship with its connected leaf node. |


![](public_sys-resources/note_3.0-en-us.png) 

The advertisement of BGP EVPN routes during the PIM (\*, G) join process is similar to that during the PIM (S, G) join process. For details, see [Table 1](#EN-US_CONCEPT_0000001182172995__table_04).

(\*, G) entries are not transmitted across the public network in the following scenarios:

* Scenario 1: Leaf nodes function as RPs.
  
  On the network shown in [Figure 2](#EN-US_CONCEPT_0000001182172995__fig_dc_vrp_mc-over-vxlan_feature_000607), Leaf 1 and Leaf 2 function as RPs. [Table 3](#EN-US_CONCEPT_0000001182172995__table_08) describes the join procedure in this scenario.
  
  **Figure 2** Time sequence for joining a multicast group when leaf nodes function as RPs  
  ![](figure/en-us_image_0000001136066036.png)
  
  **Table 3** Procedure for joining a multicast group when leaf nodes function as RPs
  | Step | Device | Key Action |
  | --- | --- | --- |
  | 1 | CE2 | After receiving an IGMP join request, CE2 sends a PIM (\*, G) Join message to Leaf 2. |
  | 2 | Leaf2 | Upon receipt of the PIM (\*, G) Join message, Leaf 2 generates an (\*, G) entry. Because Leaf 2 is an RP, it does not send a C-multicast route (Shared Tree Join route) to other devices. Then, an RPT rooted at Leaf 2 and with CE2 as a leaf node is established. |
  | 3 | CE1 | After receiving multicast traffic from the multicast source, CE1 sends a PIM Register message to Leaf 1. |
  | 4 | Leaf1 | Upon receipt of the PIM Register message, Leaf 1 generates an (S, G) entry. |
  | 5 | Leaf1 | Leaf 1 sends a Source Active A-D route to all its BGP MVPN peers. |
  | 6 | Leaf2 | Upon receipt of the Source Active A-D route, Leaf 2 generates an (S, G) entry, which inherits the outbound interface of the corresponding (\*, G) entry. |
  | 7 | Leaf2 | Leaf 2 initiates a switchover to an SPT and sends a C-multicast route (Source Tree Join route) to Leaf 1. |
  | 8 | Leaf1 | Upon receipt of the C-multicast route (Source Tree Join route), Leaf 1 diverts multicast traffic to the I-PMSI tunnel (VXLAN tunnel) based on the corresponding C-multicast forwarding entry. Finally, multicast traffic is transmitted to CE2. |
* Scenario 2: CEs function as RPs.
  
  On the network shown in [Figure 3](#EN-US_CONCEPT_0000001182172995__fig_dc_vrp_mc-over-vxlan_feature_000608), CE2 and CE3 function as RPs, an MSDP peer relationship is established between CE2 and Leaf 2, and between CE3 and Leaf 3. [Table 4](#EN-US_CONCEPT_0000001182172995__table_09) describes the join procedure in this scenario.
  
  **Figure 3** Time sequence for joining a multicast group when CEs function as RPs  
  ![](figure/en-us_image_0000001136225830.png)
  
  **Table 4** Procedure for joining a multicast group when CEs function as RPs
  | Step | Device | Key Action |
  | --- | --- | --- |
  | 1 | CE2 | After receiving an IGMP join request, CE2 generates a PIM (\*, G) entry. Because CE2 is an RP, it does not send the PIM (\*, G) entry upstream. |
  | 2 | CE1 | After receiving multicast traffic from the multicast server, CE1 sends a PIM Register message to CE3. |
  | 3 | CE3 | Upon receipt of the PIM Register message, CE3 generates an (S, G) entry. |
  | 4 | CE3 | CE3 sends an MSDP SA message carrying the (S, G) entry information to its MSDP peer, Leaf 1. |
  | 5 | Leaf1 | Upon receipt of the MSDP SA message, Leaf 1 generates an (S, G) entry. |
  | 6 | Leaf1 | Leaf 1 sends a Source Active A-D route carrying the (S, G) entry information to other leaf nodes. |
  | 7 | Leaf2 | Upon receipt of the Source Active A-D route, Leaf 2 learns the (S, G) entry information carried in the route and sends an MSDP SA message carrying the (S, G) entry information to its MSDP peer, CE2. |
  | 8 | CE2 | Upon receipt of the MSDP SA message, CE2 learns the (S, G) entry information carried in the message and generates an (S, G) entry. CE2 directly initiates an (S, G) join request to the multicast source. This implementation process is similar to that in PIM (S, G) Join mode. During this process, leaf nodes also generate an (S, G) entry. Finally, multicast traffic is forwarded to the multicast receiver. |