Configuring Two-way Frame Delay Measurement in VPLS Networking
==============================================================

In VPLS networking, if the clocks of the MEPs at both ends of a link are not synchronized and the requirement for delay measurement is not high, two-way frame delay measurement can be configured for the link.

#### Context

Two-way frame delay measurement in VPLS networking can be either on-demand or proactive. On-demand two-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive two-way frame delay measurement is performed continuously to allow proactive reporting of packet transmission delays or performance results.

* To implement singular or periodic two-way frame delay measurement, configure on-demand two-way frame delay measurement.
* To implement continual two-way frame delay measurement, configure proactive two-way frame delay measurement in VPLS networking.


#### Procedure

* Configure on-demand two-way frame delay measurement for a PW.
  
  
  1. Perform the following steps on the devices at both ends of a PW where on-demand two-way frame delay measurement will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Run [**map**](cmdqueryname=map) **vsi** *vsi-name*
        
        The MA is bound to a VSI.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device on a PW where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on a PW where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiving device on a PW where on-demand two-way frame delay measurement will be implemented, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. On the transmitting device on a PW where two-way frame delay measurement will be implemented, run [**delay-measure two-way send**](cmdqueryname=delay-measure+two-way+send) **test-id***test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     On-demand two-way frame delay measurement is configured for a PW.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure on-demand two-way frame delay measurement for an AC.
  
  
  1. Perform the following steps on the devices at both ends of an AC where on-demand two-way frame delay measurement will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Perform the following steps on the devices where the MEPs reside:
        
        + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
          
          The MA is bound to a VLAN.
        + On the PE, run [**map**](cmdqueryname=map) **vsi** *vsi-name*
          
          The MA is bound to a VSI.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
        
        The MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device on an AC where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on an AC where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiving device on an AC where on-demand two-way frame delay measurement will be implemented, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. On the transmitting device on an AC where on-demand two-way frame delay measurement will be implemented, run [**delay-measure two-way send**](cmdqueryname=delay-measure+two-way+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     On-demand two-way frame delay measurement is configured for an AC.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive two-way frame delay measurement.
  
  
  1. Perform the following steps on the devices at both ends of a PW or  where proactive two-way frame delay measurement will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
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
        
        The remote MEP ID is configured.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The CCM transmission function is enabled.
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. (Optional) Run the [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure delay thresholds for proactive two-way frame delay measurement based on a MEP.
     11. (Optional) Run the [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ] command to configure delay thresholds for two-way frame jitter in proactive two-way frame delay measurement based on a MEP.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device on a PW where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **peer-ip** *peer-ip* [ **vc-id** *vc-id* ] ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device on a PW where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **remote-mep** *mep-id* ] [ **description** *description* ] command to configure a test instance.
     3. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Upper and lower thresholds are set for two-way frame delay in proactive two-way frame delay measurement based on a specified test instance.
     4. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified test instance.
  3. On the receiving device on a PW where proactive two-way frame delay measurement will be implemented, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. On the transmitting device on a PW where proactive two-way frame delay measurement will be implemented, run [**delay-measure two-way continual send**](cmdqueryname=delay-measure+two-way+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive two-way frame delay measurement is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **twoway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates two-way frame delay measurement to check statistics about the delay in bidirectional packet transmission.