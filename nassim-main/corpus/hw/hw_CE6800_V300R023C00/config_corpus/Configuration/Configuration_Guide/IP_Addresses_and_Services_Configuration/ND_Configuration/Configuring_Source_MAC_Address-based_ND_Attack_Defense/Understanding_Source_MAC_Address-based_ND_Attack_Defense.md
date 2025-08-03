Understanding Source MAC Address-based ND Attack Defense
========================================================

Understanding Source MAC Address-based ND Attack Defense

#### Context

ND has powerful functions. However, if there is no security mechanism, attackers may use ND to attack network devices. As shown in [Figure 1](#EN-US_CONCEPT_0000001176741953__fig539983713414), HostB can simulate a user to send a large number of ND messages to other devices, causing Device to be attacked.

**Figure 1** Network diagram of ND attack defense  
![](figure/en-us_image_0000001176662085.png)

#### Attack Detection for ND Messages with Fixed Source MAC Addresses

The system collects statistics about ND messages sent to the CPU based on the source MAC addresses of the messages. If the number of ND messages with the same source MAC address received within 5 seconds exceeds a specified threshold, the system considers that an attack has occurred and adds the MAC address to an attack entry. Before the attack entry ages out, the system performs the following operations based on a configured detection mode:

* If the detection mode is set to filter, the system generates log information and filters out ND messages sent from the source MAC address.
* If the detection mode is set to monitor, the system generates only log information and does not filter out ND messages sent from the source MAC address.

After a configured aging time expires, the ND attack entries with fixed source MAC addresses are aged out. Some important servers may send a large number of ND messages. To prevent these messages from being filtered out, configure the MAC addresses of the servers as protected ones.


#### MAC Address Check for ND

To improve network reliability, configure the system to proactively check source MAC address consistency for four types of ICMPv6 messages. The check rules are as follows:

* NS: The system checks whether the source MAC address is the same as the MAC address in the Source Link-Layer Address (SLLA) option. If not, the NS message is discarded.
* NA: The system checks whether the source MAC address is the same as the MAC address in the Target Link-layer Address (TLLA) option. If not, the NA message is discarded.
* RS: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RS message is discarded.
* RA: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RA message is discarded.

#### Benefits

Source MAC address-based ND attack defense improves network reliability and prevents ND attack messages with source MAC addresses from consuming CPU resources, protecting other services.