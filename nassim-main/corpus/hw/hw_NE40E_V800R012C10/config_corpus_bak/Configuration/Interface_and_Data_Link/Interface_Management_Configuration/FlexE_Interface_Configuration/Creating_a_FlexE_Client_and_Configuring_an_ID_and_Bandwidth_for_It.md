Creating a FlexE Client and Configuring an ID and Bandwidth for It
==================================================================

FlexE clients correspond to externally observed user interfaces. Each FlexE client can be flexibly allocated bandwidth from a group resource pool, and the bandwidth can be adjusted.

#### Context

To ensure that the FlexE clients on both ends can communicate with each other, you need to configure the same ID and bandwidth for them.

**Table 1** Numbers of physical ports that can be added to the same group and **port-id** value ranges for different subcard models
| **Model** | Numbers of Physical Ports that Can Be Added to the Same Group | **port-id Value Range** |
| --- | --- | --- |
| CR5DE2NE4X14 | 0, 1 | 2-21, 1000-3000 |
| CR5D0E5XMF94 | 0, 1 | 129-148, 1000-3000 |
| CR5D0E5XMF90 | 0, 1 | 129-148, 1000-3000 |
| CR5D00E1NC98 | 0 | 129-148, 1000-3000 |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flexe client-instance**](cmdqueryname=flexe+client-instance) *clientIndex* [ **flexe-group** *groupIndex* **flexe-type** **full-function** [ **port-id** *portId* ] ]
   
   
   
   A FlexE client is created and its view is displayed.
3. Run [**flexe-clientid**](cmdqueryname=flexe-clientid) *clientid*
   
   
   
   An ID is configured for the FlexE client.
4. Configure bandwidth for the FlexE client.
   
   
   * If the bandwidth mode is configured for the FlexE card, run the [**flexe-bandwidth**](cmdqueryname=flexe-bandwidth) { **1** | **1.25** | **2** | **2.5** | **3** | **3.75** | **4** | *bandwidth-value* } command to configure bandwidth for the FlexE client.
   * If the timeslot mode is configured for the FlexE card, run the [**binding interface**](cmdqueryname=binding+interface) *interface-type* *interface-number* **time-slot** *timeslot-list* [ **sub-time-slot** *subtime-slot* ] command to bind one or more sub-timeslots to the FlexE client. The bound sub-timeslots constitute the bandwidth of the FlexE client.
5. (Optional) Run [**minimal available bandwidth**](cmdqueryname=minimal+available+bandwidth) *bandPercent*
   
   
   
   The minimum available bandwidth percentage is configured for the FlexE client.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.