Verifying the Configuration
===========================

After configuring a CCC VPWS PW, you can check CCC connection information, such as interfaces used by the CCC connection.

#### Prerequisites

A CCC VPWS PW has been configured.


#### Procedure

* Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** { **local** | **remote** } ] command to check CCC connection information.
* Run the [**display l2vpn ccc-interface vc-type**](cmdqueryname=display+l2vpn+ccc-interface+vc-type) **ccc** [ **down** | **up** ] command to check information about interfaces used by CCC connections.
* Run the [**display mpls l2vpn vpws**](cmdqueryname=display+mpls+l2vpn+vpws) [ **interface** *interface-type interface-number* [ **verbose** ] ] command to check VPWS information.