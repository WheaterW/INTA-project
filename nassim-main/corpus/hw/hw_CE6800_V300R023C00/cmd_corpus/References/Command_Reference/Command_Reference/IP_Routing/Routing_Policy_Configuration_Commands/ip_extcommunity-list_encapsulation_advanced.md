ip extcommunity-list encapsulation advanced
===========================================

ip extcommunity-list encapsulation advanced

Function
--------



The **ip extcommunity-list encapsulation advanced** command configures an advanced encapsulation extended community filter.

The **undo ip extcommunity-list encapsulation advanced** command deletes an advanced encapsulation extended community filter.



By default, no advanced encapsulation extended community filter is configured.


Format
------

**ip extcommunity-list encapsulation advanced** *encapsulation-name* [ **index** *index-value* ] *matchMode* *regular*

**undo ip extcommunity-list encapsulation advanced** *encapsulation-name* [ **index** *index-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *encapsulation-name* | Specifies the name of an advanced encapsulation extended community filter. | The value is a string of 1 to 51 case-sensitive characters. It cannot be comprised of only digits. If spaces are used, the string must start and end with double quotation marks ("). |
| **index** *index-value* | Specifies the index of an advanced encapsulation extended community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the advanced encapsulation extended community filter. | The value is an enumerated type:   * permit: Indicates the permit matching mode. * deny: Indicates the deny matching mode. |
| *regular* | Specifies a regular expression to match the advanced encapsulation extended community attribute. | The value is a string of 1 to 1024 characters. It can contain spaces. |
| **advanced** | Indicates the advanced encapsulation extended community attribute. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure an encapsulation extended community filter, run the **ip extcommunity-list encapsulation** command. The filter can then be used to filter BGP EVPN routes that carry the encapsulation extended community attribute.The filter can be configured as a matching condition for a route-policy using a command, such as the if-match extcommunity-list encapsulation aaa command.The **undo ip extcommunity-list encapsulation** command deletes the encapsulation extended community filter of a specified node.



**Configuration Impact**



After the command is run, routes that do not match any rules of the filter are filtered out.



**Precautions**



Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the route-policy, reduce the number of regular expressions or use non-regular expression matching commands.




Example
-------

# Configure an advanced encapsulation extended community filter named aaa.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-list encapsulation advanced aaa permit 0:*

```