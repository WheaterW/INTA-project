Verifying the Configuration
===========================

After configuring a hard-pipe VPWS/VPLS PW, check the configurations.

#### Prerequisites

A hard-pipe VPWS/VPLS PW has been configured.


#### Procedure

* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) [ **hard-pipe** ] [ *vc-id* | **state** { **up** | **down** } ] command to check static PW configurations in an IP hard pipe environment.
* Run the [**display mpls switch-l2vc**](cmdqueryname=display+mpls+switch-l2vc) [ **hard-pipe** ][ **brief** | **state** { **up** | **down** } | *peerIp* *pwId* **encapsulation** *encapsulation-type* ] command to check static MS-PW information in an IP hard pipe environment.
* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check the hard-pipe configuration of a VPLS static PW.
* Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* **hard-pipe** [ **peer** *peer-address* [ **negotiation-vc-id** *vc-id* ] ] command to check traffic statistics about hard-pipe static VPLS PWs.