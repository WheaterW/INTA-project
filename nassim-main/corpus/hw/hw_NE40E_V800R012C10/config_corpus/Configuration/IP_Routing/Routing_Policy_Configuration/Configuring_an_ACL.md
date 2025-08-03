Configuring an ACL
==================

Configuring an ACL

#### Context

An ACL is a set of sequential filter rules. In an ACL rule, you can specify packet information, such as the inbound interface name, source or destination IP address, protocol type, source or destination port number, and permit or deny mode. Then, a device matches received packets against the rules and determines whether to accept or discard the packets.

An ACL consisting of a set of rules is used only to sort packets based on the defined rules. To filter packets, the ACL must be used together with a routing policy.

ACLs are classified as the ACLs that apply to IPv4 routes or those that apply to IPv6 routes. ACLs are also classified as interface-based ACLs, basic ACLs, or advanced ACLs based on the usage. You can specify an IP address and a subnet range in an ACL to match the source IP address, destination network segment address, or the next-hop address of each route.

ACLs can be configured on network devices, such as access and core devices, to improve network security and stability. ACLs can be used to provide the following functions:

* Protect devices against IP, TCP, and Internet Control Message Protocol (ICMP) packet attacks.
* Control network access. For example, ACLs can be used to control enterprise network users' access to external networks, the specific network resources that users can access, and the period during which users can access networks.
* Limit network traffic and improve network performance. For example, ACLs can be used to limit bandwidth for upstream and downstream traffic and to apply charging rules to user requested bandwidth, ensuring efficient utilization of network resources.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
   
   
   
   A route-policy node is created, and the route-policy view is displayed.
3. Run [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* }
   
   
   
   An ACL-based matching rule is defined.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The ACL view is displayed.
6. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   A rule is configured for the ACL.
   
   
   
   When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
   
   When a filtering policy of a routing protocol is used to filter routes:
   * If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
   * If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
   * If a route has not matched any ACL rules, the route will not be received or advertised by the system.
   * If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
   * In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
     
     Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
     
     Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl) command to check the rules of the configured ACL.