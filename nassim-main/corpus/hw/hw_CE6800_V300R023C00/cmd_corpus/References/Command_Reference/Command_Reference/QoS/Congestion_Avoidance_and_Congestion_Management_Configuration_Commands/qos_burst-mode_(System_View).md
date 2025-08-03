qos burst-mode (System View)
============================

qos burst-mode (System View)

Function
--------



The **qos burst-mode** command configures the burst traffic buffer mode on a device.

The **undo qos burst-mode** command restores the default burst traffic buffer mode on a device.



By default, the burst traffic buffer mode is standard mode.


Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM:

**qos burst-mode** { **enhanced** | **shared** }

**undo qos burst-mode** { **enhanced** | **shared** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**qos burst-mode enhanced slot** *slot-id*

**undo qos burst-mode enhanced slot** *slot-id*

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode):

**qos burst-mode** { **enhanced** | **extreme** } **slot** *slot-id*

**undo qos burst-mode** { **enhanced** | **extreme** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enhanced** | Sets the burst traffic buffer mode to enhanced. | - |
| **shared** | Sets the burst traffic buffer mode to fully shared.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | - |
| **slot** *slot-id* | Specifies an available slot.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 49. |
| **extreme** | Sets the burst traffic buffer mode to extreme.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device buffer is allocated in static and dynamic modes. By default, each interface is allocated some static buffer resources for the basic buffer requirement. The remaining buffer is used as the dynamic buffer of the device.There are four burst traffic buffer modes: standard mode, enhanced mode, extreme mode, and fully shared mode.

* Standard mode: Each interface reserves some static buffer. When traffic burst occurs, a small part of the global shared buffer can be used. This mode applies to scenarios where traffic on all interfaces is balanced and burst traffic is light.
* Enhanced mode: Each interface reserves some static buffer. When traffic burst occurs, a large part of the global shared buffer can be used. This mode applies to scenarios where medium burst traffic exists on some interfaces.
* Extreme mode: Each interface reserves some static buffer. When traffic burst occurs, most of the global shared buffer can be used. This mode applies to scenarios where medium burst traffic exists on some interfaces.
* Fully shared mode: No static buffer is reserved on an interface. When traffic burst occurs, a large part of the global shared buffer can be used. This mode applies to scenarios where heavy burst traffic exists on a small number of interfaces but only a small number of interfaces have burst traffic at the same time. If traffic burst occurs on multiple interfaces at the same time, the shared buffer may be used up. As a result, interfaces that have no burst traffic cannot forward traffic at the line rate.

**Precautions**

* The burst traffic buffer mode can be switched to the enhanced mode, extreme mode, or fully shared mode only in the standard mode.
* When the burst traffic buffer mode is set to the fully shared mode, low-priority packets may be scheduled earlier than high-priority packets on an interface. For example, in an Eth-Trunk scenario, high-priority LACP packets are discarded, causing a negotiation failure. As a result, the Eth-Trunk goes Down. Therefore, this mode is not recommended.
* The plane buffer optimization function and the burst traffic buffer mode are mutually exclusive.


Example
-------

# Configure the enhanced burst traffic buffer mode.
```
<HUAWEI> system-view
[~HUAWEI] qos burst-mode enhanced slot 1

```

# Configure the shared burst traffic buffer mode.
```
<HUAWEI> system-view
[~HUAWEI] qos burst-mode shared

```

# Configure the enhanced burst traffic buffer mode.
```
<HUAWEI> system-view
[~HUAWEI] qos burst-mode enhanced

```