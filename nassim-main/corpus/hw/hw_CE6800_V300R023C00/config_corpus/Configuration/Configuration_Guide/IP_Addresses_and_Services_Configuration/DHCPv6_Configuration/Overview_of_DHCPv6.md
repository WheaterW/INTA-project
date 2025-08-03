Overview of DHCPv6
==================

Overview of DHCPv6

#### Definition

Dynamic Host Configuration Protocol for IPv6 (DHCPv6) is a stateful protocol that assigns IPv6 addresses or prefixes and other configuration parameters to hosts.


#### Purpose

Because of the large address space offered by 128-bit IPv6 addresses, it is necessary to use automatic address allocation and management policies. One common mechanism is IPv6 stateless address autoconfiguration. With this mechanism, hosts automatically configure IPv6 addresses based on prefixes carried in router advertisement (RA) messages after IPv6 route advertisement is enabled on a neighboring gateway.

When stateless address autoconfiguration is used, a gateway does not record the addresses of IPv6 hosts connected to it, resulting in poor manageability. In addition, IPv6 hosts cannot obtain configuration parameters such as the DNS server IPv6 address, resulting in poor availability. Internet service providers (ISPs) do not provide instructions for automatic allocation of IPv6 prefixes. Therefore, IPv6 address prefixes must be manually configured during IPv6 network deployment.

To address this issue, DHCPv6 is introduced. Compared with other IPv6 address allocation modes (such as manual configuration and stateless address autoconfiguration based on prefixes in RA messages), DHCPv6 is a stateful address autoconfiguration protocol and provides the following functions:

* Controls IPv6 address allocation more effectively. DHCPv6 records the IPv6 addresses that have been allocated and allocates available IPv6 addresses to hosts based on certain rules, facilitating network management.
* Allocates IPv6 address prefixes to network devices, facilitating network-wide automatic configuration and hierarchical management.
* Provides other network configuration parameters such as the DNS server IPv6 address.