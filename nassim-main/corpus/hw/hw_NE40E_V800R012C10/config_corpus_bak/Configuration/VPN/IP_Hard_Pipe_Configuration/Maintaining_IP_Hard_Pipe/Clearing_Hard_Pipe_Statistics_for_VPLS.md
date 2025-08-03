Clearing Hard Pipe Statistics for VPLS
======================================

This section describes how to clear IP hard pipe statistics for VPLS.

#### Context

To clear IP hard pipe statistics in a specified VSI, run the **reset** command in the user view.


#### Procedure

* Run the [**reset traffic-statistics hard-pipe**](cmdqueryname=reset+traffic-statistics+hard-pipe) **vsi** *vsi-name* [ **peer** *peer-ip* [ **negotiation-vc-id** *pw-id* ] ] command to clear hard-pipe static PW traffic statistics in a specified LDP VSI.