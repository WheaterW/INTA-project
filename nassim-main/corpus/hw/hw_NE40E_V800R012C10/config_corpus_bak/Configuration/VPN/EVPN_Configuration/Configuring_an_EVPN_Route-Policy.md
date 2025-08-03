Configuring an EVPN Route-Policy
================================

An EVPN route-policy can be configured to control EVPN route receiving and advertisement.

#### Context

An EVPN route-policy is used to match specified EVPN route information or to match some attributes in EVPN route information and change these attributes as required. In addition, an EVPN route-policy can be deployed to control the routing table size, thereby conserving system resources.

A route-policy can consist of multiple nodes, and each node can comprise the following clauses:

* if-match clause
  
  Defines the matching rules used by the current route-policy to match EVPN routes. The matching objects are some attributes of the EVPN routes.
* apply clause
  
  Specifies actions. Specifically, configuration commands are run after a route satisfies the matching rules specified by the if-match clauses. The apply clauses can change some attributes of EVPN routes.

After a route-policy is created, apply the route-policy to EVPN or L3VPN to make it take effect.


#### Procedure

1. Create a route-policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
      
      
      
      A route-policy node is created, and its view is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure filter criteria (if-match clause).
   
   
   
   | Filter Criteria | Configuration Procedure |
   | --- | --- |
   | Filtering by VNI | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**filter-list vni**](cmdqueryname=filter-list+vni) *vni-list-name* command to create a VNI list and enter its view. 3. Run the [**vni**](cmdqueryname=vni) *vni-id* command to configure a VNI ID. 4. Run the [**quit**](cmdqueryname=quit) command to return to the system view. 5. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 6. Configure matching rules based on VNI lists:    * Run the [**if-match l2vni**](cmdqueryname=if-match+l2vni) [ *l2vni-name* ] command to configure a matching rule based on a Layer 2 VNI list.    * Run the [**if-match l3vni**](cmdqueryname=if-match+l3vni) [ *l3vni-name* ] command to configure a matching rule based on a Layer 3 VNI list. 7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Filtering by MPLS label | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 3. Run the [**if-match**](cmdqueryname=if-match) { **mpls-label** | **mpls-label2** } \* command to configure a matching rule based on an MPLS label. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Filtering by route type | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 3. Run the [**if-match route-type**](cmdqueryname=if-match+route-type) **evpn** { **ad** | **es** | **inclusive** | **join** | **leave** | **mac** | **prefix** | **smet** } \* command to configure a matching rule based on the route type. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Filtering by Ethernet tag | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**filter-list eth-tag**](cmdqueryname=filter-list+eth-tag) *eth-tag-list* command to create an Ethernet tag list. 3. Run the [**eth-tag**](cmdqueryname=eth-tag) *ethtag-value* command to configure an Ethernet tag of the Ethernet tag list. 4. Run the [**quit**](cmdqueryname=quit) command to return to the system view. 5. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 6. Run the [**if-match eth-tag-list**](cmdqueryname=if-match+eth-tag-list) *eth-tag-list-name* command to configure a matching rule based on the Ethernet tag. 7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Filtering by MAC address | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**filter-list mac**](cmdqueryname=filter-list+mac) *mac-list-name* command to create a MAC address list. 3. Run the [**mac**](cmdqueryname=mac) *mac-address* command to configure MAC addresses in the MAC address list. 4. Run the [**quit**](cmdqueryname=quit) command to return to the system view. 5. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 6. Run the [**if-match mac-list**](cmdqueryname=if-match+mac-list) *mac-list-name* command to configure a matching rule based on the MAC address list. 7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Filtering by encapsulation extended community attribute | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Configure a filter for encapsulation extended community attributes.     * Run the [**ip extcommunity-list encapsulation**](cmdqueryname=ip+extcommunity-list+encapsulation) **basic** *encapsulation-name* [ **index** *index-value* ] { **permit** | **deny** } { *encap-value* } & <1-16> command to create a filter for basic encapsulation extended community attributes.    * Run the [**ip extcommunity-list encapsulation**](cmdqueryname=ip+extcommunity-list+encapsulation) **advanced** *encapsulation-name* [ **index** *index-value* ] { **permit** | **deny** } *regular* command to create a filter for advanced encapsulation extended community attributes. NOTE:  In an EVPN VXLAN scenario, EVPN routes carry VXLAN-encapsulated extended community attributes. You can set *encap-value* to **0:8** to filter EVPN routes in this scenario. In an EVPN MPLS scenario, a device may receive EVPN routes carrying MPLS-encapsulated extended community attributes. To filter these routes, set *encap-value* to **0:10**. 3. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* to enter the route-policy view. 4. Run the [**if-match extcommunity-list encapsulation**](cmdqueryname=if-match+extcommunity-list+encapsulation) *encapsulation-name* command to configure a matching rule based on the extended community attribute filter. 5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
3. Configure an apply clause.
   
   
   
   [Configuring Apply clauses](dc_vrp_route-policy_cfg_0010.html) helps you add or modify the attributes of EVPN routes.
4. Apply a route-policy.
   
   
   
   | Usage Scenario | Configuration Procedure |
   | --- | --- |
   | Control route receiving and advertisement between BGP EVPN peers. | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view. 3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view. 4. Run the [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* { **import** | **export** } command to configure a route-policy for the routes received from the BGP EVPN peer (group) or advertised to the BGP EVPN peer (group). 5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Control the routes sent by an EVPN instance through EVPN or the routes received by an EVPN instance through BGP EVPN. | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Use either of the following methods to enter the EVPN instance view:     * Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws** command to create a VPWS EVPN instance and enter its view.    * Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to create a BD EVPN instance and enter the BD EVPN instance view. 3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the EVPN instance. 4. Associate the current EVPN instance with an import route-policy.    * Run the [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* command to apply an import route-policy to the EVPN instance, so that the EVPN instance can filter routes to be imported.    * Run the [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* command to apply an export route-policy to the EVPN instance, so that the EVPN instance can filter routes to be advertised. 5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Control the routes sent by an L3VPN instance through EVPN or the routes received by an L3VPN instance through BGP EVPN. | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view. 3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the IPv4 or IPv6 address family view of the VPN instance. 4. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance. 5. Apply a route-policy to the VPN instance IPv4/IPv6 address family.    * Run the [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn** command to apply an import route-policy to the VPN instance IPv4/IPv6 address family, so that the address family can filter routes to be imported from EVPN.    * Run the [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn** command to apply an export route-policy to the VPN instance IPv4/IPv6 address family, so that the address family can filter routes to be advertised to EVPN. 6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |
   | Configure the function to recurse BGP EVPN routes to next hops based on a route-policy. | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view. 3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view. 4. Run the [**nexthop recursive-lookup route-policy**](cmdqueryname=nexthop+recursive-lookup+route-policy) *route-policy-name* command to configure the function to recurse BGP EVPN routes to next hops based on the specified route-policy. 5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. |

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check EVPN route information after the EVPN route-policy is applied.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check VPN IPv4 routes to which an EVPN route-policy has been applied.
* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check VPN IPv6 routes to which an EVPN route-policy has been applied.