Verifying the Configuration
===========================

Verifying the Configuration

#### Prerequisites

BGP VPWS has been configured.


#### Procedure

* Run the [**display mpls l2vpn**](cmdqueryname=display+mpls+l2vpn) [ *l2vpn-name* [ **local-ce** | **remote-ce** ] ] command to check BGP VPWS information.
* Run the [**display mpls l2vpn connection**](cmdqueryname=display+mpls+l2vpn+connection) *l2vpn-name* [ **remote-ce** *remote-ce-id* | **down** | **up** | **verbose** ] command to check BGP VPWS connection information.
* Run the [**display mpls l2vpn**](cmdqueryname=display+mpls+l2vpn) { **export-route-target-list** | **import-route-target-list** } command to check the VPN target list of BGP VPWS.