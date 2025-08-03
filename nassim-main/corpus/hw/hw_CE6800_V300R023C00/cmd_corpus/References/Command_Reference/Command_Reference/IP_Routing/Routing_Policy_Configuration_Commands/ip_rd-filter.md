ip rd-filter
============

ip rd-filter

Function
--------



The **ip rd-filter** command configures a route distinguisher (RD) filter.

The **undo ip rd-filter** command deletes an RD filter.



By default, no RD filter is configured.


Format
------

**ip rd-filter** *rdfIndex* [ **index** *index-number* ] *matchMode* { *rdStr* } &<1-10>

**undo ip rd-filter** *rdfIndex* [ **index** *index-number* ] [ *matchMode* { *rdStr* } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rdfIndex* | Specifies the number of an RD filter. | The value is an integer in the range from 1 to 1024. |
| **index** *index-number* | Specifies the sequence number of an RD filter. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Specifies the matching mode of an RD filter. | The value is an enumerated type:   * permit: Permits a route to match the rules if its RD matches the rules. * deny: Denies a route if its RD matches the rules. |
| *rdStr* | Specifies the RD filter. | RD filter. The formats are as follows:   * 16-bit AS number:32-bit user-defined number, for example, 101:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. * 32-bit IP address:16-bit user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0-255.255.255.255, and the user-defined number ranges from 0 to 65535. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535, and a user-defined number ranges from 0 to 65535.   The value on the right of the colon can be replaced with an asterisk (\*), indicating any match. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The RD filter has the following rules:

* If the RD filter is not configured but is used to filter routes, the matching result is permit.For example, the RD filter 100 is not configured but is used by the route-policy:route-policy test permit node 10if-match rd-filter 100When the route-policy is used to filter routes, the routes match this if-match clause, and the routes match the node 10 in the route-policy named test.
* If the RD filter is configured but the RD of routes does not match any RD defined in the RD filter, the default matching result is deny.For example, the RD of routes is 100:1, and the configuration of the RD filter is as follows:ip rd-filter 100 permit 1.1.1.1:100When the RD filter is used to filter routes, the matching result is deny.
* The relationship between the rules of the RD filter is "OR", which is different from the community filter because each route has only one RD but can have multiple communities.For example, the RD filters in the following formats have the same matching results:Format 1:ip rd-filter 100 permit 100:1 200:1 2.2.2.2:1 3.3.3.3:1Format 2:ip rd-filter 100 permit 100:1 200:1ip rd-filter 100 permit 2.2.2.2:1ip rd-filter 100 permit 3.3.3.3:1The community filters in the following formats have different matching results:Format 1:ip community-filter 1 permit 100:1 200:1 300:1Format 2:ip community-filter 1 permit 100:1ip community-filter 1 permit 200:1 300:1In the preceding configuration of the community filter, the community defined in each rule must be a sub-set of route communities so that the rule can be matched.
* Routes are filtered according to the configuration order of multiple rules. For example:ip rd-filter 100 deny 200:1 5.5.5.5:1ip rd-filter 100 permit 200:\* 5.5.5.5:\*In this situation, the route with the RD 200:1 or 5.5.5.5:1 is denied. If the configuration order of multiple rules is reversed as follows:ip rd-filter 100 permit 200:\* 5.5.5.5:\*ip rd-filter 100 deny 200:1 5.5.5.5:1In this situation, the route with the RD 200:1 or 5.5.5.5:1 is permitted.

**Precautions**

An RD filter-based matching rule is affected by the **as-notation plain** command:

* If the **as-notation plain** command is run, route matching can succeed only after the RD is set to an integral 4-byte AS number using the rdStr parameter.
* If the **as-notation plain** command is not run, route matching can succeed only after the RD is set to a 4-byte AS number in dotted notation using the rdStr parameter.Note: If the **as-notation plain** command is run after an RD filter is configured, you need to reconfigure the RD value using the rdStr parameter; otherwise, route matching may fail against an import or export route-policy, causing a network fault.


Example
-------

# Configure an RD filter.
```
<HUAWEI> system-view
[~HUAWEI] ip rd-filter 1 permit 100:1

```