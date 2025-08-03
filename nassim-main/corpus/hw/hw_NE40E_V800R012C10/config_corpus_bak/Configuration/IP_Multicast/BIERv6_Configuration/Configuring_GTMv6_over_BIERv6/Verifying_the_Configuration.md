Verifying the Configuration
===========================

After configuring a GTMv6 over BIERv6 network, check the committed configurations and whether they have taken effect.

#### Procedure

* Run the **[**display bgp mvpn vpnv6 all peer**](cmdqueryname=display+bgp+mvpn+vpnv6+all+peer)** command to check information about BGP-IPv6 MVPN peers.
* Run the **[**display multicast ipv6 routing-table**](cmdqueryname=display+multicast+ipv6+routing-table)** command to check information about the IPv6 multicast routing table.
* Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) *ipv6-source-address* [ *ipv6-group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check RPF routing information of a specified IPv6 multicast source.
* Run the [**display mvpn ipv6**](cmdqueryname=display+mvpn+ipv6) **public** **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check I-PMSI tunnel information in a specified public network VPN instance.
* Run the [**display mvpn ipv6**](cmdqueryname=display+mvpn+ipv6) **public** **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check S-PMSI tunnel information in a specified public network VPN instance.
* Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command to check the IPv6 PIM routing table.
* Run the [**display pim ipv6 claimed-route**](cmdqueryname=display+pim+ipv6+claimed-route) [ *ipv6-source-address* ] command to check information about the IPv6 unicast routes used by IPv6 PIM.