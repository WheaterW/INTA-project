One-Way Frame Delay Measurement When an L2VPN Is Connected to an L3VPN
======================================================================

One-way frame delay measurement can be configured when CFM is enabled for an L2VPN connected to an L3VPN to monitor link connectivity and a MEP has the time synchronized with that on an RMEP.

#### Context

One-way frame delay measurement can be implemented in either of the following modes: On-demand one-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive one-way frame delay measurement is carried out continuously to permit proactive reporting of packet transmission delays or performance results.

* The on-demand mode is manually initiated and allows frame delay statistics to be collected at a time or a specific number of times for diagnosis.
* The proactive mode allows delay statistics to be collected periodically.


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
        
        An outward-facing MEP is configured.
     5. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP ID is specified.
     6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     7. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
     8. (Optional) Run [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) *threshold-value*
        
        An alarm threshold is set for one-way frame delay measurement.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**delay-measure one-way receive**](cmdqueryname=delay-measure+one-way+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive 1DM messages.
  4. On the initiator MEP, run [**delay-measure one-way send**](cmdqueryname=delay-measure+one-way+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     One-way frame delay measurement is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive one-way frame delay measurement.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Proactive statistics are sent by the PM module to an NMS.
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
     9. Run either of the following commands to set an alarm threshold:
        
        1. (Optional) To set the delay threshold for proactive one-way frame delay measurement, run the [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* command.
        2. (Optional) To set the delay threshold for one-way frame delay measurement, run the [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) *threshold-value* command.
        
        The [**delay-measure one-way delay-threshold**](cmdqueryname=delay-measure+one-way+delay-threshold) and [**delay-measure one-way threshold**](cmdqueryname=delay-measure+one-way+threshold) commands are mutually exclusive.
     10. (Optional) Run [**delay-measure one-way variation-threshold**](cmdqueryname=delay-measure+one-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         The delay variation threshold is set for proactive one-way frame delay measurement.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where one-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiver RMEP, run [**delay-measure one-way continual receive**](cmdqueryname=delay-measure+one-way+continual+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive 1DM messages.
  4. On the initiator MEP, run [**delay-measure one-way continual send**](cmdqueryname=delay-measure+one-way+continual+send) **test-id** *test-id-value* **interval** *interval-value*
     
     Proactive one-way frame delay measurement is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **oneway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the MEP that initiates one-way frame delay measurement and verify the configuration.