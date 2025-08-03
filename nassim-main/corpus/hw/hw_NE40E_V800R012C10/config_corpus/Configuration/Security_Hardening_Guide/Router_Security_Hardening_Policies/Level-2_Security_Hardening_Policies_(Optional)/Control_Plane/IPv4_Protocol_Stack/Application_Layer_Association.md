Application Layer Association
=============================

Application Layer Association

#### Security Policy

The control plane is associated with the forwarding plane to control invalid packets, reduce attacks caused by device vulnerabilities, and ensure security on the control and forwarding planes. The control plane detects changes in protocols, centrally processes the characteristics of these changes, establishes a characteristics status table, and informs the forwarding plane of the changed status.

Protocol switch: Security policies can be configured on interfaces, boards, and an entire device. Packets for which the protocol switch is disabled are discarded or sent using very little bandwidth. This prevents exhaustion of CPU resources and ensures proper network operations.

Whitelist: A whitelist protects dynamic protocol sessions. Once a session is successfully established using TCP or UDP, the device dynamically sends a whitelist for this protocol and ensures that packets are sent reliably using sufficient bandwidth. The whitelist matching condition contains a 5-tuple, which includes the source IP address, destination IP address, source port ID, destination port ID, and protocol ID.

When processing protocol packets, the application layer association module first matches them against the whitelist. The packets matching the whitelist are sent at a high rate to the CPU. Then, the application layer association module matches common packets of an enabled protocol and then sends the matching packets to the CPU at a specified rate. If the protocol has not been configured, the system assigns the default minimum bandwidth to packets of this protocol.

Finally, policies can be set for the packets that do not match any whitelist or protocol so that packets are either discarded or sent at a specified low rate.


#### Attack Methods

In [Figure 1](#EN-US_CONCEPT_0000001180503115__fig_dc_vrp_sec_maintenance_002801), a device is connected to a large number of users. Additionally, several services (such as routing, HWTACACS, ICMP, IGMP, and MPLS) are enabled on the device, but these services do not need to be transmitted using Telnet. If an attacker sends an excessive number of Telnet requests, the device has to waste resources processing these requests. To prevent this risk, you can disable Telnet on the device. The device then assigns the default minimum bandwidth to Telnet packets, regardless of how many Telnet packets need to be processed. This implementation helps improve system security and prevent Telnet packets from consuming excessive resources.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After Telnet is disabled, you can run the corresponding command to enable the device to discard Telnet packets instead of assigning the default minimum bandwidth to Telnet packets. In this case, the device directly discards the Telnet attack packets.

For enabled services or protocols, the device can send packets at the specified rate. This protects the CPU from attacks and ensures proper network operations.

**Figure 1** Application layer association  
![](figure/en-us_image_0000001134623518.png)

#### Configuration and Maintenance Methods

Run the **application-apperceive default-action** { **drop** | **min-to-cp** } command to configure the default action for packets. The default action is taken when no matching application layer association policy is found.


#### Configuration and Maintenance Suggestions

Configuration and maintenance methods are irrelevant to configurations.


#### Verifying the Security Hardening Result

* Run the **display application-apperceive** [ **slot** *slot-id* ] command to check information about application layer association.
* Run the **display cpu-defend** **application-apperceive** **statistics** [ **slot** *slot-id* ] command to check information about the packets discarded by application layer association.