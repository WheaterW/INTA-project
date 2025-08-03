Configuring the Function to Increase the Priority of EVPN MAC Routes
====================================================================

Configuring the function to increase the priority of EVPN MAC routes helps prevent MAC routes received from the network side from being suppressed in special scenarios.

#### Usage Scenario

On the EVPN VPLS network shown in [Figure 1](#EN-US_TASK_0000001419796597__fig17853203404315), two PEs are connected through both network-side and access-side links. As a result, MAC route flapping may occur, and the local MAC routes learned from the access side may be the same as the remote MAC routes learned from EVPN peers. If this is the case, the MAC routes received from the network side are suppressed. To prevent this situation, configure the function to increase the priority of MAC routes learned from the network side.

**Figure 1** EVPN VPLS networking  
![](figure/en-us_image_0000001420839945.png)

#### Pre-configuration Tasks

Before configuring the function to increase the priority of EVPN MAC routes, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPLS over SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html).

#### Procedure

1. Configure a route-policy on PE2 to set the community attributes of EVPN MAC routes to be advertised to other PEs. This section uses community attributes as an example. For details about other policy settings, see [Configuring an EVPN Route-Policy](dc_vrp_evpn_cfg_0150.html).
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
   4. Run the [**peer**](cmdqueryname=peer+advertise-community) { *group-name* | *ipv4-address* | *ipv6-address* } **advertise-community** command to advertise the community attribute to the peer.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* command to create a route-policy with a specified node and enter the route-policy view.
   8. Run the [**if-match route-type**](cmdqueryname=if-match+route-type) **evpn** **mac** command to configure a matching rule for the EVPN MAC route type.
   9. Run the [**apply community**](cmdqueryname=apply+community) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ] or [**apply community community-list**](cmdqueryname=apply+community+community-list) *community-list-name* [ **additive** ] command to set route attributes.
   10. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   12. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the EVPN instance view.
   13. Run the [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* command to apply an export route-policy to the EVPN instance, so that the EVPN instance can filter routes to be advertised.
   14. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Route receiver PE1 applies a route-policy to increase the priority of learned EVPN MAC routes.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Configure a community filter.
      
      
      * To configure a standard community filter, run the [**ip community-filter basic**](cmdqueryname=ip+community-filter+basic) *basCfName* [ **index** *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> or [**ip community-filter**](cmdqueryname=ip+community-filter) *cfIndex* [ **index** *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> command.
      * To configure an advanced community filter, run the [**ip community-filter**](cmdqueryname=ip+community-filter) { **advanced** *comm-filter-name* | *adv-comm-filter-num* } [ **index** *index-number* ] *matchMode* *regular-expression* command.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node* command to create a route-policy with a specified node and enter the route-policy view.
   5. Run the [**if-match community-filter**](cmdqueryname=if-match+community-filter) { *basIndex* [ **whole-match** ] | *AdvIndex* [ **sort-match** ]} &<1-16> command to configure a matching rule based on the community filter.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   8. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the EVPN instance view.
   9. Run the [**mac-high-priority trigger route-policy**](cmdqueryname=mac-high-priority+trigger+route-policy) *policy-name* command to apply a route-policy to increase the priority of EVPN MAC routes imported into the EVPN instance.
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp evpn all routing-table mac-route**](cmdqueryname=display+bgp+evpn+routing-table) *prefix* command on PE1 to check whether the received MAC route carries the community attribute. *prefix* is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X]. For example, *prefix* can be 0:48:0001-0001-0001:0:0.0.0.0.