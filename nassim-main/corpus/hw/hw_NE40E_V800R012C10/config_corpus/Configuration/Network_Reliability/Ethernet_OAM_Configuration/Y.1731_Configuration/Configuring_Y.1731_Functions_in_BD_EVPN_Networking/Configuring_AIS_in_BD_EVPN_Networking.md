Configuring AIS in BD EVPN Networking
=====================================

Configuring AIS prohibits a MEP in an MD of a higher level from sending the same alarm as that sent by a MEP in an MD of a lower level to the NMS.

#### Context

As shown in [Figure 1](#EN-US_TASK_0172362146__fig_dc_vrp_cfg_01154401), the MEPs configured on the access interfaces of CE1 and CE2 reside in level-6 MD1. The MEPs configured on PE1 and PE2 reside in level-3 MD2. When a fault occurs, a MEP in level-3 MD2 first detects the fault and sends an alarm to the NMS. After a certain period, a MEP in level-6 MD1 also detects the fault and sends the same alarm to the NMS. Therefore, the AIS function needs to be configured on the PEs to prohibit the MEP in the MD of a higher level from sending alarms to the NMS.**Figure 1** Networking diagram of configuring AIS in BD EVPN networking  
![](images/fig_dc_vrp_cfg_01151603.png)  



#### Procedure

1. Perform the following steps on a PE:
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   4. Run [**map**](cmdqueryname=map) **bridge-domain**  *bd-id*
      
      The MA is bound to a BD instance.
   5. Run [**ais enable**](cmdqueryname=ais+enable)
      
      AIS is enabled for the current MA.
   6. (Optional) Run [**ais link-status**](cmdqueryname=ais+link-status) **interface** { *interface-name* | *interface-type* *interface-number* } AIS is configured to monitor interfaces in the current MA.
   7. (Optional) Run [**ais interval**](cmdqueryname=ais+interval) *{ 1 | 60 }*
      
      The interval at which AIS packets are sent is set.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the range of VLANs to which AIS packets are to be sent is set, setting the interval at which AIS packets are sent to 60s is recommended.
   8. Run [**ais level**](cmdqueryname=ais+level) *level-value*
      
      The level of AIS packets to be sent is set.
   9. Run [**ais vlan**](cmdqueryname=ais+vlan) { **pe-vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *hig-ce-vid* ] } &<1â10> | **vid** { *low-vid* [ **to** *high-vid* ] } &<1â10>} **mep** *mep-id*
      
      The range of VLANs to which AIS packets are to be sent is set.
   10. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
2. Perform the following steps on a CE:
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   4. Run [**map vlan**](cmdqueryname=map+vlan) *vlan-id*
      
      The MA is bound to the current VLAN.
   5. Run [**ais enable**](cmdqueryname=ais+enable)
      
      AIS is enabled for the current MA.
   6. (Optional) Run [**ais suppress-alarm**](cmdqueryname=ais+suppress-alarm)
      
      Alarm suppression is enabled for the current MA.
      
      In an MD nesting scenario, if alarm suppression is enabled for the MD of a high level, a MEP in this MD does not send alarms that a MEP in an MD of a low level has sent to the NMS after receiving an AIS packet.
   7. (Optional) Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **alarm ais disable**
      
      The AIS alarm suppression function is disabled for the current MA.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display cfm ma**](cmdqueryname=display+cfm+ma) command on a PE to check information about MAs. The command output shows that the value of **Sending Ais Packet** is **Yes**.
* Run the [**display cfm ma**](cmdqueryname=display+cfm+ma) command on a CE to check information about MAs. The command output shows that the value of **Suppressing Alarms** is **Yes**.