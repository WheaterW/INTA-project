Resetting BGP Connections
=========================

After modifying BGP configurations, you can reset or softly reset the BGP connections for new configurations to take effect.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting BGP connections interrupts VPN services. Exercise caution when running this command.

After modifying BGP configurations, you can reset or softly reset the BGP connections for new configurations to take effect. Soft reset requires BGP peers to have the route refresh capability. That means BGP peers must support Route-Refresh messages.


#### Procedure

* Run the [**refresh bgp**](cmdqueryname=refresh+bgp) **vpn-instance** *vpn-instance-name* **ipv4-family** { **all** | *peer-address* | **group** *group-name* | **internal** | **external** } { **import** | **export** } command in the user view to trigger the soft reset of the VPN instance IPv4 address family's BGP connections in the inbound or outbound direction, so that the new configurations can take effect.
* Run the [**refresh bgp**](cmdqueryname=refresh+bgp) **vpnv4** { **all** | *peer-address* | **group** *group-name* | **internal** | **external** } { **import** | **export** } command in the user view to trigger the soft reset of the BGP VPNv4 connections in the inbound or outbound direction, so that the new configurations can take effect.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpn-instance** *vpn-instance-name* **ipv4-family** { *as-number* | *peer-address* | **group** *group-name* | **all** | **internal** | **external** } command in the user view to reset the BGP connections of the VPN instance IPv4 address family, so that the new configurations can take effect.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) **vpnv4** { *as-number* | *peer-address* | **group** *group-name* | **all** | **internal** | **external** } command in the user view to reset the BGP VPNv4 connections, so that the new configurations can take effect.
* Run the [**reset bgp**](cmdqueryname=reset+bgp) ****vpnv4**** [ **ipv4-address** | **ipv6-address** ] **slow-peer** command in the user view to reset the BGP connection with a specified slow peer for the new configuration to take effect.