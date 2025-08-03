Setting an Aging Time for Dynamic Router Ports
==============================================

Setting an Aging Time for Dynamic Router Ports

#### Context

A router port sends IGMP Report/Leave messages to and receives multicast packets from an upstream Layer 3 device. With IGMP snooping configured, a device can dynamically learn router ports and monitor the delivery of multicast data from the upstream device in real time. If a dynamic router port does not receive an IGMP General Query or a PIM Hello message before the port times out (due to network congestion or instability), the device deletes the port from the router port list. This may cause multicast data transmission failures. To address this issue, you can set a larger aging time for router ports.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Set an aging time for dynamic router ports.
   
   
   ```
   [igmp snooping router-aging-time](cmdqueryname=igmp+snooping+router-aging-time) routerAgingTimeValue
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```