Verifying the Configuration
===========================

After configuring a GTMv4 over BIERv6 network, check the committed configurations and whether they have taken effect.

#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* command on a receiver PE to check whether the route to the source address and the route to the RP address are BGP routes and advertised through GTM.
* Run the **[**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer)** command to check information about BGP MVPN peers.
* Run the **[**display multicast routing-table**](cmdqueryname=display+multicast+routing-table)** command to check information about the multicast routing table.
* Run the [**display multicast rpf-info**](cmdqueryname=display+multicast+rpf-info) *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check RPF routing information of a specified multicast source.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) **public** **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check I-PMSI tunnel information in the public network instance.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) **public** **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check S-PMSI tunnel information in the public network instance.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check the PIM routing table.
* Run the [**display pim**](cmdqueryname=display+pim) **claimed-route** [ *source-address* ] command to check information about the unicast routes used by PIM.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *ip-address* command on a receiver PE to check whether the route to the source carries IPv6 extended community attributes.