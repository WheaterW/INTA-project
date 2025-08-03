Fundamentals of NTP Access Control
==================================

Fundamentals of NTP Access Control

#### NTP Authentication

NTP authentication can be enabled on networks requiring high security. Different keys can be used in different NTP operating modes.

When NTP authentication is enabled in an NTP operating mode, the system records the key IDs corresponding to the operating mode in use. The authentication process is as follows:

* For packets sent by the system: The system determines whether authentication is required in an NTP operating mode. If authentication is not required, the system directly sends packets. If authentication is required, the system authenticates packets using both the key ID and an authentication algorithm before sending the packets.
* For packets received by the system: The system determines whether authentication is required on the received packets. If authentication is required, the system authenticates the packets based on the key ID and a decryption algorithm. If authentication fails, the system discards the packets. If authentication succeeds, the system processes the received packets.

#### Access Authority

Access authority is a simple measure taken to protect devices. You can configure access authority on a device to protect its local clock.

NTP access control is implemented based on an access control list (ACL). NTP supports up to five levels of access authority. An ACL rule may be specified for each level of access authority. If an NTP access request matches an ACL rule, the device requesting access is given access authority corresponding to that level.

When an NTP access request reaches the local end, access authority is matched against the following access permissions in sequence. **Peer** has the maximum access permission.

1. Peer: This indicates that a time request may be made and a control query may be performed on the local clock. The local clock can also be synchronized to a remote server.
2. Server: This indicates that a time request may be made and a control query may be performed on the local clock. The local clock cannot be synchronized to a remote server.
3. Synchronization: This indicates that time requests are made only on the local clock.
4. Query: This indicates that control queries are performed only on the local clock.
5. Limited: When the rate of NTP packets exceeds the upper limit, incoming NTP packets are discarded. If the Kiss-of-Death (KOD) function is enabled, a kiss code is sent.


#### KOD

The KOD function can be enabled on the server to perform access control. This is useful if the volume of packets received from clients may overload a server's loadbearing capabilities within a specified period. KOD is a modern access control technology implemented in NTPv4 and is used by the server to provide information, such as status reports and access control, to the client.

A KOD packet is a special type of NTP packet. In a KOD packet, the stratum field is 0. KOD packets support two types of kiss codes: DENY and RATE.

With the KOD function enabled on a server, the server sends kiss code DENY or RATE to the client based on configuration.

* When receiving the kiss code DENY, the client terminates all connections to the server, and stops sending packets to the server.
* When receiving the kiss code RATE, the client immediately reduces its polling interval to the server. The client will continue to reduce the interval if it receives subsequent RATE kiss codes.

After the KOD function is enabled, the corresponding ACL rule needs to be configured. When the ACL rule is configured as deny, the server sends the kiss code DENY. When the ACL rule is configured as permit and the number of NTP packets received reaches the configured upper limit, the server sends the RATE kiss code.