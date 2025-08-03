display bgp routing-table statistics(Attribute Filter)
======================================================

display bgp routing-table statistics(Attribute Filter)

Function
--------



The **display bgp routing-table statistics** command displays BGP public network route statistics based on multiple attribute filters.




Format
------

**display bgp routing-table statistics as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp routing-table statistics community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp routing-table statistics large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Displays statistics about BGP routes. | - |
| **as-path-filter** *as-path-filter-num* | Specifies the number of the AS\_Path filter used for matching. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. It cannot contain spaces. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer ranging from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP public network routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the BGP routes that match community filter 10.
```
<HUAWEI> display bgp routing-table statistics community-filter 10
 Total Number of Routes: 1

```

# Display statistics about the BGP routes that match the Large-community filter aaa.
```
<HUAWEI> display bgp routing-table statistics large-community-filter aaa
 Total Number of Routes: 2

```

# Display statistics about BGP public network route matching the AS\_Path filter pas.
```
<HUAWEI> display bgp routing-table statistics as-path-filter pas
 Total Number of Routes: 2

```

**Table 1** Description of the **display bgp routing-table statistics(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Total number of routes. |