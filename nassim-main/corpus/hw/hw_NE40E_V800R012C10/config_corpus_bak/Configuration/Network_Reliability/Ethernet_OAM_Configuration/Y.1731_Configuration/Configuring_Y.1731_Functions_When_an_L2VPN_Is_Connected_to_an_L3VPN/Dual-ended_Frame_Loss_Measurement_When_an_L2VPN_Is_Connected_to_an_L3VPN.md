Dual-ended Frame Loss Measurement When an L2VPN Is Connected to an L3VPN
========================================================================

When a CFM-enabled L2VPN is connected to an L3VPN, dual-ended frame loss measurement is enabled to collect detailed statistics and monitor link quality.

#### Context

Dual-ended frame loss measurement in L2VPN accessing L3VPN scenarios is performed continuously to allow proactive reporting of frame loss or performance results.

Frame loss measurement is deployed on end-to-end MEPs. In Y.1731, frame loss statistics are collected based on the transmit and receive counters carried in CCMs. Dual-ended frame loss measurement can be successfully performed only when the RMEP is in the up state.


#### Procedure

* Perform the following steps on the devices that initiate dual-ended frame loss measurement:
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
     
     Proactive statistics are sent by the PM module to an NMS.
  3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
     
     The MD view is displayed.
  4. Run [**ma**](cmdqueryname=ma) *ma-name*
     
     The MA view is displayed.
  5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
     
     An outward-facing MEP is configured.
  6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
     
     The RMEP ID is set.
  7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
     
     The MEP is enabled to send CCMs.
  8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
     
     The RMEP is enabled to receive CCMs.
  9. Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
     
     A test instance is configured.
  10. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
  11. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
      
      Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
  12. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
      
      Dual-ended frame loss measurement is configured.
  13. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.