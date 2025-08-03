ptp min-delayreq-interval
=========================

ptp min-delayreq-interval

Function
--------

The **ptp min-delayreq-interval** command sets the minimum interval at which a 1588v2 interface sends Delay\_Req messages.

The **undo ptp min-delayreq-interval** command restores the default minimum interval at which a 1588v2 interface sends Delay\_Req messages.

By default, the minimum interval at which a 1588v2 interface sends Delay\_Req messages is 128/1024s.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp min-delayreq-interval** *min-delayreq-interval*

**undo ptp min-delayreq-interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-delayreq-interval** *min-delayreq-interval* | Specifies the minimum interval at which a 1588v2 interface sends Delay\_Req packets. | The value is an integer ranging from 0 to 20. In 1588v2 mode, the default value is 7. The values supported (mapping between the min-delayreq-interval value and the actual sending interval) are as follows:   * 0 1/1024s * 1 2/1024s * 2 4/1024s * 3 8/1024s * 4 16/1024s * 5 32/1024s * 6 64/1024s * 7 128/1024s * 8 256/1024s * 9 512/1024s * 10 1s * 11 2s * 12 4s * 13 8s * 14 16s * 15 32s * 16 64s * 17 128s * 18 256s * 19 512s * 20 1024s |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

Two 1588v2 devices exchange Announce messages to determine the master-slave hierarchy. The master device sends Sync messages to notify the slave device of time signal parameters and uses a delay measurement mechanism to achieve time signal accuracy.

Different delays on links may affect 1588v2 time synchronization accuracy. 1588v2 uses the delay measurement mechanism to correct time signals. A delay measurement process is implemented by sending delay measurement request messages and delay response messages. Either of the following parameters can be configured in the ptp delay-mechanism command to specify a delay measurement mechanism:

* delay: configures the delay request-response mechanism, in which information about the clock and time is calculated based on the delay time of an entire link between the master and slave clocks. Only the slave clock can send Delay\_Req messages to the master clock, and the master clock replies with Delay\_Resp messages. Upon receipt of the responses, the slave clock uses information carried in Delay\_Resp messages to correct time signals.
* pdelay: configures the peer delay mechanism, in which information about the clock and time is calculated based on the delay time of each link along the path between the master and slave clocks. In this mode, the master and slave clocks can send Pdelay\_Rep messages to each other and then correct time signals based on the Pdelay\_Resp messages. Upon receipt of the responses, the slave or master clock uses information carried in Pdelay\_Resp messages to correct time signals.If min-delayreq-interval is set to a small value, 1588v2 devices frequently exchange 1588v2 messages, occupying many bandwidth resources. If min-delayreq-interval is set to a large value, required time synchronization accuracy cannot be guaranteed. Therefore, if required time synchronization accuracy is guaranteed, set min-delayreq-interval to a larger value.


Example
-------

# Set the minimum interval at which
100GE
1/0/1 sends Delay\_Req packets to 256/1024s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp min-delayreq-interval 8

```