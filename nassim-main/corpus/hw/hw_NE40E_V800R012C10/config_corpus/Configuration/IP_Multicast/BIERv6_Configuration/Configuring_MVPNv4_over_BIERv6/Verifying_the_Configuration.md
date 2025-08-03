Verifying the Configuration
===========================

After configuring an MVPNv4 over BIERv6 network, check the committed configurations and whether they have taken effect.

#### Procedure

* Run the **[**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer)** command to check information about BGP MVPN peers.
* Run the **[**display multicast routing-table**](cmdqueryname=display+multicast+routing-table)** command to check information about the multicast routing table.
* Run the [**display multicast**](cmdqueryname=display+multicast) { **vpn-instance** *vpn-instance-name* | **all-instance** } **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check reverse path forwarding (RPF) routing information of a specified multicast source.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check I-PMSI tunnel information of a specified VPN instance.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command on a sender PE or receiver PE to check S-PMSI tunnel information of a specified VPN instance.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check the PIM routing table.
* Run the [**display pim**](cmdqueryname=display+pim) { **vpn-instance** *vpn-instance-name* | **all-instance** } **claimed-route** [ *source-address* ] command to check information about the unicast routes used by PIM.