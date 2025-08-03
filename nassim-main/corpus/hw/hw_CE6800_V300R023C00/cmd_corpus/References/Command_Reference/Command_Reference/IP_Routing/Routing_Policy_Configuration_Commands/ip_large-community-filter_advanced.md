ip large-community-filter advanced
==================================

ip large-community-filter advanced

Function
--------



The **ip large-community-filter advanced** command sets an advanced Large-Community filter.

The **undo ip large-community-filter advanced** command deletes an advanced configured Large-Community filter.



By default, no advanced Large-Community filter is configured.


Format
------

**ip large-community-filter advanced** *large-comm-filter-name* [ **index** *index-number* ] *matchMode* *regular-expression*

**undo ip large-community-filter advanced** *large-comm-filter-name* [ **index** *index-number* ] [ *matchMode* *regular-expression* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *large-comm-filter-name* | Specifies the name of an advanced Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **index** *index-number* | Specifies the index of a Large-Community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of a Large-Community filter. | The value is an enumerated type:   * permit: Sets the matching mode of a Large-Community filter to permit. * deny: Sets the matching mode of a Large-Community filter to deny. |
| *regular-expression* | Specifies a regular expression that matches BGP routes with the Large-Community attribute. | The value is a string of 1 to 1024 characters without spaces. |
| **advanced** | Sets an advanced Large-Community filter. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. The ip large-community-filter command works with the **if-match large-community-filter** command so that a filtering rule based on a specific Large-Community filter can be used to filter BGP routes.



**Follow-up Procedure**



Run the **display ip large-community-filter** command to view detailed configuration of the Large-Community filter.



**Precautions**



The relationship between rules configured using the large-community-filter command is AND, which is different from that configured using the rd-filter command. This is because each route can have only one RD but can have multiple large communities.The default action of a large-community filter is deny. That is, if a route is not permitted in a filtering, the route cannot pass the filtering. If all filtering rules in a filter are deny, no route can pass the filter. In this case, you need to set permit after deny for multiple times or one time to allow all the other routes to pass the filter.Regular expression matching is CPU-intensive processing. When a large number of regular expressions are configured in a policy to match route attributes and the corresponding route attributes are long, the policy processing performance deteriorates. To improve the processing performance of the routing policy, reduce the number of regular expressions or use non-regular expression matching commands.After the **route-policy nonexistent-config-check disable** command is run, the system still checks whether the large-community filter referenced in the command has been created. That is, a nonexistent large-community filter cannot be referenced in the command.If too many regular expressions are configured, the performance is affected, and even the protocol peer flapping occurs.




Example
-------

# Configure an advanced Large-Community filter whose name is aa.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-filter advanced aa permit ^10

```