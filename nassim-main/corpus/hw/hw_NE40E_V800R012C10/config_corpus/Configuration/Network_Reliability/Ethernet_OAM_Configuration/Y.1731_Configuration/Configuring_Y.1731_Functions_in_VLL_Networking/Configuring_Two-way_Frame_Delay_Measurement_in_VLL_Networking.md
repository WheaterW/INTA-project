Configuring Two-way Frame Delay Measurement in VLL Networking
=============================================================

In VLL networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

#### Context

Two-way frame delay measurement in VLL networking can be either on-demand or proactive. On-demand two-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive two-way frame delay measurement is performed continuously to allow proactive reporting of packet transmission delays or performance results.

* To implement singular or periodic two-way frame delay measurement for a PW or an AC, configure on-demand two-way frame delay measurement in VLL networking.
* To implement continual two-way frame delay measurement for a PW, configure proactive two-way frame delay measurement in VLL networking.
  
  802.1p priorities carried by packets on a network are used to differentiate services, and therefore different policies can be deployed for services. As shown in [Figure 1](#EN-US_TASK_0172362068__fig_dc_vrp_cfg_01151801), the 802.1p priority values contained in traffic passing through the P are 1 and 2.
  
  Two-way frame delay measurement is performed for the link between PE1 and PE2. Assume that traffic (with the priority value of 2) that is not involved in frame delay measurement is sent out after two-way frame delay measurement is enabled. The traffic is forwarded preferentially, because its priority is high. As a result, the traffic (with the priority value of 1) that is involved in frame delay measurement fails to reach PE2 in time, causing incorrect frame delay statistics.
  
  802.1p-priority-based two-way frame delay measurement can be configured for the VLL for accurate proactive frame delay tests.
  
  **Figure 1** Networking diagram for Y.1731 priority-based frame loss measurement on a VLL  
  ![](images/fig_dc_vrp_cfg_01151501.png)


#### Procedure

* Configure on-demand two-way frame delay measurement.
  + Configure on-demand two-way frame delay measurement for a PW.
    
    1. Perform the following steps on the devices at both ends of a PW where two-way frame delay measurement will be implemented:
       
       1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
       2. Run the [**cfm md**](cmdqueryname=cfm+md) *md-name* command to enter the MD view.
       3. Run the [**ma**](cmdqueryname=ma) *ma-name* command to enter the MA view.
       4. Associate the MA with a service.
          - In the LDP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
          - In the BGP VLL scenario, run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run the [**mep mep-id**](cmdqueryname=mep+mep-id) command to configure a MEP.
       6. Run the [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id* command to set an RMEP ID.
       7. Run the [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable) command to enable the MEP to send CCMs.
       8. Run the [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable** command to enable the MEP to receive CCMs.
       9. Run the [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw** command to configure a measurement point.
    2. Configure a test instance.
       
       1. Perform the following step on the receiving device on a PW where on-demand two-way frame delay measurement will be implemented:
          
          Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
       2. Perform the following step on the transmitting device on a PW where on-demand two-way frame delay measurement will be implemented:
          
          Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
    3. Perform the following step on the receiving device on a PW where two-way frame delay measurement will be implemented:
       
       Run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
       
       The DMM reception function is configured on the device.
    4. Perform the following step on the transmitting device on a PW where two-way frame delay measurement will be implemented:
       
       Run [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) **send** **test-id** *test-id* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand two-way frame delay measurement is configured on the PW side.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure on-demand two-way frame delay measurement for an AC.
    
    1. Perform the following steps on the devices at both ends of an AC where on-demand two-way frame delay measurement will be implemented:
       
       1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
       2. Run the [**cfm md**](cmdqueryname=cfm+md) *md-name* command to enter the MD view.
       3. Run the [**ma**](cmdqueryname=ma) *ma-name* command to enter the MA view.
       4. Perform the following steps on the devices where the MEPs reside:
          - On the CE, run the [**map**](cmdqueryname=map) **vlan** *vlan-id* command to bind the MA to a VLAN.
          - Associate the MA with a service.
            
            LDP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
            
            BGP VLL scenarios
            
            Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
       5. Run the [**mep mep-id**](cmdqueryname=mep+mep-id) command to configure a MEP.
       6. Run the [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id* command to set an RMEP ID.
       7. Run the [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable) command to enable the MEP to send CCMs.
       8. Run the [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable** command to enable the MEP to receive CCMs.
       9. Run the [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **ac** command to configure a measurement point for an AC.
    2. Configure a test instance.
       
       1. Perform the following step on the receiving device on an AC where on-demand two-way frame delay measurement will be implemented:
          
          Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
       2. Perform the following step on the transmitting device on an AC where on-demand two-way frame delay measurement will be implemented:
          
          Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
    3. Perform the following step on the receiving device on an AC where two-way frame delay measurement will be implemented:
       
       Run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
       
       The DMM reception function is configured on the device.
    4. Perform the following step on the transmitting device on an AC where two-way frame delay measurement will be implemented:
       
       Run [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) **send** **test-id** *test-id* **interval** { **1000** | **10000** } **count** *count-value*
       
       On-demand two-way frame delay measurement is configured on the AC side.
    5. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Configure proactive two-way frame delay measurement.
  
  
  1. Perform the following steps on the devices at both ends of a PW where proactive two-way frame delay measurement will be implemented:
     
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. (Optional) Run the [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable) command to enable PM to manage and send Y.1731 proactive performance statistics to the NMS.
     3. Run the [**cfm md**](cmdqueryname=cfm+md) *md-name* command to enter the MD view.
     4. Run the [**ma**](cmdqueryname=ma) *ma-name* command to enter the MA view.
     5. Associate the MA with a service.
        
        LDP VLL scenarios
        
        Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
        
        BGP VLL scenarios
        
        Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
     6. Run the [**mep mep-id**](cmdqueryname=mep+mep-id) command to configure a MEP.
     7. Run the [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id* command to set an RMEP ID.
     8. Run the [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable) command to enable the MEP to send CCMs.
     9. Run the [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable** command to enable the MEP to receive CCMs.
     10. Run the [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **pw** command to configure a measurement point.
     11. (Optional) Run the [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure delay thresholds for proactive two-way frame delay measurement based on a MEP.
     12. (Optional) Run the [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure thresholds for frame jitter in proactive two-way frame delay measurement based on a MEP.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device on a PW where on-demand two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on a PW where on-demand two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     3. (Optional) Run the [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to set delay thresholds for proactive two-way frame delay measurement based on a test instance.
     4. (Optional) Run the [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to set thresholds for frame jitter in proactive two-way frame delay measurement based on a test instance.
  3. Perform the following step on the receiving device on a PW where proactive two-way frame delay measurement will be implemented:
     
     Run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. Perform the following step on the transmitting device on a PW where proactive two-way frame delay measurement will be implemented:
     
     Run [**delay-measure two-way continual send**](cmdqueryname=delay-measure+two-way+continual+send) **test-id** *test-id-value* **interval** *interval-value*
     
     Proactive two-way frame delay measurement is enabled on the PW side.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **twoway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates two-way frame delay measurement to check statistics about the delay in bidirectional packet transmission.