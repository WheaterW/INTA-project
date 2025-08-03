Configuring a Global Address Pool
=================================

Configuring a Global Address Pool

#### Context

An address pool is a collection of IPv4 addresses that a DHCPv4 server can assign to clients. In addition to IPv4 addresses, network parameters such as the lease, subnet mask, and default gateway can be configured in the address pool. When the DHCPv4 server assigns IPv4 addresses to clients, these network parameters are also assigned to them.

A global address pool is an address pool created in the system view for a specified network segment. Addresses in the global address pool can be assigned to clients connected to all interfaces of the device. If a DHCPv4 server and client are located on different network segments, a DHCPv4 relay agent needs to be deployed.

A DHCPv4 server selects an address pool based on whether a DHCPv4 relay agent is deployed. If no DHCPv4 relay agent is deployed, the DHCPv4 server selects an address pool that is on the same network segment as the IPv4 address of the interface that receives DHCPv4 request messages. If a DHCPv4 relay agent is deployed, the DHCPv4 server selects an address pool that is on the same network segment as the IPv4 address specified in the giaddr field of received DHCPv4 request messages.

You need to determine the number of IPv4 addresses to be deployed in the address pool based on the number of clients and the time and frequency of connection and disconnection.

IPv4 addresses in an address pool can be classified by their usage as follows:

* **Used**: indicates that the IPv4 address has been used.
* **Idle**: indicates that the IPv4 address is idle.
* **Static-bind**: indicates that the IPv4 address has been bound to a MAC address and is not in use.
* **Static-bind used**: indicates that the IPv4 address has been bound to a MAC address and used.
* **Disable**: indicates that the IPv4 address cannot be used.
* **Expired**: indicates that the lease of the IPv4 address has expired and the IPv4 address is idle.
  
  After an IPv4 address in the address pool expires, it enters the Expired state. The records of allocating IPv4 addresses in the Expired state are retained in the address pool. This allows the original IPv4 address to be allocated to a user, ensuring IPv4 address stability.
  
  When IPv4 addresses in the Idle state in the address pool are exhausted, the address pool automatically reclaims the IPv4 addresses in the Expired state and allocates them to new users.
* **Conflict**: indicates that the IPv4 address conflicts with another one on the network.Setting an IPv4 address to the Conflict state can prevent an IPv4 address conflict. An IPv4 address in the Conflict state exists in either of the following situations:
  + After receiving a DHCPDISCOVER message from a client, a DHCPv4 server pings an IPv4 address before allocating the IPv4 address. If the ping operation succeeds, the DHCPv4 server sets the IPv4 address to the Conflict state and allocates another IPv4 address to the client.
  + After receiving a DHCPDECLINE message, a DHCPv4 server checks whether the corresponding IPv4 address has lease information. If the address has lease information (for example, the address is in the Used or Expired state), the server sets it to the Conflict state.
    
    For example, after obtaining an IPv4 address, a DHCPv4 client immediately sends a gratuitous ARP packet. If the client receives a response, it sends a DHCPDECLINE message to notify the DHCPv4 server of the IPv4 address conflict. The DHCPv4 server sets the IPv4 address to the Conflict state, and the client sends a DHCPDISCOVER message to apply for an IPv4 address again.
  
  When IPv4 addresses in the Idle and Expired states in the address pool are exhausted, the address pool automatically reclaims the IPv4 addresses in the Conflict state and allocates them to new users. An IPv4 address in the Conflict state cannot be allocated within 1 minute.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a global address pool and enter its view.
   
   
   ```
   [ip pool](cmdqueryname=ip+pool) pool-name
   ```
   
   By default, no global address pool is created on a device.
3. Configure the range of IPv4 addresses that can be dynamically allocated in the global address pool.
   
   
   ```
   [network](cmdqueryname=network) ip-address [ mask { mask | mask-length } ]
   ```
   
   By default, the range of IPv4 addresses that can be dynamically allocated is not configured.
