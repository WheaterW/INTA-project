preference (RIPng view)
=======================

preference (RIPng view)

Function
--------



The **preference** command specifies a priority for RIPng routes. Alternatively, you can set a priority for a specific route using a route-policy.

The **undo preference** command restores the default setting.



By default, the priority of RIPng routes is 100.


Format
------

**preference** { { **route-policy** *route-policy-name* } | *value* } \*

**undo preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy, using which the priority of the routes meeting matching conditions can be set. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *value* | Specifies the priority of RIPng routes. | The value is an integer ranging from 1 to 255. |



Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A smaller value indicates a higher preference. To enable RIPng routes to have a higher preference than the routes learned from other IGPs, set a smaller preference value for RIPng routes. The preference determines the routing algorithm through which the optimal route is obtained in the IP routing table.

**Prerequisites**

A route-policy has been configured using the **route-policy** command.

**Configuration Impact**

If the preference command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Apply route-policy named policy1 to set the priority of RIPng routes to 60.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ripng 100
[*HUAWEI-ripng-100] preference route-policy policy1 60

```

# Restore the default priority of RIPng routes.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] undo preference

```

# Set the priority of RIPng routes to 120.
```
<HUAWEI> system-view
[~HUAWEI] ripng 100
[*HUAWEI-ripng-100] preference 120

```