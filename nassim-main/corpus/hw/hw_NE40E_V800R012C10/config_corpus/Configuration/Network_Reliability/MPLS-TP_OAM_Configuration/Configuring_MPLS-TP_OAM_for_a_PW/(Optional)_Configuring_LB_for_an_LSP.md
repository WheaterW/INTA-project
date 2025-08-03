(Optional) Configuring LB for an LSP
====================================

This section describes how to configure loopback (LB) to monitor the connectivity of MPLS-TP links.

#### Context

LB is the most common tool that monitors the connectivity between MEPs or between a MEP and a MIP. Unlike CC or CV that is performed periodically, LB is performed at a time.

Commands can be run to trigger LB, and LB packets are used to check the following information:

* Availability of a remote device
* Round-trip delay in communication between MEPs
* Loss of ping packets

Both the loopback function enabled using the **ping meg** command and CC enabled using the **cc enable** command are used to monitor the connectivity of bidirectional links. The following table describes differences between them.

**Table 1** Differences between loopback and CC
| Item | Loopback enabled using the [**ping meg**](cmdqueryname=ping+meg) command | CC enabled using the [**cc enable**](cmdqueryname=cc+enable) command |
| --- | --- | --- |
| Configuration procedure | To enable loopback, perform the following step:  Run the [**ping meg**](cmdqueryname=ping+meg) command on a MEP to enable loopback and display statistics in real time. | To enable CC, perform the following steps:  1. (Optional) Run the [**cc interval**](cmdqueryname=cc+interval) command to set an interval at which CCMs are sent on a MEP and its RMEP. 2. (Optional) Run the [**cc exp**](cmdqueryname=cc+exp) command to set a priority for CCMs on the MEP and its RMEP. 3. Run the [**cc send enable**](cmdqueryname=cc+send+enable) command to enable the MEP and its RMEP to send CCMs. 4. Run the [**cc receive enable**](cmdqueryname=cc+receive+enable) command to enable the MEP and its RMEP to receive CCMs. |
| Statistics display | The [**ping meg**](cmdqueryname=ping+meg) command displays statistics on the MEP. | An alarm is generated and reported if a connectivity fault between the MEP and its RMEP occurs. |
| Detection method | On-demand monitoring: monitors connectivity of a MEG at a time. | Proactive monitoring: periodically monitors connectivity of a MEG. |
| Detection object | MEP or MIP | MEP |




#### Procedure

* Run [**ping meg**](cmdqueryname=ping+meg) *meg-name* [ { **mip** **ttl** *ttl-number* { **mip-id** *mip-id-value* | **node-id** *node-id-value* } [ **if-num** *if-numvalue* ] } | **-c** *count-value* | **packet-size** *size-value* | **-t** *timeout-value* ] \* [ **request-tlv** ]
  
  
  
  LB is enabled to monitor the connectivity of an MPLS-TP link.
  
  The *timeout-value* parameter specifies a period for waiting for a response packet.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the network speed is slow, set the *timeout-value* parameter to a large value in the [**ping meg**](cmdqueryname=ping+meg) command.