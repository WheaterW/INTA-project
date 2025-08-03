if-match large-community-filter
===============================

if-match large-community-filter

Function
--------



The **if-match large-community-filter** command sets a filtering rule that is based on a Large-Community filter.

The **undo if-match large-community-filter** command deletes the configured filtering rule.



By default, no filtering rule based on a Large-Community filter is set.


Format
------

**if-match large-community-filter** *large-comm-filter-name* [ **whole-match** ]

**undo if-match large-community-filter** *large-comm-filter-name* [ **whole-match** ]

**undo if-match large-community-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *large-comm-filter-name* | Specifies the name of a Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters and cannot contain digits only. Spaces are allowed only when the string is enclosed in double quotation marks (" "). |
| **whole-match** | Indicates exact match. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Large-Community attribute is a private attribute of BGP. Therefore, you can run the **if-match large-community-filter** command to filter BGP routes with a specified Large-Community attribute value. For the filtering rule to take effect, run the **ip large-community-filter** command to define a Large-Community filter first. For example:

* If the if-match large-community-filter a command is run but the large-community-filter a command is not run, the **if-match large-community-filter** command fails to be delivered.
* If the if-match large-community-filter a and ip large-community-filter basic a permit 1:1:1 commands are both run, only BGP routes with the Large-Community value of 1:1:1 are permitted.

**Prerequisites**



A Large-Community filter has been configured using the **ip large-community-filter** command.



**Configuration Impact**



The BGP routes that match a filtering rule based on the Large-Community attribute are permitted, and the BGP routes that do not match a filtering rule based on Large-Community attribute are denied.




Example
-------

# Set an exact match rule that is based on the Large-Community filter a.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-filter basic a permit 100:200:300
[*HUAWEI] route-policy test permit node 11
[*HUAWEI-route-policy] if-match large-community-filter a whole-match

```

# Set a filtering rule that is based on the Large-Community filter aa.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-filter basic aa permit 1:1:1
[*HUAWEI] route-policy test permit node 12
[*HUAWEI-route-policy] if-match large-community-filter aa

```

# Set a filtering rule that is based on the Large-Community filter a.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-filter basic a permit 100:200:300
[*HUAWEI] route-policy test permit node 10
[*HUAWEI-route-policy] if-match large-community-filter a

```