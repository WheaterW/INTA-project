ip community-filter basic
=========================

ip community-filter basic

Function
--------



The **ip community-filter basic** command adds a basic community filter.

The **undo ip community-filter basic** command deletes a basic community filter.



By default, no basic community filter exists.


Format
------

**ip community-filter basic** *basCfName* [ **index** *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20>

**undo ip community-filter basic** *basCfName* [ **index** *index-val* ] [ *matchMode* ] [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **index** *index-val* | Specifies the sequence number of a basic community filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Sets the matching mode of the community filter. | The value is an enumerated type:   * permit: Sets the matching mode of the community filter to permit. * deny: Sets the matching mode of the community filter to deny. |
| *cmntyStr* | Specifies a community number. | The value is in the format of aa:nn. The values of aa, and nn are integers ranging from 0 to 65535. |
| *cmntyNum* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **internet** | Allows the routes that match the community filter to be sent to all peers. | - |
| **no-advertise** | Prevents routes from being advertised to other peers. | - |
| **no-export** | Prevents routes from being advertised outside an AS. If an AS confederation is used, routes are not advertised outside the AS confederation, but to other sub-ASs in the AS confederation. | - |
| **no-export-subconfed** | Prevents routes from being advertised outside an AS. If an AS confederation is used, routes are not advertised to any other sub-ASs in the AS confederation. | - |
| **basic** *basCfName* | Specifies the name of a basic community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |



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



Only a community number or well-known community attribute can be specified in a basic community filter. Only a regular expression can be specified as a matching rule in an advanced community filter.The relationship between the rules of the community filter is "AND", which is different from that of an RD filter. This is because each route has only one RD but can have multiple communities.A community filter in different formats may lead to different matching results. For example:Format 1:ip community-filter 1 permit 100:1 200:1 300:1The relationship between 100:1, 200:1, and 300:1 is "AND."Format 2:ip community-filter 1 permit 100:1ip community-filter 1 permit 200:1 300:1The relationship between 200:1 and 300:1 is "AND", and the relationship between 100:1 and 200:1 or 300:1 is "OR. "In the preceding configuration of the community filter, the community defined in each rule must be a sub-set of the route community set so that the rule can be matched.The RD filters in the following formats have the same matching result:Format 1:ip rd-filter 100 permit 100:1 200:1 2.2.2.2:1 3.3.3.3:1Format 2:ip rd-filter 100 permit 100:1 200:1ip rd-filter 100 permit 2.2.2.2:1ip rd-filter 100 permit 3.3.3.3:1The **apply comm-filter delete** command run in the Route-Policy view deletes the specified community attribute from routes. An **ip community-filter** command can be used to specify community attributes but one such command specifies only one community attribute each time. To delete more than one community attribute, run the corresponding command multiple times. If multiple community attributes are specified in one filter, none of them can be deleted. For details, see the **apply comm-filter delete** command.By default, Community filters work in deny mode. If a route is not permitted, the route cannot pass the filter. If all filtering rules in a filter work in deny mode, all routes are denied by this filter. To prevent this problem, configure a filtering rule in permit mode after configuring one or more filtering rules in deny mode so that other routes can pass the filter.




Example
-------

# Configure a basic community filter named aa.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter basic aa deny 1

```