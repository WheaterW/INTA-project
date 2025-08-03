Understanding Dynamic ARP Inspection
====================================

Understanding Dynamic ARP Inspection

#### Fundamentals

Networks are susceptible to various ARP attacks. A common ARP spoofing attack is a man-in-the-middle (MITM) attack.

In an MITM attack, an attacker establishes separate connections with two communication ends and exchanges data between them. The two communication ends consider that they are communicating directly with each other, when in fact the entire session is controlled by the attacker. For example, in this attack, the attacker intercepts â and potentially alters â messages exchanged between the two communication ends.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001207477320__fig18625142813017), the attacker poses as UserB to send a bogus ARP message to UserA, which records an incorrect ARP entry for UserB. In this way, the attacker can obtain data exchanged between UserA and UserB, compromising the security of data exchanged between them.

**Figure 1** MITM attack  
![](figure/en-us_image_0000001251877283.png)

To defend against MITM attacks, deploy dynamic ARP inspection (DAI) on the device. When enabled with DAI, the device compares the source IP address, source MAC address, interface, and VLAN information in a received ARP message with DHCP snooping binding entries. If they match, the device considers the message valid and forwards it. If they do not match, the device considers the message invalid and discards it.

![](public_sys-resources/note_3.0-en-us.png) 

DAI applies only to DHCP snooping scenarios. The device enabled with DHCP snooping automatically generates DHCP snooping binding entries when DHCP users go online. For users with static IP addresses, the device does not generate DHCP snooping binding entries. In this case, you need to manually add static binding entries. For details about DHCP snooping, see the fundamentals of DHCP snooping.

If the attacker sends bogus ARP messages to the device enabled with DAI, the device detects the attack based on the binding entries and discards these messages. If the alarm function for ARP messages discarded by DAI is also enabled on the device, the device generates an alarm when the number of discarded ARP messages exceeds the alarm threshold.