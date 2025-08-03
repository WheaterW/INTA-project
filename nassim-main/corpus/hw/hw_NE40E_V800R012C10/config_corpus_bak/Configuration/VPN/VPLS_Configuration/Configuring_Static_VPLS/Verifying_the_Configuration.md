Verifying the Configuration
===========================

After configuring static VPLS, check its VSI, AC interface, and label stack information.

#### Prerequisites

Static VPLS has been configured.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi services**](cmdqueryname=display+vsi+services) { *vsi-name* | **all** | **interface** *interface-type* *interface-number* | **vlan** *vlan-id* } command to check information about the AC interfaces bound to the VSI.
* Run the [**display mpls label-stack vpls vsi**](cmdqueryname=display+mpls+label-stack+vpls+vsi) *vsi-name* **peer** *peer-id* **vc-id** *vc-id* command to check label stack information.