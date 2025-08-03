RADIUS Attributes
=================

RADIUS attributes are Attribute fields in RADIUS packets, which carry authentication, authorization, and accounting information. This section contains the following information:

* [Standard RADIUS Attributes](#EN-US_CONCEPT_0000001564115733__section01)
* [Huawei Proprietary RADIUS Attributes](#EN-US_CONCEPT_0000001564115733__section02)
* [RADIUS Attributes Available in Packets](#EN-US_CONCEPT_0000001564115733__section03)

#### Standard RADIUS Attributes

RFC 2865, RFC 2866, and RFC 3576 define standard RADIUS attributes that are supported by all mainstream vendors. For details, see [Table 1](#EN-US_CONCEPT_0000001564115733__tab_2).

Choose Columns...


OK
Cancel
Select All



**Table 1** Standard RADIUS attributes
| Attribute No. | Attribute Name | Attribute Type | Description |
| --- | --- | --- | --- |
| 1 | User-Name | string | User name for authentication. The user name format can be *user name@domain name* or *user name*. |
| 2 | User-Password | string | User password for authentication, which is only valid for Password Authentication Protocol (PAP) authentication. |
| 3 | CHAP-Password | string | User password for authentication, which is only valid for Challenge-Handshake Authentication Protocol (CHAP) authentication. |
| 4 | NAS-IP-Address | ipaddr | Internet Protocol (IP) address of the NAS carried in authentication request packets. By default, the attribute value is the source IP address of the authentication request packets sent by the NAS. You can change the attribute value using the [**radius-attribute nas-ip**](cmdqueryname=radius-attribute+nas-ip) command. |
| 5 | NAS-Port | integer | Physical port number of the network access server that is authenticating the user, which is in either of the following formats:  * new: slot ID (8 bits) + sub-slot ID (4 bits) + port number (8 bits) + Virtual Local Area Network (VLAN) ID (12 bits) * old: slot ID (12 bits) + port number (8 bits) + VLAN ID (12 bits) |
| 6 | Service-Type | integer | Service type of the user to be authenticated:  * 2 (Framed): 802.1X authentication users (using fixed user names) * 6 (Administrative): administrator * 8 (Authenticate Only): reauthentication only |
| 7 | Framed-Protocol | integer | Encapsulation protocol of frame services:  * For a non-administrator user, the value is fixed as 1. * For an administrator, the value is fixed as 6. |
| 8 | Framed-IP-Address | ipaddr | User IP address. |
| 11 | Filter-Id | string | User group name, service scheme name and IPv4 ACL number.  NOTE:   * The IPv4 ACL number and service scheme name carried in the Filter-Id (11) attribute can be authorized only to access users. They are listed in descending order of the authorization priority and cannot be carried together. * The authorization priority of the service scheme name carried in the Filter-Id (11) attribute is lower than that of the HW-User-Policy (26-146) attribute. |
| 12 | Framed-MTU | integer | MTU of a user packet. |
| 14 | Login-IP-Host | ipaddr | Administrator IP address:  * If the value is 0 or 0xFFFFFFFF, the IP address of an administrator is not checked. * If this attribute uses other values, the NAS checks whether the administrator IP address is the same as the delivered attribute value. |
| 15 | Login-Service | integer | Login service type used by the administrator:  * 0: Telnet * 50: SSH * 51: FTP * 52: Terminal   NOTE:  An attribute can contain multiple service types. |
| 18 | Reply-Message | string | Whether a user is authenticated:  * When an Access-Accept packet is returned, the user is successfully authenticated. * When an Access-Reject packet is returned, the user fails authentication. |
| 19 | Callback-Number | string | Information sent from the authentication server and displayed to a user, such as a mobile number. |
| 24 | State | string | * This attribute is available to be sent by the server to the client in an Access-Challenge and must be sent unmodified from the client to the server in the new Access-Request reply to that challenge, if any. * This attribute is sent by the server to the client in an Access-Accept packet that also includes a Terminate-Action attribute with the value of RADIUS-Request. If the NAS performs the termination action by sending a new Access-Request packet upon the termination of the current session, it must include the State attribute unchanged in the Access-Request packet. |
| 25 | Class | string | If the RADIUS server sends a RADIUS Access-Accept packet carrying the Class attribute to the NAS, the subsequent RADIUS Accounting-Request packets sent from the NAS must carry the Class attribute with the same value. |
| 26 | Vendor-Specific | string | Vendor-specific attribute. For details, see [Table 2](#EN-US_CONCEPT_0000001564115733__tab_3). A packet can carry one or more private attributes. Each private attribute contains one or more sub-attributes. |
| 27 | Session-Timeout | integer | In an Access-Accept packet, this attribute indicates the maximum number of seconds a user should be allowed to remain connected.  In an Access-Challenge packet, this attribute indicates the reauthentication duration of EAP authentication users. When this attribute is set to 0:  * If the **aaa-author session-timeout invalid-value enable** command is not configured, the Session-Timeout attribute delivered by the server does not take effect, and the user logout or reauthentication period depends on the device configuration. * If the **aaa-author session-timeout invalid-value enable** command is configured, the Session-Timeout attribute delivered by the server takes effect, and the device does not log out or reauthenticate users.   NOTE:   * When the RADIUS server delivers only this attribute, the value of attribute 29 Termination-Action is set to 0 (users are disconnected) by default. * When the value of the Session-Timeout attribute authorized by the RADIUS server is the maximum value 4294967295, the configuration does not take effect. |
| 29 | Termination-Action | integer | What action the NAS should take when the specified service is completed:  * 0: disconnection * 1: reauthentication   NOTE:  This attribute is valid only for 802.1X authentication users. |
| 32 | NAS-Identifier | string | String identifying the network access server originating the Access-Request. By default, the attribute value is the host name of the user. You can run the [**radius-server nas-identifier-format**](cmdqueryname=radius-server+nas-identifier-format) command to change the attribute value to the user VLAN ID or AP MAC address. |
| 40 | Acct-Status-Type | integer | Accounting-Request packet type:  * 1: Accounting-Request(Start) packet * 2: Accounting-Request(Stop) packet * 3: Accounting-Request(Interim-update) packet |
| 41 | Acct-Delay-Time | integer | Number of seconds the client has been trying to send the accounting packet (excluding the network transmission time). |
| 42 | Acct-Input-Octets | integer | Number of bytes in upstream traffic, corresponding to the lower 32 bits in the data structure for storing the upstream traffic. This attribute and the RADIUS attribute 52 (Acct-Input-Gigawords) compose the upstream traffic.  The traffic unit must be the same as that on the RADIUS server and can be bytes, Kbytes, Mbytes, or Gbytes. To set the traffic unit for each RADIUS server, run the [**radius-server traffic-unit**](cmdqueryname=radius-server+traffic-unit) command. By default, RADIUS traffic is measured in bytes. |
| 43 | Acct-Output-Octets | integer | Number of bytes in downstream traffic, corresponding to the lower 32 bits in the data structure for storing the downstream traffic. This attribute and the RADIUS attribute 53 (Acct-Output-Gigawords) compose the downstream traffic.  The traffic unit must be the same as that on the RADIUS server and can be bytes, Kbytes, Mbytes, or Gbytes. To set the traffic unit for each RADIUS server, run the [**radius-server traffic-unit**](cmdqueryname=radius-server+traffic-unit) command. By default, RADIUS traffic is measured in bytes. |
| 44 | Acct-Session-Id | string | Accounting session ID. The Accounting-Request(Start), Accounting-Request(Interim-update) packet, and Accounting-Request(Stop) packets of the same accounting session must have the same session ID.  The format of this attribute is: Host name (7 bits) + Slot ID (2 bits) + Subcard number (1 bit) + Port number (2 bits) + Outer VLAN ID (4 bits) + Inner VLAN ID (5 bits) + Central Processing Unit (CPU) Tick (6 bits) + User ID prefix (2 bits) + User ID (5 bits). |
| 45 | Acct-Authentic | integer | User authentication mode:  * 1: RADIUS authentication * 2: Local authentication * 3: Other remote authentications |
| 46 | Acct-Session-Time | integer | How long the user has received service, in seconds.  NOTE:  If the administrator modifies the system time after the user goes online, the online time calculated by the device may be incorrect. |
| 47 | Acct-Input-Packets | integer | Number of incoming packets. |
| 48 | Acct-Output-Packets | integer | Number of outgoing packets. |
| 49 | Acct-Terminate-Cause | string | Cause of a terminated session:  * User-Request (1): The user requests termination of service. * Lost Carrier (2): The connection is torn down due to a handshake failure or heartbeat timeout, such as an ARP probe failure or PPP handshake failure. * Lost Service (3): The connection initiated by the peer device is torn down. * Idle Timeout (4): The idle timer expires. * Session Timeout (5): The session times out or the traffic threshold is reached. * Admin Reset (6): The administrator disconnects the user. * Admin Reboot (7): The administrator restarts the NAS. * Port Error (8): A port fails. * NAS Error (9): The NAS encounters an internal error. * NAS Request (10): The NAS ends the session due to resource changes. * NAS Reboot (11): The NAS automatically restarts. * Port Unneeded (12): The port is down. * Port Preempted (13): The port is preempted. * Port Suspended (14): The port is suspended. * Service Unavailable (15): The service is unavailable. * Callback (16): NAS is terminating the current session to perform a callback for a new session. * User Error (17): User authentication fails or times out. * Host Request (18): A host sends a request. |
| 52 | Acct-Input-Gigawords | integer | Number of upstream bytes, corresponding to the higher 32 bits in the data structure for storing the upstream traffic. The value is a multiple of 4 GB (2^32). This attribute and the RADIUS attribute 42 (Acct-Input-Octets) compose the upstream traffic.  The traffic unit must be the same as that on the RADIUS server and can be bytes, Kbytes, Mbytes, or Gbytes. To set the traffic unit for each RADIUS server, run the [**radius-server traffic-unit**](cmdqueryname=radius-server+traffic-unit) command. By default, RADIUS traffic is measured in bytes. |
| 53 | Acct-Output-Gigawords | integer | Number of downstream bytes, corresponding to the higher 32 bits in the data structure for storing the downstream traffic. The value is a multiple of 4 GB (2^32). This attribute and the RADIUS attribute 43 (Acct-Output-Octets) compose the downstream traffic.  The traffic unit must be the same as that on the RADIUS server and can be bytes, Kbytes, Mbytes, or Gbytes. To set the traffic unit for each RADIUS server, run the [**radius-server traffic-unit**](cmdqueryname=radius-server+traffic-unit) command. By default, RADIUS traffic is measured in bytes. |
| 55 | Event-Timestamp | integer | Time when an Accounting-Request packet is generated. The value is the number of seconds elapsed since 00:00:00 of January 1, 1970. |
| 60 | CHAP-Challenge | string | Challenge field in CHAP authentication. This field is generated by the NAS for Message Digest algorithm 5 (MD5) calculation. |
| 61 | NAS-Port-Type | integer | NAS port type. The default type of wired users is Ethernet (15). |
| 64 | Tunnel-Type | integer | Protocol type of the tunnel. The value is fixed as 13, indicating VLAN. |
| 65 | Tunnel-Medium-Type | integer | Medium type used on the tunnel. The value is fixed as 6, indicating Ethernet. |
| 66 | Tunnel-Client-Endpoint | string | Address of the client end of the tunnel. |
| 67 | Tunnel-Server-Endpoint | string | Address of the server end of the tunnel. |
| 79 | EAP-Message | string | Encapsulates Extended Access Protocol (EAP) packets so that RADIUS supports EAP authentication. When an EAP packet is longer than 253 bytes, the packet is encapsulated into multiple attributes. A RADIUS packet can carry multiple EAP-Message attributes. |
| 80 | Message-Authenticator | string | Authenticates and verifies authentication packets to prevent spoofing packets. This attribute is used only when RADIUS supports EAP authentication. |
| 81 | Tunnel-Private-Group-ID | string | Tunnel private group ID, which is used to deliver user VLAN IDs.  NOTE:   * Authorization can be performed based on the VLAN name, VLAN description, and VLAN ID, which are listed in ascending order of priority. |
| 82 | Tunnel-Assignment-ID | string | Specific ID allocated to a tunnel. |
| 85 | Acct-Interim-Interval | integer | Interim accounting interval. The value ranges from 60 to 3932100, in seconds. It is recommended that the interval be at least 600 seconds. |
| 87 | NAS-Port-Id | string | Port of the NAS that is authenticating the user. The NAS-Port-Id attribute has the following formats:  * New:  For Ethernet access users, the NAS port ID is in the format of "slot=xx; subslot=xx; port=xxx; VLAN ID=xxxx; interfaceName=port", where slot is 64 (indicating access through an Eth-Trunk interface) or ranges from 0 to 15, subslot from 0 to 15, port from 0 to 255, and VLAN ID from 1 to 4094 and interfaceName indicates the user access interface, including the interface type and number. * Old:  For Ethernet access users, the NAS-Port-Id is in the format "port number (2 characters) + sub-slot ID (2 bytes) + card number (3 bytes) + VLAN ID (9 characters)." * **vendor** *vendor-id*: The format defined by the vendor is used for encapsulation. Currently, the value of *vendor-id* can only be 9. The format is interface type+interface number, indicating a user access interface. To check the user access interface, run the **display access-user** **user-id** *user-id* command and view the **User access Interface** field in the command output. |
| 90 | Tunnel-Client-Auth-ID | string | Client tunnel ID used in the authentication phase during tunnel establishment. |
| 91 | Tunnel-Server-Auth-ID | string | Server tunnel ID used in the authentication phase during tunnel establishment. |
| 98 | Login-IPv6-Host | ipaddr | Host system address. |
| 195 | HW-SecurityStr | string | Security information of users in EAP relay authentication. |




#### Huawei Proprietary RADIUS Attributes

RADIUS is a fully extensible protocol. The No. 26 attribute (Vendor-Specific) defined in RFC 2865 can be used to extend RADIUS for implementing functions not supported by standard RADIUS attributes. **[Table 2](#EN-US_CONCEPT_0000001564115733__tab_3)** describes Huawei proprietary RADIUS attributes.

![](public_sys-resources/note_3.0-en-us.png) 

Extended RADIUS attributes contain the vendor ID of the device. The vendor ID of Huawei is 2011.


Choose Columns...


OK
Cancel
Select All



**Table 2** Huawei proprietary RADIUS attributes
| Attribute No. | Attribute Name | Attribute Type | Description |
| --- | --- | --- | --- |
| 26-1 | HW-Input-Peak-Information-Rate | integer | Peak rate at which the user accesses the NAS, in bit/s. The value is a 4-byte integer. |
| 26-2 | HW-Input-Committed-Information-Rate | integer | Average rate at which the user accesses the NAS, in bit/s. The value is a 4-byte integer. |
| 26-3 | HW-Input-Committed-Burst-Size | integer | Committed burst size at which the user accesses the NAS, in bit/s. The value is a 4-byte integer. |
| 26-4 | HW-Output-Peak-Information-Rate | integer | Peak rate at which the NAS connects to the user, in bit/s. The value is a 4-byte integer. |
| 26-5 | HW-Output-Committed-Information-Rate | integer | Average rate at which the NAS connects to the user, in bit/s. The value is a 4-byte integer. |
| 26-6 | HW-Output-Committed-Burst-Size | integer | Committed burst size at which the NAS connects to the user, in bit/s. The value is a 4-byte integer. |
| 26-18 | HW-UserName-Access-Limit | integer | Maximum number of users who are allowed to access the network using the same user name. The value 0 indicates that no user is allowed to access the network. The value 0xFFFFFFFF (4294967295) indicates that the number of users who are allowed to access the network using the same user name is not limited. The value 1 indicates that the maximum number of users who are allowed to access the network using the same user name is 1. |
| 26-26 | HW-Connect-ID | integer | Index of a user connection. |
| 26-28 | HW-FTP-Directory | string | Initial directory of an FTP user. |
| 26-29 | HW-Exec-Privilege | integer | Administrator (such as Telnet user) priority, ranging from 0 to 3. The priority that is greater than or equal to 4 is invalid. |
| 26-59 | HW-NAS-Startup-Time-Stamp | integer | NAS start time, represented by the number of seconds elapsed since 00:00:00 of January 1, 1970. |
| 26-60 | HW-IP-Host-Address | string | User IP address and MAC address carried in authentication and accounting packets, in the format A.B.C.D hh:hh:hh:hh:hh:hh. The IP address and MAC address are separated by a space.  If the user's IP address is detected to be invalid during authentication, the IP address is set to 255.255.255.255. |
| 26-138 | HW-Domain-Name | string | Name of the domain used for user authentication. This attribute can be the domain name contained in a user name or the name of a forcible domain. |
| 26-153 | HW-Access-Type | integer | User access type carried in the authentication and accounting request packets sent by the device to the RADIUS server:   * 1: 802.1X user * 6: administrator |
| 26-244 | HW-Reachable-Detect | string | Server reachability detection. Authentication and accounting packets carrying this attribute are server probe packets. |
| 26-254 | HW-Version | string | Software version of the device. |
| 26-255 | HW-Product-ID | string | NAS product name. |




#### RADIUS Attributes Available in Packets

RADIUS attributes are carried in RADIUS authentication packets. [Table 3](#EN-US_CONCEPT_0000001564115733__table16653121761019) describes RADIUS attributes available in accounting and dynamic authorization packets.

![](public_sys-resources/note_3.0-en-us.png) 

* 1: indicates that the attribute must appear once in the packet.
* 0: indicates that the attribute cannot appear in the packet (it will be discarded if it is contained).
* 0-1: indicates that the attribute can appear once or does not appear in the packet.
* 0+: indicates that the attribute may appear multiple times or does not appear in the packet.

**Table 3** RADIUS Attributes Available in Packets
| Attribute | RADIUS Authentication Packet (**Access**) | | | | RADIUS Accounting Packet (**Accounting**) | | | | | | RADIUS Dynamic Authorization Packet (CoA) | | | RADIUS Dynamic Authorization Packet (DM) | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| / | **Request** | **Accept** | **Reject** | **Challenge** | **Request(Start)** | **Request(Interim-Update)** | **Request(Stop)** | **Response(start)** | **Response(Interim-Update)** | **Response(Stop)** | **REQUEST** | **ACK** | **NAK** | **REQUEST** | **ACK** | **NAK** |
| User-Name(1) | 1 | 0-1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 |
| User-Password(2) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CHAP-Password(3) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| NAS-IP-Address(4) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 |
| NAS-Port(5) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Service-Type(6) | 1 | 0-1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Framed-Protocol(7) | 1 | 0-1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Framed-IP-Address(8) | 0-1 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 |
| Filter-Id(11) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| Framed-MTU(12) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Login-IP-Host(14) | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Login-Service(15) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Reply-Message(18) | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Callback-Number(19) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| State(24) | 0-1 | 0-1 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Class(25) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Vendor-Specific(26) | 0+ | 0+ | 0-1 | 0 | 0+ | 0+ | 0+ | 0+ | 0+ | 0 | 0+ | 0+ | 0+ | 0+ | 0+ | 0+ |
| Session-Timeout(27) | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0-1 | 0-1 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| Termination-Action(29) | 0 | 0-1 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| NAS-Identifier(32) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0 | 0 | 0 |
| Acct-Status-Type(40) | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Delay-Time(41) | 0 | 0 | 0 | 0 | 0-1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Input-Octets(42) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Output-Octets(43) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Session-id(44) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| Acct-Authentic(45) | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Session-Time(46) | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Input-Packets(47) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Output-Packets(48) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Terminate-Cause(49) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Input-Gigawords(52) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Output-Gigawords(53) | 0 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Event-Timestamp(55) | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CHAP-Challenge(60) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| NAS-Port-Type(61) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Type(64) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Medium-Type(65) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Client-Endpoint (66) | 0-1 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Server-Endpoint (67) | 0-1 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| EAP-Message(79) | 0-1 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Message-Authenticator(80) | 0-1 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Private-Group-ID(81) | 0 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Assignment-ID (82) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Acct-Interim-Interval(85) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| NAS-Port-Id(87) | 0-1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0-1 | 0 | 0 |
| Tunnel-Client-Auth-ID(90) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Tunnel-Server-Auth-ID(91) | 0 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Login-IPv6-Host(98) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-SecurityStr(195) | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Input-Peak-Information-Rate(26-1) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-Input-Committed-Information-Rate(26-2) | 0 | 0-1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-Input-Committed-Burst-Size(26-3) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-Output-Peak-Information-Rate(26-4) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-Output-Committed-Information-Rate(26-5) | 0 | 0-1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-Output-Committed-Burst-Size(26-6) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 |
| HW-UserName-Access-Limit(26-18) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Connect-ID(26-26) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ftp-directory(26-28) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Exec-Privilege(26-29) | 0 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-NAS-Startup-Time-Stamp(26-59) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-IP-Host-Address(26-60) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Domain-Name(26-138) | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Access-Type(26-153) | 1 | 0-1 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Reachable-Detect(26-244) | 0-1 | 0 | 0 | 0 | 0-1 | 0-1 | 0-1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Version(26-254) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HW-Product-ID(26-255) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |