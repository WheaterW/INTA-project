Configuring Single-ended Frame Loss Measurement in VLAN Networking
==================================================================

In VLAN networking, CFM is enabled. CCMs are not used to monitor link connectivity, preventing them from using a lot of network bandwidth resources. If accurate frame loss measurement needs to be performed for a link, single-ended frame loss measurement can be configured to monitor the link quality.

#### Context

Single-ended frame loss measurement in VLAN networking can be either on-demand or proactive. On-demand single-ended frame loss measurement is manually initiated for diagnosis of frame loss in a limited time. It can be singular or periodic measurement. Proactive single-ended frame loss measurement is performed continuously to permit proactive reporting of frame loss or performance results.

* To implement singular or periodic single-ended frame loss measurement, configure on-demand single-end frame loss measurement in VLAN networking.
* To implement continual single-ended frame loss measurement, configure proactive single-ended frame loss measurement in VLAN networking.


#### Procedure

* Configure on-demand single-ended frame loss measurement.
  
  
  1. Perform the following steps on the devices configured with MEPs at both ends of a link:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
        
        The MA is bound to a VLAN.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
  2. Configure the test instance.
     
     1. Perform the following step on the receiving device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id)  *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id)  *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiving device of a link where single-ended frame loss measurement will be implemented, run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The LMM reception function is configured on the device.
  4. On the device that initiates single-ended frame loss measurement, run [**loss-measure single-ended send**](cmdqueryname=loss-measure+single-ended+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     Single-ended frame loss measurement is enabled for a VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive single-ended frame loss measurement.
  
  
  1. Perform the following steps on the devices at both ends of a link where proactive single-ended frame loss measurement will be implemented:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
        
        The MA is bound to a VLAN.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. (Optional) Run the [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure lower and upper thresholds for the near-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
     11. (Optional) Run the [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the lower and upper thresholds for the near-end frame loss rate in proactive single-ended frame loss measurement based on the test instance.
     12. (Optional) Run the [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure lower and upper thresholds for the far-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
     13. (Optional) Run the [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to configure the lower and upper thresholds for the far-end frame loss rate in proactive single-ended frame loss measurement based on the test instance.
  2. Configure the test instance.
     
     1. Perform the following step on the receiving device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id)  *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id)  *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiving device on a link where proactive single-ended frame loss measurement will be implemented, run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The LMM reception function is configured on the device.
  4. On the transmitting device on a link where proactive single-ended frame loss measurement will be implemented, run [**loss-measure single-ended continual send**](cmdqueryname=loss-measure+single-ended+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive single-ended frame loss measurement is configured on the device.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates single-ended frame loss measurement to check statistics about single-ended frame loss.