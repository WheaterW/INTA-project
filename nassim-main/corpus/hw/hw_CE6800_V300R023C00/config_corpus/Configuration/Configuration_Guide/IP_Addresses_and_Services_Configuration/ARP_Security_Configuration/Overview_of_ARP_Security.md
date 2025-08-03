Overview of ARP Security
========================

Overview of ARP Security

#### Definition

Address Resolution Protocol (ARP) security protects devices against attacks that tamper with or forge ARP messages, improving device and communication security.


#### Purpose

If two hosts need to communicate, the sender must know the network-layer IP address of the receiver. IP datagrams, however, must be encapsulated with media access control (MAC) addresses before they can be transmitted over the physical network. Therefore, ARP is needed to map IP addresses to MAC addresses to ensure the transmission of datagrams. ARP is easy to use but lacks security protection mechanisms. Attackers may use ARP to attack network devices. The following ARP attacks exist on networks:

* ARP spoofing attack
  
  Attackers send bogus ARP messages to modify ARP entries on gateways or valid hosts, interrupting the transmission of valid ARP messages. ARP anti-spoofing protects the device against ARP attacks, improving communication security and reliability, as described in [Table 1](#EN-US_CONCEPT_0000001176661631__table1617061210529).
  
  **Table 1** ARP anti-spoofing security solution
  | ARP Security Function | Description |
  | --- | --- |
  | ARP message validity check | After receiving an ARP message, a device checks whether the source and destination MAC addresses in the Ethernet header match those in the Data field of the message. If they are different, the device discards the ARP message. If no inconsistency is detected, the ARP message is accepted. |
  | Fixed ARP | After a device learns the ARP entry of a user, it does not update the ARP entry or only modifies some fields in the ARP entry when receiving ARP messages from other users. This ensures that valid ARP entries are not replaced by attackers using forged ARP messages. |
  | Dynamic ARP inspection | After dynamic ARP inspection (DAI) is enabled on a device, the device compares the source IP address, source MAC address, interface, and VLAN information in a received ARP message with DHCP snooping binding entries. If they match, the device considers the message valid and forwards it. If they do not match, the device considers the message invalid and discards it.  This function applies only to DHCP snooping scenarios. |
  | ARP gateway anti-collision | If an attacker forges the gateway IP address to send ARP messages to other user hosts on a LAN, the user hosts record incorrect gateway address mappings in their ARP tables. As a result, all traffic from the user hosts to the gateway is sent to the attacker and the attacker can intercept related data, causing network access failures of these user hosts. To defend against attacks from a bogus gateway, enable ARP gateway anti-collision on the gateway if user hosts are directly connected to the gateway. |
  | Strict ARP learning | A device learns the MAC addresses of only the ARP reply messages in response to the ARP request messages sent by itself. This prevents attacks initiated by ARP request messages and the ARP reply messages that are not in response to the request messages that the device itself sends. |
* ARP flood attack (denial of service)
  
  Attackers forge and send to a device excessive ARP request messages and gratuitous ARP messages with IP addresses that cannot be mapped to MAC addresses. As a result, the device's ARP buffer overflows, and the device is incapable of caching valid ARP entries. In this case, valid ARP messages cannot be transmitted. ARP anti-flood relieves CPU loads and prevents an ARP entry overflow, ensuring normal device running. [Table 2](#EN-US_CONCEPT_0000001176661631__table123833183539) describes the ARP anti-flood security solution.
  
  **Table 2** ARP anti-flood security solution
  | ARP Security Function | Description |
  | --- | --- |
  | ARP entry limiting | A device limits the number of ARP entries that an interface can learn to prevent an ARP entry overflow, improving ARP entry security. |
  | Rate limiting on ARP messages | A device counts the number of received ARP messages. If the number of ARP messages received in a specified period exceeds an upper limit, the device does not process the excess ARP messages. This function prevents an ARP entry overflow. |
  | Rate limiting on ARP Miss messages | A device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the limit, the device does not process excess ARP Miss messages, relieving the burden on the CPU. |