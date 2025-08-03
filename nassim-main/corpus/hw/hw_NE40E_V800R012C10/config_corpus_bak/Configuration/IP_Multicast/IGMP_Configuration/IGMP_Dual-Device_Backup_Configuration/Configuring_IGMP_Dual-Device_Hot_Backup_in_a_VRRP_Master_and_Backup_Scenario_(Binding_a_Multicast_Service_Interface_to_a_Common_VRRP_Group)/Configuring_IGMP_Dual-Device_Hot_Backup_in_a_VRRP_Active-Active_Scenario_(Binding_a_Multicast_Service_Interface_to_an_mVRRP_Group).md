Configuring IGMP Dual-Device Hot Backup in a VRRP Active-Active Scenario (Binding a Multicast Service Interface to an mVRRP Group)
==================================================================================================================================

If a node or link fails on an IGMP dual-device hot backup network, a rapid multicast service switchover is triggered, improving service reliability. This section describes how to configure IGMP dual-device hot backup in a VRRP active-active scenario.

#### Prerequisites

A VRRP group has been configured using the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command, and the group has been configured as an mVRRP group using the [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ] command.


#### Context

In a VRRP active-active scenario, both the master and backup devices in a VRRP group can receive IGMP messages, but only the master device can send multicast traffic to downstream devices. Such implementation facilitates multicast service control and management and improves multicast service reliability.

To configure IGMP dual-device hot backup in a VRRP active-active scenario, perform the following steps on the devices in the same VRRP group.


#### Procedure

1. Configure an interface monitoring group and a BFD session.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name*
      
      
      
      An interface monitoring group is created, and the group view is displayed.
   3. Run [**monitor enable**](cmdqueryname=monitor+enable)
      
      
      
      The monitoring function is enabled for the interface monitoring group.
   4. Run [**binding interface**](cmdqueryname=binding+interface) *interface-name*
      
      
      
      The interface to be monitored is added to the interface monitoring group.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **peer-ip** *ip-address*
      
      
      
      A BFD session is created to monitor a specified peer.
   7. Run [**discriminator local**](cmdqueryname=discriminator+local) *discr-value*
      
      
      
      A local discriminator is configured.
   8. Run [**discriminator remote**](cmdqueryname=discriminator+remote) *discr-value*
      
      
      
      A remote discriminator is configured.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure rapid service link switching.
   1. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
      
      
      
      IP multicast routing is enabled.
   2. Run [**interface**](cmdqueryname=interface) *interface-type**interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**pim sm**](cmdqueryname=pim+sm)
      
      
      
      PIM-SM is enabled on the interface.
   4. Run [**igmp enable**](cmdqueryname=igmp+enable)
      
      
      
      IGMP is enabled.
   5. (Only on the interface that connects the backup device to the master device) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track****bfd-session** { *bfd-session-id* | **session-name** *bfd-configure-name* } [ **increased** *value-increased* | [ **reduced** *priority-value* ] ]
      
      
      
      The mVRRP group is enabled to track the BFD session.
   6. (On the interface that connects the master and backup devices) Run [**vrrp vrid track monitor-group**](cmdqueryname=vrrp+vrid+track+monitor-group) *virtual-router-id* **track** **monitor-group** [ *monitor-group-name* ] **failure-ratio** *failure-ratio-value* [ **link** | [ **reduced** *priority-value* ] ]
      
      
      
      The mVRRP group is enabled to track the interface monitoring group.
   7. (On the interface that connects to a downstream device) Run [**multicast track admin-vrrp**](cmdqueryname=multicast+track+admin-vrrp) **interface** *interface-type**interface-number* **vrid** *vrid-value*
      
      
      
      The multicast service interface is bound to the mVRRP group.
   8. (On the interface that connects to a downstream device) Run [**pim ignore dr-state**](cmdqueryname=pim+ignore+dr-state)
      
      
      
      The interface is enabled to ignore the PIM DR state.
   9. (On the interface that connects to a downstream device) Run [**pim ignore assert-state**](cmdqueryname=pim+ignore+assert-state)
      
      
      
      The interface is enabled to ignore the PIM Assert state.
   10. (On the interface that connects to a downstream device) Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.