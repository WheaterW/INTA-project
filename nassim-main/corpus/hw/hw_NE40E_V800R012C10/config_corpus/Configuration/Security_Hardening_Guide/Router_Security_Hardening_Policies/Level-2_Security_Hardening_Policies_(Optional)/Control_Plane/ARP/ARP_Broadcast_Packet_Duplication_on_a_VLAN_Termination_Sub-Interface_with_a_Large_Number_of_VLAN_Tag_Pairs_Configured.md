ARP Broadcast Packet Duplication on a VLAN Termination Sub-Interface with a Large Number of VLAN Tag Pairs Configured
=====================================================================================================================

ARP Broadcast Packet Duplication on a VLAN Termination Sub-Interface with a Large Number of VLAN Tag Pairs Configured

#### Security Policy

* Sending packets to specified VLANs of users who get online through a DHCP relay agent
  
  A DHCP relay agent stores VLAN information of online users. When online users exist and a VLAN tag termination sub-interface receives ARP Miss packets, the DHCP relay agent broadcasts ARP Request packets only within specified user VLANs.
* Incremental step value and maximum aging time of fake entries on VLAN tag termination sub-interfaces with a large number of VLAN tag pairs configured
  
  More than 4000 VLAN tag pairs are configured on a VLAN tag termination sub-interface. Upon receipt of ARP Miss packets, the sub-interface keeps broadcasting ARP Request packets, triggering the generation of fake entries. The aging time increases by 15s each time fake entries are generated, and the maximum aging time is 3 minutes.
* Rate at which packets are sent by a board
  
  If more than 64 VLAN tag pairs are configured on a VLAN tag termination sub-interface, the sub-interface sends complete VLAN information in several ARP broadcast packets to the hardware abstraction layer (HAL) module for replication. The rate at which packets are sent can be set on a board. The maximum rate is 30000 packets per second.

#### Attack Methods

After a large number of VLAN tag pairs are configured on a Layer 3 termination sub-interface, IP traffic keeps being sent to cause the sub-interface to broadcast ARP Request packets. ARP broadcast packets are replicated and sent to VLANs identified by all VLAN tag pairs that are configured on the sub-interface. Each packet may be replicated tens of thousands of times (depending on the number of VLAN tag pairs configured on the sub-interface).

When ARP broadcast packets are duplicated, a huge number of CPU resources are consumed, adversely affecting the other services.


#### Configuration and Maintenance Methods

Set the rate at which ARP packets are sent.

The rate at which ARP packets are sent is set globally. The default rate is 500 pps. After the rate is set, excess packets are cached before being sent.
```
<HUAWEI> system-view
```
```
[~HUAWEI] arp broadcast-send maximum 500 
```


#### Configuration and Maintenance Suggestions

If a device has a large number of VLAN tag pairs configured on a VLAN tag termination sub-interface, you can adjust the rate at which ARP packets are broadcast based on CPU usage. Run the **arp pads** command to query statistics about packets discarded after the buffer is full of packets to be sent.


#### Verifying the Security Hardening Result

Run the [**display arp**](cmdqueryname=display+arp) command to check ARP entries.