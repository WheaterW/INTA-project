Verifying the Configuration
===========================

After controlling route advertisement, check information about filtered and advertised routes.

#### Prerequisites

Configurations have been performed to control route advertisement.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp+ipv6+network) **ipv6** **network** command to check routing information advertised by BGP4+.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+cidr) **cidr** command to check classless inter-domain routing (CIDR) information.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table+community+internet+no-advertise) **community** [ *aa:nn* &<1-13> ] [ **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] \* [ **whole-match** ] command to check information about the routes carrying the specified BGP4+ community attribute.
* Run the [**display bgp**](cmdqueryname=display+bgp+ipv6) **ipv6** [**peer**](cmdqueryname=peer+verbose) [ *ipv6-address* ] **verbose** command to check information about BGP4+ peers.
* Run the [**display bgp**](cmdqueryname=display+bgp+ipv6) **ipv6** [**peer**](cmdqueryname=peer+log-info) *ipv6-address* **log-info** command to check information about BGP4+ peers.