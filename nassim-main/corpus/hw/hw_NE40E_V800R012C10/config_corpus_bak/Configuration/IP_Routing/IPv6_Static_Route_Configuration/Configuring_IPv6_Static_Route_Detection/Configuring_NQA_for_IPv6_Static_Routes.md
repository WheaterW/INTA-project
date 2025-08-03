Configuring NQA for IPv6 Static Routes
======================================

If an IPv6 static route is associated with a network quality analysis (NQA) test instance, NQA tests the link status periodically. If NQA detects a fault along the associated IPv6 static route, the IPv6 static route is deleted, and traffic is switched to another route.

#### Usage Scenario

On live networks, the status of IPv6 static routes needs to be monitored in real time to ensure network stability. If the link status changes, a primary/backup link switchover is performed. Bidirectional Forwarding Detection (BFD) for IPv6 static routes can implement detection within milliseconds. However, BFD for IPv6 static routes requires that both ends of a link support BFD.

NQA for IPv6 static routes can monitor the link status of static routes as long as one end supports NQA.

If a link fails, an NQA test instance immediately detects the fault and instructs the routing management module to delete the IPv6 static route associated with the NQA test instance from the IPv6 routing table. Traffic is then forwarded over another link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, NQA test instances of only the ICMP or TCP type can be associated with static routes to implement fast fault detection.


#### Pre-configuration Tasks

Before configuring NQA for IPv6 static routes, configure parameters of the link layer protocol and IPv6 addresses for interfaces and ensure that the link layer protocol on the interfaces is up.


#### Procedure

1. Configure an NQA test instance of the ICMP or TCP type.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name* *test-name*
      
      An NQA test instance is created, and the test instance view is displayed.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Running the [**undo nqa all-test-instance**](cmdqueryname=undo+nqa+all-test-instance) command will delete the parameters of the NQA test instance bound to the static route. As a result, the static route status may change, and services may be interrupted.
   3. Run [**test-type**](cmdqueryname=test-type) { **icmp** | **tcp** }
      
      The type of the test instance is set to ICMP or TCP.
   4. Run [**destination-address**](cmdqueryname=destination-address) **ipv6** *destAddress6*
      
      A destination address is configured.
      
      In an NQA test instance, you can specify the destination end by running the [**destination-address**](cmdqueryname=destination-address) command to configure a destination address for the NQA test instance.
   5. Run any of the following commands to start an NQA test instance:
      * [**start**](cmdqueryname=start) **at** [ *yyyy/mm/dd* ] *hh:mm:ss* [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
      * [**start**](cmdqueryname=start) **delay** { **seconds** *second* | *hh:mm:ss* } [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
      * [**start**](cmdqueryname=start) **now** [ **end** { **at** [ *yyyy/mm/dd* ] *hh:mm:ss* | **delay** { **seconds** *second* | *hh:mm:ss* } | **lifetime** { **seconds** *second* | *hh:mm:ss* } } ]
      * [**start**](cmdqueryname=start) **daily** *hh:mm:ss* **to** *hh:mm:ss* [ **begin** { *yyyy/mm/dd* | *yyyy-mm-dd* } ] [ **end** { *yyyy/mm/dd* | *yyyy-mm-dd* } ]
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For details of optional procedures when configuring an ICMP NQA test instance, see the *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - System Monitor*.
   6. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
2. Associate an IPv6 static route with an NQA test instance.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run either of the following commands as required to associate an IPv6 static route with an NQA test instance:
      
      * To associate an IPv6 static route with an NQA test instance on the public network, run the [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* } [ **preference** *preference* | **tag** *tag* ] \* **track nqa** *admin-name* *test-name* [ **description** *text* ] command.
      * To associate an IPv6 static route with an NQA test instance in a VPN instance, run the [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] } [ **preference** *preference* | **tag** *tag* ]\* **track nqa** *admin-name* *test-name* [ **description** *text* ] command.
   3. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) Precautions for associating a static route with an NQA test instance are as follows:
      * The destination address of an NQA test instance cannot be the destination address of an associated static route.
      * If the static route associated with one NQA test instance is associated with another NQA test instance, the association between the static route and the original NQA test instance is deleted.
      * An NQA test instance must have been created before you associate it with a static route.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **|** **include** **nqa** command to check the configurations of NQA for IPv6 static routes.
* Run the [**display nqa results**](cmdqueryname=display+nqa+results) [ **test-instance** *admin-name* *test-name* ] command to check the NQA test results.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The NQA test results cannot be displayed automatically. You need to run the [**display nqa results**](cmdqueryname=display+nqa+results) command to view the results.