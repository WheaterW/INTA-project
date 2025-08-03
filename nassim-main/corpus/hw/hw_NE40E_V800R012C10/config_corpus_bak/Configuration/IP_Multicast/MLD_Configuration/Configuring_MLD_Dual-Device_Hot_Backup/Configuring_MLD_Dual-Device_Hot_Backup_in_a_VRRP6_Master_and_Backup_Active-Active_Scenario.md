Configuring MLD Dual-Device Hot Backup in a VRRP6 Master/Backup Active-Active Scenario
======================================================================================

MLD dual-device hot backup can trigger a rapid multicast service switchover if a node or link fails, improving service reliability.

#### Prerequisites

A VRRP6 group has been created using the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* [ **virtual-ip** *virtual-address* ] command.


#### Context

In a VRRP6 active-active scenario, both the master and backup devices in a VRRP6 group can receive MLD messages, but only the master device can send multicast traffic to downstream devices. Such implementation helps the system control and manage multicast services more flexibly, improving reliability of the services.

Perform the following steps on the devices that back up each other:


#### Procedure

1. (Optional) Configuring an interface monitoring group and BFD.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name*
      
      
      
      The interface monitoring group view is displayed.
   3. Run [**monitor enable**](cmdqueryname=monitor+enable)
      
      
      
      The monitoring function is enabled for the interface monitoring group.
   4. Run [**binding interface**](cmdqueryname=binding+interface) { *interface-type**interface-number* | *interface-name* } [ **down-weight***down-weight-value* ]
      
      
      
      An interface to be monitored is added to the interface monitoring group.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run **[**bfd**](cmdqueryname=bfd)** **session-name** **[**bind**](cmdqueryname=bind)** **[**peer-ipv6**](cmdqueryname=peer-ipv6)** **peer-ipv6** [ **vpn-instance****vpn-name** ] [ **source-ipv6****source-ipv6** ] **[**track-interface**](cmdqueryname=track-interface)** **interface** { **interface-name** | *interface-type* **interface-number**}
      
      
      
      A BFD for IPv6 session is created, related information is bound to the session, and the BFD session view is displayed.
   7. Run [**discriminator local**](cmdqueryname=discriminator+local) *discr-value*
      
      
      
      A local discriminator is configured.
   8. Run [**discriminator remote**](cmdqueryname=discriminator+remote) *discr-value*
      
      
      
      A remote discriminator is configured.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure rapid service link switching.
   1. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
      
      
      
      IPv6 multicast routing is enabled.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
      
      
      
      IPv6 PIM is enabled on the interface.
   4. Run [**mld enable**](cmdqueryname=mld+enable)
      
      
      
      MLD is enabled.
   5. (On the master device) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** **bfd-session** *bfd-session-id* [ **increased** *value-increased* | [ **reduced** *value-reduced* ] ]
      
      
      
      The VRRP6 group is configured to track a BFD session.
   6. (On the backup device) Run **[**vrrp6 vrid**](cmdqueryname=vrrp6+vrid)** *virtual-router-id*[**track bfd-session**](cmdqueryname=track+bfd-session) **bfd-session-id** { ****peer**** | ****link**** }
      
      
      
      The VRRP6 group is configured to track a BFD session.
   7. (On the interface connected to a downstream device) Run [**multicast ipv6 track admin-vrrp6**](cmdqueryname=multicast+ipv6+track+admin-vrrp6) **interface** *interface-type* *interface-number* **vrid** *vrid-value*
      
      
      
      The multicast service interface is bound to the mVRRP6 group.
   8. (On the interface connected to a downstream device) Run [**multicast ipv6 track vrrp6**](cmdqueryname=multicast+ipv6+track+vrrp6) **vrid** *vrid-value*
      
      
      
      The multicast service interface is bound to a VRRP6 group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A multicast service interface can be bound to only one type of VRRP6 group, either mVRRP6 or common VRRP6 group. You can select one type as required. In a VRRP6 master/backup active-active scenario, you are advised to bind the interface to a common VRRP6 group.
   9. (On the interface connected to a downstream device) Run [**pim ipv6 ignore dr-state**](cmdqueryname=pim+ipv6+ignore+dr-state)
      
      
      
      The interface is enabled to ignore the PIM DR state.
   10. (On the interface connected to a downstream device) Run [**pim ipv6 ignore assert-state**](cmdqueryname=pim+ipv6+ignore+assert-state)
       
       
       
       The interface is enabled to ignore the PIM Assert state.
   11. (On the interface connected to a downstream device) Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
       
       
       
       The RBP is bound to the interface.
   12. (On the interface connected to a downstream device) Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   13. (On the interface connected to a downstream device) Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.