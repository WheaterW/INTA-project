(Optional) Configuring CC and CV for an LSPa TE-LSP
===================================================

This section describes how to configure CC and CV for LSP.

#### Context

Continuity check (CC) and connectivity verification (CV) are two fault management functions of MPLS-TP OAM. CC is used to detect loss of continuity (LOC) between MEPs in a MEG. CV is used to detect forwarding errors between MEGs or between MEPs in a MEG. CC and CV are both proactive OAM operations but have the following differences:

* CC detects LOC on a link between any MEPs in a MEG. A MEP sends continuity check messages (CCMs) to its remote MEP (RMEP) at a specified interval. If the RMEP does not receive CCMs within a period of 3.5 times as long as the specified interval, the RMEP considers that the connectivity between the MEPs has errors, reports an alarm, and enters the Down state. After that, automatic protection switching (APS) is triggered on both MEPs. Upon receipt of a CCM from the MEP, the RMEP clears the alarm and exits from the Down state.
* CV enables a MEP to report alarms when receiving unexpected packets. For example, if a CV-enabled device receives a packet from an LSP and finds that this packet is incorrectly transmitted through the LSP, the device will report an alarm indicating a forwarding error.
  
  Transport networks have strict requirements on the correctness of data forwarding. In addition, MPLS-TP requires that the data plane should be able to work without IP support, which means that packet forwarding is based on label switching only. Therefore, the correctness of label-based forwarding must be ensured.

In practice, CC and CV are used together in the NE40E. The configurations for CC and CV are the same. Perform the following steps on a MEP and its RMEP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name*
   
   
   
   A MEG is created, and the MEG view is displayed.
3. (Optional) Run either of the following commands:
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the same value is set on the local MEP and its RMEP; otherwise, an alarm will be generated.
   
   * To configure an interval at which CCMs are sent, run the [**cc interval**](cmdqueryname=cc+interval) *interval-value* command.
     
     Optional CCM transmission intervals and their usage scenarios are as follows:
     + 3.3 ms: 300 frames are sent per second. This interval is recommended for protection switching.
     + 10 ms: 100 frames are sent per second.
     + 100 ms: 10 frames are sent per second. This interval is recommended for performance monitoring.
     + 1000 ms: 1 frame is sent per second. This interval is recommended for fault management.
     + 10000 ms: 6 frames are sent per minute.
     + 60000 ms: 1 frame is sent per minute.
     + 600000 ms: 6 frames are sent per hour.Select a proper CCM transmission interval to meet CC application requirements.
   * To configure a priority for CCMs in the MEG view, run the [**cc exp**](cmdqueryname=cc+exp) *exp-value* command.
     
     If the MPLS-TP network is severely congested and the priority of CCMs is low, CCMs fail to be sent. Therefore, configure an appropriate priority for CCMs according to network conditions.
4. (Optional) On the local MEP, run [**rdi disable**](cmdqueryname=rdi+disable)
   
   
   
   RDI is disabled.
   
   RDI is enabled by default.
   
   If an MEP detects a defect or fault, the RDI flag is set to 1 in CCMs. The MEP then sends the CCMs to the RMEP to notify it of the defect or fault.
5. Perform the following steps to enable CC/CV on the MEP and RMEP (this operation sequence prevents alarm misreports during the enabling process):
   1. Run the [**cc send enable**](cmdqueryname=cc+send+enable) command on the local MEP to enable the MEP to send CCMs.
   2. Run the [**cc send enable**](cmdqueryname=cc+send+enable) command on the RMEP to enable the RMEP to send CCMs.
   3. Run the [**cc receive enable**](cmdqueryname=cc+receive+enable) command on the local MEP to enable the MEP to receive CCMs.
   4. Run the [**cc receive enable**](cmdqueryname=cc+receive+enable) command on the RMEP to enable the RMEP to receive CCMs.