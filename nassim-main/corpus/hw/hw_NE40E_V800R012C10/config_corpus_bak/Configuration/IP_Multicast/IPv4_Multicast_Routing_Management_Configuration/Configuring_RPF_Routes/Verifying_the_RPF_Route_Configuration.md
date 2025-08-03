Verifying the RPF Route Configuration
=====================================

After configuring Reverse Path Forwarding (RPF) routes, verify configuration of the RPF routes.

#### Prerequisites

RPF routes have been configured.


#### Procedure

* Run the [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **rpf-info** *source-address* [ *group-address* ] [ **rpt** | **spt** ] command to check information about the source-specific RPF route.
* Run the [**display multicast rpf-info**](cmdqueryname=display+multicast+rpf-info) *source-address* command. The command output shows RPF routing information about a specified multicast source, including the RPF interface, RPF neighbor, optimal route and type of the route, and configured multicast load splitting policy.