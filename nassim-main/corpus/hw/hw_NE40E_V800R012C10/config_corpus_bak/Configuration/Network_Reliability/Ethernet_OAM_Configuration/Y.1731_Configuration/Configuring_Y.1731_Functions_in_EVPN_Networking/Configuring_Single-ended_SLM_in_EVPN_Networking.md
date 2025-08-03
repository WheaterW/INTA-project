Configuring Single-ended SLM in EVPN Networking
===============================================

To perform frame loss performance measurement on a point-to-multipoint or multipoint-to-multipoint links, deploy single-ended synthetic loss measurement (SLM) to monitor the link quality.

#### Context

In EVPN networking, single-ended SLM includes on-demand and proactive SLM functions. On-demand single-ended SLM collects single-ended frame loss statistics at one or more specific times for diagnosis. Proactive single-ended SLM collects single-ended frame loss statistics periodically.

* To collect performance statistics about frame loss on the network or AC side at a time or periodically, configure on-demand single-ended SLM through the EVPN.
* To continuously collect performance statistics about frame loss on the AC side, configure proactive single-ended SLM through the EVPN.

Service packets are prioritized based on 802.1p priorities and are transmitted using different policies. Traffic from PE1 to PE3 shown in [Figure 1](#EN-US_TASK_0172362128__fig1282413014478) carries 802.1p priority values of 1 and 2. When implementing single-ended SLM for traffic over the PE1-PE3 link, PE1 sends SLM frames with varied priorities and checks the frame loss. Based on the check result, the network administrator can adjust the QoS policy for the link.**Figure 1** Networking diagram for single-ended SLM  
![](figure/en-us_image_0000001475274292.png)


#### Procedure

* Configure on-demand single-ended SLM.
  
  
  
  Configure on-demand single-ended SLM on the AC side.
  
  1. Perform the following steps on the devices at both ends of an AC where on-demand single-ended SLM will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Perform the following steps on the devices where the MEPs reside:
        
        + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
          
          The MA is bound to a VLAN.
        + On the PE, run [**map**](cmdqueryname=map) **evpn** **vpn-instance** *evpn-instance-name*
          
          The MA is associated with an EVPN instance.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **inward**
        
        A MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP is configured.
     7. (Optional) Run [**mep ccm-send**](cmdqueryname=mep+ccm-send) [ **mep-id** *mep-id* ] **enable**
        
        The CCM transmission function is enabled.
     8. (Optional) Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     9. Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
  2. Perform the following step on the receiving device on the AC side where SLM will be implemented:
     
     Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
     
     The RMEP is enabled to receive SLM frames.
  3. Perform the following step on the transmitting device on an AC where single-ended SLM will be implemented:
     
     Run [**loss-measure single-ended-synthetic send**](cmdqueryname=loss-measure+single-ended-synthetic+send) **test-id** *test-id* **interval** { **100** | **1000** } [ **sending-count** *count-value* ] [ **time-out** *time-out-value* ]
     
     On-demand SLM is enabled on the AC side.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive single-ended SLM on the AC side.
  
  
  1. Perform the following steps on the devices at both ends of an AC where proactive single-ended SLM will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        PM is enabled to manage Y.1731 proactive performance statistics.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Run [**map**](cmdqueryname=map) **evpn** **vpn-instance** *evpn-instance-name*
        
        The MA is associated with an EVPN instance.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **inward**
        
        An interface-based MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP is configured.
     8. (Optional) Run [**mep ccm-send**](cmdqueryname=mep+ccm-send) [ **mep-id** *mep-id* ] **enable**
        
        The CCM transmission function is enabled.
        
        This command can be configured only on an interface-based MEP.
     9. (Optional) Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     11. (Optional) Run [**loss-measure single-ended-synthetic local-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Upper and lower thresholds are set for the near-end frame loss rate in proactive single-ended frame loss measurement based on a specified test instance.
     12. (Optional) Run [**loss-measure single-ended-synthetic remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Upper and lower thresholds are set for the far-end frame loss rate in proactive single-ended frame loss measurement based on a specified test instance.
  2. Perform the following configuration on the RMEP that receives proactive single-ended SLM frames on the AC side:
     
     Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
     
     The RMEP is enabled to receive SLM frames.
  3. Perform the following configuration on the MEP that sends SLM frames to initiate proactive single-ended SLM on the AC side:
     
     Run [**loss-measure single-ended-synthetic continual send**](cmdqueryname=loss-measure+single-ended-synthetic+continual+send) **test-id** *test-id* **interval** { **1000** | **10000** } [ **sending-count** *count-value* ] [ **time-out** *timeout* ] [ **period** *period* ]
     
     Proactive SLM is enabled on the network side or AC side.
  4. (Optional) Configure expansion for single-ended SLM.
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     2. Run [**y1731 synthetic-loss expansion enable**](cmdqueryname=y1731+synthetic-loss+expansion+enable)
        
        Capacity expansion for single-ended SLM is enabled.
        
        When the number of SLM instances reaches the upper limit, this function increases the upper limit.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After configuring single-ended SLM, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-synthetic-loss** **test-id** *test-id* [ **count** *count* ] command on the MEP that has been enabled to send SLM frames.