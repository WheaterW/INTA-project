Configuring Single-ended SLM in VLL Networking
==============================================

This section describes how to configure single-ended synthetic loss measurement (SLM) in virtual leased line (VLL) networking. To collect performance statistics for frame loss on point-to-multipoint links or load balancing links of an Eth-Trunk interface, deploy single-ended SLM, which helps monitor link quality.

#### Context

In VLL networking, single-ended SLM includes on-demand and proactive SLM functions. On-demand single-ended SLM collects single-ended frame loss statistics at one or more specific times for diagnosis. Proactive single-ended SLM collects single-ended frame loss statistics periodically.

* To collect performance statistics about frame loss on a PW or an AC at a time or periodically, configure on-demand single-ended SLM.
* To continuously collect performance statistics about frame loss on a PW or an AC, configure proactive single-ended SLM.

Service packets are prioritized based on 802.1p priorities and are transmitted using different policies. Traffic from PE1 to PE3 shown in [Figure 1](#EN-US_TASK_0172362069__fig1282413014478) carries 802.1p priority values of 1 and 2. When implementing single-ended SLM for traffic over the PE1-PE3 link, PE1 sends SLM frames with varied priorities and checks the frame loss. Based on the check result, the network administrator can adjust the QoS policy for the link.**Figure 1** Networking diagram for single-ended SLM  
![](figure/en-us_image_0000001526031141.png)


#### Procedure

* Configure on-demand single-ended SLM.
  + Configure on-demand single-ended SLM on the PW side.
    
    1. Perform the following steps on the devices at both ends of a PW where on-demand single-ended SLM will be implemented:
       
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
          
          The MD view is displayed.
       3. Run [**ma**](cmdqueryname=ma) *ma-name*
          
          The MA view is displayed.
       4. Associate the MA with a service.
          - In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          - In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Configure a MEP according to the following table.
          
          **Table 1** MEP configuration
          | Operation | Command |
          | --- | --- |
          | Configure an interface-based MEP. | [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** { *interface-type interface-number* | *interface-type interface-number.subnumber* } [ { **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* } ] |
       6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
          
          An RMEP ID is specified.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The MEP is enabled to send CCMs.
          
          This command can be configured only on an interface-based MEP.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The RMEP is enabled to receive CCMs.
       9. Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
    2. Perform the following step on the RMEP that receives SLM frames on the PW side:
       
       Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
       
       The RMEP is enabled to receive SLM frames.
    3. Perform the following step on the MEP that sends SLM frames to initiate SLM on the PW side:
       
       Run [**loss-measure single-ended-synthetic send**](cmdqueryname=loss-measure+single-ended-synthetic+send) **test-id** *test-id* **interval** { **100** | **1000** } [ **sending-count** *count-value* ] [ **time-out** *time-out-value* ]
       
       On-demand SLM is enabled on the PW side.
    4. (Optional) Configure expansion for single-ended SLM.
       1. Run [**quit**](cmdqueryname=quit)
          
          Return to the system view.
       2. Run [**y1731 synthetic-loss expansion enable**](cmdqueryname=y1731+synthetic-loss+expansion+enable)
          
          Capacity expansion for single-ended SLM is enabled.
          
          When the number of SLM instances reaches the upper limit, this function increases the upper limit.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure on-demand single-ended SLM on the AC side.
    
    1. Perform the following steps on the devices at both ends of an AC where single-ended on-demand SLM will be implemented:
       
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
          
          The MD view is displayed.
       3. Run [**ma**](cmdqueryname=ma) *ma-name*
          
          The MA view is displayed.
       4. Perform the following steps on the devices where the MEPs reside:
          
          - On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
            
            The MA is bound to a VLAN.
          - On the PE, associate the MA with a service.
            
            In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          
          In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
          
          The MEP is configured.
       6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
          
          An RMEP ID is specified.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The MEP is enabled to send CCMs.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The RMEP is enabled to receive CCMs.
       9. Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
    2. Perform the following step on the RMEP that receives single-ended SLM frames on the AC side:
       
       Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
       
       The RMEP is enabled to receive SLM frames.
    3. Perform the following configuration on the MEP that sends SLM frames to initiate SLM on the AC side:
       
       Run [**loss-measure single-ended-synthetic send**](cmdqueryname=loss-measure+single-ended-synthetic+send) **test-id** *test-id* **interval** { **100** | **1000** } [ **sending-count** *count-value* ] [ **time-out** *time-out-value* ]
       
       On demand SLM is enabled on the AC side.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure single-ended proactive SLM.
  
  
  1. Perform the following steps on the devices at both ends of a PW or an AC where proactive SLM will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Performance management (PM) is enabled to manage Y.1731 proactive performance statistics.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Associate the MA with a service.
        + In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
        + In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
     6. Configure a MEP according to the following table.
        
        **Table 2** MEP configuration
        | Operation | Command |
        | --- | --- |
        | Configure an interface-based MEP. | [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** { *interface-type interface-number* | *interface-type interface-number.subnumber* } [ { **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* } ] |
        | Configure an AC- or PW-based MEP. | [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **peer-ip** *peer-ip* [ **vc-id** *vc-id* ] [ **mac** *mac-address* ] { **outward** | **inward** } |
     7. (Optional) Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* { **ac** | **pw** }
        
        An interface on the PW side is configured as the measurement point.
        
        This command can be configured only on a PW-based MEP.
     8. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP ID is specified.
     9. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
        
        This command can be configured only on an interface-based MEP.
     10. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
         
         The RMEP is enabled to receive CCMs.
     11. Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     12. (Optional) Run [**loss-measure single-ended-synthetic local-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Alarm thresholds are configured for the near-end frame loss ratio of proactive SLM.
     13. (Optional) Run [**loss-measure single-ended-synthetic remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended-synthetic+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Alarm thresholds are configured for the far-end frame loss ratio of proactive SLM.
  2. Perform the following configuration on the RMEP that receives SLM frames on the PW side:
     
     Run [**loss-measure single-ended-synthetic receive**](cmdqueryname=loss-measure+single-ended-synthetic+receive) **test-id** *test-id* [ **time-out** *timeout-value* ]
     
     The RMEP is enabled to receive SLM frames.
  3. Perform the following step on the MEP that sends SLM frames to initiate proactive single-ended SLM on the PW side:
     
     Run [**loss-measure single-ended-synthetic continual send**](cmdqueryname=loss-measure+single-ended-synthetic+continual+send) **test-id** *test-id* **interval** { **1000** | **10000** } [ **sending-count** *count-value* ] [ **time-out** *timeout* ] [ **period** *period* ]
     
     Proactive SLM is enabled on the PW side.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After configuring single-ended SLM, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-synthetic-loss** **test-id** *test-id* [ **count** *count* ] command on the MEP that has been enabled to send SLM frames.