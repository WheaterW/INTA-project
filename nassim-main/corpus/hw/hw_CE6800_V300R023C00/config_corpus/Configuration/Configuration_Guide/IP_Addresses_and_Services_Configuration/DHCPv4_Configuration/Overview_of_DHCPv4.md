Overview of DHCPv4
==================

Overview of DHCPv4

#### Definition

The Dynamic Host Configuration Protocol (DHCP) dynamically configures and uniformly manages IPv4 addresses of hosts. To distinguish from the Dynamic Host Configuration Protocol for IPv6 (DHCPv6), use DHCPv4 in the following sections.

DHCPv4 is defined in RFC 2131 and uses the client/server communication model. A DHCPv4 client requests configuration information from a DHCPv4 server, and the server returns the configuration information allocated to the client.

DHCPv4 supports dynamic and static IPv4 address allocation. Network administrators can use either of the two mechanisms to allocate IPv4 addresses to hosts based on network requirements.

* Dynamic allocation: DHCPv4 allocates an IPv4 address with a limited validity period (known as a lease) to a client.
  
  This mechanism applies to scenarios where hosts temporarily access the network and the number of idle IPv4 addresses is less than the total number of hosts.
* Static allocation: Network administrators use DHCPv4 to allocate fixed IPv4 addresses to specified hosts.
  
  Compared with manual IPv4 address configuration, DHCPv4 static allocation prevents manual configuration errors and helps network administrators perform unified maintenance and management.

#### Purpose

As networks expand and become more complex, network configurations also become more complex. In addition, a sharp increase in computers and their location changes cause IPv4 addresses to frequently change and become insufficient. To properly and dynamically allocate IPv4 addresses to hosts, DHCPv4 is used.

DHCPv4 is developed based on the Bootstrap Protocol (BOOTP) which runs in a static environment where each host has a fixed network connection. For each host using BOOTP, an administrator must configure a specific BOOTP parameter file that keeps unchanged in a long period. DHCPv4 is an extension of BOOTP by:

* Dynamically allocating an IPv4 address to each host, instead of specifying an IPv4 address for each host.
* Allocating other configuration parameters, such as the boot file of a client, so that the client can obtain all the required configuration information by using only one message.

DHCPv4 properly and dynamically allocates IPv4 addresses, which improves IPv4 address utilization and prevents the waste of IPv4 addresses. It simplifies network deployment and scale-out, even for small networks.


#### Benefits

DHCPv4 offers the following benefits:

* Reduced client configuration and maintenance costs
  
  DHCPv4 is easy to configure and deploy. For non-technical users, DHCPv4 minimizes configuration-related operations on clients and reduces remote deployment and maintenance costs.
* Centralized management
  
  A DHCPv4 server can manage the configurations of multiple network segments. When the configuration of a network segment changes, an administrator only needs to update the corresponding configuration on the DHCPv4 server.