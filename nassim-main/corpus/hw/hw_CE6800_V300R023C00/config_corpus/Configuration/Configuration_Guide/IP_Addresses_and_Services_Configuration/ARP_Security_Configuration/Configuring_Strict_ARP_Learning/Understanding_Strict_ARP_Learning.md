Understanding Strict ARP Learning
=================================

Understanding Strict ARP Learning

#### Fundamentals

If strict ARP learning is not configured, a device processes ARP entries as follows:

* After receiving an ARP reply message in response to the ARP request message that the device itself sends, the device checks whether the source IP address in the message matches an ARP entry. If no matching entry exists, the device creates an ARP entry using the source IP address and MAC address carried in the message. If a matching entry exists, the device updates the entry based on the source IP address and MAC address carried in the message.
* After receiving an ARP request message, the device sends an ARP reply message and then creates an ARP entry.

If strict ARP learning is configured, a device processes ARP messages as follows:

* After receiving an ARP reply message, the device checks whether the message is in response to an ARP request message sent by itself. If so, the device learns and updates ARP entries. If not, the device does not learn or update ARP entries.
* After receiving an ARP request message, the device sends an ARP reply message but does not learn or update ARP entries.


#### Application Scenarios

If many user hosts simultaneously send a large number of ARP messages to a device, or attackers send bogus ARP messages to the device, the following issues occur:

* Processing ARP messages consumes many CPU resources. The device learns many invalid ARP entries, which exhausts ARP entry resources and prevents the device from learning ARP entries for ARP messages from authorized users. Consequently, communication of authorized users is interrupted.
* After receiving bogus ARP messages, the device incorrectly updates the ARP entries, resulting in user communicate failures.

To avoid the preceding issues, configure strict ARP learning on the device. After strict ARP learning is configured, the device learns only ARP entries for ARP reply messages in response to ARP request messages sent by itself. In this way, the device can defend against most ARP attacks.