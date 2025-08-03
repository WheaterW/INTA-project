Configuring OSPF Local MT
=========================

On a network where multicast and an MPLS TE tunnel are deployed, you can configure OSPF local MT to create a correct multicast routing table and guide multicast packet forwarding.

#### Usage Scenario

When multicast and an Interior Gateway Protocol (IGP) Shortcut-enabled MPLS TE tunnel are configured on a network, the outbound interface of the route calculated by an IGP may not be a physical interface but a TE tunnel interface. Based on a unicast route to a multicast source address, the Router sends a Join message through a TE tunnel interface. In this case, devices spanned by the TE tunnel cannot detect the Join message so that they do not create any multicast forwarding entry.

To resolve this problem, enable OSPF local MT. After local MT is enabled, if the outbound interface of a calculated route is an IGP Shortcut-enabled TE tunnel interface, the route management (RM) module creates an independent Multicast IGP (MIGP) routing table for the multicast protocol, calculates a physical outbound interface for the route, and adds the route to the MIGP routing table. Multicast packets are then forwarded along this route.

Configuring filtering policies for local MT controls the number of entries in the MIGP routing table and speeds up the MIGP routing table lookup.


#### Pre-configuration Tasks

Before configuring local MT, complete the following tasks:

* Configure addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).
* [Configure the IGP Shortcut](dc_vrp_te-p2p_cfg_0034.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**local-mt enable**](cmdqueryname=local-mt+enable)
   
   
   
   Local MT is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Local MT takes effect only in the OSPF process of a public network instance.
   * Local MT does not support Forwarding Adjacency (FA).
4. (Optional) Run any of the following commands as required:
   
   
   * Based on a basic ACL:
     1. Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **acl** { *acl-number* | *acl-name* }
        
        A filtering policy is configured for OSPF local MT.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        An ACL rule is configured.
        
        When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
        
        When a filter-policy of a routing protocol is used to filter routes:
        + If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
        + If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
        + If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
        + If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
        + Routes can be filtered using a blacklist or whitelist:
          
          If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
          
          Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
          
          Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
   * Based on an IP prefix list:
     
     Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **ip-prefix** *ip-prefix-name*
     
     A routing policy is configured for OSPF local MT.
   * Based on a route-policy:
     
     Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **route-policy** *route-policy-name*
     
     A route-policy is configured for OSPF local MT.
   * Based on a route-filter:
     
     Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **route-filter** *route-filter-name*
     
     A route-filter is configured for OSPF local MT.
   
   After an MIGP routing table is created, OSPF performs route calculation. If the outbound interface of the calculated route is an IGP Shortcut-enabled TE tunnel interface, the Router saves the physical interface on which the tunnel interface is configured as the outbound interface in the MIGP routing table. Multicast packets are then forwarded along this route.
   
   After the routing policy is configured, only the matching routes to the multicast source address are added to the MIGP routing table, which controls the number of entries in the MIGP routing table and speeds up MIGP routing table lookup.
   
   Configure a routing policy before you enable local MT, because if an excessive number of routes to a non-multicast source address exist in an MIGP routing table, the number of entries may exceed the upper limit.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **migp-routing** [ *ip-address* [ *mask* | *mask-length* ] ] [ **interface** *interface-type* *interface-number* ] [ **nexthop** *nexthop-address* ] command to check information about the OSPF MIGP routing table.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **routing** command to check OSPF routing information.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information.