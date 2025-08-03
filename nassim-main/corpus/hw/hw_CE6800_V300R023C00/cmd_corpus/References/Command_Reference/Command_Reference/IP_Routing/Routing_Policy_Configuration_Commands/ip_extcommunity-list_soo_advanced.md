ip extcommunity-list soo advanced
=================================

ip extcommunity-list soo advanced

Function
--------



The **ip extcommunity-list soo advanced** command configures an advanced Source of Origin (SoO) extended community filter.

The **undo ip extcommunity-list soo advanced** command deletes a specified advanced SoO extended community filter.



By default, no advanced SoO extended community filter is configured.


Format
------

**ip extcommunity-list soo advanced** *advanced-extcomm-filter-name* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip extcommunity-list soo advanced** *advanced-extcomm-filter-name* [ **index** *index-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-number* | Specifies the sequence number of an SoO extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the SoO extended community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the SoO extended community filter to permit. * deny: Sets the matching mode of the SoO extended community filter to deny. |
| *regular-expression* | Specifies an SoO extended community-based regular expression. | The value is a string of 1 to 1024 characters, spaces supported. |
| **advanced** *advanced-extcomm-filter-name* | Specifies the name of the advanced SoO extended community filter. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all digits. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



SoO records the BGP route originator. To configure an SoO extended community filter so that BGP routes carrying SoO can be filtered, run the **ip extcommunity-list soo** command.An SoO extended community filter can be used as a matching condition of a route-policy using a command, such as the **if-match extcommunity-list soo aaa** command.The relationship between the rules of the SoO extended community filter is "AND".The **undo ip extcommunity-list soo** command deletes a specified SoO extended community filter.The **display ip extcommunity-list soo** command displays detailed configurations of the SoO extended community filter.



**Precautions**

The extended community attributes of routes include the VPN target and SoO. This command is used to match the SoO.The default action of a source of origin (SoO) extended community filter is deny. That is, if a route is not permitted during filtering, the route cannot pass the filtering. If all the filtering rules in a filter are in deny mode, no route can pass the filter. In this case, you need to set set a permit rule after multiple deny rules (or one deny rule) to allow all the other routes to pass the filter.For an SoO advanced extended community filter, if the attribute value is in the format of 4-byte AS number:2-byte user-defined number, the filtering rule using the regular expression is affected by the **as-notation plain** command.

* If the **as-notation plain** command is run, a regular expression in the format of 4-byte integer AS number:2-byte user-defined number must be configured so that routes can match the regular expression.
* If the **as-notation plain** command is not run, you need to configure a regular expression in the format of 4-byte AS number in dotted notation:2-byte user-defined number so that the route can match the rule.Note: If the **as-notation plain** command is configured, you need to reconfigure the regular expression. Otherwise, routes may fail to match the import or export policy, causing network faults.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the route-policy, reduce the number of regular expressions or use non-regular expression matching commands.


Example
-------

# Configure an SoO extended community filter named aaa with SoO configured.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-list soo advanced aaa permit ^2

```