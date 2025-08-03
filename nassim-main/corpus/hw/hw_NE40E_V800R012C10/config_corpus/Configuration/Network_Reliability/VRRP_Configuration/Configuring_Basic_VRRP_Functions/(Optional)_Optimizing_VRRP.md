(Optional) Optimizing VRRP
==========================

To optimize VRRP, enable ping to a virtual IP address, set the interval at which the master device sends gratuitous ARP packets, and disable a device from checking TTL values in received VRRP Advertisement packets.

#### Context

[Table 1](#EN-US_TASK_0172361757__tab_dc_vrp_vrrp_cfg_010801) describes VRRP optimization functions.

**Table 1** Optimization functions and their usage scenarios
| Basic Function | Usage Scenario |
| --- | --- |
| [Configuring a VRRP version number](#EN-US_TASK_0172361757__step_08) | VRRP4 supports VRRPv2 and VRRPv3.  * A VRRPv2 group can send and receive only VRRPv2 Advertisement packets. If the VRRPv2 group receives VRRPv3 Advertisement packets, it discards these packets. * A VRRPv3 group can send and receive both VRRPv2 and VRRPv3 Advertisement packets. The VRRPv3 group can communicate with both VRRPv2 and VRRPv3 groups. |
| [Pinging a virtual IP address](#EN-US_TASK_0172361757__step_01) | Hosts can ping the virtual IP address of a VRRP group. This function can be used to monitor the connectivity of links between hosts and a gateway. |
| [Enabling passive ARP](#EN-US_TASK_0172361757__step_10) | In most cases, after receiving an ARP request packet that is destined for a virtual IP address, the backup device in a VRRP group does not learn the ARP entry of the requester. If a link or the master device in the VRRP group fails, a master/backup device switchover is performed. The original backup device becomes the master device and must learn user-side ARP entries before taking over the traffic forwarded by the original master device. During user-side ARP entry learning, traffic is interrupted temporarily. You can enable passive ARP to resolve this issue. |
| [Setting the interval at which the master device sends gratuitous ARP packets](#EN-US_TASK_0172361757__step_02) | To ensure that the destination MAC address and outbound interface on a downstream device (switch) connected to the master device in a VRRP group are updated in a timely manner, the master device sends gratuitous ARP packets to the downstream device at a specified interval. |
| [Disabling a device from checking TTL values in VRRP Advertisement packets](#EN-US_TASK_0172361757__step_03) | A VRRP-enabled device checks the TTL value in every received VRRP Advertisement packet and discards a packet if its TTL value is not 255. However, if devices of different vendors are deployed on a network, checking TTL values in VRRP Advertisement packets may cause a device to incorrectly discard packets. To resolve this issue, disable the device from checking TTL values in VRRP Advertisement packets to implement interworking between different vendors' devices. |
| [Sending mode for VRRP Advertisement packets in VLANs](#EN-US_TASK_0172361757__step_04) | When a VRRP group is configured for a super VLAN on a device enabled with VLAN aggregation, VRRP Advertisement packets can be sent to a specified sub-VLAN or all sub-VLANs of the super VLAN. Sending VRRP Advertisement packets to a specified sub-VLAN can improve bandwidth usage efficiency. |
| [Specifying a mode that the master device uses to send gratuitous ARP packets](#EN-US_TASK_0172361757__step_05) | The master device sends gratuitous ARP packets to all VLAN users through its sub-interface for QinQ VLAN tag termination. After VLAN users attached to a switching device learn the virtual MAC address, they send packets through the master device. To reduce system burdens, enable the sub-interface for QinQ VLAN tag termination to send gratuitous ARP packets only with the first VLAN ID specified in the inner tag and each VLAN ID in the outer tag. |
| [Mode that the master device uses to send packets through a dot1q termination sub-interface](#EN-US_TASK_0172361757__step_06) | If VRRP is enabled on a dot1q termination sub-interface, VRRP packets are encapsulated with VLAN tags before being transmitted to VRRP devices in specific VLANs. |
| [Mode that the master device uses to send packets through a QinQ termination sub-interface](#EN-US_TASK_0172361757__step_07) | If VRRP is enabled on a QinQ termination sub-interface, VRRP packets are encapsulated with inner and outer VLAN tags before being transmitted to VRRP devices in specific VLANs. |



#### Procedure

* Configure a VRRP version number.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp version**](cmdqueryname=vrrp+version) { **v2** | **v3** }
     
     
     
     A VRRP version number for the device is set.
  3. Run either of the following commands:
     
     
     + To configure the device to send VRRP Advertisement packets of a specified version, run the [**vrrp version-3 send-packet-mode**](cmdqueryname=vrrp+version-3+send-packet-mode) { **v2-only** | **v3-only** | **v2v3-both** } command in the system view.
     + To configure the device's interface to send VRRP Advertisement packets of a specified version, run the [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **version-3 send-packet-mode** { **v2-only** | **v3-only** | **v2v3-both** } command in the view of the interface on which the VRRP group is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable a device to allow hosts to ping a virtual IP address.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp virtual-ip ping enable**](cmdqueryname=vrrp+virtual-ip+ping+enable)
     
     
     
     The ping to a virtual IP address is enabled.
     
     
     
     After the ping function is enabled, a device on an external network can ping a virtual IP address. This function exposes the device to ICMP attacks. The [**undo vrrp virtual-ip ping enable**](cmdqueryname=undo+vrrp+virtual-ip+ping+enable) command can be run to disable the ping function.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable passive ARP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**arp learning passive enable**](cmdqueryname=arp+learning+passive+enable)
     
     
     
     Passive ARP is enabled.
     
     After passive ARP is enabled, a backup device in a VRRP group learns ARP entries after receiving an ARP request packet sent to a virtual IP address. If a VRRP group performs a master/backup switchover, the new master device can take over without the need to relearn ARP entries, ensuring service continuity.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the interval at which the master device sends gratuitous ARP packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vrrp gratuitous-arp timeout**](cmdqueryname=vrrp+gratuitous-arp+timeout) *time*
     
     
     
     The interval at which the master device sends gratuitous ARP packets is set.
     
     
     
     After the interval at which gratuitous ARP packets are sent is set, the master device sends gratuitous ARP packets at the specified interval.
     
     To restore the default interval, run the [**undo vrrp gratuitous-arp timeout**](cmdqueryname=undo+vrrp+gratuitous-arp+timeout) command in the system view.
     
     To disable the master device from periodically sending gratuitous ARP packets, run the [**vrrp gratuitous-arp timeout disable**](cmdqueryname=vrrp+gratuitous-arp+timeout+disable) command in the system view. After that, the master can send gratuitous ARP packets only during a master/backup VRRP switchover.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable a device from checking TTL values in VRRP Advertisement packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  3. Run [**vrrp un-check ttl**](cmdqueryname=vrrp+un-check+ttl)
     
     
     
     The device is disabled from checking TTL values in VRRP Advertisement packets.
     
     
     
     To enable a device to check TTL values in received VRRP Advertisement packets, run the [**undo vrrp un-check ttl**](cmdqueryname=undo+vrrp+un-check+ttl) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the mode for sending VRRP Advertisement packets in VLANs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface vlanif**](cmdqueryname=interface+vlanif) *vlan-id*
     
     
     
     The VLANIF interface view is displayed.
  3. Run [**vrrp advertise send-mode**](cmdqueryname=vrrp+advertise+send-mode) { *sub-vlan-id* | **all** }
     
     
     
     The mode for sending VRRP Advertisement packets in VLANs is configured.
     
     
     
     + If *sub-vlan-id* is specified, VRRP Advertisement packets are sent to a specified sub-VLAN.
     + If **all** is specified, VRRP Advertisement packets are broadcast to all sub-VLANs of a super VLAN.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Specifying the parameter **all** is not recommended. If **all** is configured, a super VLAN broadcasts a VRRP Advertisement packet to all its sub-VLANs, reducing the CPU running efficiency.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Specify a mode that the master device uses to send gratuitous ARP packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  3. Run [**vrrp arp send-mode simple**](cmdqueryname=vrrp+arp+send-mode+simple)
     
     
     
     A mode is specified for the master device to send gratuitous ARP packets.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Specify a mode that the master device uses to send gratuitous ARP packets through a dot1q termination sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the dot1q termination sub-interface on which the VRRP group is configured is displayed.
  3. Run [**dot1q vrrp**](cmdqueryname=dot1q+vrrp) **vid** *vid*
     
     
     
     VRRP packets are sent to the VLAN with a specified ID.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Specify a mode that the master device uses to send packets through a QinQ termination sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the QinQ termination sub-interface on which the VRRP group is configured is displayed.
  3. Run [**qinq vrrp**](cmdqueryname=qinq+vrrp) **pe-vid** *pe-vid* **ce-vid** *ce-vid*
     
     
     
     VRRP packets with a specified inner VLAN ID and a specified outer VLAN ID are sent to VLANs.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The *pe-vid* and *ce-vid* parameters to be specified in the [**qinq vrrp**](cmdqueryname=qinq+vrrp) command are configured using the [**qinq termination pe-vid ce-vid**](cmdqueryname=qinq+termination+pe-vid+ce-vid) command.
     
     The system adds tags to VRRP packets based on the *pe-vid* and *ce-vid* values configured using the [**qinq vrrp**](cmdqueryname=qinq+vrrp) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.