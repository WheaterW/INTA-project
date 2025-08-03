display bgp ipv6 routing-table statistics(Attribute)
====================================================

display bgp ipv6 routing-table statistics(Attribute)

Function
--------



The **display bgp ipv6 routing-table statistics** command displays statistics about BGP4+ public network routes based on specified multiple attribute values.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table statistics**

**display bgp ipv6 routing-table statistics regular-expression** *strRegular*

**display bgp ipv6 routing-table statistics community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp ipv6 routing-table statistics large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Displays BGP route statistics. | The value is a string of 1 to 80 characters. |
| **community** *communityNum* | Specify community number. | The value is an integer that ranges from 0 to 4294967295. |
| **community** *strCommunityNum* | Specify community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP routes carrying the internet community attribute. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community** *largeCommuStr* | Specifies a value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **regular-expression** *strRegular* | Specifies the regular expression that matches AS\_Path. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP4+ public network routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP4+ public network routes.
```
<HUAWEI> display bgp ipv6 routing-table statistics
 Total Number of Routes: 2

```

# Display statistics about the BGP4+ public network routes with the community attribute.
```
<HUAWEI> display bgp ipv6 routing-table statistics community
 Total Number of Routes: 1

```

# Display statistics about the BGP4+ public network routes with the Large-Community attribute.
```
<HUAWEI> display bgp ipv6 routing-table statistics large-community
 Total Number of Routes: 4

```

# Display statistics about BGP4+ public network routes that match the AS regular expression ^20.
```
<HUAWEI> display bgp ipv6 routing-table statistics regular-expression ^20
 Total Number of Routes: 2

```

**Table 1** Description of the **display bgp ipv6 routing-table statistics(Attribute)** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes in the routing table. |