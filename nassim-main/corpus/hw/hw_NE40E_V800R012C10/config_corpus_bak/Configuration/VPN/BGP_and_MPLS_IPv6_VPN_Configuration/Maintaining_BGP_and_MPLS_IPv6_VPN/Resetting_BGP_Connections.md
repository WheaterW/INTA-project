Resetting BGP Connections
=========================

If a faulty BGP connection needs to be reset or a new BGP connection configuration needs to take effect, you can reset or softly reset the BGP connection.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting BGP connections interrupts VPN services. Exercise caution when running this command.

After changing a BGP connection configuration, you can reset or softly reset the BGP connection for the new configuration to take effect. Soft reset requires BGP peers to be able to refresh routes. That means BGP peers must support Route-Refresh messages.


#### Procedure

* Run the [**refresh bgp**](cmdqueryname=refresh+bgp) **vpnv6** { **all** | *ipv4-address* | **group** *group-name* | **internal** | **external** } { **import** | **export** } command to trigger the soft reset of BGP VPNv6 connections in the inbound or outbound direction.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv6-family** { **all** | *as-number* | *ipv6-address* | **group** *group-name* | **external** } command to reset the BGP connections of a specified VPN instance IPv6 address family.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpnv6** { *as-number* | *ipv4-address* | **group** *group-name* | **all** | **internal** | **external** } command to reset BGP VPNv6 connections.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) ****vpnv6**** [ **ipv4-address** | **ipv6-address** ] **slow-peer** command to reset the BGP VPNv6 connection with the specified slow peer for the new configuration to take effect.