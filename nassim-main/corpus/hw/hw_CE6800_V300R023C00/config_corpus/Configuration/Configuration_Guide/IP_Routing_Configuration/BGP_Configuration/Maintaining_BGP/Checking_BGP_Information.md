Checking BGP Information
========================

Checking BGP Information

#### Context

After BGP functions are configured, you can run the following commands in the user view to check BGP information.

![](public_sys-resources/notice_3.0-en-us.png) 

The following table lists only common keywords in display commands. For details about other command formats, see the corresponding command page or command association information.


**Table 1** Checking BGP information
| Operation | Command |
| --- | --- |
| Check BGP public network route information. | [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) |
| Check detailed information about BGP routes. | [**display bgp routing-table verbose**](cmdqueryname=display+bgp+routing-table+verbose) |
| Check BGP routing information of a specified peer. | [**display bgp routing-table peer**](cmdqueryname=display+bgp+routing-table+peer) |
| Check the BGP routes that flapped within a specified period. | [**display bgp routing-table time-range**](cmdqueryname=display+bgp+routing-table+time-range) |
| Check CIDR BGP routing information. | [**display bgp routing-table cidr**](cmdqueryname=display+bgp+routing-table+cidr) |
| Check the recursion result with a specified peer IP address. | [**display bgp routing-table relay-nexthop interface**](cmdqueryname=display+bgp+routing-table+relay-nexthop+interface) |
| Check BGP route statistics. | [**display bgp routing-table statistics**](cmdqueryname=display+bgp+routing-table+statistics) |
| Check the statistics of BGP Best and Best External routes. | [**display bgp routing-table statistics best**](cmdqueryname=display+bgp+routing-table+statistics+best) |
| Check information about dampened BGP routes. | [**display bgp routing-table dampened**](cmdqueryname=display+bgp+routing-table+dampened) |
| Check the configured BGP route dampening parameters. | [**display bgp routing-table dampening parameter**](cmdqueryname=display+bgp+routing-table+dampening+parameter) |
| Check the routes with the same destination address and mask but different origin AS numbers. | [**display bgp routing-table different-origin-as**](cmdqueryname=display+bgp+routing-table+different-origin-as) |
| Check statistics about BGP route flapping. | [**display bgp routing-table flap-info**](cmdqueryname=display+bgp+routing-table+flap-info) |
| Check the routes imported by BGP using the **network** command. | [**display bgp network**](cmdqueryname=display+bgp+network) |
| Check BGP peer information. | [**display bgp peer**](cmdqueryname=display+bgp+peer) |
| Check information about BGP peer groups. | [**display bgp group**](cmdqueryname=display+bgp+group) |
| Check BGP error information. | [**display bgp error discard**](cmdqueryname=display+bgp+error+discard) |
| Check the log information of BGP peers. | [**display bgp peer log-info**](cmdqueryname=display+bgp+peer+log-info) |
| Check statistics about the routes of a specified peer. | [**display bgp peer statistics**](cmdqueryname=display+bgp+peer+statistics) |
| Check prefix-based ORF information received from a specified peer. | [**display bgp peer orf ip-prefix**](cmdqueryname=display+bgp+peer+orf+ip-prefix) |
| Check the router ID of the device. | [**display bgp router-id**](cmdqueryname=display+bgp+router-id) |
| Check BGP resource specifications. | [**display bgp resource**](cmdqueryname=display+bgp+resource) |
| Check the cause of BGP peer relationship disconnection and flapping. | [**display bgp troubleshooting**](cmdqueryname=display+bgp+troubleshooting) |
| Check information about BGP update peer-groups. | [**display bgp update-peer-group**](cmdqueryname=display+bgp+update-peer-group) |
| Check information about enabled BGP debugging functions. | [**display debugging bgp**](cmdqueryname=display+debugging+bgp) |
| Check the default configurations in BGP initialization. | [**display default-parameter bgp**](cmdqueryname=display+default-parameter+bgp) |
| Check information about the BFD sessions established by BGP. | [**display bgp bfd session**](cmdqueryname=display+bgp+bfd+session) |
| Check information about BGP peers in an address family, including the peer status and route statistics. | [**display bgp all summary**](cmdqueryname=display+bgp+all+summary) |
| Check GR information on a BGP speaker. | [**display bgp graceful-restart status**](cmdqueryname=display+bgp+graceful-restart+status) |
| Check local GR information on a BGP speaker. | [**display bgp local-graceful-restart status**](cmdqueryname=display+bgp+local-graceful-restart+status) |