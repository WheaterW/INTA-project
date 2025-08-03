Verifying the Configuration
===========================

After configuring VPLS multi-homing, check local and remote VSI and VPLS connection information.

#### Prerequisites

VPLS multi-homing has been configured.


#### Procedure

* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) **bgp-mh** command to check VPLS connection information in VPLS multi-homing scenarios.
* Run the [**display vsi remote**](cmdqueryname=display+vsi+remote) **bgp** [ **nexthop** *nexthopValue* { **export-vpn-target** *ertValue* ] | **route-distinguisher** *rdValue* } command to check remote VSI information.