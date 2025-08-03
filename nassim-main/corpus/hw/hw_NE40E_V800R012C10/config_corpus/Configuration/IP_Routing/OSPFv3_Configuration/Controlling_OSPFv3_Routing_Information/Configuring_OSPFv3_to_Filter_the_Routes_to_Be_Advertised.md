Configuring OSPFv3 to Filter the Routes to Be Advertised
========================================================

After filtering conditions are set for imported routes, only the routes that pass the filtering can be advertised.

#### Context

When OSPFv3 receives LSAs, it can filter the received routes based on a filtering policy before advertising them to neighbors.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. (Optional) Run **[**default-route-advertise**](cmdqueryname=default-route-advertise)** [ [ **always** | **permit-calculate-other** ] | **cost***cost* | **type***type* | **tag***tag* | **distribute-delay***delay* | { **route-policy***route-policy-name* | **route-filter***route-filter-name* } ] \* or [**default-route-advertise**](cmdqueryname=default-route-advertise) [ **permit-calculate-other** | **cost** *cost* | **type** *type* | **tag** *tag* | **distribute-delay***delay* | { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* } | **permit-preference-less-than** *preference-value* ] \*
   
   
   
   The device is configured to advertise default routes to OSPFv3 routing areas.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent low-priority active default routes from being imported, which would otherwise cause routing loops, you are advised to specify the **permit-preference-less-than** parameter. This parameter is used only when **always** is not specified.
4. Run any of the following commands as required:
   
   
   * Configure a basic ACL:
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        The ACL view is displayed.
     3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
        
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
     4. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
        
        The OSPFv3 view is displayed.
     5. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl6-name** *acl6-name* } **export** [ **bgp** | **direct** | **static** | **unr** | { **isis** | **ospfv3** | **ripng** } [ *process-id* ] ]
        
        An export policy is configured to filter the routes that are imported using the [**import-route**](cmdqueryname=import-route) command and are to be advertised. Only the matched routes can be advertised.
   * Based on an IPv6 prefix list:
     
     Run the [**filter-policy**](cmdqueryname=filter-policy) **ipv6-prefix** *ipv6-prefix-name* **export** [ **bgp** | **direct** | **static** | **unr** | { **isis** | **ospfv3** | **ripng** } [ *process-id* ] ] command to configure an export policy to filter the routes that are imported using the [**import-route**](cmdqueryname=import-route) command and are to be advertised. Only the matched routes can be advertised.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.