port high-performance mode
==========================

port high-performance mode

Function
--------



The **port high-performance mode** command configures the high-performance mode for an interface.

The **undo port high-performance mode** command restores the default high-performance mode of an interface.



By default, the high-performance mode of a switch is mode1.


Format
------

**port high-performance mode** { **mode1** | **mode2** | **mode3** | **mode4** | **mode5** }

**undo port high-performance mode** [ **mode1** | **mode2** | **mode3** | **mode4** | **mode5** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mode1** | Indicates that all ports are available. | - |
| **mode2** | Indicates that 25GE ports 21 to 28 are unavailable. | - |
| **mode3** | Indicates that 25GE ports 19 to 30 are unavailable. | - |
| **mode4** | Indicates that 25GE ports 17 to 32 are unavailable. | - |
| **mode5** | Indicates that 25GE ports 13 to 36 are unavailable. | - |



Views
-----

system view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the bandwidth of the internal interface between chips is insufficient, a hwBoardFail alarm is generated. In this case, you need to change the high-performance mode to increase the interconnection bandwidth. The default mode is mode 1. Change the mode to mode 2, mode 3 and another mode in sequence until the alarm is cleared.



**Precautions**



If an unavailable interface is in Up state in a specified high-performance mode, the high-performance mode command will fail to be executed. You need to shut down the interface first.In a specified high-performance mode, if an unavailable interface in this mode is used by a peer-link interface, this command fails to be executed. You need to delete the peer-link configuration of the interface first.




Example
-------

# Set the high-performance mode of a device to mode2, indicating that 100GE interfaces numbered 21 to 28 are unavailable.
```
<HUAWEI> system-view
[~HUAWEI] port high-performance mode mode2
Warning: 100GE ports 21 to 28 will become unavailable. Continue? [Y/N]:y

```