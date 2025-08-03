Configuring OSPF to Import External Routes
==========================================

Importing the routes discovered by other routing protocols can enrich OSPF routing information.

#### Context

When a device on an OSPF network needs to access a device running a non-OSPF routing protocol, the device needs to import the routes of the non-OSPF routing protocol into the OSPF network.

OSPF provides loop-free intra-area routes and inter-area routes; however, OSPF cannot prevent external routing loops. Therefore, exercise caution when configuring OSPF to import external routes.

Perform the following operations on the Router that functions as the ASBR running OSPF:

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

OSPF and other dynamic routing protocols such as IS-IS and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPF, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**import-route**](cmdqueryname=import-route) { **bgp** [ **permit-ibgp** ] | **direct** | **rip** [ *process-id-rip* ] | **static** | **unr** | **isis** [ *process-id-isis* ] | **ospf** [ *process-id-ospf* ] } [ { **inherit-cost** | **cost** *cost* } | **tag** *tag* | **type** *type* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] \*
   
   
   
   The device is configured to import routes from another protocol.
4. (Optional) Run [**default**](cmdqueryname=default) { **cost** { *cost* | **inherit-metric** } | **tag** *tag* | **type** *type* } \*
   
   
   
   The default values of parameters (the cost, number of routes, tag, and type) are set for imported routes.
   
   When OSPF imports external routes, you can set default values for some additional parameters, such as the cost, number of routes to be imported, route tag, and route type. The route tag is used to identify the protocol-related information. For example, it can be used to differentiate AS numbers carried in BGP routes imported by OSPF.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) You can run one of the following commands to set the cost of the imported route. The following commands are listed in descending order of priorities.
   * Run the [**apply cost**](cmdqueryname=apply+cost) command to set the cost of a route.
   * Run the [**import-route**](cmdqueryname=import-route) command to set the cost of the imported route.
   * Run the [**default**](cmdqueryname=default) command to set the default cost of the imported route.
5. (Optional) Run any of the following commands as required:
   
   
   * Based on a basic ACL:
     1. Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **static** | **unr** | **bgp** | { rip | **isis** | **ospf** } [ *process-id* ] ]
        
        The device is configured to filter the routes imported in step [3](#EN-US_TASK_0172365574__substep_dc_vrp_cfg_01623001) so that only the matched routes are advertised.
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
     5. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
        
        The OSPF view is displayed.
   * Based on an IP prefix list:
     
     Run [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **static** | **unr** | **bgp** | { **rip** | **isis** | **ospf** } [ *process-id* ] ]
     
     The device is configured to filter the routes imported in step [3](#EN-US_TASK_0172365574__substep_dc_vrp_cfg_01623001) so that only the matched routes are advertised.
   
   OSPF filters the imported routes. OSPF uses Type 5 LSAs to carry routes that meet the filtering conditions and advertises these Type 5 LSAs.
   
   You can specify the parameter *protocol* [ *process-id* ] to filter the routes of a certain routing protocol or a certain OSPF process. If *protocol* [ *process-id* ] is not specified, OSPF filters all imported routes.
   
   The [**import-route**](cmdqueryname=import-route) command cannot be used to import external default routes.
6. Run [**import-route limit**](cmdqueryname=import-route+limit) *limit-number* [ **threshold-alarm** { **upper-limit** *upper-limit-value* | **lower-limit** *lower-limit-value* } \* ]
   
   
   
   The maximum number of LSAs generated when OSPF imports routes is set.
   
   
   
   If OSPF imports a large number of external routes and advertises them to a device with a small routing table capacity, the device may restart unexpectedly. To address this problem, set a limit on the number of LSAs generated when OSPF imports external routes. You can check the overload status based on the value of the **Current status** field in the [**display ospf brief**](cmdqueryname=display+ospf+brief) command output.
   * Normal: The number is less than or equal to the lower alarm threshold.
   * Approach limit: The number is approaching (reaching or exceeding 90% of) the upper alarm threshold.
   * Exceed limit: The number has reached or exceeded the limit.
   
   Ensure that *upper-limit-value* is greater than or equal to *lower-limit-value*.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.