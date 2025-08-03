ARP Spoofing Attack
===================

ARP Spoofing Attack

#### Security Policies

ARP spoofing attack defense prevents devices from being attacked by bogus clients or gateways or by malformed ARP packets.

* Strict ARP learning
  
  The device learns the MAC addresses of only the ARP reply packets in response to the ARP request packets sent by itself. This prevents attacks that send ARP request packets and ARP reply packets that are not in response to the request packets that the device itself sends. Strict ARP learning effectively protects the network or devices from bogus clients or gateways.
* Validity check on ARP packets
  
  After receiving an ARP packet, the device checks whether the source and destination MAC addresses in the Ethernet header match those in the Data field of the packet. If they match, the device considers the packet valid and allows it to pass. If they do not match, the device considers the packet an attack packet and discards it. Validity check on ARP packets effectively protects the network or devices from malformed ARP packet attacks.


#### Attack Types

In ARP spoofing attacks, attackers send fake ARP packets to modify ARP entries on gateways or valid hosts. As a result, valid ARP packets cannot be transmitted.

* An attacker responds with a forged ARP reply packet to a client so that the client learns an incorrect gateway address.
* An attacker sends a forged ARP request packet to the gateway so that the gateway learns incorrect ARP entries.
* An attacker sends malformed ARP packets to a device so that the device learns incorrect ARP entries.


#### Configuration Guide

* **Configure strict ARP learning.**
  
  Strict ARP learning can be configured globally and in the interface view and takes effect as follows:
  + If strict ARP learning is configured globally and in the interface view, strict ARP learning configured in the interface view is adopted.
  + If strict ARP learning is not configured in the interface view, strict ARP learning configured globally is adopted.
  Enable strict ARP learning globally.
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] arp learning strict
  ```
  
  Enable strict ARP learning in the interface view.
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] interface gigabitethernet 0/2/3
  ```
  ```
  [~HUAWEI-GigabitEthernet0/2/3] arp learning strict force-enable
  ```
* **Configure validity check on ARP packets.**
  
  You can specify only source or destination MAC addresses or both source and destination MAC addresses to verify ARP packets. The check principles are as follows:
  + If **source-mac** is specified:
    
    - After receiving an ARP Request packet, an interface only checks whether the source MAC address in the Ethernet packet header is consistent with that in the Data field of the ARP packet.
    - After receiving an ARP Response packet, an interface only checks whether the source MAC address in the Ethernet packet header is consistent with that in the Data field of the ARP packet.
  + If **destination-mac** is specified:
    
    - After receiving an ARP Request packet, an interface does not check whether the destination MAC address in the Ethernet packet header is consistent with that in the Data field of the ARP packet because ARP packets are broadcast packets.
    - After receiving an ARP Response packet, an interface only checks whether the destination MAC address in the Ethernet packet header is consistent with that in the Data field of the ARP packet.
  + If both **source-mac** and **destination-mac** are specified:
    
    - After receiving an ARP Request packet, an interface only checks whether the source MAC address in the Ethernet packet header is consistent with that in the Data field of the ARP packet.
    - After receiving an ARP Response packet, an interface checks whether both the source MAC address and destination MAC address in the Ethernet packet header are respectively the same as those in the Data field of the ARP packet.
  Enable validity check on ARP packets in the interface view.
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] interface gigabitethernet 0/1/1
  ```
  ```
  [~HUAWEI-GigabitEthernet0/1/1] arp validate source-mac destination-mac
  ```

#### Configuration Suggestions

When static ARP is configured on a VLANIF interface, the downstream traffic cannot be forwarded if the user traffic is switched between member interfaces of a VLAN due to topology changes. Therefore, do not specify the outbound interface when configuring static ARP. The outbound interface can be learned by sending ARP packets.

The device can prevent ARP attacks by sending gratuitous ARP packets. However, services will be interrupted, affecting the service quality. If ARP attacks persist, manual intervention is required.

In some scenarios, a device has to learn multicast MAC addresses to generate ARP entries.


#### Verifying the Hardening Result

* Run the [**display arp learning strict**](cmdqueryname=display+arp+learning+strict) command to check the configuration of strict ARP learning.
* Run the [**display arp-limit**](cmdqueryname=display+arp-limit) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check the configuration of ARP entry limit.
* Run the [**display arp speed-limit**](cmdqueryname=display+arp+speed-limit) { **destination-ip** | **source-ip** } [ **slot** *slot-id* ] command to check the configuration of ARP packet rate limit.