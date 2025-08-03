Overview of 802.1X Authentication
=================================

Overview of 802.1X Authentication

#### Definition

802.1X defines a port-based network access control protocol to authenticate users and control their access rights based on access ports of LAN access devices.


#### Benefits

802.1X authentication provides high security:

* Authentication packets are encapsulated using EAP and multiple encryption algorithms are supported. You can select an authentication mode based on the actual scenario and obtain certificates to verify the client and server. For details about the supported authentication modes, see [Authentication Mode Selection](galaxy_nac_cfg_0040.html#EN-US_CONCEPT_0000001563880241__section1682995484180154).
* Authentication packets and data packets are transmitted through different logical interfaces, strengthening network security.
* 802.1X is a Layer 2 protocol that does not require Layer 3 processing and can implement access control at the access layer.

#### 802.1X Authentication System

In [Figure 1](#EN-US_CONCEPT_0000001513040266__fig_dc_fd_nac_000401), the 802.1X authentication system uses a typical client/server architecture, which consists of three types of entities: client, access device, and authentication server.

**Figure 1** 802.1X authentication system  
![](figure/en-us_image_0000001512841006.png)

* The client is usually a user terminal that initiates 802.1X authentication using the client software. The client must support Extensible Authentication Protocol over LAN (EAPoL).
* The access device is usually an 802.1X-capable network device that provides a physical or logical port for the client to access a LAN.
* The authentication server, typically a RADIUS server, performs user authentication, authorization, and accounting.