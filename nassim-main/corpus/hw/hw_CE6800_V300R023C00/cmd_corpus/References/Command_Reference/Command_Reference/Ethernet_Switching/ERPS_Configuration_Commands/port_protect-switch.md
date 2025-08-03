port protect-switch
===================

port protect-switch

Function
--------



The **port protect-switch** command configures a manual blocking mode for an ERPS port.



By default, no port is blocked.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**port** { *interface-name* | *interface-type* *interface-number* } **protect-switch** { **force** | **manual** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-number* | Specifies the name of an interface. | - |
| **force** | Indicates the forced switch (FS) mode for blocking an ERPS port. | - |
| **manual** | Indicates the manual switch (MS) mode for blocking an ERPS port. | - |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In case the ring protection link (RPL) has high bandwidth, blocking a link with low bandwidth and unblocking the RPL allow traffic to use the RPL and have more bandwidth. ERPSv2 supports both FS and MS modes for blocking an ERPS port.

* FS: forcibly blocks a port immediately after FS is configured, irrespective of whether link failures have occurred.
* MS: forcibly blocks a port on which MS is configured when link failures and FS conditions are absent.FS takes precedence over MS.

**Prerequisites**

The erps ring or port (ERPS ring view) command has been run to add the port to an ERPS ring.The **version v2** command has been run to specify ERPSv2.

**Precautions**

* The ERPS ring specified by ring-id must be the one to which the port belongs; otherwise, the command does not take effect.
* The **port protect-switch** command run in the ERPS ring view has the same effect as the **erps ring protect-switch** command run in the interface view.
* If the current port blocking mode is MS and you want to change it to FS, run the port interface-type interface-number protect-switch force command to set the FS mode. If the current port blocking mode is FS and you want to change it to MS, run the **clear** command in the ERPS ring view to clear the FS mode, and then run the **port interface-type interface-number protect-switch manual** command to set the MS mode.
* You can clear the manual port blocking mode only by using the **clear** command in the ERPS ring view.
* The **erps ring protect-switch** command is not saved in the configuration file.

Example
-------

# Specify the FS mode to block 100GE 1/0/1 on ERPS ring 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2
[*HUAWEI-erps-ring5] control-vlan 100
[*HUAWEI-erps-ring5] protected-instance all
[*HUAWEI-erps-ring5] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] stp disable
[*HUAWEI-100GE1/0/1] erps ring 5
[*HUAWEI-100GE1/0/1] commit
[~HUAWEI-100GE1/0/1] quit
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] port 100GE 1/0/1 protect-switch force

```