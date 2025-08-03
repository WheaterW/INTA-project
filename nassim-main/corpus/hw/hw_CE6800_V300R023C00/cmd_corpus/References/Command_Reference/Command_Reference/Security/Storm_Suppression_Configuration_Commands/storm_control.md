storm control
=============

storm control

Function
--------



The **storm control** command is used to storm control broadcast, unknown multicast, or unknown unicast packets received under the interface.

The **undo storm control** command cancels storm control.



By default, storm control is not configured on an interface.


Format
------

**storm control** { **broadcast** | **multicast** | **unknown-unicast** } **min-rate** **percent** *min-rate-value-percent* **max-rate** **percent** *max-rate-value-percent*

**storm control** { **broadcast** | **multicast** | **unknown-unicast** } **min-rate** *min-rate-value* **max-rate** *max-rate-value*

**storm control** { **broadcast** | **multicast** | **unknown-unicast** } **min-rate** **kbps** *min-rate-value-kbps* **max-rate** **kbps** *max-rate-value-kbps*

**undo storm control** { **broadcast** | **multicast** | **unknown-unicast** | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Enables storm control for broadcast packets. | - |
| **multicast** | Enables storm control for unknown multicast packets. | - |
| **unknown-unicast** | Enables storm control for unknown unicast packets. | - |
| **min-rate** | Specifies the lower threshold for storm control. | - |
| **percent** *min-rate-value-percent* | Specifies the lower threshold that is expressed in percentage. When the average rate of packets received by an interface is smaller than this value within the storm detection interval, the interface starts to forward packets. | The value is an integer that ranges from 1 to 100, in percentage. |
| **percent** *max-rate-value-percent* | Specifies the upper threshold that is expressed in percentage. When the average rate of packets received by an interface is greater than or equal to this value within the storm detection interval, storm control is performed on the interface. | The value is an integer that ranges from 1 to 100, in percentage. |
| **max-rate** | Specifies the upper threshold for storm control. | - |
| *min-rate-value* | Specifies the lower threshold that is expressed in pps. When the average rate of packets received by an interface is smaller than this value within the storm detection interval, the interface starts to forward packets. | The value is an integer ranging from 1 to 595240000, in pps. |
| *max-rate-value* | Specifies the upper threshold that is expressed in pps. When the average rate of packets received by an interface is greater than or equal to this value within the storm detection interval, storm control is performed on the interface. | The value is an integer ranging from 1 to 595240000, in pps. |
| **kbps** *max-rate-value-kbps* | Specifies the upper threshold that is expressed in kbit/s. When the average rate of packets received by an interface is greater than or equal to this value within the storm detection interval, storm control is performed on the interface. | The value is an integer ranging from 1 to 400000000, in kbit/s. |
| **kbps** *min-rate-value-kbps* | Specifies the lower threshold that is expressed in kbit/s. When the average rate of packets received by an interface is smaller than this value within the storm detection interval, the interface starts to forward packets. | The value is an integer ranging from 1 to 400000000, in kbit/s. |
| **all** | Disables storm control for broadcast, unknown multicast, and unknown unicast packets. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the average rate of receiving packets on an interface is greater than or equal to the value of max-rate-value, max-rate-value-kbps, or max-rate-value-percent in storm detection, the storm control action is taken for the packets.

**Precautions**



Storm control and traffic suppression cannot be configured on the same interface in the inbound direction. For example, if traffic suppression is configured for broadcast packets, storm control cannot be configured for these packets.




Example
-------

# Perform storm control on broadcast packets received on the interface. When the average rate of packets within the storm detection interval is higher than or equal to 8000 pps, the interface performs storm control. When the rate of packets received by an interface is smaller than 2000 pps and the storm control action is set to block, the interface is recovered to forward packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm control broadcast min-rate 2000 max-rate 8000

```