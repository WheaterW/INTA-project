Configuring IPv6 IS-IS Route Leaking
====================================

Configuring IS-IS route leaking enables you to optimize IS-IS route selection on a two-level-area network.

#### Context

If multiple Level-1-2 devices in a Level-1 area are connected to devices in the Level-2 area, a Level-1 LSP sent by each Level-1-2 device carries an ATT flag bit of 1. This Level-1 area will have multiple routes to the Level-2 area and other Level-1 areas.

By default, routing information in a Level-1 area is leaked to the Level-2 area, enabling Level-1-2 and Level-2 devices to learn the topology of the entire network. Devices in a Level-1 area are unaware of the entire network topology because they only maintain LSDBs in the local Level-1 area. Therefore, a device in a Level-1 area can forward traffic to a Level-2 device only through the nearest Level-1-2 device. However, the used route may not be optimal.

To help a device in a Level-1 area to select the optimal route to another area, configure IPv6 IS-IS route leaking so that some routes in the Level-2 area can leak to the local Level-1 area.

If you want the Level-2 area to know only some of the routes in the local Level-1 area, configure a policy so that only desired routes can leak to the Level-2 area.


#### Procedure

* Configure route leaking from the Level-2 area to the Level-1 area.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Configure the routes in the Level-2 area and other Level-1 areas that meet the specified conditions to leak to the local Level-1 area.
     
     
     
     Run any of the following commands as required:
     
     + Based on the basic ACL:
       1. Run the [**ipv6 import-route isis level-2 into level-1**](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) [ **filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* } | **tag** *tag* | **no-bier** ] \* command.
       2. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
          
          Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
          
          A rule is configured for the ACL.
       4. When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
          
          When a filter-policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route matching the rule will be accepted or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route matching the rule will not be accepted or advertised by the system.
          - If the network segment of a route is not within the range specified in an ACL rule, the route will not be accepted or advertised by the system.
          - If an ACL does not contain any rules, none of the routes matched against the filter-policy that uses this ACL will be accepted or advertised by the system.
          - Routes can be filtered using a blacklist or whitelist:
            
            If ACL rules are used for matching in configuration order, the system matches the rules in ascending order of their IDs.
            
            Filtering using a blacklist: Configure a rule with a smaller ID and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger ID in the same ACL and specify the action **permit** in this rule to accept or advertise the other routes.
            
            Filtering using a whitelist: Configure a rule with a smaller ID and specify the action **permit** in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger ID in the same ACL and specify the action **deny** in this rule to filter out the unwanted routes.
     + Configure an IP prefix list:
       
       Run the [**ipv6 import-route isis level-2 into level-1**](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) [ **filter-policy** **ipv6-prefix** *ipv6-prefix-name* | **tag** *tag* | **no-bier** ] \* command.
     + Based on a route-policy:
       
       Run the [**ipv6 import-route isis level-2 into level-1**](cmdqueryname=ipv6+import-route+isis+level-2+into+level-1) [ **filter-policy** **route-policy** *route-policy-name* | **tag** *tag* | **no-bier** ] \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The command is run on the Level-1-2 device that is connected to an external area.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure route leaking from the Level-1 area to the Level-2 area.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Configure the routes that meet the specified conditions in the Level-1 area to leak to the Level-2 area.
     
     
     
     Run any of the following commands as required:
     
     + Based on the basic ACL:
       1. Run the [**ipv6 import-route isis level-1 into level-2**](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) [ **filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* } | **tag** *tag* | **no-bier** ] \* command.
       2. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name*  **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
          
          The ACL view is displayed.
       4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
          
          A rule is configured for the ACL.
          
          When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
          
          When a filtering policy of a routing protocol is used to filter routes:
          - If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
          - If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
          - If a route has not matched any ACL rules, the route will not be received or advertised by the system.
          - If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
          - In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
            
            Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
            
            Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
     + Configure an IP prefix list:
       
       Run the [**ipv6 import-route isis level-1 into level-2**](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) [ **filter-policy** **ipv6-prefix** *ipv6-prefix-name* | **tag** *tag* | **no-bier** ] \* command.
     + Based on a route-policy:
       
       Run the [**ipv6 import-route isis level-1 into level-2**](cmdqueryname=ipv6+import-route+isis+level-1+into+level-2) [ **filter-policy** **route-policy** *route-policy-name* | **tag** *tag* | **no-bier** ] \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The command is run on the Level-1-2 device that is connected to an external area.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.