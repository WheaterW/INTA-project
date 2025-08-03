if-match as-path length
=======================

if-match as-path length

Function
--------



The **if-match as-path length** command configures a matching rule that is based on the AS\_Path length.

The **undo if-match as-path length** command deletes a matching rule that is based on the AS\_Path length.



By default, no matching rules that are based on the AS\_Path length are configured.


Format
------

**if-match as-path length** *length-value*

**if-match as-path length greater-equal** *greater-equal-value* **less-equal** *less-equal-value*

**if-match as-path length** { **greater-equal** *greater-equal-value* | **less-equal** *less-equal-value* }

**undo if-match as-path length** [ *length-value* | **greater-equal** *greater-equal-value* **less-equal** *less-equal-value* | { **greater-equal** *greater-equal-value* | **less-equal** *less-equal-value* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *length-value* | Specifies the AS\_Path length. | The value is an integer ranging from 0 to 2047. |
| **greater-equal** *greater-equal-value* | Specifies the minimum AS\_Path length for matching. | The value is an integer ranging from 0 to 2046. |
| **less-equal** *less-equal-value* | Specifies the maximum AS\_Path length for matching. | The value is an integer ranging from 1 to 2047. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure a matching rule that is based on the AS\_Path length, run the if-match as-path length command. After the matching rule is configured, attributes of the routes that match the matching rule can be modified based on the apply clause.



**Precautions**



AS\_Path is a private attribute of BGP. Therefore, matching rules that are based on the AS\_Path length are mainly used to filter BGP routes.If greEqualVal is configured, but lessEqualVal is not, the maximum value 2047 of lessEqualVal is used. If lessEqualVal is configured, but greEqualVal is not, the minimum value 0 of greEqualVal is used. If both greEqualVal and lessEqualVal are configured, lessEqualVal must be greater than greEqualVal.




Example
-------

# Configure a matching rule to match routes with the AS\_Path length of 8.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test permit node 10
[*HUAWEI-route-policy] if-match as-path length 8

```