Overview of DHCPv6
==================

Dynamic Host Configuration Protocol for IPv6 (DHCPv6) is a stateful protocol that assigns IPv6 addresses or prefixes and other configuration parameters to hosts.

#### Introduction

IPv6 has made it possible to have virtually unlimited IP addresses by increasing the IP address length from 32 bits to 128 bits. This increase in IP address length requires efficient IPv6 address space management and assignment.

IPv6 provides the following address allocation modes:

* Manual configuration. IPv6 addresses/prefixes and other network configuration parameters are manually configured, such as the DNS server address, network information service (NIS) server address, and Simple Network Time Protocol (SNTP) server address.
* Stateless address allocation. A host uses the prefix carried in a received Router Advertisement (RA) message and the local interface ID to automatically generate an IPv6 address.
* Stateful address autoconfiguration using DHCPv6. DHCPv6 address allocation can be implemented in any of the following modes:
  + A DHCPv6 server automatically configures IPv6 addresses/prefixes and other network configuration parameters, such as the DNS server address, NIS server address, and SNTP server address.
  + A host uses the prefix carried in a received RA message and the local interface ID to automatically generate an IPv6 address. The DHCPv6 server assigns configuration parameters other than IPv6 addresses, such as the DNS server address, NIS server address, and SNTP server address.
  + DHCPv6 Prefix Delegation (PD). IPv6 prefixes do not need to be manually configured for the downstream routers. The DHCPv6 prefix delegation mechanism allows a downstream router to send DHCPv6 messages carrying the IA\_PD option to an upstream router to apply for IPv6 prefixes. After the upstream router assigns a prefix that has less than 64 bits to the downstream router, the downstream router automatically subnets the delegated prefix into /64 prefixes and assigns the /64 prefixes to the links attached to IPv6 hosts through RA messages. This mechanism implements automatic configuration of IPv6 addresses for IPv6 hosts and hierarchical IPv6 prefix delegation.