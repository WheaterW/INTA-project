Configuring Single-ended SLM in VLAN Networking
===============================================

This section describes how to configure single-ended synthetic loss measurement (SLM) in virtual local area network (VLAN) networking. To collect performance statistics for frame loss on point-to-multipoint or multipoint-to-multipoint links, deploy single-ended SLM, which helps monitor link quality.

#### Context

In VLAN networking, single-ended SLM includes on-demand and proactive SLM functions. On-demand single-ended SLM collects single-ended frame loss statistics at one or more specific times for diagnosis. Proactive single-ended SLM collects single-ended frame loss statistics periodically. To collect performance statistics about packet loss at a time or periodically, configure single-ended on-demand synthetic packet LM.

* To collect performance statistics about frame loss on a PW or an AC at a time or periodically, configure on-demand single-ended SLM through the VLAN.
* To continuously collect performance statistics about frame loss on a PW or an AC, configure proactive single-ended SLM through the VLAN.

Service packets are prioritized based on 802.1p priorities and are transmitted using different policies. Traffic from PE1 to PE3 shown in [Figure 1](#EN-US_TASK_0172362105__fig1282413014478) carries 802.1p priority values of 1 and 2. When implementing single-ended SLM for traffic over the PE1-PE3 link, PE1 sends SLM frames with varied priorities and checks the frame loss. Based on the check result, the network administrator can adjust the QoS policy for the link.**Figure 1** Networking diagram for single-ended SLM  
![](figure/en-us_image_0000001475432880.png)


#### Procedure

* Configure on-demand single-ended SLM.
  
  
  1. Perform the following steps on the devices at both ends of a link on a VLAN where on-demand single-ended SLM will be implemented:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm enable**](cmdqueryname=cfm+enable)
        
        CFM is enabled globally.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Run [**map**](cmdqueryname=map) **vlan** **vlan-id**
        
        The MA is bound to a VLAN.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        A maintenance association end point (MEP) is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) **mep-id-value**
        
        An RMEP ID is specified.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send continuity check messages (CCMs).
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
     10. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
         
         A test instance is configured.
  2. Perform the following configuration on the RMEP that receives SLM frames:
     
     Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
     
     The RMEP is enabled to receive SLM frames.
  3. Perform the following configuration on the MEP that sends SLM frames to initiate SLM:
     
     Run [**loss-measure single-ended-synthetic send**](cmdqueryname=loss-measure+single-ended-synthetic+send) **test-id** *test-id* **interval** { **100** | **1000** } [ **sending-count** *count-value* ] [ **time-out** *time-out-value* ]
     
     The MEP is enabled to send SLM frames.
  4. (Optional) Configure expansion for single-ended SLM.
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**y1731 synthetic-loss expansion enable**](cmdqueryname=y1731+synthetic-loss+expansion+enable)
        
        Capacity expansion for single-ended SLM is enabled.
        
        When the number of SLM instances reaches the upper limit, this function increases the upper limit.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure single-ended proactive SLM.
  
  
  1. Perform the following steps on the devices at both ends of a link on a VLAN where single-ended proactive SLM will be implemented:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Performance management (PM) is enabled to manage Y.1731 proactive performance statistics.
     3. Run [**cfm enable**](cmdqueryname=cfm+enable)
        
        CFM is enabled globally.
     4. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     5. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     6. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
        
        The MA is bound to a VLAN.
     7. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     8. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) **mep-id-value**
        
        An RMEP ID is specified.
     9. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     10. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
         
         The RMEP is enabled to receive CCMs.
     11. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
         
         A test instance is configured.
     12. (Optional) Run [**loss-measure single-ended-synthetic local-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
     13. (Optional) Run [**loss-measure single-ended-synthetic remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
  2. Perform the following step on the receiving device where proactive single-ended SLM will be implemented:
     
     Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
     
     The RMEP is enabled to receive SLM frames.
  3. Perform the following step on the transmitting device where proactive single-ended SLM will be implemented:
     
     Run [**loss-measure single-ended-synthetic continual send**](cmdqueryname=loss-measure+single-ended-synthetic+continual+send) **test-id** *test-id* **interval** { **1000** | **10000** } [ **sending-count** *count-value* ] [ **time-out** *timeout* ] [ **period** *period* ]
     
     Proactive single-ended SLM is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.