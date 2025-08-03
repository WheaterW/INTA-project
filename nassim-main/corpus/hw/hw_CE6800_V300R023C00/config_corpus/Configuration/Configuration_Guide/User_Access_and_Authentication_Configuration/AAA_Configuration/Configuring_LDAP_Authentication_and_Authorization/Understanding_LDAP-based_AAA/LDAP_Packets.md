LDAP Packets
============

LDAP Packets

#### LDAP Packet Format

The LDAP packets used for authentication and authorization include bindRequest, bindResponse, searchRequest, and searchResponse packets. These packets have similar format, as shown in [Figure 1](#EN-US_CONCEPT_0000001512676522__fig_dc_ldap_000200).**Figure 1** LDAP packet format  
![](figure/en-us_image_0000001513037050.png)

**Table 1** Description of fields in an LDAP packet
| Field | Description |
| --- | --- |
| LDAP Header | LDAP packet header, including the specific packet type. |
| messageID | Message ID. A server identifies request packets sent by clients according to the message IDs and correctly returns response packets. |
| protocolOP | Packet body, which carries packet type and authentication as well authorization information. Common packet types include bindRequest(0), bindResponse(1), searchRequest(3), searchResEntry(4), searchResDone(5), and searchResRef(19). |




#### LDAP Packet Types

LDAP packets include bind and search packets. [Table 2](#EN-US_CONCEPT_0000001512676522__tab-ldap-1) describes the LDAP bind packets and [Table 3](#EN-US_CONCEPT_0000001512676522__tab-ldap-2) describes the LDAP search packets.

**Table 2** LDAP bind packets
| Packet | Description |
| --- | --- |
| bindRequest | Bind request packet. After LDAP binding is selected by a client, the client sends a bind request packet to the LDAP server. |
| bindResponse | Bind response packet. After receiving and recording a bind request packet, the LDAP server returns a bind response packet. |
| unbindRequest | Unbind request packet. After completing all LDAP operations, the client sends an unbind request packet to request the server to terminate the LDAP session. |


**Table 3** LDAP search packets
| Packet | Description |
| --- | --- |
| searchRequest | Search request packet. After passing authentication, the client sends a search request packet to the server. The packet contains the search range, Base-DN, and filter criterion. |
| searchResultEntry | Search result packet, which carries the DN that is found. |
| searchResDone | Search status returned by the server to the client:  * success: The search operation is successful. * referral: If LDAP server does not store the Base-DN but knows the server that stores the Base-DN, then the packet contains this server's URL address. |
| searchResRef | Reference search result returned by the server to the client. If an LDAP server stores the directory of another LDAP server and the Base-DNs of the two servers are the same, the packet contains the URL address of the other server. |