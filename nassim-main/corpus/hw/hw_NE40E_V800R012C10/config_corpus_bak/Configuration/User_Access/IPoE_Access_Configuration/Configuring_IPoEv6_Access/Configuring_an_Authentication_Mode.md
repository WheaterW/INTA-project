Configuring an Authentication Mode
==================================

This section describes several authentication modes. Configure an authentication mode based on networking requirements.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The same authentication mode (for example, binding authentication or web authentication) must be configured for the IPv4 and IPv6 services of a dual-stack user.

One or more of the following modes can be configured for access authentication.

* Web authentication or fast authentication
  
  If an IPv6 user requests to access the Internet, a web server needs to provide IPv6 Hypertext Transfer Protocol (HTTP) services to allow the user to access the web server by entering a username and a password for authentication. The web server extracts user information such as the source IPv6 address, username, and password from an IPv6 HTTP packet and encapsulates the information into a portal packet. Then, the web server sends the portal packet to the NE40E for authentication. The NE40E needs to extract authentication information from the portal protocol packet and confirm the user to be authenticated based on the IPv6 address.
  
  If an IPv4/IPv6 dual-stack user requests to access the Internet, the user can still use the IPv4 address for web authentication. If the authentication is successful, the user can access the Internet using either the IPv4 or IPv6 address. Therefore, the web server does not need to be upgraded.
* Web+MAC authentication
* Binding authentication
  
  DHCPv4 options are used for binding authentication on an IPv4 network. If the network transitions to an IPv6 network, using DHCPv6 to assign IPv6 addresses is recommended. Authentication information can be added to DHCPv6 options. This ensures that the same authentication information is encapsulated into the respective options after IPv4-IPv6 transition.

#### Procedure

* Web authentication or fast authenticationFor configuration details, see [Configuring Web Authentication or Fast Authentication](dc_ne_ipox_cfg_0037.html).
* Binding authenticationFor configuration details, see [Configuring Binding Authentication](dc_ne_ipox_cfg_0005.html).