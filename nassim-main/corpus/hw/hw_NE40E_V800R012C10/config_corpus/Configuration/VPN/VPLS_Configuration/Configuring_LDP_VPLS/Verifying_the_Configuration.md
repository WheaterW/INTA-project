Verifying the Configuration
===========================

After configuring LDP VPLS, check information about local VSIs, remote VSIs, VPLS connections, outbound interfaces of VSI PWs, and tunnel policies applied to VSIs.

#### Prerequisites

LDP VPLS has been configured.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi remote**](cmdqueryname=display+vsi+remote) **ldp** [ [ **router-id** *ip-address* ] [ **pw-id** *pw-id* ] | **unmatch** | **verbose** ] command to check remote VSI information.
* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **ldp** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check VPLS connection information.
* Run the [**display vsi pw out-interface**](cmdqueryname=display+vsi+pw+out-interface) [ **vsi** *vsi-name* ] command to check the outbound interface information of VSI PWs.
* Run the [**display l2vpn vsi-list tunnel-policy**](cmdqueryname=display+l2vpn+vsi-list+tunnel-policy) *policy-name* command to check information about the tunnel policies applied to VSIs.
* Run the [**display vpls forwarding-info**](cmdqueryname=display+vpls+forwarding-info) [ **state** { **up** | **down** } | **vsi** *vsi-name* [ **peer** *peer-address* [ **negotiation-vc-id** *vc-id* ] ] ] [ **verbose** ] command to check VSI forwarding information.
* Run the [**display vsi services**](cmdqueryname=display+vsi+services) { *vsi-name* | **all** | **interface** *interface-type* *interface-number* | **vlan** *vlan-id* } command to check information about the AC interfaces associated with a specified VSI.
* Run the [**display admin-vsi binding**](cmdqueryname=display+admin-vsi+binding) [ **admin-vsi** *vsi-name* ] command to check information about the binding between the mVSI and service VSIs.
* Run the [**display mpls label-stack vpls vsi**](cmdqueryname=display+mpls+label-stack+vpls+vsi) *vsi-name* **peer** *peer-id* **vc-id** *vc-id* command to check label stack information.
* Run the [**display vsi**](cmdqueryname=display+vsi) { **name** *vsi-name* **peer-info** [ *peer-ip-address* ] | **peer-info** } command to check information about peer PW status.