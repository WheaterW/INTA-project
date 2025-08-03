Checking BGP4+ Information
==========================

Checking BGP4+ Information

#### Context

After BGP4+ functions are configured, you can run the following commands in the user view to check BGP4+ information.

![](public_sys-resources/notice_3.0-en-us.png) 

The following table lists only common keywords in display commands. For details about other command formats, see the corresponding command page or command association information.


**Table 1** Checking BGP4+ information
| Operation | Command |
| --- | --- |
| Check BGP4+ public network route information. | [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) |
| Check BGP4+ routing information of a specified peer. | [**display bgp ipv6 routing-table peer**](cmdqueryname=display+bgp+ipv6+routing-table+peer) |
| Check the BGP4+ routes that flapped within a specified period. | [**display bgp ipv6 routing-table time-range**](cmdqueryname=display+bgp+ipv6+routing-table+time-range) |
| Check BGP4+ route statistics. | [**display bgp ipv6 routing-table statistics**](cmdqueryname=display+bgp+ipv6+routing-table+statistics) |
| Check the statistics of BGP4+ Best and Best External routes. | [**display bgp ipv6 routing-table statistics best**](cmdqueryname=display+bgp+ipv6+routing-table+statistics+best) |
| Check information about dampened BGP4+ routes. | [**display bgp ipv6 routing-table dampened**](cmdqueryname=display+bgp+ipv6+routing-table+dampened) |
| Check the configured BGP4+ route dampening parameters. | [**display bgp ipv6 routing-table dampening parameter**](cmdqueryname=display+bgp+ipv6+routing-table+dampening+parameter) |
| Check the routes with the same destination address and mask but different origin AS numbers. | [**display bgp ipv6 routing-table different-origin-as**](cmdqueryname=display+bgp+ipv6+routing-table+different-origin-as) |
| Check statistics about BGP4+ route flapping. | [**display bgp ipv6 routing-table flap-info**](cmdqueryname=display+bgp+ipv6+routing-table+flap-info) |
| Check flapping statistics about the routes that match an AS\_Path regular expression. | [**display bgp ipv6 routing-table flap-info regular-expression**](cmdqueryname=display+bgp+ipv6+routing-table+flap-info+regular-expression) |
| Check the routes imported by BGP4+ using the **network** command. | [**display bgp ipv6 network**](cmdqueryname=display+bgp+ipv6+network) |
| Check BGP4+ peer information. | [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) |
| Check information about BGP4+ peer groups. | [**display bgp ipv6 group**](cmdqueryname=display+bgp+ipv6+group) |
| Check the log information of BGP4+ peers. | [**display bgp ipv6 peer log-info**](cmdqueryname=display+bgp+ipv6+peer+log-info) |
| Check statistics about the routes of a specified BGP4+ peer. | [**display bgp ipv6 peer statistics**](cmdqueryname=display+bgp+ipv6+peer+statistics) |
| Check the cause of BGP4+ peer relationship disconnection and flapping. | [**display bgp troubleshooting**](cmdqueryname=display+bgp+troubleshooting) |
| Check information about BGP4+ update peer-groups. | [**display bgp ipv6 update-peer-group**](cmdqueryname=display+bgp+ipv6+update-peer-group) |
| Check information about the BFD sessions established by BGP4+. | [**display bgp ipv6 bfd session**](cmdqueryname=display+bgp+ipv6+bfd+session) |