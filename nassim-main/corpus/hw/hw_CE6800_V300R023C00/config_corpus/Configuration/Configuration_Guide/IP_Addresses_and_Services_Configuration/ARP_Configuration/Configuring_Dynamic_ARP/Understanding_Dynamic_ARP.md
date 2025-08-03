Understanding Dynamic ARP
=========================

Understanding Dynamic ARP

#### Definition

Dynamic ARP allows devices to dynamically learn and update the mapping between IP and MAC addresses through ARP messages. That is, you do not need to manually configure the mapping.


#### Creating and Updating Dynamic ARP Entries

When an ARP message received by a device meets either of the following conditions:

* If the source IP address of the ARP message is on the same network segment as the IP address of the inbound interface, the device automatically creates or updates an ARP entry.
* If the received ARP message is a gratuitous ARP message:
  + If the source IP address of the gratuitous ARP message is the same as the local IP address, the device periodically sends a gratuitous ARP reply message to notify the IP address conflict until the conflict is removed.
  + If the gratuitous ARP message is received on the VLANIF or VBDIF interface and its source IP address is different from the local IP address but they belong to the same network segment, the device learns and updates the ARP entry based on the received gratuitous ARP message. In other cases, the device does not learn an ARP entry after receiving a gratuitous ARP message.

#### Aging Dynamic ARP Entries

After the aging timer of a dynamic ARP entry on a device expires, the device sends ARP aging probe messages to the peer device. In this case, if the device does not receive an ARP reply message after sending a specified maximum number of aging probe messages, the dynamic ARP entry is aged. To prevent ARP probing from consuming a large amount of system resources, a device can limit the rate of sending ARP probe messages. Shutting down an interface triggers ARP entries on the interface to be deleted.

**Table 1** Dynamic ARP aging mechanism
| Concept | Description | Scenario |
| --- | --- | --- |
| Aging time | Every dynamic ARP entry has a lifecycle, which is also called aging time. If a dynamic ARP entry is not updated after its lifecycle ends, this dynamic ARP entry is deleted from the ARP table. | Two interconnected devices can use ARP to learn the mapping between their IP and MAC addresses and save the mapping in their ARP tables. Then, the two devices can communicate using the ARP entries. When the peer device becomes faulty or its NIC is replaced but the local device does not receive any status change information about the peer device, the local device continues to send IP datagrams to the peer device. As a result, network traffic is interrupted because the ARP table of the local device is not promptly updated. To reduce the risk of network traffic interruptions, an aging timer can be set for each ARP entry. After the aging timer of a dynamic ARP entry expires, the entry is automatically deleted. |
| Aging probe mode | Before a dynamic ARP entry on a device is aged, the device sends ARP aging probe messages to other devices on the same network segment. An ARP aging probe message can be a unicast or broadcast message. By default, broadcast ARP aging probe messages are sent. | If the IP address of the peer device remains unchanged but its MAC address changes frequently, it is recommended that you configure the local device to broadcast ARP aging probe messages. If the MAC address of the peer device remains unchanged, network bandwidth resources are insufficient, and the aging time of ARP entries is set to a small value, it is recommended that you configure the local device to unicast ARP aging probe messages. |
| Number of probes for aging dynamic ARP entries | Before a dynamic ARP entry is aged out, a device sends ARP aging probe messages to the peer device. If the device does not receive an ARP reply message after sending a specified maximum number of aging probe messages, the dynamic ARP entry is deleted. | The ARP aging timer can help reduce the risk of network traffic interruptions that occur because an ARP table is not updated quickly enough, but it cannot eliminate problems caused by delays. For example, if the aging time of a dynamic ARP entry is N seconds, the local device can detect the status change of the peer device after N seconds. During this period, the ARP table of the local device is not updated. You can set the number of probes for aging dynamic ARP entries to ensure that the ARP table is updated in time in the preceding situation. |



#### Application Scenarios

The dynamic ARP aging mechanism ensures that ARP entries unused during a specified period are automatically deleted. This mechanism helps save the storage space of ARP tables and speed up ARP table lookups. Dynamic ARP applies to networks with complex topologies and high real-time communication requirements.