Understanding ARP Gateway Anti-Collision
========================================

Understanding ARP Gateway Anti-Collision

#### Fundamentals

As shown in [Figure 1](#EN-US_CONCEPT_0000001176661623__fig166881358496), attacker B forges the gateway (Device) address to send a bogus ARP message to HostA. HostA incorrectly considers the attacker Device and records an incorrect ARP entry for Device. As a result, Device cannot receive messages from HostA and their communication is interrupted.

**Figure 1** ARP gateway collision  
![](figure/en-us_image_0000001808086881.png "Click to enlarge")

To prevent bogus gateway attacks, enable ARP gateway anti-collision on Device. In addition, you can enable gratuitous ARP message sending on Device so that Device can broadcast correct gratuitous ARP messages to all user hosts. In this manner, the gateway address mappings recorded by the attacked user hosts can be corrected.