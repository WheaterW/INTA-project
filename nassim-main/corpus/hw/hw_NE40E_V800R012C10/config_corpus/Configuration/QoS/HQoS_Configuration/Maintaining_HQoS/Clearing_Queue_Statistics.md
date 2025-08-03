Clearing Queue Statistics
=========================

This section describes how to clear statistics about a specified GQ, user queue or QoS profile statistics on a specified interface, and FQ statistics of a specified user.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Queue statistics cannot be restored after being cleared. Exercise caution when performing this operation.

To clear queue statistics, run the corresponding reset command in the user view.


#### Procedure

* Run the [**reset user-group-queue**](cmdqueryname=reset+user-group-queue) [ **name** ] *group-name* **statistics** [ **group** *group-name* ] **slot** { *slot-id* | *all* } { **inbound** | **outbound** } command to clear statistics about a specified GQ.
* Run the [**reset qos-profile statistics**](cmdqueryname=reset+qos-profile+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vid** *vid* | **ce-vid** *ce-vid* | **vid** *vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } command to clear QoS profile statistics on a specified interface.
* Run the [**reset port-queue statistics**](cmdqueryname=reset+port-queue+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } [ *cos-value* ] **outbound** or [**reset port-queue statistics**](cmdqueryname=reset+port-queue+statistics) [ **slot** *slot-id* ] [ *cos-value* ] **outbound** command to clear PQ statistics.
* Run the [**reset qos user-id**](cmdqueryname=reset+qos+user-id) *user-id* { **inbound** | **outbound** } to clear statistics about eight priority queues and CAR traffic policing of a specified user.
  
  
  
  In VS mode, this command is supported only by the admin VS.
* Run the [**reset user-group-queue statistics interface**](cmdqueryname=reset+user-group-queue+statistics+interface) { *interface-name* | *interface-type* *interface-number* } **pe-vid** *pe-vid* **ce-vid** *ce-vid* { **inbound** | **outbound** } command to clear GQ statistics on a specified interface.
* Run the [**reset sub-port-queue statistics**](cmdqueryname=reset+sub-port-queue+statistics) **interface** { *interface-type* *interface-number* | *interface-name* } **outbound** command to clear statistics about sub-interface queues.
* Run the [**reset qos-profile statistics**](cmdqueryname=reset+qos-profile+statistics) **vni** *vni-id* { **inbound** | **outbound** } command to clear QoS profile statistics of a specified VNI.
* Run the [**reset qos-profile statistics**](cmdqueryname=reset+qos-profile+statistics) **vni** *vni-id* { **inbound** | **outbound** } **source** *sourceip* **peer** *peerip* command to clear QoS profile statistics on a specified NVE interface.
* Run the [**reset qos default flow-queue statistics**](cmdqueryname=reset+qos+default+flow-queue+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } **outbound** command to clear FQ statistics on a specified channelized sub-interface.
* Run the [**reset qos-profile statistics bridge-domain**](cmdqueryname=reset+qos-profile+statistics+bridge-domain) *bdid* { **inbound** | **outbound** } command to clear QoS profile statistics on all member interfaces in a specified BD.
* Run the [**reset qos-profile statistics vsi**](cmdqueryname=reset+qos-profile+statistics+vsi) *vsiname* { **inbound** | **outbound** } command to clear QoS profile statistics on all member interfaces in a specified VSI.