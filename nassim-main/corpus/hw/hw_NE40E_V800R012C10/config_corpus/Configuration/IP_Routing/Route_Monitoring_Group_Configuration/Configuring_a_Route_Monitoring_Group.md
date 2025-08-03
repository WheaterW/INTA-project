Configuring a Route Monitoring Group
====================================

You can add network-side routes to a route monitoring group and associate access-side service modules with it so that the service modules can perform primary/backup link switchovers upon route changes in the group in a dual-device hot backup scenario. This mechanism can prevent traffic congestion or loss.

#### Procedure

* Configure a route monitoring group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip route-monitor-group**](cmdqueryname=ip+route-monitor-group) *group-name*
     
     
     
     A route monitoring group is created, and the route monitoring group view is displayed.
  3. Run [**track ip route**](cmdqueryname=track+ip+route) [ **vpn-instance** *vpn-instance-name* ] *destination* { *mask* | *mask-length* } [ **down-weight** *down-weight-value* ]
     
     
     
     A route is added to the route monitoring group.
     
     
     
     To add more routes to the route monitoring group, repeat this step.
  4. (Optional) Run [**trigger-up-delay**](cmdqueryname=trigger-up-delay) *delay-value*
     
     
     
     A delay is configured for the RM module to instruct the service module associated with the route monitoring group to perform a switchback.
     
     
     
     When a route in a route monitoring group becomes active again, the RM module needs to re-deliver the route to the forwarding table and create forwarding entries, which takes some time. If the RM module immediately instructs the service module to perform a link switchover, packet loss may occur. To prevent this problem, run the [**trigger-up-delay**](cmdqueryname=trigger-up-delay) command to configure a delay for the RM module to instruct the service module to perform a link switchback so that the RM module instructs the service module to perform a link switchback after forwarding entries are created.
     
     If the value of *delay-value* is set to 0, the RM module instructs the service module to perform a link switchback immediately when the down-weight sum of the route monitoring group falls below the switchback threshold.
  5. Run [**monitor enable**](cmdqueryname=monitor+enable)
     
     
     
     The route monitoring group is enabled.
     
     
     
     When a large number of routes are added to or deleted from a route monitoring group, the down-weight sum of the route monitoring group may change frequently, which in turn leads to service flapping of the service modules associated with the route monitoring group. To prevent such service flapping, run the [**undo monitor enable**](cmdqueryname=undo+monitor+enable) command to disable the route monitoring group so that it is dissociated from all service modules. After the configuration is complete, run the [**monitor enable**](cmdqueryname=monitor+enable) command to re-associate the route monitoring group with the service modules.
  6. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the route monitoring group view.
  7. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The access-side interface view is displayed.
  8. (Optional) Run [**track route-monitor-group**](cmdqueryname=track+route-monitor-group) *groupName* [ **trigger-down-weight** *downWeight* ]
     
     
     
     The interface is configured to track the route monitoring group.
     
     
     
     An interface that tracks a route monitoring group is called a track interface. To allow multiple interfaces to track the same IPv4 route monitoring group, run this command on the interfaces one by one.
     
     After an IPv4 route monitoring group is created and routes are added to the group, to use the IPv4 route monitoring group to trigger the status change of a user-side interface, run this command to associate the interface with the IPv4 route monitoring group. When the down-weight sum of the IPv4 route monitoring group reaches the set *downWeight* value, the status of the interface is set to Down, and services are switched to the backup link. When the down-weight sum of the IPv4 route monitoring group falls below the configured *downWeight* value, the status of the interface is set to Up again, and services are switched back to the primary link. In this manner, the user-side interface can detect network-side route faults in time, ensuring user-side service reliability.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an IPv6 route monitoring group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 route-monitor-group**](cmdqueryname=ipv6+route-monitor-group) *group-name*
     
     
     
     An IPv6 route monitoring group is created, and the route monitoring group view is displayed.
  3. Run [**track ipv6 route**](cmdqueryname=track+ipv6+route) [ **vpn-instance** *vpn-instance-name* ] *destination* *mask-length* [ **down-weight** *down-weight-value* ]
     
     
     
     An IPv6 route is added to the IPv6 route monitoring group.
     
     
     
     To add more IPv6 routes to the route monitoring group, repeat this step.
  4. (Optional) Run [**trigger-up-delay**](cmdqueryname=trigger-up-delay) *delay-value*
     
     
     
     A delay is configured for the IPv6 RM module to instruct the service module associated with the IPv6 route monitoring group to perform a switchback.
     
     
     
     When an IPv6 route in an IPv6 route monitoring group becomes active again, the IPv6 RM module needs to re-deliver the route to the forwarding table and create forwarding entries, which takes some time. If the IPv6 RM module immediately instructs the service module to perform a link switchover, packet loss may occur. To prevent this problem, run the [**trigger-up-delay**](cmdqueryname=trigger-up-delay) command to configure a delay for the IPv6 RM module to instruct the service module to perform a link switchback so that the RM module instructs the service module to perform a link switchback after forwarding entries are created.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the value of *delay-value* is set to 0, the IPv6 RM module instructs the service module to perform a link switchback immediately when the down-weight sum of the route monitoring group falls below the switchback threshold. In the case of immediate switchback, packet loss may occur. To prevent this problem, run the **trigger-up-delay** command to configure a delay for the RM module to instruct the service module to perform a link switchback so that the RM module instructs the service module to perform a link switchback after forwarding entries are created.
  5. Run [**monitor enable**](cmdqueryname=monitor+enable)
     
     
     
     The IPv6 route monitoring group is enabled.
     
     
     
     When a large number of IPv6 routes are added to or deleted from an IPv6 route monitoring group, the down-weight sum of the route monitoring group may change frequently, which in turn leads to service flapping of the service modules associated with the route monitoring group. To prevent such service flapping, run the [**undo monitor enable**](cmdqueryname=undo+monitor+enable) command to disable the IPv6 route monitoring group so that it is dissociated from all service modules. After the configuration is complete, run the [**monitor enable**](cmdqueryname=monitor+enable) command to re-associate the route monitoring group with the service modules.
  6. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the route monitoring group view.
  7. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The access-side interface view is displayed.
  8. (Optional) Run [**track ipv6 route-monitor-group**](cmdqueryname=track+ipv6+route-monitor-group) *groupName* [ **trigger-down-weight** *downWeight* ]
     
     
     
     The interface is configured to track the IPv6 route monitoring group.
     
     
     
     An interface that tracks a route monitoring group is called a track interface. To allow multiple interfaces to track the same IPv6 route monitoring group, run this command on the interfaces one by one.
     
     After an IPv6 route monitoring group is created and routes are added to the group, to use the IPv6 route monitoring group to trigger the status change of a user-side interface, run this command to associate the interface with the IPv6 route monitoring group. When the down-weight sum of the IPv6 route monitoring group reaches the set *downWeight* value, the status of the interface is set to Down, and services are switched to the backup link. When the down-weight sum of the IPv6 route monitoring group falls below the configured *downWeight* value, the status of the interface is set to Up again, and services are switched back to the primary link. In this manner, the user-side interface can detect network-side route faults in time, ensuring user-side service reliability.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Example

After configuring the route monitoring group, check the configurations.

* Run the [**display ip route-monitor-group**](cmdqueryname=display+ip+route-monitor-group) [ *group-name* ] command to check route monitoring group information.
* Run the [**display ip route-monitor-group track-route**](cmdqueryname=display+ip+route-monitor-group+track-route) [ **vpn-instance** *vpn-instance-name* ] *dest-address* { *mask* | *mask-length* } command to check information about all route monitoring groups to which a route has been added.
* Run the [**display ipv6 route-monitor-group**](cmdqueryname=display+ipv6+route-monitor-group) [ *group-name* ] command to check IPv6 route monitoring group information.
* Run the [**display ipv6 route-monitor-group track-route**](cmdqueryname=display+ipv6+route-monitor-group+track-route) [ **vpn-instance** *vpn-instance-name* ] *destination* *mask-length* command to check information about all IPv6 route monitoring groups to which a route has been added.


#### Follow-up Procedure

Associate service modules with the status of a route monitoring group in a dual-device hot backup scenario. This prevents traffic overload and forwarding failures when the primary link on the network side fails and thus improves user experience.