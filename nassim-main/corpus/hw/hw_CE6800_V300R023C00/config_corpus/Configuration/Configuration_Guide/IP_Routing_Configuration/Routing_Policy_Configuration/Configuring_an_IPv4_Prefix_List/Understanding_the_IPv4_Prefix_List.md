Understanding the IPv4 Prefix List
==================================

An IP prefix list is a filter that contains a group of matching rules and is used to filter routes to be advertised or accepted. You can specify an IP prefix and a mask length range in an IP prefix list so that the destination network segment addresses or next-hop addresses of routes can be matched against the IP prefix list. IP prefix lists can be configured for both IPv4 and IPv6 routes, and IPv4 and IPv6 prefix lists are implemented in the same way. An IP prefix list is matched against routes using either of the following parameters:

* Mask length: A mask length, together with an IP address, identifies an IP prefix. The IP prefix in an IP prefix list is used to filter routes with the same IP prefix. For example, the mask length of a route to 10.1.1.1/16 is 16, indicating that the valid prefix is 16 (10.1.0.0).
* Mask length range: A mask length range can be defined in an IP prefix list to match routes with the same IP prefix and different mask lengths within the specified mask length range.

#### IP prefix matching rules

Multiple indexes can be created in an IP prefix list, and each index identifies a matching rule. As shown in [Figure 1](#EN-US_CONCEPT_0000001130783778__fig8214115318126), routes to be filtered are matched against an IP prefix list in ascending order by IP prefix index.

* If a route matches an index that is mapped to an entry configured in permit mode, the route is permitted. If the index is mapped to an entry configured in deny mode, the route is rejected.
* If the route does not match any index in the IP prefix list, the route is filtered out.

**Figure 1** IP prefix matching rules  
![](figure/en-us_image_0000001130783788.png)

Rules for filtering routes based on an IP prefix list are as follows:

* Sequential match: Routes are matched against IP prefixes one by one in the IP prefix list in ascending order by index number of the IP prefixes. During configuration, note that entries in the same IP prefix list can be sorted in different orders by index, leading to different filtering results.
* Unique match: Once a route matches a prefix, the route stops being matched against other prefixes in the IP prefix list.
* Default deny: If routes do not match any prefix in an IP prefix list, the routes are filtered out by default. If one or more entries in deny mode are created in the IP prefix list, create an entry to allow all other routes to pass.

#### Rules for Matching Routes Against Masks in IP Prefixes

Compared with an ACL, an IP prefix list is easy to configure and flexible to apply and can match route masks.

An IPv4 prefix list can be configured using the **ip ip-prefix** command. The common syntax is as follows:

[**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [ **index** *index-number* ] { **permit** | **deny** } *ipv4-address* *mask-length* [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]

The *ipv4-address* *mask-length* parameters set a network ID and the [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] parameters set a mask length range for routes to be filtered. [Figure 1](#EN-US_CONCEPT_0000001130783778__fig8214115318126) describes address range parameters in an IP prefix list.

**Table 1** Parameters used to set a mask length range in an IP prefix list
| Parameter | Meaning |
| --- | --- |
| *ipv4-address* | Specifies a network ID. |
| *mask-length* | Specifies the number of the most significant bits in a specified network ID that a route prefix must match. |
| **greater-equal** *greater-equal-value* | Specifies the minimum mask length in a mask length range. |
| **less-equal** *less-equal-value* | Specifies the maximum mask length in a mask length range. |

For given routes to be filtered, they can be matched against a specific mask length or against a mask length range:

* If neither **greater-equal** nor **less-equal** is specified, the routes are exactly matched against the specified *mask-length*.
* If only **greater-equal** is specified, the routes are matched against the mask length range of [*greater-equal-value*, 32]. *greater-equal-value* must be greater than or equal to *mask-length*.
* If only **less-equal** is specified, the routes are matched against the mask length range of [*mask-length*, *less-equal-value*].
* If both **greater-equal** and **less-equal** are specified, the routes are matched against the mask length range of [*greater-equal-value*, *less-equal-value*].

![](public_sys-resources/note_3.0-en-us.png) 

*ipv4-address* can be set to all 0s (0.0.0.0) that is a wildcard address. In this case, either a mask length or a mask length range can be specified for the prefix:

* If a mask length is specified, all routes with the mask length are permitted or rejected.
* If a mask length range is specified, all routes with mask lengths in the range are permitted or rejected.

[Table 2](#EN-US_CONCEPT_0000001130783778__table396025011510) describes the implementation of route matching rules when the preceding wildcard address is used.

**Table 2** Implementation of wildcard address-based route matching rules (IPv4)
| Whether *greater-equal* and *less-equal* Are Configured | Condition | Matching Rule | Example |
| --- | --- | --- | --- |
| Neither *greater-equal* nor *less-equal* is configured. | After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and 0, respectively. | Matches only default IPv4 routes. | An IPv4 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ip-prefix aa index 10 permit 1.1.1.1 0 Error: Failed to add the address prefix list 0.0.0.0/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 0 ```  Matching rule: Only the default IPv4 route is permitted. |
| After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and *X* (non-0 value), respectively. | Matches all routes with the mask length of *X*. | Pre-processing:  ``` ip ip-prefix aa index 10 permit 0.0.1.1 16 ```  Post-processing:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 16 ```  Matching rule: Routes with the mask length of 16 are permitted. |
| *greater-equal* is configured, but *less-equal* is not. | After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and 0, respectively. | Matches all routes with mask lengths within the range of *greater-equal* to 32. | An IPv4 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ip-prefix aa index 10 permit 1.1.1.1 0 greater-equal 16 Error: Failed to add the address prefix list 0.0.0.0/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 0 greater-equal 16 less-equal 32 ```  Matching rule: Routes with mask lengths within the range of 16 to 32 are permitted. |
| After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and *X* (non-0 value), respectively. | Matches all routes with mask lengths within the range of *greater-equal* to 32. | Pre-processing:  ``` ip ip-prefix aa index 10 permit 0.0.1.1 16 greater-equal 20 ```  Post-processing:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 16 greater-equal 20 less-equal 32 ```  Matching rule: Routes with mask lengths within the range of 20 to 32 are permitted. |
| *greater-equal* is not configured, but *less-equal* is configured. | After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and 0, respectively. | Matches all routes with mask lengths within the range of 0 to *less-equal*. | An IPv4 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ip-prefix aa index 10 permit 1.1.1.1 0 less-equal 30 Error: Failed to add the address prefix list 0.0.0.0/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 0 less-equal 30 ```  Matching rule: Routes with mask lengths within the range of 0 to 30 are permitted. |
| After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and *X* (non-0 value), respectively. | Matches all the routes whose mask lengths are within the range of *X* to *less-equal*. | Pre-processing:  ``` ip ip-prefix aa index 10 permit 0.0.1.1 16 less-equal 30 ```  Post-processing:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 16 greater-equal 16 less-equal 30 ```  Matching rule: Routes with mask lengths within the range of 16 to 30 are permitted. |
| Both *greater-equal* and *less-equal* are configured. | After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and 0, respectively. | Matches all routes with mask lengths within the range from *greater-equal* to *less-equal*. | An IPv4 prefix list cannot be configured if the prefix and mask do not match. For example:  ``` ip ip-prefix aa index 10 permit 1.1.1.1 0 greater-equal 5 less-equal 30 Error: Failed to add the address prefix list 0.0.0.0/0, because the destination address and mask do not match. ```  Correct configuration:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 0 greater-equal 5 less-equal 30 ```  Matching rule: Routes with mask lengths within the range of 5 to 30 are permitted. |
| After the processing, *ipv4-address* and *mask-length* are 0.0.0.0 and *X* (non-0 value), respectively. | Matches all routes with mask lengths within the range from *greater-equal* to *less-equal*. | Pre-processing:  ``` ip ip-prefix aa index 10 permit 0.0.1.1 16 greater-equal 20 less-equal 30 ```  Post-processing:  ``` ip ip-prefix aa index 10 permit 0.0.0.0 16 greater-equal 20 less-equal 30 ```  Matching rule: Routes with mask lengths within the range of 20 to 30 are permitted. |