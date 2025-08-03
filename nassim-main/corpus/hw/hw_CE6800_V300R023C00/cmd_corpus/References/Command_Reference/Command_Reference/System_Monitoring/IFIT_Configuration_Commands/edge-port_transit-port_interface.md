edge-port transit-port interface
================================

edge-port transit-port interface

Function
--------



The **edge-port interface** command configures a port as the edge port for IFIT.

The **transit-port interface** command configures a port as the transparent transmission port for IFIT.

The **undo edge-port interface** command restores the port function based on the NE role.

The **undo transit-port interface** command restores the port function based on the NE role.



By default, the IFIT capability of an interface is determined by the role of the IFIT NE.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

{ **edge-port** | **transit-port** } { **interface** { *interface-type* *interface-number* | *interface-name* } } &<1-8>

**undo** { **edge-port** | **transit-port** } { **interface** { *interface-type* *interface-number* | *interface-name* } } &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure IFIT on an interface, you can run this command. If the interface is specified as an edge port, the IFIT header is removed from outgoing traffic on the interface. If the interface is specified as a transit port, the IFIT header is retained in outgoing traffic on the interface.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify the edge port of the device.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] edge-port interface 100GE1/0/1

```

# Specify the transparent transmission port of the device.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] transit-port interface 100GE1/0/1

```