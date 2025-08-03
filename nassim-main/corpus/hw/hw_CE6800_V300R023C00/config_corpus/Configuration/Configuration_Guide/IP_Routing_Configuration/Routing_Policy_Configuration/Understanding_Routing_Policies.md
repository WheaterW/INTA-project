Understanding Routing Policies
==============================

Understanding Routing Policies

#### Implementation

Routing policies are implemented in the following steps:

1. Define rules: The rules that contain characteristics of routes to which routing policies are applied need to be defined. You can specify attributes, such as a destination address and the address of a device that advertises routes, in the rules.
2. Apply rules: The rules are used in a routing policy to advertise, accept, and import routes.


#### Filters

A filter, the core of a routing policy, is used to define a set of matching rules. Various filters are provided for routing policies. [Table 1](#EN-US_CONCEPT_0000001130623984__tab_dc_vrp_route-policy_feature_001401) lists applicable scopes and matching conditions of different filters.

**Table 1** Filter comparison
| Filter | Applicable Scope | Matching Condition |
| --- | --- | --- |
| [ACL](vrp_route-policy_cfg_0006.html) | Dynamic routing protocols | Source address, destination address, and next hop |
| [IP prefix list](vrp_route-policy_cfg_0004.html) | Dynamic routing protocols | Source address, destination address, and next hop |
| [AS\_Path filter](vrp_route-policy_cfg_0007.html) | BGP | AS\_Path attribute |
| [Community filter](vrp_route-policy_cfg_0008.html) | BGP | Community attribute |
| [Large-community](vrp_route-policy_cfg_0009.html) | BGP | Large-Community attribute |
| [Extended community](vrp_route-policy_cfg_0119.html) | BGP | VPN-Target extended community attribute, SoO extended community attribute, encapsulation extended community attribute |
| [Route Distinguisher (RD) filter](vrp_route-policy_cfg_0010.html) | VPN | RD attribute |
| [Route-Policy](vrp_route-policy_cfg_0011.html) | Dynamic routing protocols | Items such as the destination address, next-hop address, metric, interface information, route type, ACL, IP prefix list, AS\_Path filter, community filter, extended community filter, MAC address list, and RD filter |

The ACL, IP prefix list, AS\_Path filter, Large-community filter, extended community filter, RD filter, and community filter can filter routes but cannot modify route attributes. A route-policy is a comprehensive filter and can use filters (including ACLs, IP prefix lists, AS\_Path filters, Large-community filters, extended community filters, RD filters, and community filters) as matching conditions to filter routes and modify route attributes for matched routes.

ACLs and IP prefix lists can be used by all routing protocols. As shown in [Figure 1](#EN-US_CONCEPT_0000001130623984__fig206471120121213), all routing protocols can directly use ACLs and IP prefix lists to filter routes.

**Figure 1** Invoking relationships in routing policies for any routing protocol  
![](figure/en-us_image_0000001130623998.png)

AS\_Path filters, community filters, Large-community filters, extended community filters, and RD filters are exclusively used by BGP. As shown in [Figure 2](#EN-US_CONCEPT_0000001130623984__fig2122131815136), AS\_Path filters, community filters, Large-community filters, extended community filters, and RD filters can be directly applied to BGP peers. After an AS\_Path filter, community filter, Large-community filter, extended community filter, or RD filteris bound to a route-policy, the route-policy can apply to the routes imported to BGP using the **network** command, BGP peers, and BGP route dampening. In addition, BGP route attributes can be modified using such a route-policy.

**Figure 2** Invoking relationship of BGP-specific routing policies  
![](figure/en-us_image_0000001130623996.png)
![](public_sys-resources/note_3.0-en-us.png) 

Invoking rules in filter-policies are described in routing protocol-specific documents. For details about the process of invoking rules in a filter-policy, see a routing protocol-specific document.