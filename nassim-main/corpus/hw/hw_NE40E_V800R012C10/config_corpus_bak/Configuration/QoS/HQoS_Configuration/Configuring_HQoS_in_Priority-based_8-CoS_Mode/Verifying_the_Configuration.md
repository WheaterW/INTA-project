Verifying the Configuration
===========================

After HQoS in priority-based 8-CoS mode is configured on an interface, you can view information about queues and packet statistics on the interface.

#### Context

Run the following commands to check the configuration.


#### Procedure

* Run the [**display flow-mapping configuration**](cmdqueryname=display+flow-mapping+configuration) [ **verbose** [ *mapping-name* ] ] command to check the configuration and reference relationship of an FQ mapping object.
* Run the [**display user-group-queue statistics**](cmdqueryname=display+user-group-queue+statistics) [ **name** ] *user-group-name* **statistics** [ **group** *group-name* ] [ **slot** *slot-id* ] { **outbound** | **inbound** } command to check GQ statistics.
* Run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) [ *qos-profile-name* ] command to check the QoS profile configuration.
* Run the [**display qos-profile statistics**](cmdqueryname=display+qos-profile+statistics) { **vni** *vni-id* | **interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vid** *vid* | **ce-vid** *ce-vid* | **vid** *vid* **ce-vid** *ce-vid* ] } { **inbound** | **outbound** } command to check QoS profile statistics.
* Run the [**display user-group-queue statistics interface**](cmdqueryname=display+user-group-queue+statistics+interface) { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } command to check GQ statistics.
* Run the [**display qos scheduling-mode**](cmdqueryname=display+qos+scheduling-mode) **slot** *slot-id* command to check the scheduling mode of a board.
* Run the [**display qos-profile statistics vpn-instance**](cmdqueryname=display+qos-profile+statistics+vpn-instance) *vpnname* { **inbound** | **outbound** } [ **verbose** ] command to check QoS profile statistics on all member interfaces in a VPN instance.
* Run the [**display qos-profile statistics vsi**](cmdqueryname=display+qos-profile+statistics+vsi) *vsi-name* { **inbound** | **outbound** } [ **verbose** ] command to check QoS traffic statistics of a specified VSI.
* Run the **[**display qos-profile statistics bridge-domain**](cmdqueryname=display+qos-profile+statistics+bridge-domain)** **bd-id** { ****inbound**** | ****outbound**** } [ ****verbose**** ] command to check QoS traffic statistics of a specified BD.