Configuring One-way Frame Delay Measurement in VLAN Networking
==============================================================

In VLAN networking, the clock frequencies between the two ends are synchronized and CFM is enabled to monitor link connectivity. If the unidirectional delay measurement needs to be performed for a link, one-way frame delay measurement can be configured to monitor the quality of the link.

#### Context

One-way frame delay measurement in a VLAN can be implemented in either of the following modes: On-demand one-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive one-way frame delay measurement is carried out continuously to permit proactive reporting of packet transmission delays or performance results.

* On-demand mode: manually collects delay statistics once or a specified number of times during diagnosis.
* Proactive mode: periodically collects delay statistics.


#### Procedure

* Configure on-demand one-way frame delay measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     5. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     7. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     8. (Optional) Run [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) *threshold-value*
        
        An alarm threshold is set for one-way frame delay measurement.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**delay-measure one-way receive**](cmdqueryname=delay-measure+one-way+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive 1DM messages.
  4. On the initiator MEP, run [**delay-measure one-way send**](cmdqueryname=delay-measure+one-way+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     On-demand one-way frame delay measurement is configured in a VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive one-way frame delay measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
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
        
        The CCM reception function is enabled.
     9. Use either of the following methods to set alarm thresholds for one-way frame delay.
        
        1. (Optional) Run [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) **mep-id** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
           
           Lower and upper thresholds are set for one-way frame delay.
        2. (Optional) Run [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) *threshold-value*
           
           An alarm threshold is set for one-way frame delay.
        
        The [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) and [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) commands are mutually exclusive.
     10. (Optional) Run [**delay-measure one-way variation-threshold**](cmdqueryname=delay-measure+one-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Lower and upper thresholds are set for one-way frame jitter.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**delay-measure one-way continual receive**](cmdqueryname=delay-measure+one-way+continual+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive 1DM messages.
  4. On the initiator MEP, run [**delay-measure one-way continual send**](cmdqueryname=delay-measure+one-way+continual+send) **test-id** *test-id-value* **interval** *interval-value*
     
     Proactive one-way frame delay measurement is configured in a VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Checking the Configurations

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **oneway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates one-way frame delay measurement to check statistics about the delay in unidirectional packet transmission.