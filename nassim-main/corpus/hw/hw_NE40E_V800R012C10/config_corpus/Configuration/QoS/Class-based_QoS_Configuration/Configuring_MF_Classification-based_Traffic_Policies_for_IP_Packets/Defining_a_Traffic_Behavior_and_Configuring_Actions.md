Defining a Traffic Behavior and Configuring Actions
===================================================

This section describes the traffic behaviors supported by a device and how to configure actions for a traffic behavior.

#### Context

A device supports various types of actions for a traffic behavior. You can configure one or more types of actions as required.


#### Procedure

* Run [**system-view**](cmdqueryname=system-view)
  
  
  
  The system view is displayed.
* Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
  
  
  
  A traffic behavior is configured and its view is displayed.
* Configure a packet filtering action.
  1. Run [**permit**](cmdqueryname=permit) | **deny**
     
     
     
     Packets are permitted or denied.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If both the **if-match any** and **deny** commands are configured, the MF classification function prevents all packets (including protocol packets) from passing through an interface. Therefore, exercise caution when using a combination of the preceding commands.
     
     If the permit or deny action is configured in both the **rule** command and the traffic behavior view, only the packets permitted by the **rule** command are processed based on the traffic behavior. If the deny action is configured in either the **rule** command or the traffic behavior view, all matched packets are discarded.
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a traffic policing action.
  
  
  
  For details, see [Defining a Traffic Behavior and Configuring Traffic Policing Actions](dc_ne_qos_cfg_0010.html) in "Traffic Policing and Traffic Shaping Configuration."
* Configure suppression for broadcast, multicast, and unknown unicast packets.
  1. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } ] \*
     
     
     
     The rate at which broadcast packets are transmitted is restricted.
  2. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } ] \*
     
     
     
     The rate at which multicast packets are transmitted is restricted.
  3. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** { **green** | **yellow** | **red** } ] } ] \*
     
     
     
     The rate at which unknown unicast packets are transmitted is restricted.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  The configured traffic behavior can be applied to the incoming or outgoing traffic on an interface.
  
  After traffic suppression is applied to an interface, the packets matching the rules are processed based on the traffic behavior, and the packets not matching the rules are forwarded.
