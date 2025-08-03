Monitoring the Running Status of VPLS
=====================================

You can view VPLS information by monitoring VPLS running status.

#### Context

In routine maintenance, you can run the following commands in any view to learn VPLS running status.


#### Procedure

1. Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
2. Run the [**display vsi remote**](cmdqueryname=display+vsi+remote) **ldp** [ [ **router-id** *ip-address* ] [ **pw-id** *pw-id* ] | **unmatch** | **verbose** ] command to check remote VSI information.
3. Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **ldp** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check VPLS connection information.
4. Run the [**display vsi pw out-interface**](cmdqueryname=display+vsi+pw+out-interface) [ **vsi** *vsi-name* ] command to check the outbound interface information of VSI PWs.
5. Run the [**display l2vpn vsi-list tunnel-policy**](cmdqueryname=display+l2vpn+vsi-list+tunnel-policy) *policy-name* command to check information about the tunnel policies applied to VSIs.
6. Run the [**display vpls forwarding-info**](cmdqueryname=display+vpls+forwarding-info) [ **state** { **up** | **down** } | **vsi** *vsi-name* [ **peer** *peer-address* [ **negotiation-vc-id** *vc-id* ] ] ] [ **verbose** ] command to check VSI forwarding information.
7. Run the [**display vsi services**](cmdqueryname=display+vsi+services) { *vsi-name* | **all** | **interface** *interface-type* *interface-number* | **vlan** *vlan-id* } command to check information about the AC interfaces associated with a specified VSI.
8. Run the [**display admin-vsi binding**](cmdqueryname=display+admin-vsi+binding) [ **admin-vsi** *vsi-name* ] command to check information about the binding between the mVSI and service VSIs.