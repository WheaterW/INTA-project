Verifying the Configuration
===========================

After configuring BGP AD VPLS, check local and remote VSI and VPLS connection information.

#### Prerequisites

BGP AD VPLS has been configured.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check VPLS VSI information.
* Run the [**display vsi bgp-ad**](cmdqueryname=display+vsi+bgp-ad) { **import-vt** | **export-vt** | **remote-export-vt** } command to check the VPN targets on a device and all its remote peers.
* Run the [**display vsi bgp-ad remote**](cmdqueryname=display+vsi+bgp-ad+remote) **vpls-id** *vpls-id* command to check information about a specified remote PE.
* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **bgp-ad** | **vsi** *vsi-name* ] [ **down** | **up** ] [ **verbose** ] command to check BGP AD VPLS connection information.