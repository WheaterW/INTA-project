(Optional) Adjusting the Hold-up Period for Trunk or Global-VE Member Interfaces to Forward Multicast Traffic
=============================================================================================================

To implement better forwarding for multicast traffic on trunk or Global-VE member interfaces, you can configure this function as required.

#### Usage Scenario

When the outbound interface of multicast traffic is a trunk or Global-VE interface, you can adjust the hold-up period for member interfaces to forward multicast traffic.


#### Prerequisites

Before adjusting the hold-up period for trunk or Global-VE member interfaces to forward multicast traffic, configure an IP-Trunk, Eth-Trunk, or Global-VE interface as the outbound interface of multicast traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface Eth-Trunk**](cmdqueryname=interface+Eth-Trunk) *trunk-id* or [**interface IP-Trunk**](cmdqueryname=interface+IP-Trunk) *trunk-id* or [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number*
   
   
   
   The trunk interface view or Global VE interface view is displayed.
3. Run [**multicast hold-up**](cmdqueryname=multicast+hold-up) *hold-up-time*
   
   
   
   The hold-up period for trunk or Global-VE member interfaces to forward multicast traffic is adjusted.
   
   By default, multicast traffic is forwarded 2 seconds after the physical state of a trunk or Global-VE member interface changes from down to up. This ensures that no packet is lost during multicast forwarding. When the multicast traffic is heavy, it takes a longer time to deliver multicast forwarding entries to member interfaces. If the default hold-up period cannot meet the requirement, you can run this command to adjust the hold-up period.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.