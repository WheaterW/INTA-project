Configuring Multicast Load Splitting
====================================

Configuring Multicast Load Splitting

#### Context

RPF checks are essential for multicast routing. According to the rules for selecting RPF routes, a device selects a unique route to forward multicast data. If multicast traffic is overloaded, network congestion may occur, affecting multicast services. With multicast load splitting, multicast routing rules are extended and no longer fully depend on RPF checks. Multicast load splitting applies to scenarios where multiple equal-cost unicast routes of the same type exist. If multiple equal-cost optimal routes are available on a network, multicast data is split based on various policies, instead of being forwarded through only one route that is selected based on RPF check rules. This optimizes network traffic forwarding when multiple multicast data flows exist. In this manner, the transmission quality of multicast data on the network is improved.


#### Procedure

* Public network instance
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable the multicast function.
     
     
     ```
     [multicast routing-enable](cmdqueryname=multicast+routing-enable)
     ```
  3. Configure multicast load splitting.
     
     
     ```
     [multicast load-splitting](cmdqueryname=multicast+load-splitting) { group | source | source-group | stable-preferred | balance-ucmp }
     ```
     
     The load splitting policies are mutually exclusive. You are advised to use one such policy consistently based on your network requirements.
     
     + **group**: indicates group address-based load splitting. This policy applies to scenarios with one source but multiple groups.
     + **source**: indicates source address-based load splitting. This policy applies to scenarios with one group but multiple sources.
     + **source-group**: indicates load splitting based on both source and group addresses. This policy applies to scenarios with multiple sources and multiple groups.
     + **stable-preferred**: indicates stable-preferred load splitting. This policy applies to scenarios requiring stable multicast services.
     + **balance-ucmp**: indicates link bandwidth-based load splitting. This policy applies to scenarios where links have different load bandwidths.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* VPN instance
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VPN instance view.
     
     
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
  3. Enable the IPv4 address family for the VPN instance and enter the VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
  4. Set an RD for the VPN instance IPv4 address family.
     
     
     ```
     [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
     ```
     
     Only after an RD is configured for this family can other configurations be performed for the VPN instance IPv4 address family.
  5. Enable the multicast function.
     
     
     ```
     [multicast routing-enable](cmdqueryname=multicast+routing-enable)
     ```
  6. Configure multicast load splitting.
     
     
     ```
     [multicast load-splitting](cmdqueryname=multicast+load-splitting) { group | source | source-group | stable-preferred | balance-ucmp }
     ```
     
     The load splitting policies are mutually exclusive. You are advised to use one such policy consistently based on your network requirements.
     
     + **group**: indicates group address-based load splitting. This policy applies to scenarios with one source but multiple groups.
     + **source**: indicates source address-based load splitting. This policy applies to scenarios with one group but multiple sources.
     + **source-group**: indicates load splitting based on both source and group addresses. This policy applies to scenarios with multiple sources and multiple groups.
     + **stable-preferred**: indicates stable-preferred load splitting. This policy applies to scenarios requiring stable multicast services.
     + **balance-ucmp**: indicates link bandwidth-based load splitting. This policy applies to scenarios where links have different load bandwidths.![](public_sys-resources/note_3.0-en-us.png) 
     
     Configurations related to VPN instances apply only to PEs. To configure multicast load splitting in a VPN instance on a PE, you must perform the configuration in the VPN instance. For other cases, configurations need to be performed in the public network instance.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```