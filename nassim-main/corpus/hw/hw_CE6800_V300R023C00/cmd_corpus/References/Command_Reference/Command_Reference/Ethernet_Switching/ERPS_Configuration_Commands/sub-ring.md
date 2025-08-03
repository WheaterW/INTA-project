sub-ring
========

sub-ring

Function
--------



The **sub-ring** command configures an ERPS ring as a sub-ring.

The **undo sub-ring** command restores the default configuration.



By default, all ERPS rings are major rings.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**sub-ring**

**undo sub-ring**


Parameters
----------

None

Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* ERPSv1 and ERPSv2 are currently available. ERPSv2 supports multi-ring topologies in addition to single ring topologies.
* To deploy ERPS on a multi-ring network, you must configure some rings as sub-rings.
* Major rings are closed, and sub-rings are open.

**Prerequisites**

* The **version v2** command has been run to specify ERPSv2.
* The ERPS ring does not have any port. If the ERPS ring has a port, run the undo erps ring ring-id or undo port interface-type interface-number command to remove the port from the ERPS ring.

Example
-------

# Configure ERPS ring 5 as a sub-ring.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2
[*HUAWEI-erps-ring5] sub-ring

```