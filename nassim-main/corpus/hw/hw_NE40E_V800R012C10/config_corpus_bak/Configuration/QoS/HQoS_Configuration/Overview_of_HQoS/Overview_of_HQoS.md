Overview of HQoS
================

Different from conventional QoS that performs queue scheduling based on interfaces, HQoS identifies different users and different services of the same user on a single interface.

Hierarchical Quality of Service (HQoS) is a technology that uses a queue scheduling mechanism to guarantee the bandwidth of multiple services of multiple users in the DiffServ model.

Traditional QoS performs 1-level traffic scheduling. The device can distinguish services on an interface but cannot identify users. Packets of the same priority are placed into the same queue on an interface and compete for the same queue resources. HQoS uses multi-level scheduling to distinguish user-specific or service-specific traffic and provide differentiated bandwidth management.

#### Scheduling Architecture of NE40Es

[Figure 1](#EN-US_CONCEPT_0172371454__en-us_concept_0267674392_fig_qos_feature_04204) shows class queues (CQs) and port schedulers. NE40Es not configured with HQoS have only CQs and port schedulers.

**Figure 1** Scheduling architecture without HQoS  
![](../figure/en-us_image_0267686636.png)

As shown in [Figure 2](#EN-US_CONCEPT_0172371454__en-us_concept_0267674392_fig_qos_feature_04205), when HQoS is configured, a router specifies a buffer for flow queues that require hierarchical scheduling and performs a round of multi-layer scheduling for these flow queues. After that, the router puts HQoS traffic and non-HQoS traffic together into the destination interface for unified scheduling.

**Figure 2** HQoS scheduling for flow queues  
![](../figure/en-us_image_0296318301.png)

* Leaf node: flow queue (FQ)
  
  A leaf node is used to buffer data flows of one priority for a user. Data flows of each user can be classified into one to eight priorities. Different users cannot share FQs. A traffic shaping value can be configured for each FQ to restrict the maximum bandwidth.
  
  An FQ has the following attributes:
  
  + Queue priority and weight
  + PIR
  + Drop policy, including tail drop and WRED
* Transit node: subscriber queue (SQ)
  
  An SQ indicates a user (for example, a VLAN, LSP, or PVC). You can configure the CIR and PIR for each SQ.
  
  Each SQ corresponds to eight FQ priorities, and one to eight FQs can be configured. If an FQ is idle, other FQs can consume the bandwidth of the FQ, but the bandwidth that can be used by an FQ cannot exceed the PIR of the FQ.
  
  An SQ functions as both a scheduler and a virtual queue to be scheduled.
  
  + As a scheduler: schedules multiple FQs. Priority queuing (PQ), weighted fair queuing (WFQ), and low priority queuing (LPQ) apply to an FQ. The FQs with the service classes EF, CS6, and CS7 use SP scheduling by default. The flow queues with the service classes BE, AF1, AF2, AF3, and AF4 use WFQ scheduling by default, with the weight 10:10:10:15:15.
  + As a virtual queue to be scheduled: is allocated two attributes, CIR and PIR. Using metering, a router classifies traffic into two parts, the part with the traffic rate lower than or equal to the CIR and the part with the traffic rate higher than the CIR. The former part is paid by users, and the latter part is also called the excess information rate (EIR). The EIR can be calculated using this format: EIR = PIR - CIR. The EIR refers to the burst traffic rate, which can reach a maximum of PIR.
* Root node: group queue (GQ)
  
  To simplify operation, you can define multiple users as a GQ, which is similar to a BGP peer group that comprises multiple BGP peers. For example, all users that require the same bandwidth or all premium users can be configured as a GQ.
  
  A GQ can be bound to multiple SQs, but an SQ can be bound only to one GQ.
  
  A GQ schedules multiple SQs. DRR first schedules the traffic with the rate lower than the CIR between SQs. If any bandwidth is remaining after the first round, DRR schedules the traffic with the rate ranges from the CIR and PIR, that is, EIR. CIR traffic is preferentially scheduled. If there is remaining bandwidth, EIR traffic is then scheduled. The traffic with the rate higher than the PIR is discarded. Therefore, if the bandwidth of a GQ reaches the PIR, the CIR of each SQ in the GQ can be guaranteed, and the maximum bandwidth that each SQ can obtain is its own PIR.
  
  In addition, a GQ, as a root node, can be configured with a PIR attribute to restrict the sum rate of multiple member users of the GQ. All users in this GQ are restricted by the PIR. The PIR of a GQ is used for rate limit but does not provide bandwidth guarantee. The PIR of a GQ is recommended to be greater than the sum of CIRs of all its member SQs. Otherwise, a user (SQ) cannot obtain sufficient bandwidth.

The following example illustrates the relationship between an FQ, SQ, and GQ.

In an example, 20 residential users live in a building. Each residential user purchases the bandwidth of 20 Mbit/s. To guarantee the bandwidth, an SQ with both the CIR and PIR of 20 Mbit/s is created for each residential user. The PIR here also restricts the maximum bandwidth for each residential user. With the subscription of VoIP and IPTV services as well as the HSI services, carriers promote a new bandwidth package with the value-added services (including VoIP and IPTV) added but the bandwidth 20 Mbit/s unchanged. Each residential user can use VoIP, IPTV, and HSI services.

To meet such bandwidth requirements, HQoS is configured as follows:

* Configure three FQs, corresponding to three services (VoIP, IPTV, and HSI), and set a CIR and PIR for each service.
* Configure 20 SQs for 20 residential users. Configure the CIR and PIR for each SQ.
* Configure a GQ for the whole building, corresponding to 20 residential users. The sum bandwidth of the 20 residential users is actually the PIR of the GQ. Each of the 20 residential users uses services individually, but the sum bandwidth of them is restricted by the PIR of the GQ.

The hierarchy model is as follows:

* FQs are used to distinguish services of a user and control bandwidth allocation among services.
* SQs are used to distinguish users and restrict the bandwidth of each user.
* GQs are used to distinguish user groups and control the traffic rate of twenty SQs.

FQs enable bandwidth allocation among services. SQs distinguish each user. GQs enable the CIR of each user to be guaranteed and all member users to share the bandwidth.

The bandwidth exceeding the CIR is not guaranteed because it is not paid by users. The CIR must be guaranteed because the CIR has been purchased by users. As shown in [Figure 2](#EN-US_CONCEPT_0172371454__en-us_concept_0267674392_fig_qos_feature_04205), the CIR of users is marked, and the bandwidth is preferentially allocated to guarantee the CIR. Therefore, the bandwidth of CIR will not be preempted by the burst traffic exceeded the service rates.

On the NE40E, HQoS can implement upstream and downstream scheduling, and the upstream and downstream scheduling structures are different.