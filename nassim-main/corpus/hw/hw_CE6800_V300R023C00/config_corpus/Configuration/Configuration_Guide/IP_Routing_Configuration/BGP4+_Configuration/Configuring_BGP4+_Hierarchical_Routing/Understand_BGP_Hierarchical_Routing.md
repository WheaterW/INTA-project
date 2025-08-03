Understand BGP Hierarchical Routing
===================================

Understand BGP Hierarchical Routing

#### Definition

BGP hierarchical routing refers to the mechanism in which BGP routes on a device are classified into base routes and hierarchical routes. BGP hierarchical routing speeds up route convergence in the case of faults on data center networks, especially when hierarchical routes greatly outnumber base routes. To implement BGP hierarchical routing convergence, the hierarchical convergence attribute is introduced. For details about this attribute, see [Hierarchical Convergence Attribute](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_section7461258183614). Base routes, which can be considered device reachability routes, carry the hierarchical convergence attribute and have a high priority. When other devices receive the base routes, they preferentially perform recursion, convergence, delivery, forwarding, and advertisement for the base routes. Hierarchical routes, which can be considered service routes (routes learned from external BGP peers for example), also carry the hierarchical convergence attribute. When devices receive hierarchical routes, they directly depend on the recursion results of base routes, which reduces the hierarchical route processing cost. As long as the basic routes can be converged, other services can also be converged based on the convergence results of the basic routes.


#### Hierarchical Convergence Attribute

The hierarchical convergence attribute is an extended optional transitive attribute used in BGP hierarchical routing and uses a reserved Type value (255).

![](public_sys-resources/note_3.0-en-us.png) 

If a Huawei device needs to communicate with a non-Huawei device that cannot process the extended attribute with the Type value of 255, you need to disable the extended attribute on the Huawei device. Otherwise, the two devices cannot communicate with each other.

[Figure 1](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig68300311578) shows the format of the BGP hierarchical convergence attribute, and [Table 1](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_table1755319320291) describes the fields in the attribute.

**Figure 1** Format of the BGP hierarchical convergence attribute  
![](figure/en-us_image_0000001176743657.png)

**Table 1** Fields in the BGP hierarchical convergence attribute
| Field | Description |
| --- | --- |
| HUAWEI Private Number | The value of this field is fixed at 2011. If the value is not 2011, the attribute with the Type value of 255 is not processed. However, if the packet contains both the correct (value of 2011) and incorrect (value other than 2011) HUAWEI Private Number attributes, the device still processes the attribute with the Type value of 255. |
| Feature Code Point | The value of this field is fixed at 2. If the value of this field is not 2, the attribute is not processed for hierarchical convergence. Instead, the field is parsed based on the corresponding feature. |
| Version Number | The value of this field is fixed at 1. If the value of **Feature Code Point** is 2, but the value of this field is not 1, the attribute is not processed for hierarchical convergence; in this case, the system skips the current attribute group and parses the next attribute group. |
| Length | Length of the attribute. |
| subval | Content of the attribute. |

The preceding five fields shown in [Table 1](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_table1755319320291) constitute a group of private attributes. A packet carrying the attribute with the Type value of 255 may contain multiple groups of private attributes. The attribute can be considered a hierarchical convergence attribute only if the combination meets the preceding definition. If a received route carries multiple groups of private attributes, the device only processes the first group of private attributes in which **Feature Code Point** is set to 2, despite an error that may occur in these private attributes. The subsequent private attributes with **Feature Code Point** set to 2 are ignored. In addition, one **Feature Code Point** can carry only one basic route or hierarchical convergence attribute. If a received route carries multiple basic route attributes or hierarchical convergence attributes, or carries both basic route and hierarchical convergence attributes, the device determines that an exception occurs and processes the route as a common one.

[Table 2](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_table13813038164813) shows the detailed definition format of the BGP hierarchical convergence attribute. This definition can be used to distinguish base routes from hierarchical routes.

**Figure 2** Detailed definition format of the BGP hierarchical convergence attribute  
![](figure/en-us_image_0000001130624194.png)

**Table 2** Fields in the detailed definition format of the BGP hierarchical convergence attribute
| Field | Description |
| --- | --- |
| sub-type | The value of this field is fixed at 1. |
| len | Length of the content following the **sub-type** field. For a base route, the value of this field is fixed at 2. If the value is not 2, the attribute is invalid and ignored. |
| Flag | Flag, in the format of S | T | R (2â7) |. The S bit indicates the protocol stack type. If the S bit is not set, it indicates IPv4; if the S bit is set, it indicates IPv6. The T bit indicates the attribute type. If the T bit is not set, it identifies a base route. If the T bit is set, it identifies a hierarchical route. |
| mask | Mask length. |
| Prefix | IPv4 or IPv6 prefix, whose length is determined by the mask length. |

