Configuring Single-ended Frame Loss Measurement in VLL Networking
=================================================================

In VLL networking, CFM is enabled. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. If frame loss measurement needs to be performed for a link, single-ended frame loss measurement can be configured to monitor the link quality.

#### Context

Single-ended frame loss measurement in VLL networking can be either on-demand or proactive. On-demand single-ended frame loss measurement is manually initiated for diagnosis of frame loss in a limited time. It can be singular or periodic measurement. Proactive single-ended frame loss measurement is continuously performed to allow proactive reporting of frame loss or performance results.

* To implement singular or periodic single-ended frame loss measurement for a PW or an AC, configure on-demand single-end frame loss measurement in VLL networking.
* To implement continual single-ended frame loss measurement for a PW, configure proactive single-ended frame loss measurement in VLL networking.
  
  Service packets are prioritized based on 802.1p priorities and are transmitted using different policies. As shown in [Figure 1](#EN-US_TASK_0172362063__fig_dc_vrp_cfg_01151501), the 802.1p priority values contained in traffic passing through the P on the VLL are 1 and 2.
  
  Frame loss measurement is performed for the link between PE1 and PE2. Assume that traffic (with the priority value of 2) that is not involved in frame loss measurement is sent out after frame loss measurement is enabled. The traffic is forwarded preferentially because its priority is high. As a result, the traffic (with the priority value of 1) that is involved in frame loss measurement fails to reach PE2 in time, causing incorrect frame loss statistics.
  
  802.1p-priority-based single-ended frame loss measurement can be configured for the VLL for accurate proactive frame loss tests.
  
  **Figure 1** Networking diagram for Y.1731 priority-based frame loss measurement on a VLL  
  ![](images/fig_dc_vrp_cfg_01151501.png)


#### Procedure

* Configure on-demand single-ended frame loss measurement.
  + Configure on-demand single-ended frame loss measurement for a PW.
    1. Perform the following steps on the PEs at both ends of a PW where single-ended frame loss measurement will be implemented:
       
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
          
          The MD view is displayed.
       3. Run [**ma**](cmdqueryname=ma) *ma-name*
          
          The MA view is displayed.
       4. Associate the MA with a service.
          
          - LDP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          - BGP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
          
          The MEP is configured.
       6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
          
          An RMEP is configured.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The CCM transmission function is enabled.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The CCM reception function is enabled.
       9. (Optional) Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw**
          
          A measurement point for collecting Y.1731 statistics is configured.
    2. Configure a test instance.
       
       1. To configure a test instance on the receiving device on a PW where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command.
       2. To configure a test instance on the transmitting device on a PW where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command.
    3. On the receiving device of a PW where single-ended frame loss measurement will be implemented:
       
       Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
       
       The LMM reception function is configured on the device.
    4. On the transmitting device of a PW where single-ended frame loss measurement will be implemented:
       
       Run [**loss-measure single-ended send**](cmdqueryname=loss-measure+single-ended+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand single-ended frame loss measurement is configured for a PW.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure on-demand single-ended frame loss measurement for an AC.
    
    1. Perform the following steps on the devices at both ends of an AC where single-ended frame loss measurement will be implemented:
       
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
          
          The MD view is displayed.
       3. Run [**ma**](cmdqueryname=ma) *ma-name*
          
          The MA view is displayed.
       4. Perform the following steps on the devices where the MEPs reside:
          
          - On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
            
            The MA is bound to a VLAN.
          - Associate the MA with a service on the PE.
          - LDP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          - BGP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
          
          The MEP is configured.
       6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
          
          An RMEP is configured.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The CCM transmission function is enabled.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The CCM reception function is enabled.
       9. Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **ac**
          
          An AC interface is configured as the measurement point.
    2. Configure a test instance.
       
       1. To configure a test instance on the receiving device on an AC where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command.
       2. To configure a test instance on the transmitting device on an AC where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command.
    3. On the receiving device of an AC where single-ended frame loss measurement will be implemented:
       
       Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
       
       The LMM reception function is configured on the device.
    4. On the transmitting device of an AC where single-ended frame loss measurement will be implemented:
       
       Run [**loss-measure single-ended**](cmdqueryname=loss-measure+single-ended) **send** **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand single-ended frame loss measurement is configured for an AC.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure proactive single-ended frame loss measurement.
  1. Perform the following steps on the devices at both ends of a PE on a PW where proactive single-ended frame loss measurement will be implemented:
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        PM is enabled to manage Y.1731 proactive performance statistics.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Associate the MA with a service.
        + LDP VLL scenarios
          
          Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
        + BGP VLL scenarios
          
          Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP is configured.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw**
         
         A measurement point for collecting Y.1731 statistics is configured.
     11. (Optional) Run the [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure lower and upper thresholds for the near-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
     12. (Optional) Run the [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the lower and upper thresholds for the near-end frame loss rate in proactive single-ended frame loss measurement based on the test instance.
     13. (Optional) Run the [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure lower and upper thresholds for the far-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
     14. (Optional) Run the [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the lower and upper thresholds for the far-end frame loss rate in proactive single-ended frame loss measurement based on the test instance.
  2. Configure a test instance.
     
     
     1. Perform the following step on the receiving device on a PW where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on a PW where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
  3. Perform the following step on the receiving devices of a PW where proactive single-ended frame loss measurement will be implemented:
     
     
     
     Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The LMM reception function is configured on the device.
  4. Perform the following step on the transmitting devices of a PW where proactive single-ended frame loss measurement will be implemented:
     
     
     
     Run the [**loss-measure single-ended continual send**](cmdqueryname=loss-measure+single-ended+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ] command to enable proactive single-ended frame loss measurement on the PW side.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates single-ended frame loss measurement to check statistics about single-ended frame loss.