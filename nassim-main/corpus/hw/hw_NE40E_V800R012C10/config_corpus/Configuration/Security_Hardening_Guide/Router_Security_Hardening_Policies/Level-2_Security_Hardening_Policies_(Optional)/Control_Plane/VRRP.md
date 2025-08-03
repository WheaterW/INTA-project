VRRP
====

VRRP

#### Security Policy

* Protocol security policies:
  + Authentication mode: VRRP supports none authentication, simple authentication (applicable only to multicast VRRP), enhanced HMAC-MD5 authentication, and enhanced HMAC-SHA256 authentication (applicable only to unicast VRRP).
  + Packet check: VRRP checks the VRRP group ID, checksum, TTL, version number, packet type, timer, number of virtual addresses, virtual address, and packet length.
* System security policies:
  
  Attack packet suppression: If a device receives more than 20 packets within a specified period of time or receives packets sent from the device itself, the device discards the packets.

#### Attack Methods

* A large number of valid VRRP packets are sent within a period of time to attack a device.
* VRRP packets that do not meet packet check requirements in a VRRP security policy are constructed to attack a device.

#### Configuration and Maintenance Methods

* Authentication mode: VRRP supports none authentication, simple authentication (applicable only to multicast VRRP), HMAC-MD5 authentication, and HMAC-SHA256 authentication (applicable only to unicast VRRP). In simple authentication, a password can be saved in simple text or ciphertext. In HMAC-MD5 authentication and HMAC-SHA256 authentication, a password is saved in ciphertext by default.
* Packet check: This function is supported by default and requires no additional configuration.

#### Configuration and Maintenance Suggestions

Authentication mode: To enhance protocol security, HMAC-MD5 authentication is recommended for non-unicast VRRP, and HMAC-SHA256 authentication is recommended for unicast VRRP.


#### Verifying the Security Hardening Result

Run the **display vrrp**  [ **interface** { **interface-nam*e* | *interface-type* *interface-number* } ] [ *virtual-id* ] **verbose** command to check the authentication configuration of VRRP packets.