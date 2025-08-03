Verifying the Configuration of Policies for Route Exchanges Between MBGP Peers
==============================================================================

After configuring policies for route exchange between MBGP peers, verify information about MBGP routes.

#### Prerequisites

Policies that control route exchange between MBGP peers have been configured.


#### Procedure

* Run the [**display bgp multicast routing-table different-origin-as**](cmdqueryname=display+bgp+multicast+routing-table+different-origin-as) command to check routes that have the same destination address but different original AS numbers.
* Run the [**display bgp multicast routing-table regular-expression**](cmdqueryname=display+bgp+multicast+routing-table+regular-expression) [ *as-regular-expression* ] command to check routes that match the AS regular expression.
* Run the [**display bgp multicast routing-table as-path-filter**](cmdqueryname=display+bgp+multicast+routing-table+as-path-filter) { *as-path-filter-number* | *as-path-filter-name* } command to check routes that match a specified AS\_Path filter.
* Run the [**display bgp multicast routing-table community-filter**](cmdqueryname=display+bgp+multicast+routing-table+community-filter) { { *community-filter-name* | *basic-community-filter-number* } [ **whole-match** ] | *advanced-community-filter-number* } command to check routes that match an MBGP community filter.
* Run the [**display bgp multicast routing-table peer**](cmdqueryname=display+bgp+multicast+routing-table+peer) *peer-address* { **advertised-routes** | **received-routes** [ **active** ] } [ **statistics** ] command to check routes sent to or received from a specified MBGP peer.
* Run the [**display bgp multicast network**](cmdqueryname=display+bgp+multicast+network) command to check routes advertised by MBGP.