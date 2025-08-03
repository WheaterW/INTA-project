Configuring CC
==============

This section describes how to configure continuity check (CC).

#### Context

CC enables a local maintenance association end point (MEP) and a remote maintenance association end point (RMEP) to periodically send continuity check messages (CCMs) to check the continuity of the link between them. When CC is enabled for connectivity fault management (CFM), CFM provides different CCM intervals to meet carriers' requirements for different quality of service (QoS) levels. [Table 1](#EN-US_TASK_0172361947__tab_dc_vrp_cfm_cfg_00001201) lists the CCM intervals and the RMEP timeout time that each one corresponds to.

If the local MEP does not receive CCMs from the RMEP within a period of 3.5 times as long as the specified interval, the link is considered to be faulty.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If CC detection is configured on a Layer 3 physical main interface, CC detection fails once each time this interface is added to or removed from an Eth-Trunk interface.


**Table 1** CCM intervals
| Interval | RMEP Timeout Time |
| --- | --- |
| 600000 ms | 2100000 ms |
| 60000 ms | 210000 ms |
| 10000 ms | 35000 ms |
| 1000 ms | 3500 ms |
| 100 ms | 350 ms |
| 50 ms | 175 ms |
| 30 ms | 105 ms |
| 20 ms | 70 ms |
| 10 ms | 35 ms |
| 3.3 ms | 11.55 ms |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   
   
   The MD view is displayed.
3. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   
   
   The MA view is displayed.
   
   
   
   In L2TPv3 scenario, MA name in CCMs is in ICC-based mode.
4. Run [**ccm-interval**](cmdqueryname=ccm-interval) *{ 3.3 | 10 | 20 | 30 | 50 | 100 | 1000 | 10000 | 60000 | 600000 }* An interval for a MEP in the current MA to send or detect CCMs is configured.
   
   
   
   The MEPs on different devices in the same MD and MA must send CCMs at the same interval.
5. (Optional) Run [**ccm tlv interface-status**](cmdqueryname=ccm+tlv+interface-status)
   
   
   
   CCMs are configured to carry the Interface Status TLV field.
6. (Optional) Run [**ccm tlv port-status**](cmdqueryname=ccm+tlv+port-status)
   
   
   
   CCMs to be sent are enabled to carry the Port Status TLV field.
7. (Optional) Run [**ccm tlv sender-id**](cmdqueryname=ccm+tlv+sender-id)
   
   
   
   CCMs to be sent are enabled to carry the Sender ID TLV field.
8. Run [**mep ccm-send**](cmdqueryname=mep+ccm-send) [ **mep-id** *mep-id* ] **enable**
   
   
   
   The specified local MEP is enabled to send CCMs.
   
   
   
   If you do not specify the **mep-id** *mep-id* parameter, all local MEPs in the MA are enabled to send CCMs.
9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
   
   
   
   The specified local MEP in the MA is enabled to receive CCMs from an RMEP in the MA.
   
   
   
   If a local MEP has been enabled to receive CCMs from an RMEP and the link between the local MEP and RMEP fails, an RMEP continuity alarm is generated on the local MEP.
   
   If you do not specify the **mep-id** *mep-id* parameter, all local MEPs in the MA are enabled to receive CCMs from RMEPs in the MA.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Follow-up Procedure

* To configure CC in multiple MAs, repeat Step 3 to Step 6.
* To configure CC in multiple MDs, repeat Step 2 to Step 6.