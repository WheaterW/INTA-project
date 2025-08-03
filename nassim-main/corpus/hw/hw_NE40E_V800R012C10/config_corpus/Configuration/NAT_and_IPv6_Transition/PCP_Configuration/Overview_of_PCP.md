Overview of PCP
===============

This section describes the basic Port Control Protocol (PCP) concepts, PCP usage scenarios, and the features that a Carrier Grade NAT (CGN) device functioning as a PCP server supports.

PCP establishes PCP connections between customer premises equipment (CPE) and CGN devices to implement point-to-point (P2P) applications between terminal users accessing different CGN devices. PCP is used in Network Address Translation (NAT444) and Dual-Stack Lite (DS-Lite) scenarios. In a PCP application, a CGN device functions as a PCP server, and a CPE functions as a PCP client. The CGN devices assign public IP addresses and port numbers to the users on the CPEs. A P2P server uses the public IP addresses and port numbers to establish P2P connections between terminal users so that the users connected to the CGN devices can access P2P services, such as teleconferences, online games, and P2P data transmission.

#### PCP Usage Scenario

During the IPv4-to-IPv6 transition, carriers use transition techniques, such as NAT444 and DS-Lite, to translate between public and private address realms. If symmetric NAT (5-tuple mode) is used, two terminal users on different internal networks (in private address realms) are difficult to communicate, which fails to meet the basic P2P application requirement for node communication. A CGN device connected to a terminal user rejects any session request initiated by the terminal user connected to the other CGN device, hindering the P2P communication between the terminal users on different private networks.

To allow P2P communication, a CGN device must run PCP. The CGN device responds the PCP connection request sent by a CPE. A listening port is started on the CGN device to forward traffic. PCP helps improve P2P traffic bandwidth and improve P2P user experience.


#### PCP Deployment

PCP can be deployed in the integrated and centralized NAT444 and DS-Lite scenarios. PCP can be smoothly implemented without changes in the existing IPv4-to-IPv6 transition infrastructure or service deployment.![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a CGN device (PCP server) has the internal server function enabled, in addition to the PCP function, the CGN device uses the NAT mappings contained in NAT server entries, without generating NAT mappings.




#### Setting a PCP Server Address

A CGN device (PCP server) must be assigned an IP address so that a CPE (PCP client) can send a request to establish a PCP connection to the CGN device.

* In a centralized NAT444 or DS-Lite scenario, a CGN device deployed on a core router (CR) or service router (SR) cannot provide user access or authentication services. A PCP server address must be statically configured on the CPE and CGN device.
* In a distributed NAT444 or DS-Lite scenario, a CGN device deployed on a BRAS provides user access or authentication services. In addition to a manually configured PCP server address, an address can be assigned to the PCP server on the CPE in either of the following modes:
  + The CGN device, functioning as a DHCP server, encapsulates a PCP server name into a DHCP Option field and then responds to a PCP server name request sent by a user on a CPE.
  + A RADIUS server delivers the hw-pcp-server-name value (a PCP server name) in an Access-Accept packet to the DHCP server, which is the CGN device. The CGN device encapsulates the PCP server name in a specified DHCP Option field and then sends the PCP server name to the user on a CPE.

#### PCP Public Address and Port Allocation

A CGN device allocates the following public network resources to each user on CPE:

* One public IP address and one public port number if a PCP request packet received by the CGN device carries no Port Reservation Option field.
* One public IP address and two consecutive public port numbers if a PCP request packet carries the Port Reservation Option field. If two consecutive public port numbers are unavailable, the CGN device allocates only one port number to the user and informs the CPE that the other port number fails to be allocated.

A PCP request originating from a CPE carries a private IP address and port number and a recommended public IP address and port number.

* If the request does not contain a PREFER\_FAILURE Option field, the CGN device allocates the recommended public IP address and port number. If the recommended public IP address and port number are unavailable, the CGN device allocates another public IP address and port number.
* If the request contains a PREFER\_FAILURE Option field, the CGN device (PCP server) allocates the recommended public IP address and port number.
  + By default, if the recommended public IP address and port number have been allocated or are unavailable, the CGN device returns the error code CANNOT\_PROVIDE\_EXTERNAL to the CPE. Upon receipt, the CPE has to resend a PCP request to obtain public network resources.
  + In a P2P application, after PCP port reservation is enabled, the CGN device can reserve a range of ports used in PCP mapping for the PCE. If a port carried in a PCP request sent by a PCE is not in a port range to be allocated, the CGN device allocates a port within the reserved port range, increasing the P2P connection success rate.

#### Setting a PCP Connection Lifetime

If a user on a piece of CPE maliciously establishes a large number of PCP connections to a CGN device, public network resources are wasted. To prevent this problem, the CGN device must be able to tear down the PCP connections to reclaim resources after the specific PCP connection lifetime elapses.

By default, the minimum lifetime is 120 seconds, and the maximum lifetime is 40000 seconds. You can set the minimum and maximum lifetime values based on the network traffic volume and the number of allowable PCP connections and public network resources on the CGN device.