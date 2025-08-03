Configuring Two-way Frame Delay Measurement in VLAN Networking
==============================================================

In VLAN networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

#### Context

Two-way frame delay measurement in VLAN networking can be either on-demand or proactive. On-demand two-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive two-way frame delay measurement is performed continuously to allow proactive reporting of packet transmission delays or performance results.

* On-demand mode: manually collects delay statistics once or a specified number of times during diagnosis.
* Proactive mode: periodically collects delay statistics.


#### Procedure

* Configure on-demand two-way frame delay measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     
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
     9. (Optional) Run [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value*, set alarm thresholds for two-way frame delay measurement.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive DMMs.
  4. On the initiator MEP, run [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) **send** **test-id** *test-id-value* **interval** *interval-value* **count** *count-value*
     
     Two-way frame delay measurement is configured in a VLAN.
     
     VLAN-specific two-way delay measurement is performed based on either of the following item
     
     + Specified destination MAC address: used if a local MEP does not learn the RMEP's MAC address.
     + Specified RMEP ID: used if a local MEP learns the RMEP's MAC address.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive two-way frame delay measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     
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
     10. Use either of the following methods to set alarm thresholds for two-way frame delay.
         
         1. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
            
            Delay thresholds are configured for proactive two-way frame delay measurement based on a MEP.
         2. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
            
            Delay thresholds are set for proactive two-way frame delay measurement based on a test instance.
         3. (Optional) Run [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value*
            
            An alarm threshold is set for two-way frame delay.
            
            The [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value* and [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) commands are mutually exclusive.
  2. Set alarm thresholds for two-way frame jitter.
     
     1. (Optional) Run the [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure thresholds for frame jitter in proactive two-way frame delay measurement based on a MEP.
     2. (Optional) Run the [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command to set thresholds for frame jitter in proactive two-way frame delay measurement based on a test instance.
  3. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  4. Perform the following step on the transmitting device where two-way frame delay measurement will be implemented:
     
     Run the [**delay-measure two-way continual send**](cmdqueryname=delay-measure+two-way+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ] command to configure proactive two-way frame delay measurement in the VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **twoway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates two-way frame delay measurement to check statistics about the delay in bidirectional packet transmission.