4. (Optional) Configure functions for the global address pool as required.
   
   
   
   **Table 1** Configuring optional functions for the global address pool
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a VPN instance for the address pool. | [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* | In normal cases, IPv4 addresses in an address pool can be allocated to clients only on a network segment to prevent IPv4 address conflicts. If clients in different VPNs apply to the same DHCPv4 server for IPv4 addresses, perform this step to use the same address pool to allocate IPv4 addresses on the same network segment to the clients.  By default, no VPN instance is configured for an address pool. |
   | Configure an IPv4 address segment in the global address pool. | [**section**](cmdqueryname=section) *section-id* *start-address* [ *end-address* ] | A global address pool consists of one or more IPv4 address segments. The IPv4 addresses in each address segment cannot overlap.  The address segment configured using the [**section**](cmdqueryname=section) command in the IP address pool view must be within the address range configured using the [**network**](cmdqueryname=network) command in the IP address pool view.  By default, no IPv4 address segment is configured in an address pool. |
   | Configure IPv4 addresses that cannot be automatically allocated to clients from the address pool. | [**excluded-ip-address**](cmdqueryname=excluded-ip-address) *start-ip-address* [ *end-ip-address* ] | To configure multiple IPv4 addresses that cannot be automatically allocated to clients from the address pool, run this command multiple times.  You do not need to exclude the gateway address configured using the [**gateway-list**](cmdqueryname=gateway-list) command, because the device automatically adds it to the list of IPv4 addresses that cannot be automatically allocated.  You do not need to exclude the IPv4 address of the server's interface connected to a client, because the device automatically sets it to the Conflict state during address allocation.  By default, all IPv4 addresses in an address pool can be automatically allocated. |
   | Configure a fixed IPv4 address allocated to a specified client. | [**static-bind**](cmdqueryname=static-bind) **ip-address** *ip-address* **mac-address** *mac-address* [ **description** *description* ] | Ensure that the bound IPv4 address is not set to an IPv4 address that cannot be allocated.  The occupied IPv4 addresses can also be statically bound or unbound. When statically binding an IPv4 address to a MAC address, ensure that the MAC address to be bound is the same as the MAC address of the user who uses the IPv4 address.  After a static binding is configured for a dynamically allocated IPv4 address, the lease becomes infinite. After the static binding is deleted, the lease is the same as that configured in the address pool.  By default, no IP address in an address pool is bound to any MAC address. |
   | Configure the function of reserving IPv4 address allocation records. | [**reserved ip-address mac**](cmdqueryname=reserved+ip-address+mac) | After this function is configured, the IPv4 address of a user is set to the Expired state after the user goes offline. In addition, the device reserves the IPv4 address allocation record based on the MAC address of the user. When the user goes online again, the device preferentially allocates this IPv4 address to the user.  By default, a device reserves IPv4 address allocation records. |
   | Change an address lease. | [**lease**](cmdqueryname=lease) { **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | **unlimited** } | After the lease of IPv4 addresses in the address pool is changed, the newly allocated IPv4 addresses use the new lease. The IPv4 addresses that have been allocated before the change still use the original lease before the lease is renewed. After the lease is renewed, these IPv4 addresses use the new lease.  A BOOTP client does not support Option 51 (IPv4 address lease option). The lease of an IPv4 address allocated to a BOOTP client is infinite, and the DHCPv4 server does not reclaim the IPv4 address.  The fixed IPv4 address allocated to a specified client can be used permanently and is not restricted by the lease.  By default, the lease of IPv4 addresses in an interface address pool is one day. |
   | Configure the device to automatically reclaim conflicting IPv4 addresses in the address pool. | [**conflict auto-recycle interval**](cmdqueryname=conflict+auto-recycle+interval) **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | The DHCPv4 server selects available IPv4 addresses from the conflicting addresses for allocation only after all available addresses are allocated. You can configure the function of automatically reclaiming conflicting IPv4 addresses and set an automatic reclaiming interval, quickly reclaiming the conflicting IPv4 addresses.  By default, a device is disabled from automatically reclaiming conflicting IPv4 addresses in an address pool. |
   | Configure an address exhaustion alarm percentage and alarm clearing percentage for the address pool. | [**alarm ip-used percentage**](cmdqueryname=alarm+ip-used+percentage) *alarm-resume-percentage* *alarm-percentage* | The alarm clearing percentage must be less than the alarm percentage.  The default address exhaustion alarm percentage and alarm clearing percentage are 100% and 50%, respectively. |
   | Configure the device to record logs during IPv4 address allocation. | [**logging**](cmdqueryname=logging) [ **allocation-fail** | **allocation-success** | **release** | **renew-fail** | **renew-success** | **detect-conflict** | **recycle-conflict** ] \* | After the log recording function is enabled, the server frequently records logs if a large number of DHCPv4 clients request IPv4 addresses. This may deteriorate device performance.  IPv4 address allocation logs are recorded in the AM module.  By default, a device is disabled from recording logs during IPv4 address allocation. |
   | Configure a gateway address for a client. | [**gateway-list**](cmdqueryname=gateway-list) *ip-address* &<1-8> | If a gateway address is configured for a client on the DHCPv4 server, the client obtains the gateway address from the DHCPv4 server and automatically generates a default route to the gateway address. The client can then access the hosts on other network segments. If the DHCPv4 server is configured to allocate a classless static route to the client using Option 121, the client does not automatically generate a default route to the gateway address. To balance traffic and improve network reliability, configure multiple gateways. Each address pool can be configured with a maximum of eight gateway addresses.  In a scenario where Virtual Router Redundancy Protocol (VRRP) and DHCPv4 are deployed, if a VRRP device functions as the DHCPv4 server, perform this task to configure the VRRP virtual IPv4 address as the gateway address.  If the DHCPv4 server and clients are on the same network segment and the DHCPv4 server functions as the gateway of the clients, this task is not required.  By default, the default gateway address pre-allocated by the DHCPv4 server to a DHCPv4 client is not specified. |
   | Configure a boot file for a client. | [**bootfile**](cmdqueryname=bootfile) *bootfile-name*: configures the name of a boot file for a DHCPv4 client.  [**sname**](cmdqueryname=sname) *sname*: configures the name of a server from which a DHCPv4 client obtains the boot file.  [**next-server**](cmdqueryname=next-server) *ip-address*: configures a file server address used by a client after the client automatically obtains an IPv4 address. | The boot file can be stored on the DHCPv4 server or a dedicated file server.  If the boot file is stored on a dedicated file server, you need to specify the file server address for a DHCPv4 client on the DHCPv4 server and ensure that the client and file server are routable.  By default, the name of a boot file, name of a server, and file server IPv4 address are not configured for a DHCPv4 client. |
   | Configure DNS information allocated by the DHCPv4 server. | [**dns-list**](cmdqueryname=dns-list) *ip-address* &<1-8>: configures the IPv4 address of a DNS server for a DHCPv4 client.  [**domain-name**](cmdqueryname=domain-name) *domain-name*: configures a DNS domain name suffix assigned to a DHCPv4 client. | You can perform this task to dynamically obtain the DNS configuration of a client through DHCPv4.  Each address pool can be configured with a maximum of eight DNS server addresses.  By default, no DNS server IPv4 address or DNS domain name suffix is configured. |
   | Configure NetBIOS information allocated by the DHCPv4 server. | [**nbns-list**](cmdqueryname=nbns-list) *ip-address* &<1-8>: configures the IPv4 address of a NetBIOS server for a DHCPv4 client.  [**netbios-type**](cmdqueryname=netbios-type) { **b-node** | **h-node** | **m-node** | **p-node** }: configures a NetBIOS node type for a DHCPv4 client. | You can perform this task to dynamically obtain the NetBIOS configuration of a client through DHCPv4.  Each address pool can be configured with a maximum of eight NetBIOS server IPv4 addresses.  By default, no NetBIOS server address or node type is configured. |
   | Configure a SIP server IPv4 address allocated by the DHCPv4 server. | [**sip-server**](cmdqueryname=sip-server) { **ip-address** *ip-address* &<1-2> | **list** *domain-name* &<1-2> } | After a SIP server IPv4 address is configured in the address pool of the DHCPv4 server, the DHCPv4 server specifies the SIP server IPv4 address when allocating IPv4 addresses to DHCPv4 clients.  By default, no SIP server IPv4 address allocated by the DHCPv4 server is configured. |
   | Configure a classless static route allocated by the DHCPv4 server. | [**option121**](cmdqueryname=option121) **ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8> | By default, no classless static route is configured. |
   | Configure Option 184 allocated by the DHCPv4 server. | [**option184**](cmdqueryname=option184) { **as-ip** *ip-address* | **fail-over** *ip-address* *dialer-string* | **ncp-ip** *ip-address* | **voice-vlan** *vlan-id* } | By default, no Option 184 is configured. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```