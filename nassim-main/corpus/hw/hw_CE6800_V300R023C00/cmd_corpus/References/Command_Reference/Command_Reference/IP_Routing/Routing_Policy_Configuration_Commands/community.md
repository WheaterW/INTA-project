community
=========

community

Function
--------



The **community** command configures community attributes for a BGP community list.

The **undo community** command deletes community attributes from a BGP community list.



By default, no community attributes are configured for a BGP community list.


Format
------

**community** { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-200>

**community** { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } [ **description** *description-text* ]

**undo community** { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-200>

**undo community all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cmntyValue* | Specifies a community number. | aa and nn are integers, each ranging from 0 to 65535. |
| *cmntyNum* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **internet** | Advertises routes to any peer. By default, all routes belong to the Internet community. | - |
| **no-advertise** | Prevents the device from advertising routes with this attribute to other BGP peers. | - |
| **no-export** | Prevents the device from advertising routes with this attribute to other ASs. | - |
| **no-export-subconfed** | Prevents the device from advertising routes with this attribute to other ASs or sub-ASs. | - |
| **description** *description-text* | Description of the Community value. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |
| **all** | Deletes all community attributes from a BGP community list. | - |



Views
-----

Community attribute list view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Community attributes are BGP-specific and are used to simplify routing policy application and network maintenance and management. A community is a set of destination addresses with the same characteristics. These addresses have no physical boundary and are independent of their ASs. They share one or multiple community attributes. To configure community attributes for a BGP community list, run the **community** command.




Example
-------

# Configure a community attribute named 123 for the BGP community list named community1.
```
<HUAWEI> system-view
[~HUAWEI] ip community-list community1
[*HUAWEI-community-list-community1] community 123

```