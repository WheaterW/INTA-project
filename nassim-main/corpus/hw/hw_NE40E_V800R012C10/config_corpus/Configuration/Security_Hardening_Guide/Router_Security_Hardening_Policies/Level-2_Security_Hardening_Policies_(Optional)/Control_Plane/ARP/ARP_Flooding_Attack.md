ARP Flooding Attack
===================

ARP Flooding Attack

#### Security Policies

ARP flooding attack defense is implemented by configuring ARP entry limit, ARP packet rate limit, and strict ARP learning.

* ARP entry limit
  
  The device limits the number of ARP entries that an interface can learn to prevent ARP entry overflow and improve ARP entry security.
* ARP packet rate limit
  
  The device counts the number of received ARP packets. If the number of ARP packets received in one second exceeds an upper limit, the device does not process the excess ARP packets. This function prevents ARP entry overflow.
* Strict ARP learning
  
  The device learns the MAC addresses of only the ARP reply packets in response to the ARP request packets sent by itself. This prevents attacks that send ARP request packets and ARP reply packets that are not in response to the request packets that the device itself sends.

Attacks by sending IP packets that cannot be parsed can be prevented by configuring the aging time of ARP fake entries. A devices stops parsing its received packets once the configured aging time of ARP faked entries expires, protecting the device from being attacked.

Memory exhaustion during ARP entry learning can be prevented by configuring the device to check the memory usage.


#### Attack Types

After receiving an IP packet in which the next-hop IP address has no matching ARP entry, the device will send an ARP request packet to learn the ARP entry. Attackers send a large number of packets whose destination IP addresses are unreachable to the device.

In this manner, the device is busy learning ARP entries, which exhausts system resources and even causes the device to restart.

* ARP request flood attack
  
  An attacker keeps sending to a device a large number of ARP request packets with fake source IP and MAC addresses, causing ARP entries on the device to overflow and the CPU usage of the device to increase. As a result, the device is paralyzed and cannot process valid ARP packets.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  As attackers keep sending ARP request packets with varied source IP or MAC addresses to target devices, target devices are busy responding to these ARP request packets and updating local ARP entries. ARP entries consume system resources. To reduce system resource consumption and improve ARP search efficiency, a network device or host generally restricts its ARP table size. Attackers exploit this rule and send excessive ARP packets with fake source IP addresses to have ARP entries on target devices overflow. In this case, the target devices cannot process valid ARP packets, causing communications to be interrupted in this DoS attack.
* ARP response flood attack
  
  An attacker keeps replying with ARP reply packets to update the mappings between the destination IP and MAC addresses in the ARP cache on target devices, causing interrupted communications on target devices.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A host on a subnet generally stores the mappings between the IP and MAC addresses of the subnet gateway (ARP entries) in its ARP cache. Attackers pretend to be the subnet gateway or a host on the subnet and broadcast an incorrect MAC address, causing all devices on the subnet to store the incorrect MAC address. As a result, devices on the subnet cannot communicate with the subnet gateway or host.

#### Configuration Guide

* **Configure the ARP entry limit.**
  
  A device limits the number of ARP entries that an interface can learn. The excess ARP entries cannot be added to the ARP entry table, preventing ARP entry overflow.
  
  Configure a limit for the number of ARP entries that a specified interface can learn.
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] interface gigabitethernet0/1/0
  ```
  ```
  [~HUAWEI-GigabitEthernet0/1/0] arp-limit maximum 20
  ```
* **Configure ARP packet rate limit.**
  
  A device limits the number of ARP packets that can be processed every second. The excess ARP entries will be discarded, preventing ARP entry overflow.
  
  An ARP packet rate can be limited based either on source IP addresses or destination IP addresses.
  + If [**source-ip**](cmdqueryname=source-ip) is specifies, the ARP packet rate is limited based on source IP addresses.
  + If [**destination-ip**](cmdqueryname=destination-ip) is specifies, the ARP packet rate is limited based on destination IP addresses.
  
  Configure an limit on the ARP packet rate to 50 pps based on destination IP addresses.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] arp speed-limit destination-ip maximum 50
  ```
* **Configure strict ARP learning.**
  
  Strict ARP learning can be configured globally and in the interface view and takes effect as follows:
  + If strict ARP learning is configured globally and in the interface view, only the function configured in the interface view takes effect.
  + If strict ARP learning is not configured in the interface view, the function configured globally takes effect.
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

Long aging time of ARP fake entries affects service convergence. Therefore, retaining the default aging time of ARP fake entries (5s) is recommended.

Configure the aging time of dynamic ARP fake entries on a specified interface to 10s.

```
<HUAWEI> system-view
```
```
[~HUAWEI] interface gigabitethernet0/1/0
```
```
[~HUAWEI-GigabitEthernet0/1/0] arp-fake expire-time 10
```

If the memory usage is so high that the traffic forwarding fails, check whether it caused by failure to learn ARP entries.


#### Configuration Suggestions

You can configure ARP entry limit, ARP packet rate limit, and strict ARP to prevent ARP flooding attacks. However, this may lead to a lower rate of learning ARP entries.

Long aging time of ARP fake entries affects service convergence. Therefore, retaining the default aging time of ARP fake entries (5s) is recommended.

If the memory usage is so high that the traffic forwarding fails, check whether it caused by failure to learn ARP entries.


#### Verifying the Hardening Result

* Run the [**display arp learning strict**](cmdqueryname=display+arp+learning+strict) command to check the configuration of strict ARP learning.
* Run the [**display arp-limit**](cmdqueryname=display+arp-limit) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check the configuration of ARP entry limit.
* Run the [**display arp speed-limit**](cmdqueryname=display+arp+speed-limit) { **destination-ip** | **source-ip** } [ **slot** *slot-id* ] command to check the configuration of ARP packet rate limit.