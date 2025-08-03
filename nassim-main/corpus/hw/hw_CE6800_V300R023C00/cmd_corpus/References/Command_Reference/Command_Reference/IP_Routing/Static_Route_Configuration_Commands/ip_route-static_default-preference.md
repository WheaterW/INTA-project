ip route-static default-preference
==================================

ip route-static default-preference

Function
--------



The **ip route-static default-preference** command sets the default priority for IPv4 static routes.

The **undo ip route-static default-preference** command restores the default setting.



By default, the default priority of static routes is 60.


Format
------

**ip route-static default-preference** *preference*

**undo ip route-static default-preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preference* | Specifies the default priority for IPv4 static routes. | It is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can change the status of a route by changing its priority. To change the default priority of the new IPv4 static routes, run the **ip route-static default-preference** command.



**Configuration Impact**



After the **ip route-static default-preference** command is used, the new priority takes effect on new IPv4 static routes that use the default priority.




Example
-------

# Set the default priority of IPv4 static routes to 70.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static default-preference 70

```