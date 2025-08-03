ip extcommunity-list encapsulation basic
========================================

ip extcommunity-list encapsulation basic

Function
--------



The **ip extcommunity-list encapsulation basic** command configures a basic encapsulation extended community filter.

The **undo ip extcommunity-list encapsulation basic** command deletes a basic encapsulation extended community filter.



By default, no basic encapsulation extended community filter is configured.


Format
------

**ip extcommunity-list encapsulation basic** *encapsulation-name* [ **index** *index-value* ] *matchMode* { *encapsulation-value* } &<1-16>

**undo ip extcommunity-list encapsulation basic** *encapsulation-name* [ **index** *index-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *encapsulation-name* | Specifies the name of a basic encapsulation extended community filter. | The value is a string of 1 to 51 case-sensitive characters. It cannot be comprised of only digits. If spaces are used, the string must start and end with double quotation marks ("). |
| **index** *index-value* | Specifies the index of a basic encapsulation extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the basic encapsulation extended community filter. | The value is an enumerated type:   * permit: Indicates the permit matching mode. * deny: Indicates the deny matching mode. |
| *encapsulation-value* | Specifies the value of the basic encapsulation extended community attribute. | The value is in the format of a 2-byte AS number:2-byte user-defined value, such as 0:100. The AS number must be 0. The user-defined value is an integer ranging from 0 to 65535. |
| **basic** | Indicates the basic encapsulation extended community attribute. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **ip extcommunity-list encapsulation** command configures an encapsulation extended community filter to filter BGP-EVPN routes carrying the encapsulated extended community attribute.An encapsulation extended community filter, such as if-match extcommunity-list encapsulation aaa, can be used as a matching condition of a route-policy.The relationship between the rules of the encapsulation extended community filter is OR.For example, an encapsulation extended community filter in either of the following formats has the same filtering effect:Format 1:ip extcommunity-list encapsulation basic aaa permit 0:1 0:2 0:3Format 2:ip extcommunity-list encapsulation basic aaa permit 0:1ip extcommunity-list encapsulation basic aaa permit 0:2 0:3

The **undo ip extcommunity-list encapsulation** command can be used to delete a single node's encapsulation extended community filter.



**Configuration Impact**



After the command is run, routes that do not match any rules of the filter are filtered out.




Example
-------

# Configure an encapsulation extended community filter named aaa.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-list encapsulation basic aaa permit 0:1 0:2 0:3

```