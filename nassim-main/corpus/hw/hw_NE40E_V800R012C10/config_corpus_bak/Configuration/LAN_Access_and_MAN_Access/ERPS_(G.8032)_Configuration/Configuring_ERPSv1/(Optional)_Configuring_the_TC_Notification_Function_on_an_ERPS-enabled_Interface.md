(Optional) Configuring the TC Notification Function on an ERPS-enabled Interface
================================================================================

When an ERPS-enabled interface has sub-interfaces bound to a BD or VPLS, to allow the interface to immediately instruct these sub-interfaces to update their ARP and MAC address entries after the interface receives topology change (TC) packets, configure the TC change notification function on the interface.

#### Prerequisites

An ERPS ring has connected to a VPLS or BD network through sub-interfaces.


#### Context

In normal situations, when the topology of an ERPS ring changes and an interface receives TC packets, the ERPS ring reselects an interface for blocking, and accordingly all devices update their ARP and MAC address entries. However, if an ERPS-enabled interface has BD- or VSI-bound sub-interfaces, the sub-interfaces cannot detect the TC event immediately. As a result, other devices in the BD or VSI cannot be promptly instructed to update their ARP and MAC address entries. To prevent this problem, the TC change notification function can be configured on the ERPS-enabled interface. If the interface receives TC packets, the interface instructs its sub-interfaces to update their ARP and MAC address entries.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the ERPS ring interface view.
   
   
   * If a sub-interface of the interface is bound to a VSI or is bound to a BD for EVPN access, run the [**erps vpls-subinterface enable**](cmdqueryname=erps+vpls-subinterface+enable) command to configure the TC notification function.
   * If a sub-interface of the interface is bound to a BD, run the [**erps bd-subinterface enable**](cmdqueryname=erps+bd-subinterface+enable) command to configure the TC notification function.
   * If a sub-interface of the interface is bound to a BD that is bound to a VSI, run the [**erps bd-subinterface enable**](cmdqueryname=erps+bd-subinterface+enable) command to configure the TC notification function, so that the VSI can update ARP and MAC entries.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.