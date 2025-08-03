RADIUS Packets
==============

RADIUS Packets

#### RADIUS Packet Format

RADIUS is based on the UDP protocol. [Figure 1](#EN-US_CONCEPT_0000001513035646__fig_dc_fd_aaa_000502) shows the RADIUS packet format.

**Figure 1** RADIUS packet format  
![](figure/en-us_image_0000001512676606.png)
Each RADIUS packet contains the following information:

* Code: The Code field is one octet and identifies the type of a RADIUS packet. Value of the Code field varies depending on the RADIUS packet type. For example, the value 1 indicates an Access-Request packet and the value 2 indicates an Access-Accept packet.
* Identifier: The Identifier field is one octet, and helps the RADIUS server match requests and responses and detect duplicate requests retransmitted within a certain period. After a client sends a request packet, the server sends a reply packet with the same Identifier value as the request packet.
* Length: The Length field is two octets and specifies length of a RADIUS packet. Octets outside the range of the Length field must be treated as padding and ignored on reception. If a packet is shorter than the Length field, it must be silently discarded.
* Authenticator: The Authenticator field is 16 octets. This value is used to authenticate the reply from the RADIUS server and is used in the password hiding algorithm.
* Attribute: This field is variable in length. RADIUS attributes carry the specific authentication, authorization, accounting information and configuration details for the request and reply packets. The Attribute field may contain multiple attributes, each of which consists of Type, Length, and Value. For details, see [RADIUS Attributes](galaxy_aaa_cfg_0030.html).
  
  + Type: The Type field is one octet and indicates the RADIUS attribute ID. The value ranges from 1 to 255.
  + Length: The Length field is one octet, and indicates the length of the RADIUS attribute (including the Type, Length and Value fields). The Length is measured in octets.
  + Value: The maximum length of the Value field is 253 bytes. The Value field contains information specific to the RADIUS attribute. The format and length of the Value field are determined by the Type and Length fields.


#### RADIUS Packet Type

RADIUS defines 16 types of packets. [Table 1](#EN-US_CONCEPT_0000001513035646__tab-radius-1) describes types of the authentication packets, and [Table 2](#EN-US_CONCEPT_0000001513035646__tab-radius-2) describes types of the accounting packets. For details about RADIUS CoA/DM packets, see [RADIUS CoA/DM](galaxy_aaa_cfg_0028.html).

**Table 1** RADIUS authentication packets
| Packet Name | Description |
| --- | --- |
| Access-Request | Access-Request packets are sent from a client to a RADIUS server and is the first packet transmitted in a RADIUS packet exchange process. This packet conveys information (such as the user name and password) used to determine whether a user is allowed access to a specific NAS and any special services requested for that user. |
| Access-Accept | After a RADIUS server receives an Access-Request packet, it must send an Access-Accept packet if all attribute values in the Access-Request packet are acceptable (authentication is successful). The user is allowed access to requested services only after the RADIUS client receives this packet. |
| Access-Reject | After a RADIUS server receives an Access-Request packet, it must send an Access-Reject packet if any of the attribute values in the Access-Request packet are not acceptable (authentication fails). |
| Access-Challenge | During EAP relay authentication, when a RADIUS server receives an Access-Request packet carrying the user name from a client, it generates a random MD5 challenge and sends the MD5 challenge to the client through an Access-Challenge packet. The client encrypts the user password using the MD5 challenge, and then sends the encrypted password in an Access-Request packet to the RADIUS server. The RADIUS server compares the encrypted password received from the client with the locally encrypted password. If they are the same, the server determines that the user is valid. |


**Table 2** RADIUS accounting packets
| Packet Name | Description |
| --- | --- |
| Accounting-Request(Start) | If a RADIUS client uses RADIUS accounting, the client sends an Accounting-Request(Start) packet to a RADIUS server before accessing network resources. |
| Accounting-Response(Start) | A RADIUS server must send an Accounting-Response(Start) packet after successfully receiving and recording an Accounting-Request(Start) packet. |
| Accounting-Request(Interim-update) | A RADIUS client periodically sends Accounting-Request(Interim-update) packets to a RADIUS server, reducing accounting deviation. This requires you to configure the real-time accounting function on the client to prevent the RADIUS server from continuing user accounting if the server fails to receive an Accounting-Request(Stop) packet from the client. |
| Accounting-Response(Interim-update) | A RADIUS server must send an Accounting-Response(Interim-update) packet after successfully receiving and recording an Accounting-Request(Interim-update) packet. |
| Accounting-Request(Stop) | When a user goes offline proactively or is forcibly disconnected by the NAS, the RADIUS client sends an Accounting-Request(Stop) packet carrying network resource usage information (including the online duration and number of incoming/outgoing bytes) to a RADIUS server, requesting the server to stop accounting. |
| Accounting-Response(Stop) | The RADIUS server must send an Accounting-Response(Stop) packet after receiving an Accounting-Request(Stop) packet. |