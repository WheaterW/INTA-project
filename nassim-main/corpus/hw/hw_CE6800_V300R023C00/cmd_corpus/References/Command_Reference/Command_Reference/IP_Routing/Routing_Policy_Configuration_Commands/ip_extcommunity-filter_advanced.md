ip extcommunity-filter advanced
===============================

ip extcommunity-filter advanced

Function
--------



The **ip extcommunity-filter advanced** command adds an advanced VPN-Target extended community filter.

The **undo ip extcommunity-filter advanced** command deletes a specified advanced VPN-Target extended community filter.



By default, no advanced VPN-Target extended community filter is configured.


Format
------

**ip extcommunity-filter advanced** *advanced-extcomm-filter-name* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip extcommunity-filter advanced** *advanced-extcomm-filter-name* [ **index** *index-number* ] [ [ *matchMode* ] *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-number* | Specifies the sequence number of an advanced VPN-Target extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the advanced VPN-Target extended community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the VPN-Target extended community filter to permit. * deny: Sets the matching mode of the VPN-Target extended community filter to deny. |
| *regular-expression* | Specifies the regular expression matched the VPN-Target extended community. | The value is a string of 1 to 1024 characters, spaces supported. |
| **advanced** *advanced-extcomm-filter-name* | Specifies the name of the advanced VPN-Target extended community filter. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A VPN-Target extended community filter can be used as a matching condition of a route-policy using a command, such as the if-match extcommunity-filter zz command.The relationship between the rules of the VPN-Target extended community filter is "OR", which is different from that of an RD filter. This is because each route has only one RD but can have multiple communities.The **undo ip extcommunity-filter** command deletes a specified VPN-Target extended community filter.The display ip extcommunity-filter command displays detailed configurations of the VPN-Target extended community filter.



**Configuration Impact**



The ip extcommunity-filter command filters routes based on the RT attributes of the routes. The routes that match the filtering are permitted to pass through, and the routes that fail to match the filtering are denied.



**Precautions**

The extended community attributes of a route include VPN-Target and Source of Origin (SoO). This command is used to match VPN-Target.The default action of a VPN-Target extended community filter is deny. That is, if a route is not permitted in a filtering, the route cannot pass the filtering. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter.For an advanced VPN-Target extended community filter, if the attribute value is in the format of 4-byte AS number:2-byte user-defined number, the filtering rule using the regular expression is affected by the **as-notation plain** command.

* If the **as-notation plain** command is run, a regular expression in the format of 4-byte AS number:2-byte user-defined number must be configured so that routes can match the regular expression.
* If the **as-notation plain** command is not run, you need to configure a regular expression in the format of 4-byte AS number in dotted notation:2-byte user-defined number so that routes can match the regular expression.Note: If the **as-notation plain** command is run, you need to reconfigure the regular expression. Otherwise, routes may fail to match the inbound or outbound policy, causing network faults.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.


Example
-------

# Configure a VPN-Target extended community filter named aa.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter advanced aa permit 200:*

```