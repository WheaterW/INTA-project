Clearing the Traffic Statistics of a VPLS PW
============================================

This section describes how to clear traffic statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Traffic statistics cannot be restored after you clear them. Exercise caution when clearing traffic statistics.



#### Procedure

* Run the [**reset traffic-statistics vsi all**](cmdqueryname=reset+traffic-statistics+vsi+all) command to clear all VPLS PW traffic statistics.
* Run the [**reset traffic-statistics vsi**](cmdqueryname=reset+traffic-statistics+vsi) { **name** *vsi-name* [ **peer** *peer-address* [ **negotiation-vc-id** *vc-id* | **ldp129** | **remote-site** *remote-site-id* ] ] | **all** } command to clear the public network traffic statistics of a specified VPLS PW with a specified VSI name.
* Run the [**reset traffic-statistics suppression vsi**](cmdqueryname=reset+traffic-statistics+suppression+vsi) **name** *vsi-name* **peer** *peer-address* [ **negotiation-vc-id** *negotiation-vc-id* | **remote-site** *remote-site-id* | **ldp129** ] command to clear the traffic suppression statistics of a specified PW.