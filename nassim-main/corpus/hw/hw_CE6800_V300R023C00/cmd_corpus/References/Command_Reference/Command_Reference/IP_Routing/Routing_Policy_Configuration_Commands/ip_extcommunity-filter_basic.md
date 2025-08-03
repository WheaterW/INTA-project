ip extcommunity-filter basic
============================

ip extcommunity-filter basic

Function
--------



The **ip extcommunity-filter basic** command adds a basic VPN-Target extended community filter.

The **undo ip extcommunity-filter basic** command deletes a specified basic VPN-Target extended community filter.



By default, no basic VPN-Target extended community filter is configured.


Format
------

**ip extcommunity-filter basic** *basic-extcomm-filter-name* [ **index** *index-number* ] *matchMode* { **rt** *extCmntyStr* } &<1-16>

**undo ip extcommunity-filter basic** *basic-extcomm-filter-name* [ **index** *index-number* ] [ *matchMode* { **rt** *extCmntyStr* } &<1-16> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-number* | Specifies the sequence number of a basic VPN-Target extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the basic VPN-Target extended community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the VPN-Target extended community filter to permit. * deny: Sets the matching mode of the VPN-Target extended community filter to deny. |
| **rt** *extCmntyStr* | Indicates the value of basic VPN-Target extended community. | The value of basic VPN-Target extended community can be expressed in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. * IPv4-address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. * Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 65536 to 4294967295. A user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number ranges from 0 to 65535. |
| **basic** *basic-extcomm-filter-name* | Specifies the name of the basic VPN-Target extended community filter. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A VPN-Target extended community filter can be used as a matching condition of a route-policy using a command, such as the if-match extcommunity-filter zz command.Only the extended community number can be specified for a basic VPN-Target extended community filter. The regular expression can be used as a matching rule in an advanced VPN-Target extended community filter.The relationship between the rules of the VPN-Target extended community filter is "OR", which is different from that of an RD filter. This is because each route has only one RD but can have multiple communities.For example, a VPN-Target extended community filter can be set in either of the following formats, with the same filtering result:Format 1:ip extcommunity-filter 1 permit rt 100:1 rt 200:1 rt 300:1The filter has one rule, which consists of three VPN-Targets: 100:1, 200:1, and 300:1. The relationship between them is "OR."Format 2:ip extcommunity-filter 1 permit rt 100:1ip extcommunity-filter 1 permit rt 200:1 rt 300:1The filter has two rules. Rule 1 consists of VPN-Target 100:1, and rule 2 consists of VPN-Targets 200:1 and 300:1. The relationship between the two rules is "OR."In format 2, the VPN-Target extended community defined in each rule must be a sub-set of route VPN-Target extended communities so that the rule can be matched.The **undo ip extcommunity-filter** command deletes a specified VPN-Target extended community filter.The display ip extcommunity-filter command displays detailed configurations of the VPN-Target extended community filter.



**Configuration Impact**



The ip extcommunity-filter command filters routes based on the RT attributes of the routes. The routes that match the filtering are permitted to pass through, and the routes that fail to match the filtering are denied.



**Precautions**



The extended community attributes of a route include VPN-target and Source of Origin (SoO). The ip extcommunity-filter command adds a VPN-Target extended community filter.By default, VPN-Target extended community filters work in deny mode. If all matching rules in a filter are configured to work in deny mode, all routes are denied by the filter; to prevent this problem, configure one matching rule in permit mode after one or multiple matching rules in deny mode so that the routes except for those denied by preceding matching rules are permitted by the filter.




Example
-------

# Configure VPN-target extended community filter named aa.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter basic aa deny rt 200:200

```