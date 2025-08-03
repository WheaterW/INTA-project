Associating Bit Error Alarms with Static TE-LSP/PW/E-PW APS
===========================================================

Interface-based bit error detection can trigger bit error alarm generation and clearing, and the association of bit error alarms with static TE-LSP/PW/E-PW APS.

#### Pre-configuration Tasks

1. Before associating bit error alarms with static TE-LSP/PW APS, complete the following tasks:
   * [Configure a tunnel protection group.](../vrp/dc_vrp_te-p2p_cfg_0162.html)
   * [Configure PW APS.](../vrp/dc_vrp_vpws_cfg_6028.html)
2. Before associating bit error alarms with static E-PW APS, [configure E-PW APS.](../vrp/dc_vrp_vpws_cfg_6034.html)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

PW-layer bit error detection utilizes TE-LSP-layer TP OAM. When configuring PW-layer bit error detection, configure TE-LSP-layer TP OAM.

Bit errors on an interface trigger APS. If high ambient temperature caused these bit errors, you must disable and then re-enable the interface. This will switch services back to the original path when ambient temperature returns to normal.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-tp ais enable**](cmdqueryname=mpls-tp+ais+enable)
   
   
   
   The AIS function is enabled globally.
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
4. Run [**trap-threshold crc-error**](cmdqueryname=trap-threshold+crc-error) **mac-fcs-sd** **alarm-threshold** *almCofVal* *almPowVal* [ **resume-threshold** *rsmCofVal* *rsmPowVal* ] [ **trigger-lsp** ] or [**trap-threshold crc-error**](cmdqueryname=trap-threshold+crc-error) **mac-fcs-exc** **alarm-threshold** *almCofVal* *almPowVal* [ **resume-threshold** *rsmCofVal* *rsmPowVal* ] [ **trigger-lsp** ]
   
   
   
   The MAC-layer SD or bit error threshold-crossing alarm is enabled, alarm generation and clearing thresholds are configured, and bit error alarms are associated with static TE-LSP, static PW, and static E-PW APS switching.