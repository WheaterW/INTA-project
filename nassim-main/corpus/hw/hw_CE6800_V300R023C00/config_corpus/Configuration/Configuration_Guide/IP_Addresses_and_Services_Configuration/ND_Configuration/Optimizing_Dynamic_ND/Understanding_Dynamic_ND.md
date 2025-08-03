Understanding Dynamic ND
========================

Understanding Dynamic ND

#### Definition

Dynamic ND allows devices to dynamically learn and update the mapping between IPv6 and MAC addresses through ND messages. That is, you do not need to manually configure the mapping.


#### Related Concepts

Dynamic ND entries can be created, updated, and aged through ND messages.

* Creating and updating dynamic ND entriesUpon receipt of an ND message whose source IPv6 address is on the same network segment as the IPv6 address of the inbound interface, a device automatically creates or updates an ND entry if the message meets either of the following conditions:
  + The destination IPv6 address is the IPv6 address of the inbound interface.
  + The destination IPv6 address is the Virtual Router Redundancy Protocol (VRRP) virtual IPv6 address of the inbound interface.
* Aging dynamic ND entries
  
  After the aging timer of a dynamic ND entry on a device expires, the device sends ND aging probe messages to the peer device. In this case, if the device does not receive an ND reply message after sending a specified maximum number of aging probe messages, the dynamic ND entry is aged. Shutting down an interface triggers ND entries on the interface to be deleted.

To prevent ND probing from consuming a large amount of system resources, a device limits the rate of sending ND probe messages. That is, in high-specification scenarios, extended periods of time are needed from when ND probing starts to when ND entry aging is complete.


#### Application Scenarios

The dynamic ND aging mechanism ensures that ND entries unused during a specified period are automatically deleted. This mechanism helps save the storage space of ND tables and speed up ND table lookups.

Dynamic ND applies to networks with complex topologies and high real-time communication requirements. Dynamic ND entries are dynamically created and updated using ND messages. In this way, they do not need to be manually maintained, greatly reducing maintenance workload.

**Table 1** Dynamic ND aging mechanism
| Concept | Description | Scenario |
| --- | --- | --- |
| Aging probe mode | Before a dynamic ND entry on a device is aged, the device sends unicast or multicast ND aging probe messages to other devices. By default, unicast ND aging probe messages are sent. | * If the IPv6 address of the peer device remains unchanged but its MAC address changes frequently, it is recommended that you configure the local device to multicast ND aging probe messages. * If the MAC address of the peer device remains unchanged, network bandwidth resources are insufficient, and the aging time of ND entries is set to a small value, it is recommended that you configure the local device to unicast ND aging probe messages. |
| Aging time | Every dynamic ND entry has a lifecycle, which is also called aging time. If a dynamic ND entry is not updated after its lifecycle ends, this dynamic ND entry is deleted from the ND table. | Two interconnected devices can use ND to learn the mapping between their IPv6 and MAC addresses and save the mapping in their ND tables. Then, the two devices can communicate using the ND entries. When the peer device becomes faulty or its NIC is replaced but the local device does not receive any status change information about the peer device, the local device continues to send IPv6 datagrams to the peer device. As a result, network traffic is interrupted because the ND table of the local device is not promptly updated. To reduce the risk of network traffic interruptions, an aging timer can be set for each ND entry. After the aging timer of a dynamic ND entry expires, the entry is automatically deleted. |
| Maximum number of probes for aging dynamic ND entries | Before a dynamic ND entry is aged, a device sends ND aging probe messages to the peer device. If the device does not receive an ND reply message after sending a specified maximum number of aging probe messages, the dynamic ND entry is deleted. | The ND aging timer can help reduce the risk of network traffic interruptions that occur because an ND table is not updated quickly enough, but it cannot eliminate problems caused by delays. For example, if the aging time of a dynamic ND entry is N seconds, the local device can detect the status change of the peer device after N seconds. During this period, the ND table of the local device is not updated. You can set the maximum number of probes for aging dynamic ND entries to ensure that the ND table is updated in time in the preceding situation. |