Configuring Dual-ended Frame Loss Measurement in BD EVPN Networking
===================================================================

In BD EVPN networking where CFM is enabled to monitor link connectivity, if accurate frame loss measurement needs to be performed for a link, configure dual-ended frame loss measurement to monitor the quality of the link.

#### Procedure

Dual-ended frame loss measurement in BD EVPN networking is carried out continuously to allow proactive reporting of frame loss or performance results.

Dual-ended frame loss measurement in BD EVPN networking is deployed on end-to-end MEPs. Frame loss statistics are collected based on the transmit and receive counters carried in CCMs. Dual-ended frame loss measurement can be successfully performed only when the RMEP is in the up state.

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
   
   PM is enabled to manage and send Y.1731 proactive performance statistics to the NMS.
3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
   
   The MD view is displayed.
4. Run [**ma**](cmdqueryname=ma) *ma-name*
   
   The MA view is displayed.
5. Perform the following steps on the devices where the MEP and RMEP reside:
   * On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
     
     The MA is bound to a VLAN.
   * On the PE, run [**map**](cmdqueryname=map) **bridge-domain** *bd-id*
     
     The MA is bound to a specified BD instance.
6. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **outward**
   
   An MEP is configured.
7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
   
   The RMEP ID is set.
8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
   
   The MEP is enabled to send CCMs.
9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
   
   The MEP is enabled to receive CCMs from the RMEP.
10. Run [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
    
    A test instance is configured.
11. (Optional) Run [**loss-measure dual-ended local-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
    
    Lower and upper thresholds are set for the near-end frame loss rate in dual-ended frame loss measurement.
12. (Optional) Run [**loss-measure dual-ended remote-ratio-threshold**](cmdqueryname=loss-measure+dual-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
    
    Lower and upper thresholds are set for the far-end frame loss rate in dual-ended frame loss measurement.
13. Run [**loss-measure dual-ended continual**](cmdqueryname=loss-measure+dual-ended+continual) **test-id** *test-id-value*
    
    Dual-ended frame loss measurement is enabled.
14. Run [**commit**](cmdqueryname=commit)
    
    The configuration is committed.

#### Verifying the Configuration

After completing the configuration, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **dual-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the MEP that initiates dual-ended frame loss measurement to check statistics about dual-ended frame loss.