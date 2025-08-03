Understanding BFD
=================

Understanding BFD

#### Fundamentals

A BFD session is established on two network devices to monitor bidirectional forwarding paths between them and serve an upper-layer application. BFD does not provide a neighbor discovery mechanism. Instead, BFD obtains neighbor information from the upper-layer application it serves for session setup. After the BFD session is set up, devices periodically send BFD packets. If a device does not receive a response within a specified detection period, the device considers the forwarding path faulty. BFD will then notify the upper-layer application for processing. The following uses association between OSPF and BFD as an example to describe the BFD session setup process.

**Figure 1** BFD session setup  
![](figure/en-us_image_0000001176661925.png)

On a simple network as shown in [Figure 1](#EN-US_CONCEPT_0000001130622344__fig_dc_bfd_fd_000301), OSPF and BFD are configured on DeviceA and DeviceB. A BFD session is set up as follows:

1. OSPF uses the Hello mechanism to discover neighbors and establishes a neighbor relationship.
2. OSPF notifies BFD of neighbor information including source and destination addresses.
3. BFD sets up a BFD session based on the received neighbor information.
4. After the BFD session is set up, BFD starts to detect and rapidly responds to link faults.

**Figure 2** Link fault detection through BFD  
![](figure/en-us_image_0000001176741829.png)

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001130622344__fig_dc_bfd_fd_000302):

1. The monitored link fails.
2. BFD quickly detects the link down event and changes the BFD session state to down.
3. BFD notifies the local OSPF process that the BFD neighbor is unreachable.
4. The local OSPF process ends the OSPF neighbor relationship.

#### BFD Detection Mechanism

Two systems establish a BFD session and periodically send BFD Control packets along the path between them. If one system does not receive BFD Control packets within a specified period, the system considers the path faulty.

BFD Control packets are encapsulated into UDP packets for transmission. In the initial phase of a BFD session, both systems negotiate BFD parameters with each other using BFD Control packets. These parameters include discriminators, desired minimum intervals for sending and receiving BFD Control packets, and local BFD session status. After the negotiation succeeds, BFD Control packets are transmitted along the path at the negotiated interval.

BFD mainly works in asynchronous mode. In this mode, both systems periodically send BFD Control packets to each other. If one system consecutively fails to receive BFD Control packets, the system considers the BFD session down.


#### Types of Links Monitored by BFD

**Table 1** Types of links monitored by BFD
| Link Type | Sub-Type | Description |
| --- | --- | --- |
| IP | * Layer 3 physical interfaces * Ethernet sub-interfaces (including Eth-Trunk sub-interfaces) | If a physical Ethernet interface has multiple sub-interfaces, separate BFD sessions can be established on the physical Ethernet interface and its sub-interfaces. |
| Eth-Trunk | * Layer 2 Eth-Trunk links * Layer 2 Eth-Trunk member links * Layer 3 Eth-Trunk links * Layer 3 Eth-Trunk member links | Separate BFD sessions can be established to detect link faults on an Eth-Trunk interface and its member interfaces at the same time. |
| VLANIF | * VLAN Ethernet member links * VLANIF interfaces | Separate BFD sessions can be established to monitor a VLANIF interface and VLAN member interfaces at the same time. |



#### BFD Packet

