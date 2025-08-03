Checking DHCPv4 Operating Status
================================

You can check DHCPv4 operating status by viewing the IPv4 address pool configurations, DHCPv4 server information, and statistics on the DHCPv4 server.

#### Prerequisites

In routine maintenance, you can run the following commands in any view to check DHCPv4 operating status.


#### Procedure

* Run the [**display ip pool**](cmdqueryname=display+ip+pool) [ **name** *pool-name* [ *section-num* [ *start-ip-address* [ *end-ip-address* ] ] | **all** | **used** ] ] [ **vpn-instance** *vpn-instance-name* ] command to check the configuration of the IPv4 address pool.
* Run the [**display dhcp-server group**](cmdqueryname=display+dhcp-server+group) [ *group-name* ] command to check the configuration of the DHCPv4 server group.
* Run the [**display dhcp-server item**](cmdqueryname=display+dhcp-server+item) *ip-address* [ **vpn-instance** *vpn-instance* ] command to check information about a DHCPv4 server.
* Run the [**display dhcp-server statistics**](cmdqueryname=display+dhcp-server+statistics) *ip-address* [ **vpn-instance** *vpn-instance* ] [ **verbose** ] command to check the statistics on a DHCPv4 server.
* Run the [**display dhcp relay address**](cmdqueryname=display+dhcp+relay+address) { **all** | **interface** *interface-type* *interface-number* | **vlan** *vlan-id* } command to check configurations about interfaces where DHCPv4 relay is enabled.
* Run the [**display dhcp-access statistics packet**](cmdqueryname=display+dhcp-access+statistics+packet) command to check statistics about DHCPv4 services.
* Run the [**display ip-pool max-usage**](cmdqueryname=display+ip-pool+max-usage) { **pool** [ *pool-name* ] | **domain** [ *domain-name* ] } command in any view to check the historical maximum usage of addresses in an IPv4 address pool.