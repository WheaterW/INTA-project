Single-ended Frame Loss Measurement When an L2VPN Is Connected to an L3VPN
==========================================================================

When an L2VPN is connected to an L3VPN, single-ended frame loss measurement is enabled to monitor link quality. This helps prevent CCMs from overloading the network.

#### Context

Single-ended frame loss measurement measures frame loss on demand or proactively. On-demand single-ended frame loss measurement is manually initiated for diagnosis of frame loss in a limited time. It can be singular or periodic measurement. Proactive single-ended frame loss measurement is continuously performed to allow proactive reporting of frame loss or performance results.

* The on-demand mode is manually initiated and allows frame loss statistics to be collected at a time or a specific number of times for diagnosis.
* To implement continual single-ended frame loss measurement, configure proactive single-ended frame loss measurement.


#### Procedure

* Configure on-demand single-ended frame loss measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        An outward-facing MEP is configured.
     5. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP ID is specified.
     6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     7. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive LMMs.
  4. On the initiator MEP, run [**loss-measure single-ended send**](cmdqueryname=loss-measure+single-ended+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     Single-ended frame loss measurement is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive single-ended frame loss measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Proactive statistics are sent by the performance management (PM) module to an NMS.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP ID is specified.
     7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
     9. (Optional) Run [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
        
        Upper and lower thresholds are set for the near-end frame loss rate in proactive single-ended frame loss measurement based on a specified MEP.
     10. (Optional) Run [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Upper and lower thresholds are set for the far-end frame loss rate in proactive single-ended frame loss measurement based on a specified MEP.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where single-ended frame loss measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
     3. (Optional) Run [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Upper and lower thresholds are set for the near-end frame loss rate in proactive single-ended frame loss measurement based on a specified test instance.
     4. (Optional) Run [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Upper and lower thresholds are set for the far-end frame loss rate in proactive single-ended frame loss measurement based on a specified test instance.
  3. Perform the following step on the receiving device on a link where proactive single-ended frame loss measurement will be implemented:
     
     Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive LMMs.
  4. Perform the following step on the transmitting device on a link where proactive single-ended frame loss measurement will be implemented:
     
     Run [**loss-measure single-ended continual send**](cmdqueryname=loss-measure+single-ended+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive single-ended frame loss measurement is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the MEP that initiates single-ended frame loss measurement and verify the configuration.