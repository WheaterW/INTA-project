Configuring a Community Attribute-Related Policy
================================================

A policy that references a community attribute needs to be configured before the community attribute is set for routing information.

#### Procedure

* Configure a community attribute-based route-policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A route-policy with a node is created, and the route-policy view is displayed.
  3. (Optional) Configure if-match clauses for the route-policy. Community attributes can be added only to the routes that match if-match clauses, and the community attributes of only the routes that match the if-match clauses can be modified. For details about the configuration, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
  4. Configure community or extended community attributes for BGP routes. This section describes only common configurations. For details, see [(Optional) Configuring an apply Clause](dc_vrp_route-policy_cfg_0010.html).
     
     
     + To configure community attributes for BGP routes, run the [**apply community**](cmdqueryname=apply+community+internet+no-advertise+no-export) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       A maximum of 32 community attributes can be configured using this command at a time.
     + To configure the BGP VPN-Target extended community attribute, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] command.
     + To configure the SoO extended community attribute for BGP routes, run the [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo+additive) { *site-of-origin* } &<1-16> **additive** command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a community attribute-based route-filter.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name* or [**edit xpl route-filter**](cmdqueryname=edit+xpl+route-filter) *route-filter-name*
     
     
     
     A route-filter is created, and the route-filter view is displayed.
  3. (Optional) Configure XPL common and condition clauses. Community attributes can be added only to the routes that match XPL clauses, and the community attributes of only the routes that match the XPL clauses can be modified. For details about the configuration, see [Common Clauses](dc_vrp_xpl_cfg_0015.html) and [Condition Clauses](dc_vrp_xpl_cfg_0016.html) in "XPL Configuration."
  4. Configure community or extended community attributes for BGP routes.
     
     
     + Configure community attributes for BGP routes. For configuration details, see [Action Clauses Used to Set Community Attributes for BGP Routes](dc_vrp_xpl_cfg_0017.html#EN-US_CONCEPT_0172366625__setion_03) in "XPL Configuration."
     + Configure the Link Bandwidth extended community attribute for BGP routes. For configuration details, see [Setting a Link Bandwidth Extended Community Attribute for BGP Routes](dc_vrp_xpl_cfg_0017.html#EN-US_CONCEPT_0172366625__section856910644816) in "XPL Configuration."
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.