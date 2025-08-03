Configuring One-way Frame Delay Measurement in VLL Networking
=============================================================

In VLL networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

#### Context

One-way frame delay measurement in VLL networking can be either on-demand or proactive. On-demand one-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive one-way frame delay measurement is carried out continuously to permit proactive reporting of packet transmission delays or performance results.

* To implement singular or periodic one-way frame delay measurement for a PW or an AC, configure on-demand one-way frame delay measurement in VLL networking.
* To implement continual one-way frame delay measurement for a PW or an AC, configure proactive one-way frame delay measurement in VLL networking.
  
  802.1p priorities carried by packets on a network are used to differentiate services, and therefore different policies can be deployed for services. As shown in [Figure 1](#EN-US_TASK_0172362067__fig_dc_vrp_cfg_01151701), the 802.1p priority values contained in traffic passing through the P on the VLL are 1 and 2.
  
  One-way frame delay measurement is performed for the link between PE1 and PE2. Assume that traffic (with the priority value of 2) that is not involved in frame delay measurement is sent out after one-way frame delay measurement is enabled. The traffic is forwarded preferentially, because its priority is high. As a result, the traffic (with the priority value of 1) that is involved in frame delay measurement fails to reach PE2 in time, causing incorrect frame delay statistics.
  
  802.1p-priority-based one-way frame delay measurement can be configured for the VLL for accurate proactive frame delay tests.
  
  **Figure 1** Networking diagram for Y.1731 priority-based frame loss measurement on a VLL  
  ![](images/fig_dc_vrp_cfg_01151501.png)


#### Procedure

* Configure on-demand one-way frame delay measurement.
  + Configure on-demand one-way frame delay measurement for a PW.
    
    1. Perform the following steps on the devices at both ends of a PW where one-way frame delay measurement will be implemented:
       
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
          
          The MD view is displayed.
       3. Run [**ma**](cmdqueryname=ma) *ma-name*
          
          The MA view is displayed.
       4. Associate the MA with a service.
          - In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          - In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
          
          The MEP is configured.
       6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
          
          The remote MEP ID is configured.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The CCM transmission function is enabled.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The CCM reception function is enabled.
       9. (Optional) Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw**
          
          A measurement point for collecting Y.1731 statistics is configured.
    2. Configure a test instance.
       
       1. To configure a test instance on the receiving device on a PW where on-demand one-way frame delay measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command.
       2. To configure a test instance on the transmitting device on a PW where on-demand one-way frame delay measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command.
    3. On the receiving device on a PW where on-demand one-way frame delay measurement will be implemented, run [**delay-measure one-way receive**](cmdqueryname=delay-measure+one-way+receive) **test-id** *test-id*
       
       The 1DMM reception function is configured on the device.
    4. On the transmitting device on a PW where one-way frame delay measurement will be implemented, run [**delay-measure one-way**](cmdqueryname=delay-measure+one-way) **send** **test-id** *test-id* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand one-way frame delay measurement is configured for a PW.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure on-demand one-way frame delay measurement for an AC.
    
    1. Perform the following steps on the devices at both ends of an AC where on-demand one-way frame delay measurement will be implemented:
       
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
          
          The remote MEP ID is configured.
       7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
          
          The CCM transmission function is enabled.
       8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
          
          The CCM reception function is enabled.
       9. Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **ac**
          
          A measurement point for collecting Y.1731 statistics is configured for an AC.
    2. Configure a test instance.
       
       1. To configure a test instance on the receiving device on an AC where on-demand one-way frame delay measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id*  [ **8021p** *8021p-value* ] [ **description** *description* ] command.
       2. To configure a test instance on the transmitting device on an AC where on-demand one-way frame delay measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id-* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ][ **8021p** *8021p-value* ] [ **description** *description* ] command.
    3. On the receiving device on an AC where on-demand one-way frame delay measurement will be implemented, run [**delay-measure one-way receive**](cmdqueryname=delay-measure+one-way+receive) **test-id** *test-id*
       
       The 1DMM reception function is configured on the remote device.
    4. On the transmitting device on an AC where on-demand one-way frame delay measurement will be implemented, run [**delay-measure one-way**](cmdqueryname=delay-measure+one-way) **send** **test-id** *test-id* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand one-way frame delay measurement is configured for an AC.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure proactive one-way frame delay measurement.
  1. Perform the following steps on the devices at both ends of a PW where proactive one-way frame delay measurement will be implemented:
     
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Associate the MA with a service.
        + In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
        + In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. (Optional) Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw**
         
         A measurement point for collecting Y.1731 statistics is configured.
     11. (Optional) Run [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Lower and upper thresholds are set for one-way frame delay.
     12. (Optional) Run [**delay-measure one-way variation-threshold**](cmdqueryname=delay-measure+one-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Lower and upper thresholds are set for one-way frame jitter.
  2. Configure a test instance.
     
     
     1. Perform the following step on the receiving device on a PW where proactive one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on a PW where proactive one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     3. Perform the following step on the receiving device on a PW where proactive one-way frame delay measurement will be implemented:
        
        Run the [**delay-measure one-way continual receive**](cmdqueryname=delay-measure+one-way+continual+receive) **test-id** *test-id* command to enable the remote device to receive 1DMMs.
     4. Perform the following step on the transmitting device on a PW where proactive one-way frame delay measurement will be implemented:
        
        Run the [**delay-measure one-way continual send**](cmdqueryname=delay-measure+one-way+continual+send) **test-id** *test-id-value* **interval** *interval-value* command to enable proactive one-way frame delay measurement on the PW side.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **oneway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates one-way frame delay measurement to check statistics about the delay in unidirectional packet transmission.