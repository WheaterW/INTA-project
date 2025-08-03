timer purge-zero-lsp route-calculate-delay
==========================================

timer purge-zero-lsp route-calculate-delay

Function
--------



The **timer purge-zero-lsp route-calculate-delay** command configures a period for the device to delay route calculation when the device receives a purge LSP.

The **undo timer purge-zero-lsp route-calculate-delay** command restores the default configuration.



By default, if the device receives a purge LSP, it delays route calculation for 10s.


Format
------

**timer purge-zero-lsp route-calculate-delay** *delay-interval*

**undo timer purge-zero-lsp route-calculate-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-interval* | Specifies a period for the device to delay route calculation when the device receives a purge LSP. | An integer ranging from 0 to 65535, in seconds. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IS-IS network, if a local LSP changes, the device sends a purge LSP to advertise the change. If purge LSPs are received or sent frequently and routes are recalculated immediately, a lot of system resources will be consumed. To prevent this problem, run the **timer purge-zero-lsp route-calculate-delay** command to configure a period for the device to delay route calculation when the device receives a purge LSP.After the command is run, the device triggers suppression by delaying route calculation after it receives a purge LSP with fragment number 0. After the delay-interval elapses, IS-IS exits from suppression. During the suppression period, IS-IS exits from suppression if the device receives a non-purge LSP with fragment number 0.

**Prerequisites**

You have created an IS-IS process and entered the IS-IS view using the **isis** command.


Example
-------

# Configure the device to delay route calculation for 5s when the device receives a purge LSP.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] timer purge-zero-lsp route-calculate-delay 5

```