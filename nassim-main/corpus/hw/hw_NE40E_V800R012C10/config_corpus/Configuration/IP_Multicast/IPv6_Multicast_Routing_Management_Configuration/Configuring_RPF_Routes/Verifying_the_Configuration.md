Verifying the Configuration
===========================

After configuring Reverse Path Forwarding (RPF) routes, check RPF routing information of a specified multicast source.

#### Procedure

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **table-name msr** command to check whether the route is configured successfully or whether the route takes effect.
* Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) *ipv6-source-address* [ **verbose** ] command. You can view the RPF routing information of a specified multicast source, including the RPF interface, RPF neighbor, preferred route and its type, and configured IPv6 multicast load splitting policy.