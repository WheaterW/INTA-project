Defining a Traffic Behavior and Configuring Actions
===================================================

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

#### Context

A device supports various types of actions for a traffic behavior. You can configure one or more types of actions as required.


#### Procedure

* Configure packet filtering actions.
  
  
  
  Perform the following configurations on the Router.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Run [**permit | deny**](cmdqueryname=permit+%7C+deny)
     
     
     
     The device is enabled to permit or deny packets.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If both the **if-match any** and **deny** commands are configured on a device, the device denies all packets, including protocol packets, that flow through an interface. Therefore, exercise caution when configuring both the commands.
     
     If the permit or deny action is configured in both the **rule** command and the traffic behavior view, only packets that are permitted by the **rule** command are processed according to the configured traffic behavior. If the deny action is configured in either the **rule** command or the traffic behavior view, all matched packets are discarded.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a traffic policing action.
  
  
  
  Perform the following configurations on the Router.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Run [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp-value* | **service-class** *class* **color** *color* ] } ] \* [ **summary** ] [ **color-aware** ] [ **limit-type pps** ]
     
     
     
     A traffic policing action is configured.
     
     
     
     After you configure a traffic policing action for a traffic policy, the traffic policy can be applied to incoming or outgoing traffic on an interface.
     
     Applying a traffic policy configured with traffic policing to an interface affects the original [**qos car**](cmdqueryname=qos+car) command.
     
     If this command is run more than once, the last configuration overrides the previous one.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the service class of a packet is re-marked as EF, BE, CS6, or CS7, the packet can be re-marked only green.
     
     If there are a large number of access users and CAR resource specifications need to be increased, run the **car resource-pool enhanced mode** command to change the CAR resource allocation mode to enhanced.
  4. Run [**user-queue**](cmdqueryname=user-queue) **cir** *cir-value* [ [ **pir** *pir-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **flow-mapping** *mapping-name* ] | [ **user-group-queue** *group-name* ] | [ **service-template** *service-template-name* ] ]\*
     
     
     
     Class-based HQoS scheduling is configured for the traffic behavior.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**user-queue**](cmdqueryname=user-queue) and [**car**](cmdqueryname=car) commands cannot both be configured in the same traffic behavior.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a packet priority.
  
  
  
  Perform the following configurations on the Router.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Perform the following configurations as required.
     
     
     + To re-mark the precedence of IP packets, run the [**remark ip-precedence**](cmdqueryname=remark+ip-precedence) *ip-precedence* command.
     + To re-mark the DSCP value of IP packets, run the [**remark**](cmdqueryname=remark) [ **ipv6** ] **dscp** *dscp-value* command.
     + To re-mark the priority of VLAN packets, run the [**remark 8021p**](cmdqueryname=remark+8021p) *8021p-value* command.
     + To re-mark the ToS value of IP packets, run the [**remark tos**](cmdqueryname=remark+tos) *tos* command.
     + To re-mark the DF value of IP packets, run the [**remark ip-df**](cmdqueryname=remark+ip-df) command.
     + To re-mark the TTL value of IP packets, run the [**remark ttl**](cmdqueryname=remark+ttl) *ttl-value* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To re-mark the DSCP value of IPv6 packets, run the [**remark ipv6 dscp**](cmdqueryname=remark+ipv6+dscp) *dscp-value* command.
     
     The [**remark ip-df**](cmdqueryname=remark+ip-df) command is supported only on the Router.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure forcible traffic classification.
  1. Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color*
     
     
     
     Packets with a certain CoS are colored.
  2. (Optional) Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color* **track** { **master** | **slave** } **bfd-session** **session-name** *bfd-session-name*
     
     
     
     The CoS and color of packets matching the traffic policy are marked based on the status of a specified BFD session.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set packet forwarding actions.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  + Redirecting packets to a public network LSP can be configured only on the ingress node of the MPLS network, and cannot be configured on other nodes such as transit or egress.
  + Redirecting packets to a public network LSP can be configured only when a single MPLS label is applied.
  
  Perform the following configurations on the Router.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Perform the following configurations as required.
     
     
     + To directly forward packets without redirecting them, run the **permit** command in the traffic behavior view.
     + To directly drop packets without redirecting them, run the **deny** command in the traffic behavior view.
       
       The deny action is mutually exclusive with other traffic actions. Traffic that is configured with the deny action cannot be further processed unless the traffic is configured with the permit action.
     + To configure the IPv4 address and outbound interface, VPN instance, and NQA test instance on a single next hop for redirecting IPv4 packets, run the following commands:
       - [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **interface** *interface-type* *interface-number* [ **route-forward** ]
       - [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
       - [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
     + To configure the IPv4 addresses and outbound interfaces, VPN instances, and NQA test instances on multiple next hops for redirecting IPv4 packets, run the following commands:
       - [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **interface** *interface-type* *interface-number* } &<2-42> [ **loadbalance** ] [ **route-forward** ] [ **unequal-cost** ]
       - [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* } &<2-42> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
       - [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] } &<2-42> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] [ **non-revertive** ]
     + To configure the IPv6 address and outbound interface, VPN instance, and NQA test instance on a single next hop for redirecting IPv6 packets, run the following commands:
       - [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ip-address* **interface** *interface-type* *interface-number* [ **route-forward** ]
       - [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
       - [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
     + To configure the IPv6 addresses and outbound interfaces, VPN instances, and NQA test instances on multiple next hops for redirecting IPv6 packets, run the following commands:
       - [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ip-address* **interface** *interface-type* *interface-number* } &<2-16> [ **loadbalance** [ **sip-hash** ] ] [ **route-forward** ] [ **pri-type common** ] [ **unequal-cost** ]
       - [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* } &<2-16> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
       - [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] } &<2-16> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
     + In a scenario in which packets are redirected to a single next hop whose IP address matches a default route or a black-hole route, if you want packets to be forwarded based on the destination IP address, run either of the following commands:
       - [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **deny** ]
       - [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
     + In a scenario in which packets are redirected to multiple next hops whose IP addresses match default or black-hole routes, if you want packets to be forwarded based on the destination IP address, run either of the following commands:
       - [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* } &<2-42> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **deny** ]
       - [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ip-address* } &<2-16> [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ]
     + To redirect IPv4 or IPv6 packets to be forwarded using private network routes to public network routes' outbound interfaces, run the [**redirect**](cmdqueryname=redirect) { **ip** | **ipv6** } **public-network** command.
     + To redirect IP packets to the public network LSP, run the [**redirect lsp public**](cmdqueryname=redirect+lsp+public) *dest-ipv4-address* [ *nexthop-address* | **interface** *interface-type* *interface-number* | **secondary** ] command.
     + To redirect packets to a specified VPN group, run the [**redirect vpn-group**](cmdqueryname=redirect+vpn-group) *vpn-group-name* command.
     + To redirect packets to a specified VSI, run the [**redirect vsi**](cmdqueryname=redirect+vsi) *vsi-name* command.
     + To redirect IPv4 packets to a specified outbound interface, run the [**redirect to interface**](cmdqueryname=redirect+to+interface) { *interface-name* | *interface-type* *interface-number* } [ **route-forward** ] command.
     + To redirect IPv6 packets to a specified outbound interface, run the [**redirect ipv6 to interface**](cmdqueryname=redirect+ipv6+to+interface) { *interface-name* | *interface-type* *interface-number* } [ **route-forward** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In IPv6 application, the IP address of the next hop specified for a Discard policy must be an IPv6 link-local address or an IPv6 unicast address; the IP address of the next hop specified for a Forward policy can be only an IPv6 unicast address.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the load balancing mode of packets.
  
  
  
  Perform the following configurations on the Router.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
     
     
     
     A traffic behavior is configured and its view is displayed.
  3. Run [**load-balance**](cmdqueryname=load-balance) { **flow** [ **l2** | **l3** ] | **packet** }
     
     
     
     The load balancing mode of packets is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.