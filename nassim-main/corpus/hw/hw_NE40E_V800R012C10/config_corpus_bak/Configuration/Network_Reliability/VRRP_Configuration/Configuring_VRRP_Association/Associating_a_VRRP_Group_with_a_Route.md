Associating a VRRP Group with a Route
=====================================

A VRRP group can track an uplink route that is connected to a network. If the tracked route is withdrawn or becomes inactive, the VRRP group is notified of the change and rapidly performs a master/backup VRRP switchover. This process shortens traffic interruptions.

#### Context

To improve device reliability, two user gateways work in master/backup mode and are connected to a Layer 3 network. VRRP is enabled on these gateways to determine their master/backup status. If an uplink route to a network becomes unreachable, user hosts cannot detect the change and still uses the route to transmit traffic. As a result, service traffic loss occurs.

Associating the VRRP group with the route can prevent service traffic loss. The VRRP group can be configured to track the uplink route to the network. If the route is withdrawn or becomes inactive, the route management (RM) module notifies the VRRP group of the change. After receiving the notification, the VRRP group changes its master device's VRRP priority and performs a master/backup switchover.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track ip route** *ip-address* { *mask-address* | *mask-length* } [ **vpn-instance** *vpn-instance-name* ] [ **reduced** *value-reduced* ]
   
   
   
   The VRRP group is associated with the route.
   
   
   
   **reduced** *value-reduced* specifies the value by which the VRRP priority decreases if the tracked route is withdrawn or becomes inactive. The value is an integer ranging from 1 to 255.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.