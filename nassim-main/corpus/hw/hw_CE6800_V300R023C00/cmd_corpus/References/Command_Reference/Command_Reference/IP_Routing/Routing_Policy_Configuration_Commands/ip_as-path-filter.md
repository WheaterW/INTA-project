ip as-path-filter
=================

ip as-path-filter

Function
--------



The **ip as-path-filter** command adds an AS\_Path filter.

The **undo ip as-path-filter** command deletes a specified AS\_Path filter.



By default, no AS\_Path filter exists.


Format
------

**ip as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip as-path-filter** { *as-path-filter-number* | *as-path-filter-name* } [ **index** *index-number* ] [ *matchMode* *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-path-filter-number* | Specifies the number of an AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed in double quotation marks ("). |
| **index** *index-number* | Specifies the sequence number of an AS\_Path filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the AS\_Path filter. | The value is an enumerated type:   * deny: Sets the matching mode of the AS\_Path filter to deny. * permit: Sets the matching mode of the AS\_Path filter to permit. |
| *regular-expression* | Specifies the AS\_Path regular expression. | The value is a string of 1 to 1024 characters, spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An AS\_Path filter uses the regular expression to define matching rules. After an AS\_Path filter is set, the RM module immediately instructs each protocol to apply the filter by default.The AS\_Path attribute is a private attribute of BGP and is mainly used to filter BGP routes.

* The AS\_Path attribute can be directly applied using a command, such as the peer as-path-filter command.
* The AS\_Path attribute can be configured as a matching condition for a route-policy using a command, such as the if-match as-path-filter zz command.

**Configuration Impact**



Multiple rules (in permit or deny mode) can be specified for a filter.



**Follow-up Procedure**



To view detailed configurations of an AS\_Path filter, run the display ip as-path-filter command.



**Precautions**



The default action of an AS\_Path filter is deny. That is, if a route is not permitted in a certain filtering, the route cannot pass the filtering of the AS\_Path filter. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter.The AS number in the regular expression of the AS\_Path filter must be in the same format as the 4-byte AS number of BGP. Otherwise, the matching fails.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.




Example
-------

# Create an AS\_Path filter with sequence number 1 to permit the routes with the AS\_Path beginning with 10.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 1 permit ^10_

```

# Create an AS\_Path filter with sequence number 3 to deny the routes that contain 30 in the AS path.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 deny _30_
[*HUAWEI] ip as-path-filter 3 permit .*

```

# Create an AS\_Path filter with sequence number 2 to permit the routes that contain 20 in the AS path.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 2 permit _20_

```