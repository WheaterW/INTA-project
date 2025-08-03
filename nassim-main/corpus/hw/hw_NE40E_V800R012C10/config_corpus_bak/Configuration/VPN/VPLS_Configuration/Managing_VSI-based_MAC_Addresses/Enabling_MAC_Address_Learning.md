Enabling MAC Address Learning
=============================

Packets can be forwarded according to MAC addresses only after MAC address learning is enabled.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ]
   
   
   
   The VSI view is displayed.
3. Run [**mac-learning**](cmdqueryname=mac-learning) { **enable** | **disable** }
   
   
   
   MAC address learning is enabled.
   
   
   
   If MAC address learning is disabled for a VSI, the VSI cannot automatically learn MAC addresses, causing packets to be broadcast on the network. Exercise caution when disabling the MAC address learning.
4. Run [**mac-learn-style**](cmdqueryname=mac-learn-style) { **qualify** | **unqualify** }
   
   
   
   The MAC address learning mode is configured.
   
   
   
   Because E2E [**mac-learn-style**](cmdqueryname=mac-learn-style) negotiation for a VSI is not allowed, [**mac-learn-style**](cmdqueryname=mac-learn-style) settings must be consistent in an E2E manner. If mode inconsistency exists, VLAN ID-based MAC address learning may become incorrect and packets may be discarded.
   
   In an HVPLS scenario, you are advised not to enable MAC address learning in qualified mode on an SPE. If the qualified mode needs to be enabled, the types of access interfaces on PEs at both ends must be consistent. The interface type can only be the dot1q VLAN tag termination sub-interface, QinQ mapping sub-interface, or QinQ stacking sub-interface. If the qualified mode is configured on an SPE, the type of VLAN tag used to learn MAC addresses must be specified. That is, the **outer-vlan** or **inner-vlan** parameter must be specified in the [**mac-learn-style**](cmdqueryname=mac-learn-style) **qualify** { **outer-vlan** | **inner-vlan** } command.
   
   * **outer-vlan**: learns MAC addresses based on outer VLAN tags.
   * **inner-vlan**: learns MAC addresses based on inner VLAN tags.
   
   In an HVPLS scenario, after a dot1q VLAN tag termination sub-interface is bound to a remote PE, to enable the SPE to learn MAC addresses in **qualify** mode, run the [**mac-learn-style**](cmdqueryname=mac-learn-style) **qualify** **outer-vlan** command. After a QinQ mapping or stacking sub-interface is bound to a remote PE, to enable the SPE to learn MAC addresses in **qualify** mode, run the [**mac-learn-style**](cmdqueryname=mac-learn-style) **qualify** **inner-vlan** or [**mac-learn-style**](cmdqueryname=mac-learn-style) **qualify** command on the SPE.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**mac-learn-style qualify**](cmdqueryname=mac-learn-style+qualify) command is run for a VSI, only a dot1q VLAN tag termination sub-interface, QinQ mapping sub-interface, or QinQ stacking sub-interface can be bound to the VSI. If **outer-vlan** is specified, only a dot1q VLAN tag termination sub-interface can be bound to the VSI. If **inner-vlan** is specified, only a QinQ mapping or QinQ stacking sub-interface can be bound to the VSI.
   
   After a dot1q VLAN tag termination sub-interface is bound to a VSI, MAC address learning in qualify mode cannot be configured. Therefore, you need to run the [**mac-learn-style qualify**](cmdqueryname=mac-learn-style+qualify) command before binding the sub-interface to a VSI. After a dot1q VLAN tag termination sub-interface is bound to a VSI, MAC address learning in qualify mode cannot be disabled. To restore the default MAC address learning mode of the VSI, unbind the dot1q VLAN tag termination sub-interface from the VSI first.
5. Run [**mac-address aging-time**](cmdqueryname=mac-address+aging-time) { *interval* | [ **local** *local-seconds* | **remote** *remote-seconds* ] }
   
   
   
   The aging time of dynamic MAC addresses is configured.
   
   
   
   If *interval* is set to 0, MAC address entries never age.
   
   The system starts an aging timer for each dynamic MAC address entry. If the MAC address entry is not updated before the aging time expires, the entry will be deleted.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.