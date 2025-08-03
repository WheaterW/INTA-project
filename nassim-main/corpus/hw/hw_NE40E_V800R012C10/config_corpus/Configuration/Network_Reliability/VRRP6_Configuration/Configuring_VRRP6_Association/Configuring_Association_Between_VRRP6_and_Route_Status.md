Configuring Association Between VRRP6 and Route Status
======================================================

A VRRP6 group can be configured to track the status of an uplink route. If the tracked route is withdrawn or becomes inactive, the VRRP6 group is notified of the change and rapidly performs a master/backup VRRP6 switchover. This shortens the duration of traffic interruptions.

#### Context

To improve device reliability, two user gateways working in master/backup mode are connected to a Layer 3 network, and VRRP6 is enabled on these gateways to determine their master/backup status. If an uplink route to a network becomes unreachable, user hosts cannot detect the change and still uses the route to transmit traffic. This may cause service traffic loss.

To resolve the problem, a VRRP6 group can be configured to track the route status. A VRRP6 group can monitor an uplink route. If the uplink route is withdrawn or becomes inactive, the VRRP6 group is instructed to reduce the master's priority to trigger a master/backup switchover.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where the VRRP6 group resides is displayed.
3. Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-ID* **track ipv6 route** *ip-address* *mask-length* [ **vpn-instance** *vpn-instance-name* ] [ **reduced** *value-reduced* ]
   
   
   
   The VRRP6 group is configured to track the route status.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.