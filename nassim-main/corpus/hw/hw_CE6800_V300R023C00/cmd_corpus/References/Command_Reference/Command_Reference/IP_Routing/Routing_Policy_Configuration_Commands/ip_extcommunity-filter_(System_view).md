ip extcommunity-filter (System view)
====================================

ip extcommunity-filter (System view)

Function
--------



The **ip extcommunity-filter** command adds an advanced VPN-Target extended community filter.

The **undo ip extcommunity-filter** command deletes a specified advanced VPN-Target extended community filter.



By default, no advanced VPN-Target extended community filter is configured.


Format
------

**ip extcommunity-filter** *advanced-extcomm-filter-num* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip extcommunity-filter** *advanced-extcomm-filter-num* [ **index** *index-number* ] [ [ *matchMode* ] *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *advanced-extcomm-filter-num* | Specifies the sequence number of a VPN-Target extended community filter. | The value is an integer ranging from 200 to 399. |
| **index** *index-number* | Specifies the sequence number of a VPN-Target extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the VPN-Target extended community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the VPN-Target extended community filter to permit. * deny: Sets the matching mode of the VPN-Target extended community filter to deny. |
| *regular-expression* | Specifies the regular expression matched the VPN-Target extended community. | The value is a string of 1 to 1024 characters, spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A VPN-Target extended community filter can be used as a matching condition of a route-policy using a command, such as the if-match extcommunity-filter zz command.The relationship between the rules of the VPN-Target extended community filter is "OR", which is different from that of an RD filter. This is because each route has only one RD but can have multiple communities.For example, a VPN-Target extended community filter can be set in either of the following formats, with the same filtering result:Format 1:ip extcommunity-filter 1 permit rt 100:1 rt 200:1 rt 300:1The filter has one rule, which consists of three VPN-Targets: 100:1, 200:1, and 300:1. The relationship between them is "OR."Format 2:ip extcommunity-filter 1 permit rt 100:1ip extcommunity-filter 1 permit rt 200:1 rt 300:1The filter has two rules. Rule 1 consists of VPN-Target 100:1, and rule 2 consists of VPN-Targets 200:1 and 300:1. The relationship between the two rules is "OR."In format 2, the VPN-Target extended community defined in each rule must be a sub-set of route VPN-Target extended communities so that the rule can be matched.The **undo ip extcommunity-filter** command deletes a specified VPN-Target extended community filter.The display ip extcommunity-filter command displays detailed configurations of the VPN-Target extended community filter.



**Configuration Impact**



The ip extcommunity-filter command filters routes based on the RT attributes of the routes. The routes that match the filtering are permitted to pass through, and the routes that fail to match the filtering are denied.



**Precautions**

The extended community attributes of a route include VPN-Target and Source of Origin (SoO). This command is used to match VPN-Target.The default action of a VPN-Target extended community filter is deny. That is, if a route is not permitted in a filtering, the route cannot pass the filtering. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter.For an advanced VPN-Target extended community filter, if the attribute value is in the format of 4-byte AS number:2-byte user-defined number, the filtering rule using the regular expression is affected by the **as-notation plain** command.

* If the **as-notation plain** command is run, a regular expression in the format of 4-byte AS number:2-byte user-defined number must be configured so that routes can match the regular expression.
* If the **as-notation plain** command is not run, you need to configure a regular expression in the format of 4-byte AS number in dotted notation:2-byte user-defined number so that routes can match the regular expression.Note: If the **as-notation plain** command is run, you need to reconfigure the regular expression. Otherwise, routes may fail to match the inbound or outbound policy, causing network faults.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.


Example
-------

# Configure VPN-target extended community filter 1 with rt configured.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter 1 deny rt 200:200

```