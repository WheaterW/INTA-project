qos burst-mode (Interface View)
===============================

qos burst-mode (Interface View)

Function
--------



The **qos burst-mode** command configures the burst traffic buffer mode on a device.

The **undo qos burst-mode** command restores the default burst traffic buffer mode on a device.



By default, the burst traffic buffer mode is standard on an interface.


Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM:

**qos burst-mode** { **enhanced** | **shared** }

**undo qos burst-mode** { **enhanced** | **shared** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**qos burst-mode enhanced**

**undo qos burst-mode enhanced**

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode):

**qos burst-mode** { **enhanced** | **extreme** }

**undo qos burst-mode** { **enhanced** | **extreme** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enhanced** | Indicates the enhanced burst traffic buffer mode. | - |
| **shared** | Indicates the shared burst traffic buffer mode.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | - |
| **extreme** | Sets the burst traffic buffer mode to extreme.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device buffer is allocated in static and dynamic modes. By default, each interface is allocated some static buffer resources for the basic buffer requirement. The remaining buffer is used as the dynamic buffer of the device.The buffer modes are as follows:

* Standard mode: Each interface reserves some static buffer. When traffic burst occurs, a small part of the global shared buffer can be used.
* Enhanced mode: Each interface reserves some static buffer. When traffic burst occurs, a large part of the global shared buffer can be used.
* Extreme mode: Each interface reserves some static buffer. When traffic burst occurs, most of the global shared buffer can be used.
* Fully shared mode: No static buffer is reserved on an interface. When traffic burst occurs, a large part of the global shared buffer can be used. This mode applies to scenarios where heavy burst traffic exists on a small number of interfaces but only a small number of interfaces have burst traffic at the same time. If traffic burst occurs on multiple interfaces at the same time, the shared buffer may be used up. As a result, interfaces that have no burst traffic cannot forward traffic at the line rate.

**Precautions**

* You cannot configure the burst traffic buffer mode in both the system view and interface view.
* For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, and CE8850-HAM, the plane buffer optimization function and the burst traffic buffer mode are mutually exclusive.
* For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, and CE6885-T, the configured burst traffic buffer mode does not take effect for the multicast buffer.


Example
-------

# Configure the enhanced burst traffic buffer mode on interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos burst-mode enhanced

```