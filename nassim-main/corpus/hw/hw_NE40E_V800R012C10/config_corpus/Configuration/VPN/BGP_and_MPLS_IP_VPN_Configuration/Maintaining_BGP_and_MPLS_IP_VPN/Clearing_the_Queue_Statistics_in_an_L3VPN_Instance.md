Clearing the Queue Statistics in an L3VPN Instance
==================================================

The queue statistics in an L3VPN instance cannot be restored once they are cleared. Exercise caution when performing this operation.

#### Context

After interfaces are bound to an L3VPN instance and the CAR is deployed on these interfaces through QoS profile application, you can run this command to clear the QoS profile statistics on all these interfaces.


#### Procedure

* Run the [**reset qos-profile statistics vpn-instance**](cmdqueryname=reset+qos-profile+statistics+vpn-instance) *vpnname* { **inbound** | **outbound** } command to clear the QoS profile statistics on all interfaces bound to an L3VPN instance.