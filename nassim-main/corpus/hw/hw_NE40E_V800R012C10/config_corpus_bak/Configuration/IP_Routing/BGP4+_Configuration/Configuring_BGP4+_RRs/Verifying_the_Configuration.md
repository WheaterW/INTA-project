Verifying the Configuration
===========================

After configuring BGP4+ RRs, check information about BGP4+ routes and peer groups.

#### Prerequisites

BGP4+ RRs have been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp+ipv6) **ipv6** [**peer**](cmdqueryname=peer+verbose) [ *ipv6-address* ] **verbose** command to check information about peers and check whether the relationship with the RR is successfully established.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check whether there are routes reflected by an RR.