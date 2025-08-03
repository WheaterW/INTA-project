wtr-timer
=========

wtr-timer

Function
--------



The **wtr-timer** command sets the wait to restore (WTR) timer of an ERPS ring.

The **undo wtr-timer** command restores the default value of the WTR timer.



By default, the WTR timer is 5 minutes for the ERPS ring.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**wtr-timer** *time-value*

**undo wtr-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the value of the WTR timer for the ERPS ring. | The value is an integer ranging from 1 to 12, in minutes. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a Layer 2 network running ERPS, if the RPL owner port is unblocked owning to a link or node failure, the involved port may not go Up immediately after the link or node recovers. Run the wtr-timer command can prevent the RPL owner port alternates between the Up and Down states. The node where the RPL owner port resides starts a WTR timer after receiving a ring auto protection switching (R-APS) PDU indicating the link or node recovery. If the node receives an R-APS PDU indicating that another port fails before the timer expires, it terminates the WTR timer. If the node does not receive any R-APS PDU indicating that another port fails before the timer expires, it blocks the RPL owner port when the timer expires and sends an R-APS PDU indicating that the RPL owner port is blocked. After receiving this R-APS PDU, the other nodes set their ports on the ring to the Forwarding state.


Example
-------

# Set the value of the WTR timer to 10 minutes for ERPS ring 10.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 10
[*HUAWEI-erps-ring10] wtr-timer 10

```