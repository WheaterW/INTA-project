Verifying the Configuration
===========================

After configuring interworking between EVPN VXLAN and traditional VPLS, verify the configurations, such as VXLAN tunnel and VPLS tunnel and route configurations.

#### Prerequisites

All configurations of interworking between EVPN VXLAN and traditional VPLS have been completed.


#### Procedure

* Check the VPLS configurations.
  + Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VSI information of the VPLS.
  + Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **ldp** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check VPLS connections.
  + Run the [**display admin-vsi binding**](cmdqueryname=display+admin-vsi+binding) [ **admin-vsi** *vsi-name* ] command to check the binding relationship between a management VSI and a service VSI.
  + Run the [**display vsi**](cmdqueryname=display+vsi) { **name** *vsi-name* **peer-info** [ *peer-ip-address* ] | **peer-info** } command to check the PW status of the peer.
  + Run the [**display vsi**](cmdqueryname=display+vsi) **name** *vsi-name* **protect-group** [ *group-name* [ **verbose** | **history** ] ] command to check summary or detailed information about the PW protection group of a specified VSI, or PW switchover information about the PW protection group of a specified VSI.
* Check the EVPN and VXLAN configurations.
  + Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | *bd-id* [ **brief** | **verbose** | **binding-info** ] ] command to check BD configurations.
  + Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] command to check EVPN instance information.
  + Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check BGP EVPN route information.
  + Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.