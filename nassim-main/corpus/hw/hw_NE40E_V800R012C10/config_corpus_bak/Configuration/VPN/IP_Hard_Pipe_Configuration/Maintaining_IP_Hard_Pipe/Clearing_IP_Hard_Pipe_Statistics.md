Clearing IP Hard Pipe Statistics
================================

This section describes how to clear IP hard pipe statistics.

#### Context

To clear IP hard pipe statistics on a specified interface, run either of the following **reset** commands in the user view.


#### Procedure

* Run the [**reset qos hard-pipe statistics**](cmdqueryname=reset+qos+hard-pipe+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } **outbound** command to clear traffic statistics on a PW-side or AC-side hard-pipe interface.
* Run the [**reset mpls l2vpn hard-pipe statistics**](cmdqueryname=reset+mpls+l2vpn+hard-pipe+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } [ **inbound** | **outbound** ] command to clear traffic statistics on an AC-side hard pipe interface.