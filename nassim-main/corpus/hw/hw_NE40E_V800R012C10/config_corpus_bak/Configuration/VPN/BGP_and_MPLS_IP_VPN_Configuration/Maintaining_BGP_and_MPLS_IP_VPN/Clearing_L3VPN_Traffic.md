Clearing L3VPN Traffic
======================

This section describes how to clear L3VPN traffic statistics.
Exercise caution when performing the action because the cleared data
cannot be restored.

#### Context

Run the following command in the user view to clear traffic
statistics.


#### Procedure

* Run the [**reset traffic-statistics vpn-instance**](cmdqueryname=reset+traffic-statistics+vpn-instance) { **name** *vpn-instance-name* | **all** } command in the user view to clear statistics
  about L3VPN traffic of a specified VPN instance or all VPN instances.