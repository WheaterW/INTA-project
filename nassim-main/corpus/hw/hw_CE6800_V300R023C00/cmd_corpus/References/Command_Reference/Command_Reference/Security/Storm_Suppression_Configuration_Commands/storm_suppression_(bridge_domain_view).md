storm suppression (bridge domain view)
======================================

storm suppression (bridge domain view)

Function
--------



The **storm suppression** command configures the maximum volume of broadcast, unknown multicast, or unknown unicast packets that can pass through a BD.

The **undo storm suppression** command cancels the configuration.



By default, the rate of broadcast, unknown multicast, or unknown unicast traffic is not limited in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**storm suppression** { **broadcast** | **multicast** | **unknown-unicast** } **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ]

**undo storm suppression** { **broadcast** | **multicast** | **unknown-unicast** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Configures broadcast packet suppression. | - |
| **multicast** | Configures unknown multicast packet suppression. | - |
| **unknown-unicast** | Configures unknown unicast packet suppression. | - |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. | The value is an integer that ranges from 0 kbit/s to 4294967295 kbit/s. |
| **gbps** | Specifies the CIR in the unit of Gbit/s. | - |
| **kbps** | Specifies the CIR in the unit of kbit/s. | - |
| **mbps** | Specifies the CIR in the unit of Mbit/s. | - |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the committed volume of traffic that can pass through. | The value is an integer that ranges from 10000 bytes to 4294967295 bytes. |
| **bytes** | Specifies the CBS in the unit of bytes. | - |
| **kbytes** | Specifies the CBS in the unit of kbytes. | - |
| **mbytes** | Specifies the CBS in the unit of Mbytes. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To rate-limit broadcast, unknown multicast, or unknown unicast packets entering a BD and prevent broadcast storms, run this command in the BD to configure traffic suppression for the specified type of packets. After this command is run, the device rate-limits broadcast, unknown multicast, or unknown unicast packets in the specified BD and discards excess packets.


Example
-------

# Set the CIR to 100 kbit/s and the CBS to 18800 bytes for outgoing unknown unicast packets in a BD.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 3
[*HUAWEI-bd3] storm suppression unknown-unicast cir 100 cbs 18800

```