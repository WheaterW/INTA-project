Verifying the Inter-AS VPWS Configuration
=========================================

After configuring inter-AS VPWS, check local and remote PW information.

#### Prerequisites

Inter-AS VPWS has been configured.


#### Procedure

* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **brief** | **interface** *interface-type* *interface-number* ] command to check local PW information.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) **remote-info** [ *vc-id* | **unmatch** | **verbose** ] command to check remote PW information.
* Run the [**display mpls l2vpn connection**](cmdqueryname=display+mpls+l2vpn+connection) *l2vpn-name* [ **remote-ce** *remote-ce-id* | **down** | **up** | **verbose** ] command to check BGP VPWS connection information.