Configuring Two-way Frame Delay Measurement in EVPN Networking
==============================================================

In EVPN networking, the clock frequencies between the two ends are not synchronized and CFM is enabled to monitor link connectivity. If the bidirectional delay measurement needs to be performed for a link, two-way frame delay measurement can be configured to monitor the quality of the link.

#### Context

Two-way frame delay measurement in EVPN networking can be either on-demand or proactive. On-demand two-way frame delay measurement is manually initiated for diagnosis of the packet transmission delay in a limited time. It can be singular or periodic measurement. Proactive two-way frame delay measurement is performed continuously to allow proactive reporting of packet transmission delays or performance results.

* To implement singular or periodic two-way frame delay measurement for an EVPN instance or an AC, configure on-demand two-way frame delay measurement in EVPN networking.
* To implement continual two-way frame delay measurement for a link, configure proactive two-way frame delay measurement in EVPN networking.


#### Procedure

* Configure on-demand two-way frame delay measurement for a device on the AC side.
  
  
  1. Perform the following steps on the devices at both ends of an AC.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Perform the following steps on the devices where the MEP and RMEP reside:
        
        + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
          
          The MA is bound to a VLAN.
        + On the PE, run [**map**](cmdqueryname=map) **evpn** **vpn-instance** *evpn-instance-name*
          
          The MA is associated with a specified EVPN instance.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **inward**
        
        A MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     7. (Optional) Run [**mep ccm-send**](cmdqueryname=mep+ccm-send) [ **mep-id** *mep-id* ] **enable**
        
        The CCM transmission function is enabled.
     8. (Optional) Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. On the receiving device on an AC where on-demand two-way frame delay measurement will be implemented, run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. On the transmitting device on an AC where on-demand two-way frame delay measurement will be implemented, run [**delay-measure two-way send**](cmdqueryname=delay-measure+two-way+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     On-demand two-way frame delay measurement is configured on the AC side.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive two-way frame delay measurement for an AC
  
  
  1. Perform the following steps on the devices at both ends of an AC where proactive two-way frame delay measurement will be implemented:
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        Performance management (PM) to manage Y.1731 proactive performance statistics is enabled. PM saves the statistics to generated statistics files and then sends the files to the NMS.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. On the PE, run [**map**](cmdqueryname=map) **evpn** **vpn-instance** *evpn-instance-name*
        
        The MA is associated with an EVPN instance.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **inward**
        
        A MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        The remote MEP ID is configured.
     8. (Optional) Run [**mep ccm-send**](cmdqueryname=mep+ccm-send) [ **mep-id** *mep-id* ] **enable**
        
        The CCM transmission function is enabled.
     9. (Optional) Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The CCM reception function is enabled.
     10. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified MEP.
     11. (Optional) Run [**delay-measure two-way delay-threshold**](cmdqueryname=delay-measure+two-way+delay-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Upper and lower thresholds are set for two-way frame delay in proactive two-way frame delay measurement based on a specified test instance.
     12. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified MEP.
     13. (Optional) Run [**delay-measure two-way variation-threshold**](cmdqueryname=delay-measure+two-way+variation-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
         
         Upper and lower thresholds are set for two-way frame jitter in proactive two-way frame delay measurement based on a specified test instance.
  2. Configure a test instance.
     
     1. Perform the following step on the receiving device where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
     2. Perform the following step on the transmitting device where two-way frame delay measurement will be implemented:
        
        Run the [**test-id**](cmdqueryname=test-id) *test-id-value* [ **testid-file** ] **mep** *mep-id* [ **mac** *mac-address* | **remote-mep** *mep-id* ] [ **8021p** *8021p-value* ] [ **description** *description* ] command to configure a test instance.
  3. Perform the following step on the receiving device where proactive two-way frame delay measurement will be implemented:
     
     Run [**delay-measure two-way receive**](cmdqueryname=delay-measure+two-way+receive) **test-id** *test-id*
     
     The DMM reception function is configured on the device.
  4. Perform the following step on the transmitting device where proactive two-way frame delay measurement will be implemented:
     
     Run [**delay-measure two-way continual send**](cmdqueryname=delay-measure+two-way+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive two-way frame delay measurement is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **twoway-delay** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the device that initiates two-way frame delay measurement to check statistics about the delay in bidirectional frame transmission.