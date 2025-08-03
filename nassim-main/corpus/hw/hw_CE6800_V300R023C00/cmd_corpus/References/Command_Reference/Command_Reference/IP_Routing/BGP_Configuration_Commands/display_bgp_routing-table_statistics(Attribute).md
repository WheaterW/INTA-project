display bgp routing-table statistics(Attribute)
===============================================

display bgp routing-table statistics(Attribute)

Function
--------



To check statistics about BGP public network routes, run the **display bgp routing-table statistics** command. You can specify multiple attribute values to query the route statistics as required.




Format
------

**display bgp routing-table statistics**

**display bgp routing-table statistics regular-expression** *strRegular*

**display bgp routing-table statistics community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> [ **whole-match** ]

**display bgp routing-table statistics large-community** [ *largeCommuStr* ] &<1-33> [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Displays statistics about BGP routes. | The value is a string of 1 to 80 characters. |
| **community** *communityNum* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies a community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP public network routes carrying the internet community attribute. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Indicates that the specified community attribute is fully matched. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community** *largeCommuStr* | Specifies the value of the Large-Community attribute. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |
| **regular-expression** *strRegular* | Specifies an AS\_Path regular expression. | The value is a string of 1 to 80 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP public network routes based on specified multiple attribute values, run this command. Multiple attribute values can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP public network route with the Large-Community attribute.
```
<HUAWEI> display bgp routing-table statistics large-community
 Total Number of Routes: 2

```

# Display BGP public network route statistics that match the AS regular expression ^20.
```
<HUAWEI> display bgp routing-table statistics regular-expression ^20
 Total Number of Routes: 1

```

# Display BGP public network route statistics.
```
<HUAWEI> display bgp routing-table statistics
 Total Number of Routes: 5

```

# Display BGP public network route statistics with community attributes.
```
<HUAWEI> display bgp routing-table statistics community
 Total Number of Routes: 3

```

**Table 1** Description of the **display bgp routing-table statistics(Attribute)** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes in the routing table. |