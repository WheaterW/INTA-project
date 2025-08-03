Two-Way Frame Delay Measurement When an L2VPN Is Connected to an L3VPN
======================================================================

Two-way frame delay measurement can be configured when CFM is enabled on an L2VPN connected to an L3VPN to monitor link connectivity and a MEP does not have the time synchronized with that on an RMEP.

#### Context

Two-way frame delay measurement in a VLAN can be implemented in either of the following modes: On-demand two-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive two-way frame delay measurement is performed continuously to allow proactive reporting of packet transmission delays or performance results.

* The proactive mode allows delay statistics to be collected periodically.
* Proactive mode: allows delay statistics to be collected periodically.


#### Procedure

* Configure on-demand two-way frame delay measurement.
  
  
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
        
        An RMEP ID is specified.
     6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     7. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
     8. (Optional) Run [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value*
        
        An alarm threshold is set for two-way frame delay measurement.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On each receiver RMEP, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive DMMs.
  4. On each initiator MEP, run [**delay-measure two-way**](cmdqueryname=delay-measure+two-way) **send** **test-id** *test-id-value* **interval** *interval-value* **count** *count-value*
     
     Two-way frame delay measurement is configured.
     
     Two-way frame delay measurement computes the delay time after an RMEP ID or a destination MAC address is specified:
     + If a local MEP has not learned the MAC address of the RMEP, specify a destination MAC address before implementing two-way frame delay measurement.
     + If a local MEP has learned the MAC address of the RMEP, specify the RMEP ID before implementing two-way frame delay measurement.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive two-way frame delay measurement.
  
  
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
     9. (Optional) Run either of the following commands to set an alarm threshold:
        
        1. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
           
           Upper and lower thresholds are set for two-way frame delay in proactive two-way frame delay measurement based on a specified MEP.
        2. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
           
           Upper and lower thresholds are set for two-way frame delay in proactive two-way frame delay measurement based on a specified test instance.
        3. (Optional) Run [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value*
           
           An alarm threshold is set for two-way frame delay measurement.
        
        The [**delay-measure two-way threshold**](cmdqueryname=delay-measure+two-way+threshold) *threshold-value* and [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) commands are mutually exclusive.
  2. Set alarm thresholds for two-way frame jitter.
     
     1. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
        
        Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified MEP.
     2. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified test instance.
  3. Configure a test instance.
     
     1. Perform the following step on the receiving device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device of a link where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  4. On each receiver RMEP, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive DMMs.
  5. Perform the following step on the transmitting device where two-way frame delay measurement will be implemented:
     
     Run [**delay-measure two-way continual send**](cmdqueryname=delay-measure+two-way+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive two-way frame delay measurement is configured in the VLAN.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **twoway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the receiving device where two-way frame delay measurement is implemented to verify the configuration.