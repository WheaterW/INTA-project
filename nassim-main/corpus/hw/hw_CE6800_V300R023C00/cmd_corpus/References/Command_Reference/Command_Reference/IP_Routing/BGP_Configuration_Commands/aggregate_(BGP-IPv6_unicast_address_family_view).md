aggregate (BGP-IPv6 unicast address family view)
================================================

aggregate (BGP-IPv6 unicast address family view)

Function
--------



The **aggregate** command adds a summarized route to the BGP routing table. The outbound interface of the summarized route on the local Router is NULL 0. When receiving the summarized route, each of the other devices automatically adds its local outbound interface to the summarized route.

The **undo aggregate** command disables the function.



By default, no routes are summarized.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**aggregate** *ipv6-address* *mask-length* [ **as-set** | **detail-suppressed** | **attribute-policy** *route-policy-name1* | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \*

**undo aggregate** *ipv6-address* *mask-length* [ **as-set** | **detail-suppressed** | **attribute-policy** *route-policy-name1* | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 address of the summarized route. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the network mask length of the summary route. | The value is an integer ranging from 1 to 128. |
| **as-set** | Generates a route carrying the AS-Set attribute. | - |
| **detail-suppressed** | Advertises only the summary route. | - |
| **attribute-policy** *route-policy-name1* | Specifies the name of a route-policy for setting attributes of a summary route. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **origin-policy** *route-policy-name2* | Specifies the name of the route-policy that allows route summarization. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **suppress-policy** *route-policy-name3* | Specifies the name of the route-policy for suppressing the advertisement of specified routes. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP route summarization is classified into manual summarization and automatic summarization. The **aggregate** command is used to implement manual summarization. Manual summarization takes precedence over automatic summarization. The aggregate ipv4-address { mask | mask-length } command can be used to summarize specific routes in the local BGP routing table and advertise all summary routes and specific routes. The summary route inherits the Origin attribute of the specific routes. If the Origin attributes of the specific routes are different, the route with the largest Origin attribute priority (incomplete\ > egp\ > igp) is selected. In addition, the generated summary route carries the atomic-aggregate attribute. Except the Origin and Atomic-aggregate attributes, the summary route discards all other attributes of the specific routes.To ensure that summary routes can prevent loops, you can specify the as-set keyword to create a summary route for loop detection. The summary route inherits the Origin, AS\_Path (loop-proof), community, and large-community attributes of specific routes. The summary route also carries the community attributes of all specific routes. When the number of community attributes of the summary route exceeds 255, the summarization stops and the routes that are not summarized are advertised as specific routes. If multiple AS\_Paths need to be summarized, exercise caution when using this parameter because frequent changes of specific routes may cause route flapping.detail-suppressed is used to suppress the advertisement of all specific routes corresponding to the summary route. Only the summary route is advertised. The summary route carries the atomic-aggregate attribute but does not carry the community attribute of the specific routes.The suppress-policy keyword can be used to generate summary routes but suppress the advertisement of specified routes. You can use the if-match clause of the route-policy to selectively suppress some specific routes. That is, the routes that match the route-policy are suppressed, but the routes that do not match the route-policy are still advertised. You can also run the **peer route-policy** command to achieve the same effect.If origin-policy is specified, a summary route is generated only when the route-policy is matched.The attribute-policy keyword can be used to set the attributes of the summary route. If the AS\_Path attribute is set in the policy through the **apply as-path** command and the keyword as-set is set in the **aggregate** command, the **apply as-path** command in the policy does not take effect. You can also run the **peer route-policy** command to achieve the same effect.

**Configuration Impact**



If detail-suppressed is configured in the command, the advertisement of specific routes will be suppressed. If suppress-policy is configured in the command, the advertisement of the specific routes that match the policy will be suppressed.



**Precautions**

When you run the **undo aggregate** command, the system checks the optional parameters (attribute-policy, origin-policy, suppress-policy, as-set, and detail-suppressed). If any of the optional parameters is not enabled, the **undo aggregate** command fails to be executed.After the **aggregate** command is run, the summary route may be preferentially selected to guide traffic forwarding after being leaked to another VPN because this route has a high priority. As a result, traffic is discarded. Therefore, you need to properly plan the mask length of the summary route.If some summary routes are withdrawn, black holes may occur, causing traffic loss.After route summarization is configured, it takes effect only when there is a BGP route whose mask is greater than the mask of the summary route. When configuring route summarization, analyze or configure special policies in advance if routes change. This prevents packet loss caused by external route changes.Conditions for BGP specific routes to participate in summarization:

1. They are optimal routes in the BGP routing table;
2. They are non-summary routes;
3. They are non-labeled routes;
4. A specific route whose mask is greater than the mask of the summary route exists.


Example
-------

# Create a summarized route carrying the AS\_Path attribute that contains the AS\_Path information of specific routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] aggregate 2001:db8:1::1 64 as-set

```