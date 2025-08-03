Configuring NQA for IPv4 Static Routes
======================================

If an IPv4 static route is associated with a network quality analysis (NQA) test instance, NQA tests the link status periodically. If NQA detects a fault along the associated IPv4 static route, the IPv4 static route is deleted, and traffic is switched to another route.

#### Usage Scenario

On live networks, the link status of IPv4 static routes must be monitored in real time so that a link switchover can be performed immediately if a link fails. Bidirectional Forwarding Detection (BFD) for IPv4 static routes can implement detection within milliseconds. However, BFD for IPv4 static routes requires that both ends of a link support BFD.

NQA for IPv4 static routes can monitor the link status of static routes as long as one end supports NQA.

If a link fails, an NQA test instance immediately detects the fault and instructs the routing management module to delete the IPv4 static route associated with the NQA test instance from the IP routing table. Traffic is then forwarded over another link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, NQA test instances of only the ICMP or TCP type can be associated with static routes to implement fast fault detection.



#### Pre-configuration Tasks

Before configuring NQA for IPv4 static routes, configure parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is up.


#### Procedure

* Configure an NQA test instance of the ICMP or TCP type.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
     
     An NQA test instance is created, and the test instance view is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Running the [**undo nqa all-test-instance**](cmdqueryname=undo+nqa+all-test-instance) command will delete the parameters of the NQA test instance bound to the static route. As a result, the static route status may change, and services may be interrupted.
  3. Run [**test-type**](cmdqueryname=test-type) { **icmp** | **tcp** }
     
     The type of the test instance is set to ICMP or TCP.
  4. Run [**destination-address**](cmdqueryname=destination-address) **ipv4** *destAddress*
     
     A destination address is configured.
     
     In an NQA test instance, you can specify the destination end by running the [**destination-address**](cmdqueryname=destination-address) command to configure a destination address for the NQA test instance.
  5. Run any of the following commands to start an NQA test instance:
     + [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **delay** { **seconds** *second* | *hh:mm:ss* } [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **now** [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
     + [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** { *yyyy/mm/dd* | *yyyy-mm-dd* } ] [ **end** { *yyyy/mm/dd* | *yyyy-mm-dd* } ]
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For details of optional procedures when configuring an ICMP NQA test instance, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - System Monitor*.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Associate an IPv4 static route with an NQA test instance.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Perform either of the following operations to associate an IPv4 static route with the NQA test instance.
     
     + To configure an IPv4 static route on the public network and associate the route with an NQA test instance, run the [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ] \* **track nqa** *admin-name* *test-name* [ **description** *text* ] command.
     + To configure an IPv4 static route on a VPN and associate the route with an NQA test instance, run the [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *nexthop-address* [ **public** ] | *interface-type* *interface-number* [ *nexthop-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-address* } [ **preference** *preference* | **tag** *tag* ] \* **track nqa** *admin-name* *test-name* [ **description** *text* ] command.
  3. Run [**commit**](cmdqueryname=commit)The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) Precautions for associating a static route with an NQA test instance are as follows:
     + The destination address of an NQA test instance cannot be the destination address of an associated static route.
     + If the static route associated with one NQA test instance is associated with another NQA test instance, the association between the static route and the original NQA test instance is deleted.
     + An NQA test instance must have been created before you associate it with a static route.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **|** **include** **nqa** command to check the configurations of NQA for static routes.
* Run the [**display nqa results**](cmdqueryname=display+nqa+results) [ **test-instance** *admin-name* *test-name* ] command to check the NQA test results.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The NQA test results cannot be displayed automatically. You need to run the [**display nqa results**](cmdqueryname=display+nqa+results) command to view the results.