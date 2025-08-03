rmon-statistics
===============

rmon-statistics

Function
--------

The **rmon-statistics enable** command enables the RMON statistics function on an interface.

The **undo rmon-statistics** command disables the RMON statistics function on an interface.

By default, the RMON statistics function is disabled on an interface.



Format
------

**rmon-statistics enable**

**undo rmon-statistics**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If traffic statistics need to be collected and recorded on an Ethernet interface, the rmon statistics function must be enabled using the rmon-statistics enable command.



Example
-------

# Enable the RMON statistics function on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] rmon-statistics enable

```