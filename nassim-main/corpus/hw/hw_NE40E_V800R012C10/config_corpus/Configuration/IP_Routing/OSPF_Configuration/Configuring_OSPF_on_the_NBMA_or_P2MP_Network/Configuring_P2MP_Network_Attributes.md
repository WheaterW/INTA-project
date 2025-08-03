Configuring P2MP Network Attributes
===================================

This section describes how to configure P2MP network attributes to implement OSPF functions.

#### Procedure

1. Disable the check on the network mask.
   
   
   
   The OSPF neighbor relationship cannot be established between the devices with different mask lengths on the P2MP network. After OSPF is disabled from checking the network mask, the OSPF neighbor relationship can be properly established.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ospf network-type**](cmdqueryname=ospf+network-type) **p2mp**
      
      
      
      The network type of the OSPF interface is configured.
      
      A P2MP network is forcibly changed from another other type of network. For details, see [Configuring Network Types for OSPF Interfaces](dc_vrp_ospf_cfg_2029.html).
   4. Run [**ospf p2mp-mask-ignore**](cmdqueryname=ospf+p2mp-mask-ignore)
      
      
      
      OSPF is disabled from checking the network mask on the P2MP network.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. (Optional) Configure the device to filter the LSA packets to be sent.
   
   
   
   When multiple links exist between two devices, you can configure the local device to filter the LSA packets to be sent. This can reduce unnecessary LSA retransmission attempts and save bandwidth resources.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
   3. Based on the basic ACL:
      
      
      1. Run [**filter-lsa-out peer**](cmdqueryname=filter-lsa-out+peer) *ip-address* { **all** | { **summary** [ **acl** { *acl-number* | *acl-name* } ] | **ase** [ **acl** { *acl-number* | *acl-name* } ] | **nssa** [ **acl** { *acl-number* | *acl-name* } ] } \* }
         
         The local device is configured to filter the LSA packets to be sent on the P2MP network.
      2. Run [**quit**](cmdqueryname=quit)
         
         Return to the system view.
      3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
         
         The ACL view is displayed.
      4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
         
         An ACL rule is configured.
         
         When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
         
         When a filter-policy of a routing protocol is used to filter routes:
         * If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
         * If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
         * If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
         * If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
         * Routes can be filtered using a blacklist or whitelist:
           
           If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
           
           Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
           
           Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.