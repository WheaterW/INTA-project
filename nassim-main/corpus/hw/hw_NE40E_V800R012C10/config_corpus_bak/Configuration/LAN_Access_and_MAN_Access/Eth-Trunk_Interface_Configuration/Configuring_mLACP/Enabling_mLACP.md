Enabling mLACP
==============

Enabling_mLACP

#### Context

mLACP synchronizes LACP configuration and status information between dual-homed devices through a reliable ICCP channel, thereby implementing master/backup protection. After an mLACP system priority, system ID, and node ID are configured for an ICCP redundancy group, mLACP is enabled for the redundancy group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**iccp redundancy group**](cmdqueryname=iccp+redundancy+group)** **groupId**
   
   
   
   An ICCP redundancy group is created, and its view is displayed.
3. Run [**mlacp system-priority**](cmdqueryname=mlacp+system-priority) *system-priority-value*
   
   
   
   A system priority is configured for an Eth-Trunk interface added to the ICCP redundancy group.
4. Run **[**mlacp system-id**](cmdqueryname=mlacp+system-id)** **system-id-value**
   
   
   
   A system ID is configured for an Eth-Trunk interface added to the ICCP redundancy group.
5. Run **[**mlacp node-id**](cmdqueryname=mlacp+node-id)** *node-id-value*
   
   
   
   A node ID is configured for an Eth-Trunk interface added to the ICCP redundancy group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The two devices added to an ICCP redundancy group must be configured with the same system priority and system ID. Otherwise, mLACP negotiation may fail.
   * The node IDs of the devices in the same redundancy group must be different. Otherwise, mLACP negotiation may fail.
6. (Optional) Run **[**mlacp selected-value**](cmdqueryname=mlacp+selected-value+unselected-value+standby-value)** **selected-value** ****unselected-value**** **unselected-value** ****standby-value**** **standby-value**
   
   
   
   Values are configured for Selected variables in mLACP.
   
   
   
   The values of the Selected variables vary by vendors. To avoid mismatches between Huawei and non-Huawei devices, you can specify values for the variables used for mLACP negotiation.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.