[Figure 3](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig10840522300), [Figure 4](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig1021019204571), [Figure 5](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig161814541427), and [Figure 6](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig1965613521868) illustrate base route and hierarchical route examples.

**Figure 3** IPv4 base route example  
![](figure/en-us_image_0000001176743663.png)
**Figure 4** IPv6 base route example  
![](figure/en-us_image_0000001130624196.png)
**Figure 5** IPv4 hierarchical route example  
![](figure/en-us_image_0000001176743659.png)
**Figure 6** IPv6 hierarchical route example  
![](figure/en-us_image_0000001176743661.png)

#### BGP Hierarchical Route Advertisement

[Figure 7](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig_dc_vrp_bgp_feature_001903) shows the equivalent networking of a data center network with two PODs connected through planes. In each POD, a Spine-Leaf network is deployed. A large number of external routes are imported to Device A. To ensure fast route convergence in the case of a device or link failure, BGP hierarchical routing can be deployed on DeviceA, and hierarchical routing convergence can be deployed on other nodes.

**Figure 7** Data center network with two PODs  
![](figure/en-us_image_0000001176743655.png "Click to enlarge")

BGP hierarchical routing is deployed on DeviceA. The route advertisement process is as follows:

1. On DeviceA, the route 10.1.1.1/32 is configured as a base route and the BGP routes learned from external peers are configured as hierarchical routes. DeviceA advertises this base route and hierarchical routes to Spine11 and Spine12.

2. Spine11 receives the base route advertised by DeviceA, and the next hop is a BGP peer of Spine11.

3. Spine11 receives the hierarchical routes advertised by DeviceA, with the **Prefix** field in the hierarchical convergence attribute being 10.1.1.1/32. Spine11 uses 10.1.1.1/32 as the next hop address for route recursion. The process of advertising routes on other devices is the same, and is therefore not described here.


#### Convergence in Case of a Failure

[Figure 8](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_fig15656118122417) shows a network in which a failure has occurred. [Table 3](#EN-US_CONCEPT_0000001176741845__en-us_concept_0000001130624138_table146421945194316) describes the convergence process upon each possible failure point.

**Figure 8** Fault scenario  
![](figure/en-us_image_0000001176743649.png)

**Table 3** Route convergence in case of a failure
| Failure point | Convergence |
| --- | --- |
| 1 | The link between DeviceA and Spine11 fails.  1. Spine11 detects the failure based on the fact that an interface down event has caused the EBGP peer relationship to go down or that the next hop is unreachable.  Spine11 first processes the base route advertised by DeviceA by updating the status of the base route to unreachable and sending a withdrawal message to P11 and P12.  Spine11 also updates the status of the hierarchical routes advertised by DeviceA to unreachable and sends a withdrawal message to P11 and P12.  2. P11 first receives the base route withdrawal message advertised by Spine11, performs convergence for the base route, and advertises a withdrawal message to Spine21.  P11 then receives the hierarchical route withdrawal message advertised by Spine11. After convergence is complete, P11 advertises a withdrawal message to Spine21. The processing on P12 is the same.  3. After receiving the base route withdrawal message advertised by P11, Spine21 performs convergence for the base route. Based on the convergence result, all hierarchical routes converge accordingly.  Spine21 also receives the base route withdrawal message advertised by P12. After convergence is complete, Spine21 advertises a withdrawal message to DeviceB.  4. DeviceB receives the base route withdrawal message advertised by Spine21. After the convergence of the base route is complete, the base route to DeviceA can be forwarded only through Spine22. Then, the hierarchical routes converge based on the convergence result of the base route. After the convergence of the hierarchical routes is complete, the hierarchical routes to DeviceA can also be forwarded only through Spine22, which concludes the service convergence. |
| 2 | Spine11 fails.  1. P11 detects the failure based on the fact that an interface down event has caused the EBGP peer relationship to go down or that the next hop is unreachable.  P11 first processes the base route advertised by DeviceA by updating the status of the base route to unreachable and sending a withdrawal message to Spine21. The processing on P12 is the same.  2. After receiving the base route withdrawal message advertised by P11, Spine21 performs convergence for the base route. Based on the convergence result, all hierarchical routes converge accordingly.  Spine21 also receives the base route withdrawal message advertised by P12. After convergence is complete, Spine21 advertises a withdrawal message to DeviceB.  3. DeviceB receives the base route withdrawal message advertised by Spine21. After the convergence of the base route is complete, the base route to DeviceA can be forwarded only through Spine22. Then, the hierarchical routes converge based on the convergence result of the base route. After the convergence of the hierarchical routes is complete, the hierarchical routes to DeviceA can also be forwarded only through Spine22, which concludes the service convergence. |