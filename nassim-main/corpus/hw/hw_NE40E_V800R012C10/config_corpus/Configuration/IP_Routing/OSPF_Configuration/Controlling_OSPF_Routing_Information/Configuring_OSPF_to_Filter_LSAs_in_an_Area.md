Configuring OSPF to Filter LSAs in an Area
==========================================

Filtering LSAs in an area can prevent unnecessary LSA transmission. This reduces the size of the LSDB on the neighboring Router and speeds up network convergence.

#### Context

After filtering conditions are set for the incoming or outgoing Type 3 LSAs (Summary LSAs) in an area, only the Type 3 LSAs that meet the filtering conditions can be received or advertised.

This function is applicable only to the ABR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPF area view is displayed.
4. Filter incoming or outgoing Type 3 LSAs in the area. 
   
   
   * Filter outgoing Type 3 LSAs in the area. Run any of the following commands as required:
     
     + Based on the basic ACL:
       1. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       2. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
          
          An ACL rule is configured.
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
          - If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
          - Routes can be filtered using a blacklist or whitelist:
            
            If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
       4. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
          
          The OSPF view is displayed.
       5. Run [**area**](cmdqueryname=area) *area-id*
          
          The OSPF area view is displayed.
       6. Run [**filter**](cmdqueryname=filter) { *acl-number* | **acl-name** *acl-name* } **export**
          
          The outgoing Type 3 LSAs of the local area are filtered based on the basic ACL.
     + Based on the IP prefix list:
       
       Run [**filter**](cmdqueryname=filter) **ip-prefix** *ip-prefix-name* **export**
       
       Outgoing Type 3 LSAs in the area are filtered based on the IP prefix list.
     + Based on the route-policy:
       
       Run [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **export**
       
       Outgoing Type 3 LSAs in the area are filtered based on the route-policy.
     + Based on a route-filter:
       
       Run [**filter**](cmdqueryname=filter) **route-filter** *route-filter-name* **export**
       
       Outgoing Type 3 LSAs in the area are filtered based on the route-filter.
   * Filter incoming Type 3 LSAs in the area. Run any of the following commands as required:
     
     + Based on the basic ACL:
       1. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       2. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
          
          An ACL rule is configured.
          
          When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
          - If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
          - Routes can be filtered using a blacklist or whitelist:
            
            If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
       4. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
          
          The OSPF view is displayed.
       5. Run [**area**](cmdqueryname=area) *area-id*
          
          The OSPF area view is displayed.
       6. Run [**filter**](cmdqueryname=filter) { *acl-number* | **acl-name** *acl-name* } **import** [ **include-abr-summary** ]
          
          Incoming Type 3 LSAs in the area are filtered based on the basic ACL.
     + Based on the IP prefix list:
       
       Run [**filter**](cmdqueryname=filter) **ip-prefix** *ip-prefix-name* **import** [ **include-abr-summary** ]
       
       Incoming Type 3 LSAs in the area are filtered based on the IP prefix list.
     + Based on the route-policy:
       
       Run [**filter**](cmdqueryname=filter) **route-policy** *route-policy-name* **import** [ **include-abr-summary** ]
       
       Incoming Type 3 LSAs in the area are filtered based on the route-policy.
     + Based on the route-filter:
       
       Run [**filter**](cmdqueryname=filter) **route-filter** *route-filter-name* **import** [ **include-abr-summary** ]
       
       Incoming Type 3 LSAs in the area are filtered based on the route-filter.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.