* Configure forcible traffic classification.
  1. Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color*
     
     
     
     Packets with a certain CoS are colored.
  2. (Optional) Run [**service-class**](cmdqueryname=service-class) *service-class* **color** *color* **track** { **master** | **slave** } **bfd-session** **session-name** *bfd-session-name*
     
     
     
     The CoS and color of packets matching the traffic policy are marked based on the status of a specified BFD session.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure packet re-marking.
  1. IP packets support multiple re-marking actions. Select the corresponding configurations in the following table based on service requirements on the network.
     
     
     
     **Table 1** IP packet re-marking configurations
     | Service Requirement | Configuration Command |
     | --- | --- |
     | The original precedence of packets needs to be changed. | [**remark ip-precedence**](cmdqueryname=remark+ip-precedence) *ip-precedence* |
     | The DSCP value carried in packets needs to be changed. | [**remark**](cmdqueryname=remark) [ **ipv6** ] **dscp** *dscp-value* |
     | The ToS value carried in packets needs to be changed. | [**remark tos**](cmdqueryname=remark+tos) *tos* |
     | Whether packets can be fragmented needs to be set. | [**remark ip-df**](cmdqueryname=remark+ip-df) *dfvalue* |
     | The TE class ID of a flow needs to be identified in SPR-based traffic diversion. | [**remark te-class**](cmdqueryname=remark+te-class) *classid* |
     | 5-tuple-based ACL matching needs to be configured for slice ID allocation. | [**remark network-slice**](cmdqueryname=remark+network-slice) *sliceId* |
     | The TTL value of packets needs to be changed. | [**remark ttl**](cmdqueryname=remark+ttl) *ttl-value* |
     | IPv6 APN information needs to be marked in packets. | **remark apn-id-ipv6** **instance** *instance-name* |
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure redirection actions for packets.
  1. IP packets support multiple redirection actions. Select the corresponding configurations in the following table based on packet types and service scenarios on the network.
     
     
     
     **Table 2** IP packet redirection configurations
     | Packet Type | Redirection Scenario | Configuration Command |
     | --- | --- | --- |
     | IPv4 packets | Configure the IPv4 address and outbound interface, VPN instance, and NQA test instance on a single next hop for redirecting IPv4 packets. | + [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **interface** *interface-type* *interface-number* [ **route-forward** ] [ **pri-type common** ] + [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] [ **public-network** ] + [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] |
     | In a scenario in which packets are redirected to a single next hop whose IP address matches a default route or a black-hole route, configure the packets to be forwarded based on the destination IP address. | [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] [ **public-network** ] |
     | Configure the IPv4 addresses and outbound interfaces, VPN instances, and NQA test instances on multiple next hops for redirecting IPv4 packets. | + [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **interface** *interface-type* *interface-number* } &2-42 [ **loadbalance** [ **sip-hash** ] [ **unequal-cost | ecmp-stateful** ] ] [ **route-forward** ] [ **pri-type common** ] + [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* } &2-42 [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] + [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] } &2-42 [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] [ **non-revertive** ] |
     | Configure IPv4 packets to be directly redirected to a specified outbound interface. | [**redirect to interface**](cmdqueryname=redirect+to+interface) { *interface-name* | *interface-type* *interface-number* } [ **route-forward** ] |
     | In a scenario in which packets are redirected to multiple next hops whose IP addresses match default or black-hole routes, configure the packets to be forwarded based on the destination IP address. | [**redirect ipv4-multinhp**](cmdqueryname=redirect+ipv4-multinhp) { **nhp** *ip-address* } &2-42 [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] |
     | IPv6 packets | Configure the IPv6 address and outbound interface, VPN instance, and NQA test instance on a single next hop for redirecting IPv6 packets. | + [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ipv6-address* **interface** *interface-type* *interface-number* [ **route-forward** ] [ **pri-type common** ] + [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ipv6-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] + [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ipv6-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] |
     | In a scenario in which packets are redirected to a single next hop whose IPv6 address matches a default route or a black-hole route, configure the packets to be forwarded based on the destination IPv6 address. | + [**redirect ipv6-nexthop**](cmdqueryname=redirect+ipv6-nexthop) *ip-address* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] [ **public-network** ] |
     | Configure the IPv6 addresses and outbound interfaces, VPN instances, and NQA test instances on multiple next hops for redirecting IPv6 packets. | + [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ipv6-address* **interface** *interface-type* *interface-number* } &2-16 [ **loadbalance** [ **sip-hash** ] [ **unequal-cost | ecmp-stateful** ] ] [ **route-forward** ] [ **pri-type common** ] + [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ipv6-address* **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* } &2-16 [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] + [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) { **nhp** *ipv6-address* **vpn** *vpn-instance-name* [ **nqa** *nqa-test-administer-name* *name-of-nqa-test-instance* ] } &2-16 [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] |
     | In a scenario in which packets are redirected to multiple next hops whose IPv6 addresses match default or black-hole routes, configure the packets to be forwarded based on the destination IPv6 address. | [**redirect ipv6-multinhp**](cmdqueryname=redirect+ipv6-multinhp) **nhp** *ipv6-address* [ **routing-filter** { **default-routing** | **blackhole-routing** } \* ] [ **pri-type common** ] |
     | Configure IPv6 packets to be directly redirected to a specified outbound interface. | [**redirect ipv6 to interface**](cmdqueryname=redirect+ipv6+to+interface) { *interface-name* | *interface-type* *interface-number* } [ **route-forward** ] |
     | IPv4 and IPv6 packets | Configure IPv4 or IPv6 packets forwarded by private network routes to be redirected to public network routes' outbound interfaces. | [**redirect**](cmdqueryname=redirect) { **ip** | **ipv6** } **public-network** |
     | Configure IP data flows to be redirected to the public network's target LSP. | [**redirect lsp public**](cmdqueryname=redirect+lsp+public) *dest-ipv4-address* [ *nexthop-address* | **interface** *interface-type* *interface-number* | **secondary** ] |
     | Configure packets to be redirected to a specified VPN group. | [**redirect vpn-group**](cmdqueryname=redirect+vpn-group) *vpn-group-name* |
     | Configure packets to be redirected to a specified VSI. | [**redirect vsi**](cmdqueryname=redirect+vsi) *vsi-name* |
     | Configure packets to be redirected to a specified tunnel. | [**redirect interface tunnel**](cmdqueryname=redirect+interface+tunnel) *tunnelname* [ ****destination-ip**** **destination-ip-address** **address-mask-length** ****vpn-instance**** **vpn-instance-name** ] [ **route-forward** ] |
     | Configure public network IPv4/IPv6 packets to be redirected to a single SR-MPLS TE Policy. | [**redirect sr-te policy**](cmdqueryname=redirect+sr-te+policy) *endpoint* *color* [ **label** *label* ] [ **route-forward** ] |
     | Configure public network IPv4/IPv6 packets to be redirected to a single SRv6 TE Policy. | [**redirect srv6-te policy**](cmdqueryname=redirect+srv6-te+policy) *endpoint* *color* [ { **sid** | **vpnsid** } *sid-ip* ] |
     | Configure IPv4/IPv6 packets to be redirected to multiple SRv6 TE Policies for load balancing. | [**redirect-template srv6-te**](cmdqueryname=redirect-template+srv6-te) *template-name*  NOTE: Before performing this configuration, you need to create an SRv6 TE Policy redirection template in the system and specify SRv6 TE Policies. 1. Run the [**redirect template**](cmdqueryname=redirect+template) *template-name* **srv6-te** command to create an SRv6 TE Policy redirection template and enter its view. 2. Run the [**endpoint**](cmdqueryname=endpoint) *endpoint* **color** *color* [ { **sid** | **vpnsid** } *sid-ip* ] command to configure an SRv6 TE Policy to which IPv4/IPv6 packets are redirected. 3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the load balancing mode of packets.
  1. Run [**load-balance**](cmdqueryname=load-balance) { **flow** [ **l2** | **l3** ] | **packet** }
     
     
     
     A load balancing mode is set for packets.
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a cascaded traffic policy.
  
  
  
  ACL rules are generally used for redirection in a traffic behavior. However, the specifications of ACL rules are limited. When ACL rules defined for MF classification do not meet the live network requirements, you can redirect the traffic behavior to a configured traffic policy to implement cascaded MF classification.
  
  
  
  1. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* [ **ip-layer** [ **srv6-inner** ] | **link-layer** **srv6-inner** ]
     
     
     
     The traffic behavior is redirected to the traffic policy.
     
     
     
     + Cascading a traffic policy over another will cause the device forwarding performance to deteriorate.
     + When the traffic on an interface matches the cascaded traffic policy:
       - The traffic is forwarded based on the traffic behavior in the cascaded traffic policy.
       - If the traffic behaviors in the two traffic policies are different, they can be individually implemented.
       - If the traffic behaviors in the two traffic policies are the same, the specific behavior configuration in the cascaded traffic policy takes effect.
     + On an interface, only one traffic policy can be applied to outgoing or incoming packets. If the traffic policy cascades over another traffic policy and is applied to an interface, both traffic policies take effect on the direction-specific interface.
     + The parameters specified for a traffic policy to be applied to an interface, such as **inbound**, **outbound**, mpls-layer, all-layer, and **link-layer**, are inherited by a cascaded traffic policy.
     + When the traffic behaviors for two-level ACLs are **service-class**, level-1 **service-class** preferentially takes effect. However, if level-1 **service-class** carries **no-remark**, level-2 **service-class** preferentially takes effect.
  2. (Optional) Run [**hierarchical-car enable**](cmdqueryname=hierarchical-car+enable)
     
     
     
     Hierarchical CAR is enabled in the cascaded traffic policy.
     
     
     
     When a traffic policy is configured in a traffic behavior, CAR can also be configured in the traffic policy to implement hierarchical CAR.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the sampling function of NetStream statistics.
  
  
  
  To charge the subscribers or collect traffic statistics based on traffic classifiers, you can configure the corresponding traffic classifier and run the following commands to enable NetStream sampling:
  
  
  
  1. Run { [**ip**](cmdqueryname=ip) | [**ipv6**](cmdqueryname=ipv6) } **netstream sampler** { **fix-packets** *packet-interval* | **fix-time** *time-interval* | **random-packets** *packet-interval* }
     
     
     
     The sampling function of NetStream statistics is configured.
     
     
     
     Traffic sampling using a traffic policy in shared mode is not supported.
  2. (Optional) Run [**ip netstream sampler except deny-action**](cmdqueryname=ip+netstream+sampler+except+deny-action)
     
     
     
     NetStream is not applied to traffic matching the ACL rule or traffic behavior that contains **deny**.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Increase the priority of the traffic behavior.
  
  
  
  If both BGP flow specification and MF classification are configured on a device, you can run the [**increase-priority**](cmdqueryname=increase-priority) command to allow the traffic behavior configured in MF classification to preferentially take effect.
  
  
  
  1. Run [**increase-priority**](cmdqueryname=increase-priority)
     
     
     
     The priority of the traffic behavior is increased.
  2. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable the logging of the first packet that matches an ACL.
  
  
  1. Run [**log first-packet**](cmdqueryname=log+first-packet)
     
     The device is enabled to log the first packet that matches an ACL.
     
     After this function is enabled, a log is recorded when the first packet matches an ACL. The log contains the inbound/outbound interface name, source IP address, destination IP address, protocol number, source port number (TCP/UDP), destination port number (TCP/UDP), time when the first packet was received (in milliseconds), and number of packets within the specified period.
  2. Run [**quit**](cmdqueryname=quit)
     
     Return to the system view.
  3. (Optional) Run [**traffic-behavior log**](cmdqueryname=traffic-behavior+log) { **entries** *number-of-entries* | **interval** *interval-time* } \*
     
     The maximum number of flows and the interval for collecting packet statistics recorded by the log are configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.