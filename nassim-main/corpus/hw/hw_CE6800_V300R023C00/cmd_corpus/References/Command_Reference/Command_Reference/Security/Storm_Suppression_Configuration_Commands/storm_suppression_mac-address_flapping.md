storm suppression mac-address flapping
======================================

storm suppression mac-address flapping

Function
--------



The **storm suppression mac-address flapping** command configures the threshold for MAC drift linkage traffic suppression on an interface.

The **undo storm suppression mac-address flapping** command removes the configured MAC drift linkage traffic suppression threshold for an interface.



By default, the percentage of bandwidth occupied by packets is 1% when traffic suppression associated with MAC address flapping is enabled.


Format
------

**storm suppression mac-address flapping** { *percent-value* | **cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] } [ **force** ]

**undo storm suppression mac-address flapping** { *percent-value* | **cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] } [ **force** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent-value* | Specifies a percentage, that is, the ratio of the packet rate to the interface rate. | The value is an integer that ranges from 1 to 100. The default value is 1. |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. | The value is an integer that ranges from 1 to 400000000. |
| **kbps** | Specifies the CIR in the unit of kbit/s. | - |
| **mbps** | Specifies the CIR in the unit of Mbit/s. | - |
| **gbps** | Specifies the CIR in the unit of Gbit/s. | - |
| **force** | Forcibly forwards packets based on the threshold for traffic suppression associated with MAC address flapping. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, the MAC flapping linkage traffic suppression action distinguishes between packet types (unknown unicast, unknown multicast, and broadcast). The suppression threshold is configured as a percentage, and the ratio is 1%. That is, the proportions of the three types of unknown unicast, unknown multicast and broadcast are 1%. The **storm suppression mac-address flapping** command can be executed to make the threshold of MAC drift linkage traffic suppression on the interface flexibly configured, and can make packets to be forwarded according to the threshold of MAC drift linkage traffic suppression.



**Precautions**

* If the MAC address flapping to the peer-link interface, the MAC flapping linkage storm suppression function will not take effect on the peer-link interface.
* If the force parameter is not configured or the command line is not configured, when the MAC address flapping occurs on the interface and the storm suppression of the corresponding interface is configured, the storm suppression configured on the interface takes effect.
* If the force parameter is configured, when the MAC address flapping occurs on the interface and the storm suppression of the corresponding interface is configured, the MAC flapping linkage storm suppression takes effect.
* Regardless of whether the force parameter is configured or not, as long as storm control is configured on the interface, MAC flapping linkage storm suppression will not take effect.
* MAC flapping linkage storm suppression is only effective for the MAC flapping port of this board.


Example
-------

# Set the threshold for traffic suppression associated with MAC address flapping to 100 kbit/s.
```
<HUAWEI> system-view
[~HUAWEI] storm suppression mac-address flapping cir 100

```