Verifying the Configuration
===========================

After configuring LDP statistics collection, check traffic statistics on the ingress and transit nodes.

#### Prerequisites

LDP statistics collection has been configured.


#### Procedure

* Run the [**display mpls ldp lsp traffic-statistics**](cmdqueryname=display+mpls+ldp+lsp+traffic-statistics+verbose) [ *ipv4âaddress* *mask-length* ] [ **verbose** ] command to check LDP traffic statistics.
* Run the [**reset mpls traffic-statistics ldp**](cmdqueryname=reset+mpls+traffic-statistics+ldp) [ *ipv4âaddress* *mask-length* ] command to delete LDP traffic statistics.