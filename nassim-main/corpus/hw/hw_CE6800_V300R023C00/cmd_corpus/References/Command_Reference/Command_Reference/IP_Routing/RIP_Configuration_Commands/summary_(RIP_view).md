summary (RIP view)
==================

summary (RIP view)

Function
--------



The **summary** command enables RIP classful summarization. The summarized routes are advertised in the form of a natural mask.

The **undo summary** command cancels the classful summarization so that subnet routes can be advertised and that subnets can communicate with each other.



By default, RIP-2 enables classful summarization.


Format
------

**summary**

**summary always**

**undo summary**

**undo summary always**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **always** | Indicates that RIP classful summarization takes effect, regardless of whether split horizon or poison reverse is configured. | - |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a large RIP network, a large routing table occupies a large number of memory resources for storage and a large number of network resources for transmission and processing. RIP-2 classful summarization can address this problem. Classful route summarization allows multiple routes with the same IP prefix and destination IP address to be summarized into one, which reduces the number of routing entries and improves scalability and efficiency of large-scale networks.If poison reverse has been enabled using the **rip poison-reverse** command or split horizon has been enabled using the **rip split-horizon** command, the default classful summarization function does not take effect. In this situation, run the **summary always** command to re-enable this function.

**Prerequisites**

A RIP process has been created and the RIP view has been displayed using the **rip** command.

**Precautions**

Classful summarization does not take effect in RIP-1.Route summarization configured on an interface takes precedence over that configured in the RIP process. The **rip summary-address** command takes precedence over the **summary** command.


Example
-------

# Enable RIPv2 classful summarization.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] summary

```

# Enable RIP-2 classful summarization when split horizon or poison reverse is configured.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] summary always

```