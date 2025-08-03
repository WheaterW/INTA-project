Configuring Dual-ended Frame Loss Measurement in VPLS Networking
================================================================

In VPLS networking, CFM is enabled to monitor link connectivity. If accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

#### Context

Dual-ended frame loss measurement in VPLS networking is carried out continuously to permit proactive reporting of frame loss or performance results. Dual-ended frame loss measurement in VPLS networking is usually deployed on end-to-end MEPs. Dual-ended frame loss measurement can be successfully performed only when the remote MEP is in the Up state.


#### Procedure

* Configure dual-ended frame loss measurement for a PW.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Perform the following steps on the devices that initiate dual-ended frame loss measurement.
  
  1. Run [**system-view**](cmdqueryname=system-view)
  2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
     
     Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
  3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     The MD view is displayed.
  4. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     The MA view is displayed.
  5. Run [**map**](cmdqueryname=map) **vsi** *vsi-name*
     
     The MA is bound to a VSI.
  6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
     
     The MEP is configured.
  7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
     
     An RMEP ID is set.
  8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
     
     The MEP is enabled to send CCMs.
  9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
     
     The MEP is enabled to receive CCMs.
  10. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **peer-ip** *peer-ip* [ **vc-id** *vc-id* ] ] [ **description** *description* ]
      
      A test instance is configured.
  11. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep-id** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  12. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  13. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is configured for a PW.
  14. Run [**commit**](cmdqueryname=commit)
      
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
     
     + On the CE, run the [**map**](cmdqueryname=map) **vlan** *vlan-id* command to bind the MA to a VLAN.
     + On the PE, run the [**map**](cmdqueryname=map) **vsi** *vsi-name* command to bind the MA to a VSI.
  6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
     
     The MEP is configured.
  7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
     
     An RMEP ID is set.
  8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
     
     The MEP is enabled to send CCMs.
  9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
     
     The MEP is enabled to receive CCMs.
  10. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
      
      A test instance is configured.
  11. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep-id** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  12. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  13. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is configured for an AC.
  14. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **dual-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the devices that initiates dual-ended frame loss measurement to check statistics about dual-ended frame loss.