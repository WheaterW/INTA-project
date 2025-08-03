DHCPv6 Server Allowing a DHCPv6 Client to Renew the Address Lease
=================================================================

IPv6 addresses that are dynamically allocated by a DHCPv6 server have leases. A message from a DHCPv6 client can carry an expected lease. When allocating network parameters, the DHCPv6 server compares the expected lease with the specified lease in the address pool and allocates an IPv6 address with a shorter lease to the DHCPv6 client. When the lease expires, the server reclaims the IPv6 address, which can then be allocated to other clients. This mechanism improves IPv6 address utilization. When the lease is about to expire, if the DHCPv6 client wants to continue using the IPv6 address, it needs to renew the lease of the IPv6 address.

The following describes how a DHCPv6 client renews its IPv6 address lease when a DHCPv6 relay agent exists or not.

#### DHCPv6 Server Allowing a DHCPv6 Client to Renew the Address Lease When No DHCPv6 Relay Agent Exists

**Figure 1** DHCPv6 server allowing a DHCPv6 client to renew the address lease when no DHCPv6 relay agent exists  
![](figure/en-us_image_0000001564130517.png)

1. When the lease reaches T1 (50% of the lifetime by default), the DHCPv6 client automatically unicasts a Renew message carrying the DUID of the DHCPv6 server that has allocated an IPv6 address to it to renew the lease.
2. After receiving the Renew message, the server checks the IPv6 address in the message. If the check is successful, the server sends a Reply message carrying the new lifetime, T1', and T2' of the address to the client.
3. If the client receives the Reply message, the lease is successfully renewed (counted from 0). If the client does not receive the Reply message when T2 (80% of the lifetime by default) expires, it automatically multicasts a Rebind message to all DHCPv6 servers on the same link to request IPv6 address lease renewal.
4. After receiving the Rebind message, the server checks the DUID of the DHCPv6 server carried in the message.
   * If the DUID carried in the message is not the local one, the server does not respond to the Rebind message.
   * If the DUID carried in the message is the local one, the server checks the IPv6 address in the message. If the check is successful, the server sends a Reply message carrying the new lifetime, T1', and T2' of the address to the client.

If the DHCPv6 client receives the Reply message from the DHCPv6 server, the lease is successfully renewed (counted from 0). If the DHCPv6 client does not receive the Reply message, it stops using the IPv6 address and resends a Solicit message to request a new IPv6 address when the valid lifetime expires.


#### DHCPv6 Server Allowing a DHCPv6 Client to Renew the Address Lease When a DHCPv6 Relay Agent Exists

**Figure 2** DHCPv6 server allowing a DHCPv6 client to renew the address lease when a DHCPv6 relay agent exists  
![](figure/en-us_image_0000001512691282.png)

1. When the lease reaches T1 (50% of the lifetime by default), the DHCPv6 client automatically unicasts a Renew message carrying the DUID of the DHCPv6 server that has allocated an IPv6 address to it to renew the lease.
2. After receiving the Renew message, the server checks the IPv6 address in the message. If the check is successful, the server sends a Reply message carrying the new lifetime, T1', and T2' of the address to the client.
3. If the client receives the Reply message, the lease is successfully renewed (counted from 0). If the client does not receive the Reply message when T2 (80% of the lifetime by default) expires, it automatically multicasts a Rebind message to the DHCPv6 relay agent. The relay agent then unicasts a Relay-forward message to the DHCPv6 server to request an IPv6 address lease renewal. For details on how the DHCPv6 relay agent processes messages, see [DHCPv6 Server Allocating Addresses and Network Configuration Parameters to Newly Connected DHCPv6 Clients When a DHCPv6 Relay Agent Exists](galaxy_dhcpv6_cfg_0007.html#EN-US_CONCEPT_0000001563770737__section_relay).
4. After receiving the Relay-forward message, the server checks the corresponding IPv6 address. If the check is successful, the server sends a Relay-reply message carrying the new lifetime, T1', and T2' of the address to the DHCPv6 relay agent. After receiving the Relay-reply message, the relay agent parses the message to obtain the new lifetime, T1', and T2', and then sends them to the DHCPv6 client through a Reply message.

If the DHCPv6 client receives the Reply message from the relay agent, the lease is successfully renewed (counted from 0). If the DHCPv6 client does not receive the Reply message, it stops using the IPv6 address and resends a Solicit message to request a new IPv6 address when the valid lifetime expires.