ip community-filter (System view)
=================================

ip community-filter (System view)

Function
--------



The **ip community-filter** command adds an advanced community filter.

The **undo ip community-filter** command deletes an advanced community filter.



By default, no advanced community filter exists.


Format
------

**ip community-filter** *adv-comm-filter-num* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip community-filter** *adv-comm-filter-num* [ **index** *index-number* ] [ *matchMode* *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *adv-comm-filter-num* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| **index** *index-number* | Specifies the sequence number of a basic community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the community filter. | The value is an enumerated type:   * deny: Sets the matching mode of the community filter to deny. * permit: Sets the matching mode of the community filter to permit. |
| *regular-expression* | Specifies a community-based regular expression. | The value is a string of 1 to 1024 characters, spaces supported. |



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



Only the community number or well-known community attribute can be specified in a basic community filter. Only the regular expression can be specified as a matching condition in an advanced community filter.The relationship between the rules of a community filter is AND, which is different from that of an RD filter. This is because each route can have only one RD but can have multiple communities.For example, if a community filter is configured in either of the following formats, the filtering results are different.Form 1:ip community-filter 1 permit 100:1 200:1 300:1The relationship between 100:1, 200:1, and 300:1 is AND.Form 2:ip community-filter 1 permit 100:1ip community-filter 1 permit 200:1 300:1The relationship between 200:1 and 300:1 is AND, and the relationship between 100:1 and 200:1 and 300:1 is OR.In the preceding community-filter configuration, the community in each rule must be a subset of the community set of the route so that the rule can be matched.In the following RD filter configurations, the two types of RD filters have the same effect.Form 1:ip rd-filter 100 permit 100:1 200:1 2.2.2.2:1 3.3.3.3:1Form 2:ip rd-filter 100 permit 100:1 200:1ip rd-filter 100 permit 2.2.2.2:1ip rd-filter 100 permit 3.3.3.3:1When you run the **apply comm-filter delete** command in the Route-Policy view to delete the community filter value, the **ip community-filter** command can contain only one community attribute each time. To delete multiple community attributes, run the **ip community-filter** command multiple times. If multiple community attributes are configured in the same filter, these attributes cannot be deleted. For an example, see the **apply comm-filter delete** command.The default action of a community filter is deny. That is, if a route is not permitted in a certain filtering, the route cannot pass the filtering of the community filter. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter. When an advanced community filter is used to filter routes, the regular expression can be configured to match a character string in the format of aa:nn or an integer. For example:Configure ip community-filter advanced aa index 30 permit ^1:1$ to filter routes with community attribute 65537 or 1:1.ip community-filter advanced aa index 30 permit ^65537$ can also be used to filter routes with community attribute 65537 or 1:1.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.




Example
-------

# Configure an advanced community filter with the sequence number 100.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter 100 permit ^10

```