priority (DCB PFC view)
=======================

priority (DCB PFC view)

Function
--------



The **priority** command specifies a priority queue for which PFC is to be enabled.

The **undo priority** command cancels the configuration.



By default, PFC is enabled for priority queue 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**priority** { *priority* } &<1-3>

**undo priority** [ *priority* ] &<0-3>

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8855, CE8851-32CQ4BQ:

**priority** { *priority* } &<1-4>

**undo priority** [ *priority* ] &<0-4>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 0 to 7. The default value is 3.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 0 to 5. The default value is 3. |



Views
-----

DCB PFC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PFC, also called Per Priority Pause or Class Based Flow Control (CBFC), enhances Ethernet Pause. Eight priority queues on the transmit interface of an upstream device correspond to eight buffers on the receive interface of a downstream device. When a receive buffer on the receive interface of the downstream device is to be congested, the downstream device sends a backpressure signal to the upstream device, requesting the upstream device to stop sending packets in the corresponding priority queue. This mechanism transmits backpressure signals level by level until reaching the source device.You can run the **priority** command to specify a priority queue for which PFC is to be enabled, and then run the **dcb pfc enable** command to enable PFC on an interface.If the command is run more than once, all configurations take effect.

**Precautions**

If a priority queue has a non-default configuration, you need to restore the configuration of the priority queue to the default configuration. Otherwise, the PFC function cannot be disabled for the priority queue.For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:PFC can be enabled for a maximum of three queues in addition to priority queue 3.For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:

* PFC can be enabled for a maximum of three queues.
* If PFC has been enabled for three queues and the system software is downgraded to a version where PFC can be enabled for only two queues, the configuration is lost. That is, PFC is not enabled for any queue.
* If PFC has been enabled for no more than two queues, the configuration is retained after the version is downgraded to a version that supports PFC for only two queues. That is, PFC still takes effect for queues enabled with PFC.
* If PFC or antilocking PFC has ever been enabled on an interface, PFC resources corresponding to the interface are occupied. To release these resources, disable PFC or antilocking PFC on the interface and restart the device.
* Currently, PFC or antilocking PFC can be enabled on a maximum of 127 interfaces. If the number of interfaces on which PFC or antilocking PFC has been enabled exceeds 127, disable the delivered configuration to reduce the number of interfaces on which PFC or antilocking PFC has been enabled, and restart the device. Then you can enable PFC or antilocking PFC on more interfaces.


Example
-------

# Add priorities 3 and 5 to the PFC profile.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc
[~HUAWEI-dcb-pfc-default] priority 3 5

```