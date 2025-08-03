ip extcommunity-list soo basic
==============================

ip extcommunity-list soo basic

Function
--------



The **ip extcommunity-list soo basic** command configures a basic Source of Origin (SoO) extended community filter.

The **undo ip extcommunity-list soo basic** command deletes a specified basic SoO extended community filter.



By default, no basic SoO extended community filter is configured.


Format
------

**ip extcommunity-list soo basic** *basic-extcomm-filter-name* [ **index** *index-number* ] *matchMode* { *site-of-origin* } &<1-16>

**undo ip extcommunity-list soo basic** *basic-extcomm-filter-name* [ **index** *index-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-number* | Specifies the sequence number of an SoO extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the SoO extended community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the SoO extended community filter to permit. * deny: Sets the matching mode of the SoO extended community filter to deny. |
| *site-of-origin* | Specifies the SoO extended community. | The SoO attribute is a BGP extended community attribute and can be expressed in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. * IPv4-address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. * Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 65536 to 4294967295. A user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number ranges from 0 to 65535. |
| **basic** *basic-extcomm-filter-name* | Specifies the name of the basic SoO extended community filter. | The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



SoO records the site where the BGP route initiator resides in the VPN scenario. The **ip extcommunity-list soo** command configures an SoO extended community filter to filter BGP routes carrying SoO.An SoO extended community filter can be used as a matching condition of a route-policy using a command, such as the if-match extcommunity-list soo aaa command.The relationship between the rules of an SoO extended community filter is "OR".For example, an SoO extended community filter in either of the following formats has the same filtering result:Format 1:ip extcommunity-list soo basic aaa permit 100:1 200:1 300:1Format 2:ip extcommunity-list soo basic aaa permit 100:1ip extcommunity-list soo basic aaa permit 200:1 300:1

The **undo ip extcommunity-list soo** command deletes a specified SoO extended community filter.The display **ip extcommunity-list soo** command displays detailed configurations of the SoO extended community filter.



**Precautions**



The extended community attributes of a route include VPN-target and SoO. The **ip extcommunity-list soo** command adds an SoO extended community filter.By default, Source of Origin (SoO) extended community filters work in deny mode. If all matching rules in a filter are configured to work in deny mode, all routes are denied by the filter; to prevent this problem, configure one matching rule in permit mode after one or multiple matching rules in deny mode so that the routes except for those denied by preceding matching rules are permitted by the filter.




Example
-------

# Configure an SoO extended community filter named aaa with SoO configured.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-list soo basic aaa permit 1.2.3.4:5

```