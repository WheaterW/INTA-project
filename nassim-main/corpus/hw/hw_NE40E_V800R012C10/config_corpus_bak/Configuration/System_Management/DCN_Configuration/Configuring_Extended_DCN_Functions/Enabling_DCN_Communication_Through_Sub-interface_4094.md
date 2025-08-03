Enabling DCN Communication Through Sub-interface 4094
=====================================================

This section describes how to configure a sub-interface numbered 4094 for each Huawei and non-Huawei NE to implement DCN communication.

#### Usage Scenario

DCN communication uses the Huawei proprietary protocol. Therefore, Huawei NEs cannot communicate with non-Huawei NEs. To implement DCN communication between Huawei NEs and non-Huawei NEs, configure sub-interfaces numbered 4094.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**dcn mode vlan**](cmdqueryname=dcn+mode+vlan)
   
   
   
   A sub-interface numbered 4094 is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.