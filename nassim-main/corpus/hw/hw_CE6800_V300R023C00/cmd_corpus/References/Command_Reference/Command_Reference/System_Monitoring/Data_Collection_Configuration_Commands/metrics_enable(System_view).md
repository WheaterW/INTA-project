metrics enable(System view)
===========================

metrics enable(System view)

Function
--------



The **metrics enable** command enables the data collection function for fault detection and locating on a device.

The **undo metrics enable** command disables the data collection function for fault detection and locating on a device.



By default, the data collection function used for fault detection and locating is enabled on a device.


Format
------

**metrics enable**

**undo metrics enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To collect data such as the number of ports and CPU usage, run this command to enable the data collection function.


Example
-------

# Enable the data collection function on the device to detect and locate faults.
```
<HUAWEI> system-view
[~HUAWEI] metrics enable

```

# Disabling the data collection function for fault locating and discovery.
```
<HUAWEI> system-view
[~HUAWEI] undo metrics enable

```