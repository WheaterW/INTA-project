ptp clock-step
==============

ptp clock-step

Function
--------

The **ptp clock-step** command configures a timestamping mode on a 1588v2 device.

The **undo ptp clock-step** command restores the default timestamping mode.

By default, packets carry timestamps in one-step mode.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp clock-step** { **one-step** | **two-step** }

**undo ptp clock-step**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **one-step** | In one-step clock mode, a Sync message in Delay mode is stamped with the time when the message is sent. | - |
| **two-step** | In two-step clock mode, a Sync message in Delay mode does not carry the timestamp of the time when the message is sent. Instead, the message records only the time when the message is generated. The Follow\_Up message carries the timestamp of the time when the Syn message is sent. | - |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Two devices exchange Announce packets to determine the master/slave relationship. The master device sends Sync packets to notify the slave device of time signal parameters and uses a delay measurement mechanism to achieve time signals accuracy.

A timestamp indicates the time when 1588v2 packets are sent during synchronization. 1588v2 uses timestamps to adjust clock signals and implement clock synchronization. Either of the following parameters can be specified in the ptp clock-step command to configure a command:

* one-step: indicates the one-step clock mode. In this mode, a Sync message is stamped with the time when the message is sent.
* two-step: indicates the two-step clock mode. In this mode, a Sync message does not carry the timestamp of the time when the message is sent. Instead, a Follow-Up message carries the timestamp of the time when the Syn message is sent.

**Precautions**

By default, the device uses the one-step mode to carry timestamps. The device that uses the one-step mode can identify Follow\_Up messages sent by another device that uses the two-step mode.

PTP interfaces that support different timestamping modes can communicate with each other.

Example
-------

# Configure the two-step clock mode.
```
<HUAWEI> system-view
[~HUAWEI] ptp device-type bc
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ptp clock-step two-step

```