display bgp ipv6 routing-table statistics(Attribute Filter)
===========================================================

display bgp ipv6 routing-table statistics(Attribute Filter)

Function
--------



The **display bgp ipv6 routing-table statistics** command displays statistics about BGP4+ public network routes based on specified multiple attribute filters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table statistics as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp ipv6 routing-table statistics community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp ipv6 routing-table statistics large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Displays BGP route statistics. | - |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP4+ public network routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP4+ public network routes that match the AS\_Path filter pas.
```
<HUAWEI> display bgp ipv6 routing-table statistics as-path-filter pas
 Total Number of Routes: 2

```

# Display statistics about the BGP4+ routes that match the Large-Community attribute filter aaa.
```
<HUAWEI> display bgp ipv6 routing-table statistics large-community-filter aaa
 Total Number of Routes: 2

```

# Display statistics about the BGP4+ routes that match community filter 10.
```
<HUAWEI> display bgp ipv6 routing-table statistics community-filter 10
 Total Number of Routes: 1

```

**Table 1** Description of the **display bgp ipv6 routing-table statistics(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes in the routing table. |