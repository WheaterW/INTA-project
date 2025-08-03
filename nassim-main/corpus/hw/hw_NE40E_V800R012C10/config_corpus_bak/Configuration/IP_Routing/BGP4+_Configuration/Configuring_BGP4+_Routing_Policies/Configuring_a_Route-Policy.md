Configuring a Route-Policy
==========================

A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met.

#### Context

A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met.

A route-policy consists of multiple nodes, and each node can comprise the following clauses:

* [if-match clause](#EN-US_TASK_0172366452__step1883863273214039)
  
  The clauses define the matching rules of a route-policy. The matching objects are route attributes.
* [apply clause](#EN-US_TASK_0172366452__step1099439341214039)
  
  The clauses specify actions. Configuration commands are run after a route meets the matching rules specified by the **if-match** clauses. The **apply** clauses can change certain route attributes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section describes only the BGP4+ route-policy. For detailed information about route-policy configurations, see "Routing Policy Configuration."



#### Procedure

1. Create a route-policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* *matchMode* **node** *node*
      
      
      
      A route-policy is created, and the view of the route-policy is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure **if-match** clauses.
   1. Run the following command to configure the **if-match** clause for the current node in the route-policy as required:
      
      
      * To match the AS\_Path attribute of BGP4+ routes, run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) *apfIndex* &<1-16> command.
      * To match BGP4+ routes against the community attribute:
        
        + [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) { *basic-comm-filter-num* [ **whole-match** ] | *adv-comm-filter-num* [ **sort-match** ] }\* &<1-16>
        + [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) *comm-filter-name* [ **whole-match** | **sort-match** ]
      * To match BGP4+ routes against the Large-community attribute, run the [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter+whole-match) *large-comm-filter-name* [ **whole-match** ] command.
      * To match BGP4+ routes against the VPN target extended community attribute, run the [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *extcomm-filter-name* [ **matches-all** | **whole-match** ] } command.
      * To match BGP4+ routes against the SoO extended community attribute, run the [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* command.
      
      The commands can be executed in any sequence. A node may have multiple or no **if-match** clauses.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The relationship between the **if-match** clauses for a node of a route-policy is "AND". A route must meet all the matching rules before the action defined by the **apply** clause is performed.
      * If no **if-match** clause is specified, all the routes are matched.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Configure the **apply** clause.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **matchMode** **node** *node*
      
      
      
      The route-policy view is displayed.
   3. Run the following command as needed to configure the **apply** clause for the current node in the route-policy:
      
      
      * To replace the AS numbers in the AS\_Path attribute of BGP4+ routes or add the specified AS number to the AS\_Path attribute, run the [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete+additive+overwrite) { *as-path-value* } &<1-128> { **additive** | **overwrite** | **delete** } or [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *asValues* { **additive** | **overwrite** | **delete** } command.
      * To delete a specified BGP4+ community attribute, run the [**apply comm-filter**](cmdqueryname=apply+comm-filter) [**delete**](cmdqueryname=delete) command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command deletes a specified community attribute from matched routes based on the referenced community filter. To delete multiple community attributes through one community filter, you need to run the [**ip community-filter**](cmdqueryname=ip+community-filter) command multiple times to configure multiple indexes for the filter, with each index corresponding to only one community attribute. If multiple community attributes are specified in the same index of the same community filter, none of them can be deleted in this case. For example, see the *HUAWEI NE40E-M2 series Universal Service Router Command Reference*.
      * To delete community attributes of BGP4+ routes, run the [**apply community**](cmdqueryname=apply+community+none) **none** command.
      * To set the community attribute of matched BGP4+ routes, run the [**apply community**](cmdqueryname=apply+community+internet+no-advertise+no-export) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ] or [**apply community**](cmdqueryname=apply+community+community-list) **community-list** *community-list-name* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        Before running the [**apply community**](cmdqueryname=apply+community+community-list) **community-list** *community-list-name* command, you need to run the [**ip community-list**](cmdqueryname=ip+community-list) command to configure a BGP community list and run the [**community**](cmdqueryname=community) command to configure community attributes for the list.
      * To delete the Large-Community attribute of BGP4+ routes, run the [**apply large-community**](cmdqueryname=apply+large-community+none) **none** command.
      * To set the Large-Community attribute of BGP4+ routes, run the [**apply large-community**](cmdqueryname=apply+large-community+additive+overwrite+delete) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } or [**apply large-community-list**](cmdqueryname=apply+large-community-list+additive+overwrite+delete) *large-community-list-name* { **additive** | **overwrite** | **delete** } command.
      * To set the BGP4+ VPN target extended community attribute, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] command.
      * To set the SoO extended community attribute for BGP4+ routes, run the [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo+additive) { *site-of-origin* } &<1-16> **additive** command.
      * To set the bandwidth extended community attribute for BGP4+ routes, run the [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+none) { *extCmntyString* | **none** } or [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+aggregate+limit) **aggregate** [ **limit** *bandwidth-value* ] command.
      * To set a MED value for BGP4+ routes, run the [**apply cost**](cmdqueryname=apply+cost+%2B+-+inherit+none) { [ **+** | **-** ] *cost* | **inherit** | **none** } command.
      * To set the MED value of BGP4+ routes as the IGP cost of the next hop, run the [**apply cost-type**](cmdqueryname=apply+cost-type+internal) **internal** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If both the [**apply cost**](cmdqueryname=apply+cost) and [**apply cost-type**](cmdqueryname=apply+cost-type) commands are run, only the [**apply cost**](cmdqueryname=apply+cost) command takes effect.
      * To set the BGP4+ VPN target extended community attribute, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] command.
      * To set the local preference for BGP4+ routes, run the [**apply local-preference**](cmdqueryname=apply+local-preference+%2B+-) [ **+** | **-** ] *preference* command.
      * To set the Origin attribute for matched BGP4+ routes, run the [**apply origin**](cmdqueryname=apply+origin+egp+igp+incomplete) { **egp** { *egpVal* } | **igp** | **incomplete** } command.
      * To set the preferred value for BGP4+ routes, run the [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferred-value* command.
      * To set dampening parameters for EBGP routes, run the [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* command.
      
      The commands in Step 3 can be configured in random order.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.