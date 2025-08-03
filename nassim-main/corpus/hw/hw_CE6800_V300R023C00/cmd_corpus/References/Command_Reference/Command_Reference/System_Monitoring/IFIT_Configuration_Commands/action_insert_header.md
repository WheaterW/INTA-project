action insert header
====================

action insert header

Function
--------



The **action insert header** command configures the mode of inserting packet headers and its working mode.

The **undo action insert header** command restores the mode of inserting packet headers and its working mode.



By default, DCN packet headers are inserted and the E2E measurement mode is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**action insert header** [ **header-mode** **dcn** ] [ **measure-mode** { **e2e** | **trace** } ]

**undo action insert header** [ **header-mode** **dcn** ] [ **measure-mode** { **e2e** | **trace** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **header-mode** | Specifies the mode of inserting packets. | - |
| **dcn** | Specifies the IFIT format on a data center network. | - |
| **measure-mode** | Specifies the measurement mode. | - |
| **e2e** | Indicates the end-to-end mode. | - |
| **trace** | Specifies the trace mode. | - |



Views
-----

IFIT traffic-behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure the mode of inserting packet headers and its working mode. By default, DCN packet header is inserted and the E2E working mode is used.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify the mode of inserting DCN packet headers and the trace measurement mode.
```
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior huawei
[*HUAWEI-ifit-dcn-instance-behavior-huawei] action insert header header-mode dcn measure-mode trace

```