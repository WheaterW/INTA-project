storm suppression (interface view)
==================================

storm suppression (interface view)

Function
--------



The **storm suppression** command configures the maximum volume of broadcast, unknown multicast, or unknown unicast packets that can pass through an interface.

The **undo storm suppression** command cancels the configuration.



By default, the percentage of bandwidth occupied by broadcast packets is 10%, the percentage of bandwidth occupied by unknown multicast packets is 100%, the percentage of bandwidth occupied by unknown unicast packets is 100%.


Format
------

**storm suppression** { **multicast** | **unknown-unicast** } { *percent-value* | **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] | **packets** *packets-per-second* }

**undo storm suppression** { **broadcast** | **multicast** | **unknown-unicast** }

**storm suppression broadcast** { *broadcast-percent* | **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] | **packets** *packets-per-second* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **multicast** | Configures unknown multicast packet suppression. | - |
| **unknown-unicast** | Configures unknown unicast packet suppression. | - |
| *percent-value* | Specifies a percentage, that is, the ratio of the packet rate to the interface rate. | The value is an integer ranging from 0 to 100, in percentage. |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. | The value is an integer that ranges from 0 to 400000000, in kbit/s. |
| **gbps** | Specifies the CIR in the unit of Gbit/s. | - |
| **kbps** | Specifies the CIR in the unit of kbit/s. | - |
| **mbps** | Specifies the CIR in the unit of Mbit/s. | - |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the committed volume of traffic that can pass through. | The value is an integer that ranges from 10000 to 4294967295, in bytes. |
| **bytes** | Specifies the CBS in the unit of bytes. | - |
| **kbytes** | Specifies the CBS in the unit of kbytes. | - |
| **mbytes** | Specifies the CBS in the unit of Mbytes. | - |
| **packets** *packets-per-second* | Specifies the number of packets transmitted per second. | The value is an integer that ranges from 0 to 595240000. |
| **broadcast** | Configures broadcast packet suppression. | - |
| *broadcast-percent* | Specifies a percentage, that is, the ratio of the packet rate to the interface rate. | The value is an integer ranging from 0 to 100. The default value is 10. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To rate-limit broadcast, unknown multicast, or unknown unicast packets entering an interface and prevent broadcast storms, run this command in the interface view to configure traffic suppression for the corresponding type of packets. After this command is run, the device rate-limits broadcast, unknown multicast, or unknown unicast packets on a specified interface and discards excess packets.


Example
-------

# Set the CIR for broadcast packets to 100 kbit/s on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm suppression broadcast cir 100

```