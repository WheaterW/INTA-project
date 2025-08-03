port-mirroring observe-port
===========================

port-mirroring observe-port

Function
--------



The **port-mirroring observe-port** command configures port mirroring on a port.

The **undo port-mirroring** command disables port mirroring on a port.



By default, port mirroring is not configured on a port.


Format
------

**port-mirroring observe-port** *observe-port-index* { **both** | **inbound** | **outbound** }

**undo port-mirroring** [ **observe-port** *observe-port-index* ] { **both** | **inbound** | **outbound** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *observe-port-index* | Specifies the index of the observing port. | The value is an integer ranging from 1 to 8. |
| **both** | Mirrors incoming and outgoing packets on a port. | - |
| **inbound** | Mirrors only incoming packets on a port. | - |
| **outbound** | Mirrors only outgoing packets on a port. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In port mirroring, you can run the **port-mirroring observe-port** command to mirror traffic to a specified observing port.

**Prerequisites**

An observing port has been configured using the **observe-port** command.

**Precautions**



To ensure that all mirrored packets are transmitted to the observing port, configure the same link type and bandwidth for the mirrored and observing ports.



For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K and CE6820S, if both mirroring and VLAN mapping are configured on an interface:In the inbound direction, mirroring takes effect first and original packets are mirrored.In the outbound direction, VLAN mapping takes effect first and modified packets are mirrored.




Example
-------

# Mirror incoming packets on 100GE1/0/1 to observing port 100GE1/0/2.
```
<HUAWEI> system-view
[HUAWEI] observe-port 1 interface 100GE 1/0/2
[HUAWEI] interface 100GE 1/0/1
[HUAWEI-100GE1/0/1] port-mirroring observe-port 1 inbound

```