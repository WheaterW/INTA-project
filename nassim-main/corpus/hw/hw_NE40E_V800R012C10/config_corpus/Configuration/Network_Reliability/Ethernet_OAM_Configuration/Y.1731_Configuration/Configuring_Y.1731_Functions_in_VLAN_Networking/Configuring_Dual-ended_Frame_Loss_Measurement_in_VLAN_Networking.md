Configuring Dual-ended Frame Loss Measurement in VLAN Networking
================================================================

In VLAN networking, if CFM is enabled to monitor link connectivity, and accurate frame loss measurement needs to be performed for a link, dual-ended frame loss measurement can be configured to monitor the quality of the link.

#### Context

Dual-ended frame loss measurement in VLAN networking is carried out continuously to permit proactive reporting of frame loss or performance results.

Dual-ended frame loss measurement in VLAN networking is usually deployed on end-to-end MEPs. Dual-ended frame loss measurement can be successfully performed only when the remote MEP is in the Up state.


#### Procedure

* Perform the following steps on the devices that initiate dual-ended frame loss measurement:
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
     
     Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
  3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     The MD view is displayed.
  4. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     The MA view is displayed.
  5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
     
     The MEP is configured.
  6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
     
     The remote MEP ID is configured.
  7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
     
     The CCM transmission function is enabled.
  8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
     
     The MEP is enabled to receive CCMs.
  9. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
     
     A test instance is configured.
  10. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep-id** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  11. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep-id** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  12. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is configured for a VLAN.
  13. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **dual-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the devices that initiates dual-ended frame loss measurement to check statistics about dual-ended frame loss.