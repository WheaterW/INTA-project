bgp default ipv4-unicast-config disable
=======================================

bgp default ipv4-unicast-config disable

Function
--------



The **bgp default ipv4-unicast-config disable** command disables the configuration of commands that belong to the IPv4 unicast address family in the BGP view.

The **undo bgp default ipv4-unicast-config disable** command restores the default configuration.



By default, the commands of the IPv4 unicast address family can be configured in the BGP view.


Format
------

**bgp default ipv4-unicast-config disable**

**undo bgp default ipv4-unicast-config disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **bgp default ipv4-unicast-config disable** command to disable the configuration of commands that belong to the IPv4 unicast address family in the BGP view.


Example
-------

# Disable the configuration of commands that belong to the IPv4 unicast address family in the BGP view.
```
<HUAWEI> system-view
[~HUAWEI] bgp default ipv4-unicast-config disable

```