[Figure 3](#EN-US_CONCEPT_0000001130622344__fig8921171315436) describes the format of a BFD packet. [Table 2](#EN-US_CONCEPT_0000001130622344__table116392048105216) describes the fields in a BFD packet.

**Figure 3** BFD packet format  
![](figure/en-us_image_0000001176741831.png)

**Table 2** Fields in a BFD packet
| Field | Length | Meaning |
| --- | --- | --- |
| Vers (Version) | 3 bits | BFD version number. The current version number is 1. |
| Diag (Diagnostic) | 5 bits | Diagnostic word, which indicates the cause of the last session status change of the local BFD system:   * 0: No diagnostic information is displayed. * 1: Detection timed out. * 2: The Echo function failed. * 3: The peer session went down. * 4: A BFD session on the forwarding plane was reset. * 5: A path monitored by BFD went down. * 6: A cascaded path that is associated with the path monitored by BFD went down. * 7: A BFD session is in the AdminDown state. * 8: A reverse cascaded path that is associated with the path monitored by BFD went down. * 9 to 31: reserved for future use. |
| Sta (State) | 2 bits | Local BFD status:   * 0: AdminDown * 1: Down * 2: Init * 3: Up |
| P (Poll) | 1 bit | Whether the transmitting system requests verification of connectivity or of a parameter change:   * 0: The transmitting system requests no verification.  * 1: The transmitting system requests verification of connectivity or of a parameter change. |
| F (Final) | 1 bit | Whether the transmitting system responds to a received BFD packet with the P bit set to 1:   * 0: The transmitting system does not respond to a received BFD packet with the P bit set to 1.  * 1: The transmitting system responds to a received BFD packet with the P bit set to 1. |
| C (Control Plane Independent) | 1 bit | Whether the forwarding plane is separate from the control plane:   * 0: The forwarding plane is not separate from the control plane. At least one of the two bits (peer C bit and local C bit) is not 1, indicating that BFD packets are transmitted on the control plane. In this case, if BFD detects a down event during graceful restart (GR), the service does not need to respond.  * 1: The forwarding plane is separate from the control plane. Both the received peer C bit and local C bit are 1, indicating that the BFD implementation of the transmitting system does not depend on the control plane. BFD packets are transmitted on the forwarding plane. Even if the control plane fails, BFD can still take effect. For example, BFD continues to monitor the link status during the IS-IS GR process on the control plane, using BFD packets with the C bit set to 1. In this case, if BFD detects a down event during GR, the service module responds to the down event by changing the topology and routes to minimize traffic loss. |
| A (Authentication Present) | 1 bit | Whether authentication is performed for a BFD session:   * 0: No authentication is performed for the BFD session. * 1: Authentication is performed for the BFD session. |
| D (Demand) | 1 bit | Whether demand mode is used:   * 0: The transmitting system does not wish to or cannot work in demand mode.  * 1: The transmitting system wishes to work in demand mode. |
| M (Multipoint) | 1 bit | This bit is reserved for BFD to support P2MP extensions in the future. |
| Detect Mult | 8 bits | Detection timeout multiplier, used by the detecting party to calculate the detection timeout duration:   * demand mode: The local detection multiplier takes effect. * asynchronous mode: The peer detection multiplier takes effect. |
| Length | 8 bits | Packet length, in bytes. |
| My Discriminator | 32 bits | Local discriminator of a BFD session. It is a unique non-zero value generated by the transmitting system. Local discriminators are used to distinguish multiple BFD sessions in a system. |
| Your Discriminator | 32 bits | Remote discriminator of a BFD session:   * 0: unknown * Non-0: value of My Discriminator received from the remote system |
| Desired Min TX Interval | 32 bits | Minimum supported local interval (in milliseconds) for sending BFD packets. |
| Required Min RX Interval | 32 bits | Minimum supported local interval (in milliseconds) for receiving BFD packets. |
| Required Min Echo RX Interval | 32 bits | Minimum supported local interval (in milliseconds) for receiving Echo packets. Value 0 indicates that the local system does not support the Echo function. |



#### BFD Session Setup Modes

BFD sessions can be set up in either static or dynamic mode, as described in [Table 3](#EN-US_CONCEPT_0000001130622344__table_dc_vrp_bfd_feature_000602). The two modes differ in the way local (My Discriminator) and remote (Your Discriminator) discriminators are configured.

**Table 3** BFD session setup modes
| BFD Session Setup Mode | Description |
| --- | --- |
| Static BFD session | * Static BFD session with manually specified discriminators  BFD session parameters (including local and remote discriminators) are configured manually, and the requests for setting up BFD sessions are delivered manually. After one end of a BFD session receives a BFD Control packet, it compares the values of My Discriminator and Your Discriminator in the packet with those of the local BFD session to determine whether they match. * Static BFD session with automatically negotiated discriminators  The BFD session is manually created, but local and remote discriminators are obtained through auto-negotiation. You must configure a static BFD session with automatically negotiated discriminators on the local device to communicate with the peer device and allow BFD to detect static routes, in BFD for static routes scenarios where a dynamic BFD session is set up on the peer device that does not support static BFD sessions. NOTE:  In static mode, configure unique local and remote discriminators for each BFD session. If the same discriminators are configured for two BFD sessions, the BFD session configured later may affect the BFD session configured earlier, causing BFD session flapping. |
| Dynamic BFD session | BFD session setup is dynamically triggered by routing protocols. The local discriminator is dynamically allocated, and the remote discriminator is obtained from BFD packets sent by the peer. After establishing a new neighbor relationship, a routing protocol notifies BFD of the neighbor relationship and detection parameters (including destination and source addresses), and then BFD sets up a session based on the received parameters. When a fault occurs on the link, the routing protocol associated with BFD can quickly detect the BFD session down event. Traffic is then switched to the backup link immediately to minimize data loss. Dynamic BFD is used on networks that require high reliability. When a BFD session is set up dynamically, the system processes the local and remote discriminators as follows:  * Dynamic allocation of the local discriminator: When an application triggers setup of a dynamic BFD session, the system allocates a dynamic local discriminator within a specified range to the BFD session. The system then sends a BFD Control packet with a Your Discriminator value of 0 to the peer to negotiate a session. * Automatic discovery of the remote discriminator: After the local end of a BFD session receives a BFD Control packet with Your Discriminator set to 0, it checks whether the packet matches the local BFD session based on 4-tuple information (source and destination IP addresses, outbound interface, and VPN index). If they match, the system learns the value of My Discriminator in the BFD control packet to obtain the remote discriminator.   NOTE:  Dynamic BFD is applicable to BFD for BGP, BFD for IS-IS, BFD for OSPF, and BFD for RIP. For details about how to configure dynamic BFD, see description of each dynamic routing protocol. |



#### BFD Session Management

A BFD session has the following states:

* Down: A BFD session is in the Down state or has just been set up.
* Init: The local system can communicate with the remote system and expects the BFD session to go up.
* Up: A BFD session has been successfully set up.
* AdminDown: A BFD session has been brought down for administrative purposes.

The BFD session state is carried in the State field of a BFD packet. The local system updates the session state according to the local session state and the received session state of the remote system. The BFD state machine implements a three-way handshake for BFD session setup or teardown to ensure that the two systems both detect the state changes. The following uses BFD session setup as an example to describe state changes of the BFD state machine.

**Figure 4** BFD session setup  
![](figure/en-us_image_0000001130622376.png)

1. DeviceA and DeviceB start their respective BFD state machines. The initial state of the BFD state machines is Down. DeviceA and DeviceB send BFD packets with the State field set to Down. For a static BFD session, the value of Your Discriminator in a BFD packet is specified manually. For a dynamic BFD session, the value of Your Discriminator is 0.
2. After receiving a BFD packet with the status being down and learning the Your Discriminator value, DeviceB switches the BFD session status to Init and sends a BFD packet with the status being Init.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the local BFD session state of DeviceB changes to Init, DeviceB no longer processes received BFD packets with the State field set to Down.
3. The BFD status change on DeviceA is the same as that on DeviceB. After receiving a BFD packet with the status being down and learning the Your Discriminator value, DeviceA sends a BFD packet with the status being Init to DeviceB.
4. After receiving a BFD packet with the State field set to Init, DeviceB changes the local session state to Up.
5. The BFD session state change on DeviceA is the same as that on DeviceB.