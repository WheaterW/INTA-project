Checking the Queue Statistics in an L3VPN Instance
==================================================

This section describes how to check the QoS profile statistics on all interfaces bound to an L3VPN instance.

#### Context

After an interface is bound to an L3VPN instance and the CAR is deployed on the interface through QoS profile application, you can run this command to check QoS profile statistics on the interface.


#### Procedure

1. Run the [**display qos-profile statistics vpn-instance**](cmdqueryname=display+qos-profile+statistics+vpn-instance)**vpnname** { **inbound** | **outbound** } [ **verbose** ] command to check QoS profile statistics on all interfaces bound to an L3VPN instance.