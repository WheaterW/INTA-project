Verifying the Configuration
===========================

After configuring LDP HVPLS, check information about VPLS VSIs (including remote VSIs), VPLS connections, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.

#### Prerequisites

LDP HVPLS has been configured.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] **mac-withdraw loop-detect** command to check information about MAC Withdraw loop detection.