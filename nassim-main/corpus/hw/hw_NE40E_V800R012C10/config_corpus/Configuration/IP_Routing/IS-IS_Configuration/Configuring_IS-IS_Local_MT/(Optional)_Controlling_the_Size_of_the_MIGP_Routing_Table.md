(Optional) Controlling the Size of the MIGP Routing Table
=========================================================

You can configure a filtering policy based on the multicast source address so that the router adds only the routes destined to the specified multicast source address to the independent Multicast IGP (MIGP) routing table, which controls the size of the MIGP routing table.

#### Context

After local MT is enabled in an IS-IS system, IS-IS calculates routes and creates an MIGP routing table. When the next-hop outbound interface calculated by IS-IS is an IGP Shortcut-enabled TE tunnel interface, the Router uses a physical interface as the next-hop outbound interface and saves it in the MIGP routing table. To control the number of entries in the MIGP routing table, speed up the MIGP routing table lookup, and reduce memory resource consumption, you can configure a multicast source address-based filtering policy so that the device adds only the matched routes to the MIGP routing table.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Configure a local MT routing policy.
   
   
   
   Run any of the following commands as required:
   
   * Based on the basic ACL:
     1. Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **acl** { *acl-number* | *acl-name* }
        
        A policy is configured for IS-IS local MT.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
        
        A rule is configured for the ACL.
        
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
   * Based on the IP prefix:
     
     Run [**local-mt filter-policy**](cmdqueryname=local-mt+filter-policy) **ip-prefix** *ip-prefix-name*
   
   A routing policy allows only the routes with the destination address being the multicast source address to be added to the MIGP routing table, reducing CPU and memory usage.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.