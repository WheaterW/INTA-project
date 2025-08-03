Basic DHCPv6 Concepts
=====================

Basic DHCPv6 Concepts

#### IPv6 Address Allocation Methods

Currently, the following methods are available to allocate IPv6 addresses:

* Manual configuration. IPv6 addresses/prefixes and other network configuration parameters are manually configured, such as the DNS, network information service (NIS), and Simple Network Time Protocol (SNTP) server addresses.
* Stateless address autoconfiguration. Hosts generate link-local addresses based on interface IDs and automatically configure IPv6 addresses based on prefixes carried in RA messages.
* Stateful address autoconfiguration using DHCPv6. DHCPv6 involves the following scenarios:
  + DHCPv6 stateful address autoconfiguration. A DHCPv6 server automatically allocates IPv6 addresses/prefixes and other network configuration parameters, such as the DNS, NIS, and SNTP server addresses.
  + DHCPv6 stateless address autoconfiguration. Host IPv6 addresses are automatically generated through RA messages. A DHCPv6 server allocates other configuration parameters such as the DNS, NIS, and SNTP server addresses except for IPv6 addresses.

#### DHCPv6 Architecture

[Figure 1](#EN-US_CONCEPT_0000001513170394__fig_dc_fd_dhcpv6_000401) shows the DHCPv6 architecture, which consists of the following three roles.

**Figure 1** DHCPv6 architecture  
![](figure/en-us_image_0000001564010677.png)

* **DHCPv6 client**
  
  A DHCPv6 client applies to a DHCPv6 server for IPv6 addresses/prefixes and other network configuration parameters to configure its address.
* **DHCPv6 server**
  
  A DHCPv6 server processes requests for address allocation, lease extension, and release from a DHCPv6 client or a DHCPv6 relay agent, and allocates IPv6 addresses/prefixes and other network configuration parameters to the client.
* **DHCPv6 relay agent**
  
  A DHCPv6 relay agent relays DHCPv6 messages between a DHCPv6 client and server to help the client configure its address. If a DHCPv6 client and server reside on the same link, the client uses a link-local multicast address to obtain an IPv6 address/prefix and other configuration parameters from the server. If a DHCPv6 client and server reside on different links, a DHCPv6 relay agent must be used to forward DHCPv6 messages between the client and server. DHCPv6 relay allows a single DHCPv6 server to serve DHCPv6 clients on different links, reducing costs and facilitating centralized management.

DHCPv6 also provides the DHCPv6 prefix delegation (PD) mechanism, which is used for prefix allocation. For details, see RFC 3633. [Figure 2](#EN-US_CONCEPT_0000001513170394__fig_dc_fd_dhcpv6_000701) shows the DHCPv6 PD architecture. In addition to a DHCPv6 relay agent, DHCPv6 PD involves the following two roles.

**Figure 2** DHCPv6 PD architecture

![](figure/en-us_image_0000001564130509.png)

* **DHCPv6 PD client**
  
  A DHCPv6 PD client interacts with a DHCPv6 PD server to obtain an IPv6 address prefix. The client then divides the obtained prefix (which is typically less than 64 bits long) into subnet segments with 64-bit prefixes and advertises the subnet segments to the user link directly connected to the IPv6 hosts through RA messages. In this way, the IPv6 hosts automatically configure addresses.
* **DHCPv6 PD server**
  
  A DHCPv6 PD server processes prefix allocation requests from a DHCPv6 PD client or relay agent and allocates an IPv6 prefix to the client.

#### DHCPv6 Unique Identifier

Each DHCPv6 server or client has a unique DHCPv6 unique identifier (DUID). A DHCPv6 server uses DUIDs to identify DHCPv6 clients, and a DHCPv6 client uses DUIDs to identify DHCPv6 servers.

The DUIDs of a DHCPv6 client and server are carried in the Client Identifier and Server Identifier options, respectively. The two options have the same format and are distinguished by the option-code field value.


#### Identity Association

An identity association (IA) enables a DHCPv6 server and client to identify, group, and manage IPv6 addresses. Each IA consists of an identity association identifier (IAID) and associated configuration information.

A DHCPv6 client must associate at least one IA with each of its interfaces for which the client requests IPv6 addresses from a DHCPv6 server. The client uses the IAs associated with the interfaces to obtain configuration information from the server. Each IA must be associated with at least one interface.

An IAID identifies an IA and must be unique on a DHCPv6 client. IAIDs are not lost or changed because of factors such as a device restart.

In an IA, the configuration information consists of one or more IPv6 addresses along with the lifetimes T1 and T2. Each address in an IA has a preferred lifetime and a valid lifetime.


#### Multicast Addresses Used by DHCPv6

In DHCPv4, a DHCPv4 client locates DHCPv4 servers by broadcasting DHCPv4 messages. To prevent broadcast storms, IPv6 uses multicast messages instead of broadcast messages. DHCPv6 uses the following two multicast addresses:

* FF02::1:2: multicast address of all DHCPv6 servers and relay agents. The address is a link-local multicast address and is used for communication between a DHCPv6 client and its neighboring servers or between a DHCPv6 client and DHCPv6 relay agents. All DHCPv6 servers and relay agents are members of the multicast group corresponding to this multicast address.
* FF05::1:3: multicast address of all DHCPv6 servers. The address is a site-local address and is used for communication between DHCPv6 relay agents and servers within a site. All DHCPv6 servers within a site are members of this multicast group.


#### UDP Port Numbers Used by DHCPv6

DHCPv6 messages are carried over UDPv6. The UDP port number that a DHCPv6 client listens to is 546, whereas a DHCPv6 server and relay agent listen to 547.