Configuring IPv6 IS-IS to Import External Routes
================================================

Configuring IS-IS to import external routes on a boundary device enables devices in the IS-IS domain to learn external routes and guide traffic forwarding.

#### Context

After IS-IS is configured on a boundary device to advertise a default route, the traffic destined for a destination outside the domain can be diverted to the boundary device for processing. However, because other devices in the IS-IS domain do not have external routes, a large amount of traffic is forwarded to the boundary device, which overloads the boundary device.

If multiple boundary devices are deployed, optimal routes to other routing domains need to be selected. In this case, all the other devices in the IS-IS routing domain must learn all or some external routes.

Routing policies can be configured to import only the external routes that match filtering conditions or advertise only the imported routes that match filtering conditions to other IS-IS devices.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

IS-IS and other dynamic routing protocols such as OSPF and BGP often import routes from each other. If no routing policy is configured or a routing policy is incorrectly configured on a device where IS-IS, OSPF, and BGP import routes from each other, a Layer 3 routing loop may occur due to a route selection result change. As a result, services are compromised.



#### Procedure

* Configure IS-IS to import external routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Configure IS-IS to import external IPv6 routes.
     
     
     + To import external routes to IS-IS and set a cost for them, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) { **direct** | **static** | **unr** | { **ripng** | **isis** | **ospfv3** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] } [ **cost** *cost* | **tag** *tag* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command.
     + To import external routes to IS-IS and keep the original costs, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) { { **ospfv3** | **ripng** | **isis** } [ *process-id* ] | **bgp** [ **permit-ibgp** ] | **direct** | **unr** } **inherit-cost** [ **tag** *tag* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* | [ **level-1** | **level-2** | **level-1-2** ] ] \* command. In this case, the protocol from which routes are imported cannot be **static**.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     IS-IS advertises all imported external routes to an IS-IS routing domain by default.
     
     If only some imported external routes need to be advertised to the IS-IS routing domain, run the [**ipv6 filter-policy export**](cmdqueryname=ipv6+filter-policy+export) command to set a filtering policy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure IS-IS to advertise some external routes to an IS-IS routing domain.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Configure IS-IS to advertise specified external routes to the IS-IS routing domain.
     
     
     
     Run any of the following commands as required:
     
     + Based on the basic ACL:
       1. Run [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) { *acl6-number* | **acl6-name** *acl6-name* } **export** [ **direct** | **static** | **ripng** *process-id* | **bgp** | **ospfv3** *process-id* | **isis** *process-id* | **unr** ]
          
          A filter policy is configured.
       2. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
          
          A rule is configured for the ACL.
          
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
     + Based on an IP prefix list:
       
       Run the [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **ipv6-prefix** *ipv6-prefix-name* **export** [ **direct** | **static** | **ripng** *process-id* | **bgp** | **ospfv3** *process-id* | **isis** *process-id* | **unr** ] command.
     + Based on a route-policy:
       
       Run the [**ipv6 filter-policy**](cmdqueryname=ipv6+filter-policy) **route-policy** *route-policy-name* **export** [ **direct** | **static** | **ripng** *process-id* | **bgp** | **ospfv3** *process-id* | **isis** *process-id* | **unr** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this command is run, only the external routes that meet the specified conditions can be advertised to the IS-IS routing domain.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.