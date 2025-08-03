Configuring an ACL
==================

Configuring an ACL

#### Context

An access control list (ACL) is a set of filtering rules, including ACLs for IPv4 routes and ACLs for IPv6 routes. You can specify an IP address and a subnet range in an ACL to match the source IP address, destination network segment address, or the next-hop address of each route.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
3. Define an ACL-based matching rule.
   
   
   ```
   [if-match acl](cmdqueryname=if-match+acl) { acl-number | acl-name }
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the ACL view.
   
   
   ```
   [acl](cmdqueryname=acl) name basic-acl-name { basic | [ number ] basic-acl-number } 
   ```
6. Configure an ACL rule.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } [ fragment-type fragment | fragment | source { source-ip-address { source-wildcard | 0 | src-netmask } | any } | time-range time-name | vpn-instance vpn-instance-name ] 
   ```
   When the [**filter-policy**](cmdqueryname=filter-policy) command of a routing protocol is used to filter routes, not the following:
   * If the action specified in an ACL rule is permit, a route matching the rule will be accepted or advertised by the device.
   * If the action specified in an ACL rule is deny, a route matching the rule will not be accepted or advertised by the device.
   * If a route does not match any ACL rules, the route will not be accepted or advertised by the device.
   * If an ACL does not contain any rules, all routes matching the route-policy that uses the ACL will not be accepted or advertised by the device.
   * Routes can be filtered using a blacklist or a whitelist:
     
     Rules are applied in ascending order by rule ID.
     
     Route filtering using a blacklist: Configure a rule with a smaller number and specify the deny action in this rule to filter out unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the permit action in this rule to accept or advertise the other routes.
     
     Route filtering using a whitelist: Configure a rule with a smaller number and specify the permit action in this rule to permit the routes to be accepted or advertised. Then, configure another rule with a larger number in the same ACL and specify the deny action in this rule to filter out unwanted routes.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display acl**](cmdqueryname=display+acl) command to check the rules of the configured ACL.