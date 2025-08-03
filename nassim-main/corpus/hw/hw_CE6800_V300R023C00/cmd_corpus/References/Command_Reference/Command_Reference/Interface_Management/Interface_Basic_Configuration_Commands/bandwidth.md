bandwidth
=========

bandwidth

Function
--------



The **bandwidth** command sets configuration bandwidth for an interface.

The **undo bandwidth** command cancels the configuration bandwidth set for an interface.



By default, no configuration bandwidth is set for an interface.


Format
------

**bandwidth** *bandwidth*

**undo bandwidth**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bandwidth* | Specifies configuration bandwidth for an interface. The bandwidth configured using this command is the expected bandwidth of an interface and does not directly affect traffic forwarding on the device. The bandwidth is generally used for traffic statistics collection on the NMS or route calculation using routing protocols. | The value is an integer ranging from 1 to 1000000, and the default unit is Mbit/s. |



Views
-----

Layer 2 100GE interface view,100ge sub-interface view,100GE interface view,Layer 2 10GE interface view,10GE sub-interface view,10GE interface view,Layer 2 200GE interface view,200GE sub-interface view,200GE interface view,25GE-L2 view,25GE sub-interface view,25GE interface view,400GE-L2 view,400GE sub-interface view,400GE interface view,Layer 2 50GE interface view,50GE sub-interface view,50GE interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Layer 2 GE interface view,Tunnel interface view,Sub-interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The interface bandwidth can be classified into physical bandwidth and configuration bandwidth. This command is used to set the configuration bandwidth of an interface without changing the physical bandwidth of the interface. The NMS can view the configuration through the ifSpeed and ifHighSpeed objects in IF-MIB.

* If the configured bandwidth is smaller than 4000 Mbit/s, ifSpeed and ifHighSpeed are displayed as bandwidth\*1000\*1000 and bandwidth respectively.
* If the configured bandwidth is greater than or equal to 4000 Mbit/s, ifSpeed and ifHighSpeed are displayed as 4294967295 (0xFFFFFFFF) and bandwidth respectively.

**Precautions**

For logical interfaces that are formed by bundling physical interfaces, such as VLANIF and Eth-Trunk interfaces, you need to run the **bandwidth** command to set a proper bandwidth for the interfaces to prevent alarms from being reported due to low default bandwidth.


Example
-------

# Set the configuration bandwidth of 100GE 1/0/1 to 10000 Mbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] bandwidth 10000

```