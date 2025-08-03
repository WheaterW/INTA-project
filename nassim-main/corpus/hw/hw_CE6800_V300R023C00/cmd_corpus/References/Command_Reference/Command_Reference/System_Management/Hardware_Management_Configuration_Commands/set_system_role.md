set system role
===============

set system role

Function
--------



The **set system role** command configures a device role.



By default, no device role is configured.


Format
------

**set system role** { **core** | **spine** | **leaf** }

**undo set system role** [ { **core** | **spine** | **leaf** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **core** | Core node. | - |
| **spine** | Spine node. | - |
| **leaf** | Leaf node. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure a device role.


Example
-------

# Configure the device as a spine node.
```
<HUAWEI> system-view
[~HUAWEI] set system role spine

```