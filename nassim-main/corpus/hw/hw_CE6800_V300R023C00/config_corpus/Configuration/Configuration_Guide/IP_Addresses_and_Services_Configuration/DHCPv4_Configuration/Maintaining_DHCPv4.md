Maintaining DHCPv4
==================

Maintaining DHCPv4

#### Clearing DHCPv4 Message Statistics

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when clearing the statistics.

To clear DHCPv4 message statistics, run reset commands in the user view.

**Table 1** Clearing DHCPv4 message statistics
| Operation | Command |
| --- | --- |
| Clear statistics about DHCPv4 messages sent and received by the device functioning as a DHCPv4 server. | [**reset dhcp server statistics**](cmdqueryname=reset+dhcp+server+statistics) |
| Clear statistics about DHCPv4 messages sent and received by the device functioning as a DHCPv4 relay agent. | [**reset dhcp relay statistics**](cmdqueryname=reset+dhcp+relay+statistics) [ **server-group** *group-name* ] |
| Clear statistics about DHCPv4 messages sent and received by the device functioning as a DHCPv4 client. | [**reset dhcp client statistics**](cmdqueryname=reset+dhcp+client+statistics) [ **interface** *interface-type interface-number* ] |
| Clear statistics about DHCPv4 messages sent and received by the device. | [**reset dhcp statistics**](cmdqueryname=reset+dhcp+statistics) |



#### Resetting an Address Pool

If a device functions as a DHCPv4 relay agent, it can request a DHCPv4 server to release client IPv4 addresses. A DHCPv4 relay agent can send a DHCPRELEASE message to a specified DHCPv4 server. After receiving the message, the server resets the corresponding IPv4 address to idle, allowing the released IPv4 address to be allocated to another DHCPv4 client.

**Table 2** Resetting an address pool
| Operation | Command |
| --- | --- |
| Reset an interface address pool configured on the device. | User view: [**reset ip pool**](cmdqueryname=reset+ip+pool) **interface** *interface-name* { *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** } |
| Reset a global address pool configured on the device. | User view: [**reset ip pool**](cmdqueryname=reset+ip+pool) **name** *ip-pool-name* { *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** } |
| Configure the device functioning as a DHCPv4 relay agent to request a DHCPv4 server to release a client IPv4 address. | System or interface view: [**dhcp relay release**](cmdqueryname=dhcp+relay+release) *client-ip-address* *mac-address* [ **vpn-instance** *vpn-instance-name* ] [ *server-ip-address* ]  NOTE:  This command releases only an IPv4 address that a DHCPv4 server dynamically allocates.  If multiple DHCPv4 relay agents exist between a DHCPv4 client and server, this command takes effect only on the first relay agent connected to the server. If the IPv4 address of a DHCPv4 server is specified, the device sends a DHCPRELEASE message only to this server. If no DHCPv4 server is specified:  * When the command is run in the system view, the device sends a DHCPRELEASE message to all the DHCPv4 servers connected to DHCPv4 relay interfaces. * When the command is run in the interface view, the device sends a DHCPRELEASE message to the DHCPv4 server connected to the interface. |



#### Locking a Global Address Pool

If the global address pool on a DHCPv4 server needs to be migrated to another DHCPv4 server, you can lock the global address pool so that the server cannot continue to allocate IPv4 addresses to DHCPv4 clients. After the address pool is migrated, new users apply for IPv4 addresses from a new address pool to go online.

**Table 3** Locking a global address pool
| Operation | Command |
| --- | --- |
| Lock a global address pool. | Global address pool view: [**lock**](cmdqueryname=lock) |



#### Forcing a PC to Release or Update the IPv4 Address

In certain scenarios such as fault locating, you can force a PC to release or update the IPv4 address. The following table lists related commands on several operating systems. For details about the commands, see related operating system documents.

**Table 4** Forcing a PC to release or update the IPv4 address
| Operation | Command |
| --- | --- |
| Release an IPv4 address. | * Windows 7: **ipconfig** /**release** * Windows 98's MS-DOS: **winipcfg** /**release** * Unix-like: **dhclient âr** |
| Renew the IPv4 address lease or apply for a new IPv4 address. | * Windows 7: **ipconfig** /**renew** * Windows 98's MS-DOS: **winipcfg** /**renew** * Unix-like: **dhclient** |



#### Canceling the Allocation of Fixed IPv4 Addresses to Clients

On a device functioning as a DHCPv4 server, you can cancel the allocation of a specified IPv4 address to a static client. For example, you can cancel the allocation of the IPv4 address 10.1.1.5 in the address pool whose network segment address is 10.1.1.0 and mask length is 24 to a client. To check the static binding between a client and an IPv4 address, run the [**display ip pool**](cmdqueryname=display+ip+pool) { **interface** *interface-pool-name* | **name** *ip-pool-name* } **used** command.

**Table 5** Canceling the allocation of fixed IPv4 addresses to clients
| Operation | Command |
| --- | --- |
| Reclaim IPv4 addresses. | User view: [**reset ip pool**](cmdqueryname=reset+ip+pool) { **interface** *interface-name* | **name** *ip-pool-name* } { *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** } |
| Remove a static binding. | * If an interface address pool is used, run the following command in the corresponding interface view: [**undo dhcp server static-bind**](cmdqueryname=undo+dhcp+server+static-bind) [ **ip-address** *ip-address* | **mac-address** *mac-address* ] * If a global address pool is used, run the following command in the corresponding address pool view: [**undo static-bind**](cmdqueryname=undo+static-bind) [ **ip-address** *ip-address* | **mac-address** *mac-address* ] |