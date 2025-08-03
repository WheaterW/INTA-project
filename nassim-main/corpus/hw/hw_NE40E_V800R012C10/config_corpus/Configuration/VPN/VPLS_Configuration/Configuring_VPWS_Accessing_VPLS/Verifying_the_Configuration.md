Verifying the Configuration
===========================

After configuring VPWS accessing VPLS, you can check information about VPWS and VPLS connections, VPLS VSIs, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.

#### Prerequisites

VPWS accessing VPLS has been configured.


#### Procedure

* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* ] command to check local LDP VPWS connection information on the PE.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi mac-withdraw loop-detect**](cmdqueryname=display+vsi+mac-withdraw+loop-detect) command to check information about MAC Withdraw loop detection.