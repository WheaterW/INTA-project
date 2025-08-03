Configuring NQA Group for IPv6 Static Route
===========================================

After an IPv6 static route is associated with an NQA group, if the NQA group detects a link fault, it withdraws the IPv6 static route, triggering traffic switching and ensuring network stability.

#### Usage Scenario

On live networks, the status of IPv6 static routes needs to be monitored in real time to ensure network stability. If the link status changes, a primary/backup link switchover is performed. NQA for IPv6 static route can monitor only a single link. To enable a static route to use NQA test instances to monitor multiple links, you can bind these NQA test instances to the same NQA group and associate the static route with the NQA group.

If a link fault occurs, the NQA group can collect statistics on the status changes of all NQA test instances bound to the NQA group and determine whether to change its status according to the configured operation. When the status of the NQA group changes, the NQA group instructs the RM module to delete the IPv6 static route associated with the NQA group from the IP routing table. Traffic is then forwarded along another path, implementing a link switchover.


#### Pre-configuration Tasks

Before configuring NQA group for IPv6 static route, complete the following task:

* Configure link-layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol of each interface is up.

#### Procedure

* Configure multiple NQA test instances of the ICMP or TCP type.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
     
     An NQA test instance is created, and the test instance view is displayed.
  3. Run [**test-type**](cmdqueryname=test-type) { **icmp** | **tcp** }
     
     The test instance type is set to ICMP or TCP.
  4. Run [**destination-address**](cmdqueryname=destination-address) **ipv6** *destAddress*6
     
     A destination address is configured.
     
     In an NQA test instance, you can specify the destination end by running the [**destination-address**](cmdqueryname=destination-address) command to configure a destination address for the NQA test instance.
  5. Run any of the following commands to start an NQA test instance:
     + [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **delay** { **seconds** *second* | *hh:mm:ss* } [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **now** [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** { *yyyy/mm/dd* | *yyyy-mm-dd* } ] [ **end** { *yyyy/mm/dd* | *yyyy-mm-dd* } ]
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For more optional configurations of NQA test instances, see the *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - System Monitor*.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
  7. Repeat the preceding steps to configure multiple NQA test instances of the ICMP or TCP type.
* Bind the preceding NQA test instances to an NQA group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nqa group**](cmdqueryname=nqa+group) *group-name*
     
     
     
     An NQA group is created, and the NQA group view is displayed.
  3. Run [**nqa test-instance**](cmdqueryname=nqa+test-instance) *admin-name* *test-name*
     
     
     
     An NQA test instance is bound to the NQA group.
     
     
     
     Run this command multiple times to bind multiple NQA test instances to the NQA group.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The NQA test instances bound to the same NQA group must be of the same type: ICMP or TCP.
  4. Run [**operator**](cmdqueryname=operator) { **and** | **or** }
     
     
     
     The operation type between test instances in the NQA group is set to AND or OR.
  5. (Optional) Run [**description**](cmdqueryname=description) *string*
     
     
     
     A description is configured for the NQA group.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind an IPv6 static route to the NQA group.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Bind an IPv6 static route to the NQA group.
     
     + To configure an IPv6 static route on the public network and associate the route with the NQA group, run the [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ] \* **track nqa-group** *group-name* [ **description** *text* ] command.
     + To configure an IPv6 static route on a VPN and associate the route with the NQA group, run the [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *nexthop-address* [ **public** ] | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ] \* **track nqa-group** *group-name* [ **description** *text* ] command.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) When configuring NQA group for IPv6 static route, pay attention to the following points:
     + The destination address of an NQA group cannot be the destination address of an associated static route.
     + If a static route is associated with another NQA group, the association between the static route and the current NQA group is removed.
     + A static route cannot be associated with an NQA group that has not been created.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display static-route ipv6 routing-table**](cmdqueryname=display+static-route+ipv6+routing-table) command to check information about IPv6 static routes.
* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **|** **include** **nqa-group** command to check the configurations of NQA group for IPv6 static route.
* Run the [**display nqa group**](cmdqueryname=display+nqa+group) [ *group-name* ] command to check the test result of the NQA group.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The test result of the NQA group cannot be displayed automatically. You need to run the [**display nqa group**](cmdqueryname=display+nqa+group) command to view the result.