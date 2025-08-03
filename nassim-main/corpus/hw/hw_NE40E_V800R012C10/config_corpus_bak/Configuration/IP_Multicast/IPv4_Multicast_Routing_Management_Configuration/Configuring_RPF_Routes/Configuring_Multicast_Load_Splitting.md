Configuring Multicast Load Splitting
====================================

Multicast load splitting applies to the scenario in which multiple equal-cost unicast routes of the same type exist. In such a case, multicast load splitting can be performed based on configured policies to optimize the transmission of multiple multicast data flows.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The configuration related to the VPN instance applies only to the provider edge (PE). If you want to configure multicast load splitting for a VPN instance on the PE, you must perform the configuration in the VPN instance view. In other cases, you need to perform the configuration in the public network instance view.

The Reverse Path Forwarding (RPF) check is a basis of multicast routing. Based on RPF rules, the Router selects a unique route for multicast data forwarding. If multicast traffic is overloaded, network congestion may occur and the multicast service is thus interrupted.

The multicast load splitting function extends multicast routing rules, and multicast routing no long fully depends on the RPF check. If there are multiple equal-cost optimal routes, multicast traffic is load split to these equal-cost routes.


#### Procedure

* Configure multicast load splitting in the public network instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast load-splitting**](cmdqueryname=multicast+load-splitting) { **stable-preferred** | **source** | **group** | **source-group** | **balance-ucmp** }
     
     
     
     Multicast load splitting is configured.
     
     
     
     + **stable-preferred**: indicates stable-preferred load splitting. This policy applies to a stable multicast networking.
       
       If stable-preferred is specified, the Router automatically adjusts and balances the entries when equal-cost routes are added or deleted; however, the Router does not automatically adjust and balance the entries when multicast routing entries are deleted.
     + **group**: indicates group address-based load splitting. This policy applies to the scenario of one source to multiple groups.
     + **source**: indicates source address-based load splitting. This policy applies to the scenario of one group to multiple sources.
     + **source-group**: indicates source and group addresses-based load splitting. This policy applies to the scenario of multiple sources to multiple groups.
     + **balance-ucmp**: Indicates link bandwidth-based load splitting. This policy is applicable to the scenario in which links have different bandwidth.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure multicast load splitting in a VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**multicast load-splitting**](cmdqueryname=multicast+load-splitting) { **stable-preferred** | **source** | **group** | **source-group** | **balance-ucmp** }
     
     
     
     Multicast load splitting is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.