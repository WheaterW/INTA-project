Verifying the Configuration
===========================

After configuring VPWS accessing public network or L3VPN, check the binding relationship between VE interfaces and the VE group and VPWS connection information.

#### Procedure

* Run the [**display virtual-ethernet ve-group**](cmdqueryname=display+virtual-ethernet+ve-group) [ *ve-group-id* | **slot** *slot-id* ] command to check the binding relationship between the VE interfaces and VE group.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **brief** | **interface** *interface-type* *interface-number* | **remote-info** [ *vc-id* ] | **state** { **down** | **up** } ] command to check information about an LDP VPWS.
* Run the [**display vll ccc**](cmdqueryname=display+vll+ccc) [ *ccc-name* | **type** **local** ] command to check the status of the local CCC.
* Run the [**display mpls l2vpn connection**](cmdqueryname=display+mpls+l2vpn+connection) *l2vpn-name* [ **remote-ce** *remote-ce-id* | **down** | **up** | **verbose** ] command to check BGP VPWS connection information.