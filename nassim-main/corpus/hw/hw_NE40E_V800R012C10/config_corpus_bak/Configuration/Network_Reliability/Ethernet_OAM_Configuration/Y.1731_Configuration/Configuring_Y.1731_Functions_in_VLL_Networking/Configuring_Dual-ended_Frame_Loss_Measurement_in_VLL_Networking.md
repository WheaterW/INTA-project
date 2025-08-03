Configuring Dual-ended Frame Loss Measurement in VLL Networking
===============================================================

In VLL networking, CFM is enabled to monitor link connectivity. If accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

#### Context

Dual-ended frame loss measurement is carried out continuously to permit proactive reporting of frame loss or performance results.

Dual-ended frame loss measurement in VLL networking is usually deployed on end-to-end MEPs. Dual-ended frame loss measurement can be successfully performed only when the RMEP is up.


#### Procedure

* Configure dual-ended frame loss measurement for a PW.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Perform the following steps on the devices that initiate dual-ended frame loss measurement.
  
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
  11. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
      
      A test instance is configured on the device.
  12. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  13. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  14. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is enabled for a PW.
  15. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
* Configure dual-ended frame loss measurement for an AC.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Perform the following steps on the devices that initiate dual-ended frame loss measurement.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
     
     Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
  3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     The MD view is displayed.
  4. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     The MA view is displayed.
  5. Perform the following steps on the devices where the MEP and RMEP reside:
     
     + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
       
       The MA is bound to a VLAN.
     + Associate the MA with a service on the PE.
       
       - LDP VLL scenarios
         
         Run the [**map**](cmdqueryname=map) **mpls l2vc** [ *peer-address* ] *l2vc-id* { **tagged** | **raw** } command to bind the MA to a specified L2VC.
       - BGP VLL scenarios
         
         Run the [**map**](cmdqueryname=map) **mpls l2vpn** *l2vpn-name* **ce** *ce-id* **ce-offset** *ce-offset-id* command to bind the MA to a specified PW.
  6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
     
     The MEP is configured.
  7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
     
     The remote MEP ID is configured.
  8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
     
     The CCM transmission function is enabled.
  9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
     
     The CCM reception function is enabled.
  10. Run [**measure-point**](cmdqueryname=measure-point) **mep** *mep-id* **ac**
      
      A measurement point for collecting Y.1731 statistics is configured for an AC.
  11. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
      
      A test instance is configured on the device.
  12. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  13. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  14. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is configured for an AC.
  15. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  PW-side statistics collecting does not apply to the scenario where load balancing among trunks and LSPs on the public network.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **dual-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the devices that initiates dual-ended frame loss measurement to check statistics about dual-ended frame loss.