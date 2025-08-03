Configuring NTP Security Mechanisms
===================================

This section describes how to ensure the security of NTP sessions through NTP security mechanisms.

#### Usage Scenario

NTP supports two security mechanisms: access authority and NTP authentication.

* Access authority
  
  Access authority is a type of simple security method provided by the NE40E to protect local NTP services.
* NTP authentication
  
  NTP authentication is required in some networks with high security demands.
  
  The configuration of NTP authentication involves configuring NTP authentication on both, the client and the server.
  
  During the configuration of NTP authentication, pay attention to the following rules:
  
  + Configure NTP authentication on both the client and the server. Otherwise, the authentication does not take effect.
  + If NTP authentication is enabled, a reliable key needs to be configured at the client side.
  + The authentication key configured on the server and that on the client must be consistent.
  + In NTP peer mode, the symmetric active end equals the client, and the symmetric passive end equals the server.

#### Pre-configuration Tasks

Before configuring NTP security mechanisms, complete the following tasks:

* Configure the link layer protocol for the interface.
* Configure the link layer protocol and routing protocol to make the server and client reachable.
* Configure ACL rules if the access authority is configured.


[Setting NTP Access Rights](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0013.html)

When receiving an access request packet, the NTP server matches the request packet with the access right in descending order (from peer, server, synchronization, query to limited). The first matched right takes effect.

[Enabling NTP Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0014.html)

Both the NTP server and the NTP client must be enabled with NTP authentication and configured with the same authentication key, and the authentication key must be declared as reliable on the client side. Otherwise, NTP authentication will fail.

[(Optional) Configuring NTP Authentication in Unicast Server/Client Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0016.html)

By configuring the authentication key ID used in the synchronization with the specific NTP server on the NTP client, you can apply NTP authentication in client/server mode. Perform the following steps on the NTP unicast client.

[(Optional) Configuring NTP Authentication in Peer Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0017.html)

By configuring the authentication key ID used in the synchronization with the peer on the local end, you can apply NTP authentication in peer mode. Perform the following steps on the symmetric active end.

[(Optional) Configuring NTP Authentication in Broadcast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0018.html)

After NTP authentication is enabled, you can configure the authentication key ID used in synchronization with the NTP broadcast server on the local Router to apply NTP authentication in broadcast mode. Perform the following steps on the NTP broadcast server.

[(Optional) Configuring NTP Authentication in Multicast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0019.html)

By configuring the authentication key ID used in the synchronization with the NTP multicast server on the local Router, you can apply NTP authentication in multicast mode. Perform the following steps on the NTP multicast server. 

[(Optional) Configuring NTP Authentication in Manycast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0036.html)

By configuring the authentication key ID used in the synchronization with the NTP manycast client on the local Router, you can apply NTP authentication in manycast mode.

[Verifying the NTP Security Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0020.html)

After configuring NTP security mechanisms, check details about the status of the NTP service and the status of NTP sessions.