Clearing Traffic Policy Statistics
==================================

This section describes the commands for clearing traffic policy statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when clearing statistics.



#### Procedure

* Run the [**reset traffic**](cmdqueryname=reset+traffic) **policy** [ [ **name** ] *policy-name* ] **statistics** **interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vid** *vid* | **ce-vid** *ce-vid* | **vid** *vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } command to clear traffic policy statistics on a specified interface.
* Run the [**reset traffic policy statistics**](cmdqueryname=reset+traffic+policy+statistics) **bridge-domain** *bdid* { **inbound** | **outbound** } command to clear traffic policy statistics in a specified BD.
* Run the [**reset traffic policy**](cmdqueryname=reset+traffic+policy) [ **name** *policy-name* ] **statistics** { **vsi** *vsi-instance-name* [ **ac-mode** ] | **vpn-instance** *vpn-instance-name* } [ **slot** *slot-id* ] { **inbound** | **outbound** } command to clear traffic policy statistics on the AC interface bound to a VSI.
* Run the [**reset flow-car**](cmdqueryname=reset+flow-car) [ **ipv6** ] [ { **source-ip** | **destination-ip** } *ip-address* ] **slot** *slot-id* command to clear the flow CAR table on a specified board.
* Run the [**reset flow-car**](cmdqueryname=reset+flow-car) [ **ipv6** ] **all** command to clear the flow CAR table of the device.
* Run the [**reset flow-car**](cmdqueryname=reset+flow-car) [ **ipv6** ] **statistics** { **source-ip** | **destination-ip** } [ *ip-address* ] **slot** *slot-id* { **inbound** | **outbound** } command to clear flow CAR statistics in a specified direction on the board in a specified slot based on the source or destination IP address.
* Run the [**reset user-queue statistics**](cmdqueryname=reset+user-queue+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } { **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* } { **inbound** | **outbound** } [ **policy** *policy-name* ] **classifier** *classifier-name* or [**reset user-queue statistics**](cmdqueryname=reset+user-queue+statistics) **bridge-domain** *bd-id* { **inbound** | **outbound** } [ **policy** *policy-name* ] **classifier** *classifier-name* command to clear user queue statistics on a specified interface.