load-balance ecmp
=================

load-balance ecmp

Function
--------



The **load-balance ecmp** command enables you to enter the ecmp view from the system view.

The **undo load-balance ecmp** command deletes the ecmp load balancing configuration and restores the default load balancing mode.



By default, it disables you to enter the ecmp view.


Format
------

**load-balance ecmp**

**undo load-balance ecmp**


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

Before modifying the ECMP load balancing configuration, enter the ECMP view.


Example
-------

# Enter the ecmp view.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp]

```