ip community-filter advanced
============================

ip community-filter advanced

Function
--------



The **ip community-filter advanced** command adds an advanced community filter.

The **undo ip community-filter advanced** command deletes an advanced community filter.



By default, no advanced community filter exists.


Format
------

**ip community-filter advanced** *comm-filter-name* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip community-filter advanced** *comm-filter-name* [ **index** *index-number* ] [ *matchMode* *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-number* | Specifies the sequence number of a basic community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the community filter to permit. * deny: Sets the matching mode of the community filter to deny. |
| *regular-expression* | Specifies a community-based regular expression. | The value is a string of 1 to 1024 characters, spaces supported. |
| **advanced** *comm-filter-name* | Specifies the name of an advanced community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The community attribute is a private attribute of BGP and can be used to filter only BGP routes. The community attribute can be used as a matching condition of a route-policy using a command, such as the **if-match community-filter** command.



**Follow-up Procedure**



Run the **display ip community-filter** command to view detailed community filter configurations.



**Precautions**



In a basic community filter, only the community number or well-known community attribute can be specified. In an advanced community filter, only the regular expression can be specified as a matching condition.The relationship between the rules of a community filter is AND, which is different from that of an RD filter. This is because each route can have only one RD but can have multiple communities.When you run the **apply comm-filter delete** command in the Route-Policy view to delete the community filter value, the **ip community-filter** command can contain only one community attribute each time. To delete multiple community attributes, run the **ip community-filter** command multiple times. If multiple community attributes are configured in the same filter, these attributes cannot be deleted. For an example, see the **apply comm-filter delete** command.The default action of a community filter is deny. That is, if a route is not permitted in a certain filtering, the route cannot pass the filtering of the community filter. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter. When an advanced community filter is used to filter routes, the regular expression can be configured to match a character string in the format of aa:nn or an integer. For example:Configure ip community-filter advanced aa index 30 permit ^1:1$ to filter routes with community attribute 65537 or 1:1.ip community-filter advanced aa index 30 permit ^65537$ can also be used to filter routes with community attribute 65537 or 1:1.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.




Example
-------

# Configure an advanced community filter with the name aa.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter advanced aa permit ^10

```