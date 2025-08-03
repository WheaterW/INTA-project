Configuring Single-ended Frame Loss Measurement in EVPN Networking
==================================================================

In EVPN networking scenarios where CFM is enabled, if CCMs are not used for link connectivity monitoring to minimize their impact on the network, you can configure single-ended frame loss measurement to measure frame loss rates and monitor link quality.

#### Context

Single-ended frame loss measurement in EVPN networking can be either on-demand or proactive. On-demand single-ended frame loss measurement is manually initiated for diagnosis of frame loss within a limited period of time. It can be performed once or multiple times (the number of times is configurable). Proactive single-ended frame loss measurement is continuously performed to allow proactive reporting of frame loss or performance results.

* Configure on-demand measurement if you need the device to collect single-ended frame loss statistics for a specified number of times.
* Configure proactive measurement if you need the device to collect single-ended frame loss statistics continuously.


#### Procedure

* Configure on-demand single-ended frame loss measurement for an AC.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     3. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     4. Perform the following steps on the devices where the MEP and RMEP reside:
        
        + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
          
          The MA is bound to a VLAN.
        + On the PE, run [**map**](cmdqueryname=map) { **evpn vpn-instance** *evpn-instance-name* | **bridge-domain** *bd-id* }
          
          The MA is bound to a specified EVPN instance.
          
          For EVPN VPWS or EVPN VPLS in common AC interface mode, specify **evpn vpn-instance** *evpn-instance-name*.
          
          For EVPN VPLS in BD mode, specify **bridge-domain** *bd-id*.
     5. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **outward**
        
        A MEP is configured.
     6. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP is configured.
     7. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
  2. Configure test instances.
     
     1. On the receiver RMEP:
        
        Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ]
        
        A test instance is configured.
     2. On the initiator MEP:
        
        Run [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ]
        
        A test instance is configured.
  3. On the receiver RMEP:
     
     Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive LMMs.
  4. On the initiator MEP:
     
     Run [**loss-measure single-ended send**](cmdqueryname=loss-measure+single-ended+send) **test-id** *test-id-value* **interval** { **1000** | **10000** } **count** *count-value*
     
     On-demand single-ended frame loss measurement is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure proactive single-ended frame loss measurement for an AC.
  
  
  1. Perform the following steps on the MEP and RMEP:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. (Optional) Run [**y1731 pm-mode enable**](cmdqueryname=y1731+pm-mode+enable)
        
        PM is enabled to manage and send Y.1731 proactive performance statistics to the NMS.
     3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
        
        The MD view is displayed.
     4. Run [**ma**](cmdqueryname=ma) *ma-name*
        
        The MA view is displayed.
     5. Perform the following steps on the devices where the MEP and RMEP reside:
        
        + On the CE, run [**map**](cmdqueryname=map) **vlan** *vlan-id*
          
          The MA is bound to a VLAN.
        + On the PE, run [**map**](cmdqueryname=map) { **evpn vpn-instance** *evpn-instance-name* | **bridge-domain** *bd-id* }
          
          The MA is bound to a specified EVPN instance.
          
          For EVPN VPWS or EVPN VPLS in common AC interface mode, specify **evpn vpn-instance** *evpn-instance-name*.
          
          For EVPN VPLS in BD mode, specify **bridge-domain** *bd-id*.
     6. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number* **outward**
        
        A MEP is configured.
     7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
        
        An RMEP is configured.
     8. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
        
        The MEP is enabled to send CCMs.
     9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
        
        The RMEP is enabled to receive CCMs.
     10. (Optional) Run [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Lower and upper thresholds are set for the near-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
     11. (Optional) Run [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **mep** *mep-id* **upper-limit** *upper-limit* **lower-limit** *lower-limit* [ **8021p** *8021p-value* ]
         
         Lower and upper thresholds are set for the far-end frame loss rate in proactive single-ended frame loss measurement on a specified MEP.
  2. Configure test instances.
     
     1. To configure a test instance on the receiving device of a link where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [ **description** *description* ] command.
     2. To configure a test instance on the transmitting device of a link where single-ended frame loss measurement will be implemented, run the [**test-id**](cmdqueryname=test-id) *test-id* [ **testid-file** ] **mep** *mep-id* [  **mac** *mac-address* | **remote-mep** *mep-id* ] [ **description** *description* ] command.
     3. (Optional) Run [**loss-measure single-ended local-ratio-threshold**](cmdqueryname=loss-measure+single-ended+local-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Lower and upper thresholds are set for the near-end frame loss rate in proactive single-ended frame loss measurement in a specified test instance.
     4. (Optional) Run [**loss-measure single-ended remote-ratio-threshold**](cmdqueryname=loss-measure+single-ended+remote-ratio-threshold) **test-id** *test-id-value* **upper-limit** *upper-limit* **lower-limit** *lower-limit*
        
        Lower and upper thresholds are set for the far-end frame loss rate in proactive single-ended frame loss measurement in a specified test instance.
  3. On the receiver RMEP:
     
     Run [**loss-measure single-ended receive**](cmdqueryname=loss-measure+single-ended+receive) **test-id** *test-id-value*
     
     The RMEP is enabled to receive LMMs.
  4. On the initiator MEP:
     
     Run [**loss-measure single-ended continual send**](cmdqueryname=loss-measure+single-ended+continual+send) **test-id** *test-id-value* **interval** *interval-value* [ **period** *period* ]
     
     Proactive single-ended frame loss measurement is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display y1731 statistic-type**](cmdqueryname=display+y1731+statistic-type) **single-loss** [ **test-id** *test-id-value* ] [ **count** *count-value* ] command on the MEP that initiates single-ended frame loss measurement to check statistics about single-ended frame loss.