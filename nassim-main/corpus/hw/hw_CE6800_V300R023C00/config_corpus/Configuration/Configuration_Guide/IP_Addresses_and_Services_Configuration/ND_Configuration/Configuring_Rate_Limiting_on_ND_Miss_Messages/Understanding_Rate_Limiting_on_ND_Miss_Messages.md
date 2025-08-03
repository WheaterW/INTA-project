Understanding Rate Limiting on ND Miss Messages
===============================================

Understanding Rate Limiting on ND Miss Messages

#### Fundamentals

If a device is flooded with IPv6 packets that contain unresolvable destination IPv6 addresses, the device generates a large number of ND Miss messages. This is because the device has no ND entry that matches the next hop of the route. IPv6 packets, which trigger ND Miss messages, are sent to the CPU for processing. As a result, the device generates and delivers many temporary ND entries based on ND Miss messages, and sends a large number of NS messages to the destination network. This increases CPU usage of the device and consumes considerable bandwidth resources of the destination network. As shown in [Figure 1](#EN-US_CONCEPT_0000001176662061__fig947703695111), the attacker sends IPv6 packets with the unresolvable destination IPv6 address 2001:db8:1::2 /64 to the gateway (DeviceA).


**Figure 1** ND Miss attack  
![](figure/en-us_image_0000001176742013.png)

#### Application Scenarios

To avoid the preceding issues, the device can be configured to limit the rate of ND Miss messages in various scenarios, as described in [Table 1](#EN-US_CONCEPT_0000001176662061__table551051810303).

**Table 1** Scenarios for rate limiting on ND Miss messages
| Scenario | Description |
| --- | --- |
| Limiting the rate of ND Miss messages globally | If a device is flooded with IPv6 packets that contain unresolvable destination IPv6 addresses, the number of ND Miss messages to be processed on the device is limited. |
| Limiting the rate of ND Miss messages on an interface | If an interface is flooded with IPv6 packets that contain unresolvable destination IPv6 addresses, the number of ND Miss messages to be processed on the interface is limited. The configuration on an interface does not affect IPv6 packet forwarding on other interfaces. |