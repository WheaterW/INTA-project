MSDP Working Mechanism
======================

MSDP Working Mechanism

#### MSDP Peer

MSDP enables RPs in different PIM-SM domains to communicate and share multicast source information, allowing inter-domain multicast services to run properly. The first task for implementing inter-domain multicast transmission is to establish MSDP peer relationships. After MSDP peer relationships are established, they exchange SA messages. An SA message carries (S, G) information registered by the source DR with the RP. Message exchange between MSDP peers ensures that SA messages sent by any RP can be received by all other RPs.

An MSDP peer relationship can be established between RPs that belong to the same autonomous system (AS) but different PIM-SM domains, or between RPs that are in different ASs. To ensure successful reverse path forwarding (RPF) checks in an inter-AS scenario, a BGP or a Multicast Border Gateway Protocol (MBGP) peer relationship must be established on the same interfaces where the MSDP peer relationship is established.

MSDP peers can also be configured on other PIM devices in addition to the RPs. As shown in [Figure 1](#EN-US_CONCEPT_0000001130783716__fig_01), MSDP peers can be created on any PIM device. The MSDP peers created on different PIM devices have different functions.

**Figure 1** Locations of MSDP peers  
![](figure/en-us_image_0000001130783736.png)

[Table 1](#EN-US_CONCEPT_0000001130783716__table530641511281) describes the functions of MSDP peers created on RPs.

**Table 1** Functions of MSDP peers created on RPs
| Classification of MSDP Peers | Location | Function |
| --- | --- | --- |
| Source MSDP peer | MSDP peer (generally the source RP, such as RP1) closest to a multicast source | The source RP creates and sends SA messages to the remote MSDP peer to advertise multicast source information registered on itself. |
| Receiver MSDP peer | MSDP peer (such as RP3) closest to a receiver | After receiving an SA message, the receiver MSDP peer joins a cross-domain shortest path tree (SPT) with the multicast source specified in the SA message as the root. After receiving multicast data from this source, the peer forwards multicast data along the rendezvous point tree (RPT) to local receivers.  The receiver MSDP peer must be configured on an RP. Otherwise, it cannot receive multicast source information from other domains. |
| Intermediate MSDP peer | MSDP peer (such as RP2) with multiple remote MSDP peers | The intermediate MSDP peer forwards SA messages received from one MSDP peer to other MSDP peers. |

MSDP peers created on common PIM devices (non-RPs) only forward received SA messages.

![](public_sys-resources/note_3.0-en-us.png) 

To ensure that all RPs on a network share source information, and to minimize the number of MSDP-enabled devices, you are advised to configure MSDP peers only on the RPs.

An RPF peer is generated when an MSDP-enabled device performs an RPF check on an SA message. After receiving an SA message, the MSDP-enabled device determines the next-hop peer on the optimal path to the source RP that had created the SA message using the Multicast RPF Routing Information Base (MRIB). This next-hop peer is called the RPF peer and it determines whether an MSDP-enabled device accepts SA messages. If the SA message is sent by the RPF peer, the message is accepted and forwarded to other MSDP peers.


#### Process of Establishing an MSDP Peer Connection

MSDP peers use port 639 to set up TCP connections. After MSDP is enabled on two devices and they are specified as MSDP peers, the devices compare their IP addresses. The device with a smaller IP address starts the ConnectRetry timer and initiates a TCP connection to the other device. The device with a larger IP address checks whether a TCP connection has been set up on port 639. The MSDP peer relationship is established once a TCP connection is set up, and MSDP peers maintain the TCP connection by exchanging KeepAlive messages.

[Figure 2](#EN-US_CONCEPT_0000001130783716__fig0531104610110) shows the process for setting up an MSDP peer relationship between DeviceA and DeviceB.

**Figure 2** Process of establishing an MSDP peer connection  
![](figure/en-us_image_0000001176743401.png)

The process for establishing an MSDP peer connection is as follows:

1. In the initial state, the MSDP session is in the DISABLED state on both devices.
2. After MSDP is enabled on both devices, and they are specified as MSDP peers, they compare the IP addresses they use to establish the TCP connection:
   * DeviceA has a smaller IP address, so it enters the CONNECTING state; DeviceB has a larger IP address, so it enters the LISTEN state.
   * DeviceA sends a TCP active open message to DeviceB and starts the ConnectRetry timer, which defines the interval for retrying TCP connection setup.
   * DeviceB sends a TCP passive open message to DeviceA and waits for a connection setup request from DeviceA.
3. After the TCP connection is set up, the MSDP session enters the ESTABLISHED state.
4. The MSDP peers send KeepAlive messages to each other to request that the MSDP connection is maintained.

#### MSDP Mesh Group

If multiple MSDP peers exist on a network, SA messages may be flooded among peers. As MSDP peers need to perform an RPF check on each received SA message, this places a heavy burden on the systems. You can add multiple MSDP peers to a mesh group. After an MSDP peer in the mesh group receives an SA message from another MSDP peer in the same mesh group, it will not send the SA message to the other MSDP peers in the group. This significantly reduces the number of SA messages transmitted between these MSDP peers. A mesh group is a full-mesh group. In other words, each mesh group member must set up an MSDP peer relationship with all of the others and recognize each other as members of the same mesh group. Each MSDP peer can only join one mesh group. Mesh group members can be located in one or more PIM-SM domains, and can also be located in one or more ASs.

As shown in [Figure 3](#EN-US_CONCEPT_0000001130783716__fig2043513311214), DeviceA, DeviceB, DeviceC, and DeviceD are added to the same mesh group. Each device must establish an MSDP peer relationship with the other three devices.

**Figure 3** MSDP peer relationships among mesh group members  
![](figure/en-us_image_0000001176663487.png)

#### MSDP Authentication

MSDP authentication ensures the security of TCP connections. After this function is enabled, you must configure the same encryption algorithm and password on both ends. Otherwise, the TCP connection cannot be established between the MSDP peers. MSDP supports the following mutually exclusive authentication modes: Message-Digest algorithm 5 (MD5) and keychain. Only one encryption mode can be selected between MSDP peers.

**MD5 authentication**

MSDP supports MD5 authentication for TCP connections. If authentication fails, no TCP connections can be established. The MD5 algorithm is insecure and poses security risks. As such, you are advised to use a more secure encryption algorithm.

**Keychain authentication**

Keychain authentication works at the application layer, and improves security by periodically changing the password and encryption algorithm without interrupting services. When keychain authentication is configured for MSDP peer relationships over TCP connections, both MSDP messages and the TCP connection setup process can be authenticated.