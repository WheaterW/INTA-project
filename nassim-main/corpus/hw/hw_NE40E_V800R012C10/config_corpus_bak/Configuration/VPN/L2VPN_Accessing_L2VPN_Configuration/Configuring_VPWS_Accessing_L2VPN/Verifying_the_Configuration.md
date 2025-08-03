Verifying the Configuration
===========================

After configuring VPWS accessing L2VPN, check the binding between the VE interfaces and VE group and information about the LDP VPWS connection.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding between the VE interfaces and VE group.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **brief** | **interface** *interface-type* *interface-number* | **remote-info** [ *vc-id* ] | **state** { **down** | **up** } ] command to check LDP VPWS connection information.
* Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** **local** ] command to check the local CCC status.
* Run the [**display mpls l2vpn connection**](cmdqueryname=display+mpls+l2vpn+connection) *l2vpn-name* [ **remote-ce** *remote-ce-id* | **down** | **up** | **verbose** ] command to check BGP VPWS connection information.