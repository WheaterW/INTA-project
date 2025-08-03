Understanding OSPFv3 Authentication
===================================

Understanding OSPFv3 Authentication

#### OSPFv3 Authentication Modes

OSPFv3 authentication encrypts OSPFv3 packets by adding authentication information to IPv6 headers of the OSPFv3 packets to ensure network security. When receiving an OSPFv3 packet from a remote device, the local device discards it if the authentication password carried in the packet is different from the local one, protecting the local device against potential attacks.

In terms of packet type, OSPFv3 authentication is classified as follows:

* Area authentication
  
  This authentication mode is configured in the OSPFv3 area view and applies to packets received by all interfaces in the OSPFv3 area.
* Process authentication
  
  This authentication mode is configured in the OSPFv3 view and applies to all packets in the OSPFv3 process.
* Interface authentication
  
  This authentication mode is configured in the interface view and applies to all packets received by the interface.

OSPFv3 uses HMAC-SHA256 or HMAC-SM3 to authenticate packets. In HMAC-SHA256 authentication, a configured password is hashed using the HMAC-SHA256 algorithm, and the ciphertext password is added to packets for authentication. This authentication mode improves password security.

OSPFv3 carries authentication types in packet headers and authentication information in packet trailers.

The authentication types are as follows:

* 1: simple authentication
* 2: ciphertext authentication

#### Application Scenario of OSPFv3 Authentication

**Figure 1** OSPFv3 authentication on a broadcast network  
![](figure/en-us_image_0000001176662847.png)

The configuration requirements are as follows:

* The interface authentication configurations must be the same on all devices on the same network so that OSPFv3 neighbor relationships can be established.
* Configurations of the area authentication parameters must be the same on all devices in the same area.