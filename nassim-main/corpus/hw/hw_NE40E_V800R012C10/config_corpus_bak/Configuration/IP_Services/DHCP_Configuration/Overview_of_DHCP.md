Overview of DHCP
================

DHCP enables a client to dynamically obtain a valid IP address from a server.

#### Introduction

The Dynamic Host Configuration Protocol (DHCP) dynamically assigns IP addresses to hosts and centrally manages host configurations. DHCP uses the client/server model. A client applies to the server for configuration parameters (such as an IP address), and the server replies with the requested configuration parameters.

The DHCP architecture involves the following roles:

* DHCP client: obtains an IP address and other network configuration parameters by exchanging DHCP messages with the DHCP server. After the DHCP client function is configured on an interface, the interface can function as a DHCP client to dynamically obtain parameters such as an IP address from the DHCP server. This facilitates configuration and centralized management.
* DHCP relay agent: relays DHCP messages between the DHCP client and server to help the client configure its address. If a DHCP client and server reside on different network segments, a DHCP relay agent must be used to forward DHCP messages between the client and server. DHCP relay allows a single DHCP server to serve DHCP clients on different network segments, reducing costs and facilitating centralized management.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The DHCP relay agent is optional in the DHCP architecture. It is required only when the DHCP client and server are on different network segments.
* DHCP server: processes requests for address allocation, address renewal, and address release from the DHCP client or DHCP relay agent, and allocates an IP address and other network configuration parameters to the DHCP client.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To protect a DHCP server against network attacks, such as man-in-the-middle attacks, starvation attacks, and DoS attacks by changing the CHADDR value, configure DHCP snooping on the intermediate device directly connected to a DHCP client. This provides security services for DHCP.