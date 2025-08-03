adaptive-routing enable
=======================

adaptive-routing enable

Function
--------



The **adaptive-routing enable** command enables global adaptive routing.

The **undo adaptive-routing enable** command disables global adaptive routing.



By default, the global adaptive routing function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**adaptive-routing enable**

**undo adaptive-routing enable**


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

**Usage Scenario**

After the adaptive routing function is enabled, the system can quickly detect network changes and adjust network paths when congestion occurs on the directly connected network. In this way, services are not blocked.

**Precautions**

* Adaptive routing can be configured only in the dragonfly topology and takes effect only when other devices in the topology are correctly configured.
* The interval between enabling and disabling global adaptive routing must be greater than 300 seconds.
* When global adaptive routing is enabled on a device, the BGP AS number of the device ranges from 4200000000 to 4200000210. If a BGP AS number not in this range is configured, the configuration fails to be delivered.
* The **adaptive-routing enable** and **load-balance ecmp stateful enable** commands cannot both be run on a device.
* The **adaptive-routing enable** and **vxlan-overlay local-preference enable** commands cannot be both run on a device.
* When global adaptive routing is disabled, adaptive routing is disabled on all interfaces that have the adaptive routing function enabled, and the role configurations on these interfaces are also deleted.

Example
-------

# Enable the global adaptive routing function.
```
<HUAWEI> system-view
[~HUAWEI] adaptive-routing enable

```