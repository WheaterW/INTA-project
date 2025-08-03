Related Concepts of HQoS
========================

Basic concepts of HQoS include the flow queue (FQ), subscriber queue (SQ), group queue (GQ), class queue (CQ), and low priority queuing (LPQ).

#### FQ

HQoS enables the device to perform user-specific queue scheduling. You can restrict the bandwidth of a user by setting the PIR. A user's services can be classed into eight FQs. You can configure priority queuing (PQ), weighted fair queuing (WFQ) or LPQ scheduling and weighted random early detection (WRED) for each FQ and configure the traffic rate for traffic shaping.


#### SQ

An SQ is a virtual queue, meaning that there is no buffer for the queue. Data enters or leaves the queue without any delay. The queue is only one level participating in hierarchical scheduling for output packets.

Each SQ is mapped to eight types of FQ priorities and can be configured with one to eight FQs. The idle queues of an SQ cannot be used by other SQs, that is, one to eight FQs share the total bandwidth of the SQ. Each SQ corresponds to one user, which is either a VLAN or VPN user. Each user can use one to eight FQs, and the CIR and PIR of an SQ are configurable.


#### GQ

One GQ consists of multiple SQs that are bundled to carry out Level-3 queue scheduling.

A GQ functions to limit the traffic rate of a group of users as a whole. Setting the shaping value to a value not less than the sum of CIRs of SQs in the GQ is recommended. If the shaping value is less than the sum of CIRs of SQs in the GQ, the traffic rate of an SQ in the GQ cannot be guaranteed.

A GQ is also a virtual queue. Each SQ can be in only one GQ. If it is not in any GQ, the device skips Level-3 queue scheduling.

A GQ can be used to perform traffic shaping. You can set a traffic shaping rate for a GQ.


#### CQ

In HQoS scheduling, packets of FQs, after CQ scheduling, enter CQs on the interface together with common packets. By default, the eight levels of FQs of each SQ map the eight CQs on an interface. To specify the mapping between FQs and CQs, you can run the **flow-mapping** command to create a flow mapping object. For details, see [Configure an FQ mapping.](dc_ne_hqos_cfg_5043_a.html#EN-US_TASK_0283210398__cmd13180192120248).


#### LPQ

![](../../../../public_sys-resources/note_3.0-en-us.png) 

LPQ is a queue scheduling mechanism that is carried out on an Ethernet interface.

HQoS on an Ethernet interface has three queue scheduling modes: PQ, WFQ, and LPQ.

The scheduling priority of the three types of queues is PQ, WFQ, and LPQ in descending order. After packets in the PQ and WFQ are all scheduled, the remaining bandwidth can be assigned to packets in the LPQ.

The internal queue scheduling mechanism for LPQ is the same as that for PQ. The difference is that when congestion occurs, the PQ queue can preempt the bandwidth of the WFQ queue whereas the LPQ queue cannot.

In practice, BE flows can be scheduled using LPQ. If networks are overloaded, BE flows are limited so that other services are processed preferentially.