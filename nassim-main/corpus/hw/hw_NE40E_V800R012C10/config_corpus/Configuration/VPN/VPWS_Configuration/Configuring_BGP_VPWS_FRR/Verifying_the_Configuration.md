Verifying the Configuration
===========================

Verifying the Configuration

#### Prerequisites

VPWS FRR has been configured.


#### Procedure

* Run the [**display mpls l2vpn connection**](cmdqueryname=display+mpls+l2vpn+connection) *l2vpn-name* [ **remote-ce** *remote-ce-id* | **down** | **up** | **verbose** ] command to check BGP VPWS connection information.
* Run the [**display mpls l2vpn oam-mapping**](cmdqueryname=display+mpls+l2vpn+oam-mapping) [ **interface** *interface-type* *interface-number* ] command to check L2VPN OAM mapping information between the specified AC interface and corresponding PW.