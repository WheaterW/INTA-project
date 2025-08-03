MSTP
====

MSTP

#### Security Policy Introduction

* Root protection
  
  To address this issue, the root protection function can be configured to protect the root bridge by preserving the role of the designated port. With this function, when the designated port receives RST BPDUs with a higher priority, the port enters the Discarding state and does not forward the BPDUs. If the port does not receive any RST BPDUs with a higher priority for a certain period (double the Forward Delay), the port transitions to the Forwarding state.
* BPDU protection
  
  After BPDU protection is enabled on the device, the device shuts down the edge port if the edge port receives an RST BPDU, and notifies the NMS of the shutdown event. The attributes of the edge port are not changed.
* TC protection
  
  TC protection is used to suppress TC-BPDUs. The number of times that TC-BPDUs are processed by a device within a given time period is configurable. If the number of TC-BPDUs that the device receives within the given time exceeds the specified threshold, the device handles TC-BPDUs only for the specified number of times. Excessive TC-BPDUs are processed by the device as a whole for once after the timeout period expires. This protects the device from frequently deleting MAC entries and ARP entries, thus avoiding over-burden.
* Loop prevention
  
  The loop protection function can be used to prevent such network loops. If the root port or alternate port cannot receive RST BPDUs from the upstream device, the root port is blocked and the device notifies the NMS that the port enters the Discarding state. The blocked port remains in the Blocked state and no longer forwards packets. This prevents loops on the network. The root port restores the Forwarding state after new RST BPDUs are received.

#### Attack Methods

* Root bridge change attack
  
  Due to incorrect configurations or malicious attacks on the network, a root bridge may receive BPDUs with a higher priority. Consequently, the legitimate root bridge is no longer able to serve as the root bridge, and the network topology is illegitimately changed, triggering spanning tree recalculation. This may transfer traffic from high-speed links to low-speed links, causing traffic congestion.
* BPDU attack
  
  An edge port changes to be a non-edge port after receiving a BPDU, which triggers spanning tree recalculation. If an attacker keeps sending bogus BPDUs to a device, network flapping occurs.
* TC protection
  
  Generally, after receiving TC-BPDUs (packets for advertising network topology changes), a device needs to delete MAC entries and ARP entries. Frequent deletion operations will exhaust CPU resources.
* Loop prevention
  
  A root port or an alternate port will age if link congestion or a one-way link failure occurs. After the root port ages, a device may re-select a root port incorrectly and after the alternate port ages, the port enters the Forwarding state. Loops may occur in such a situation.

#### Configuration and Maintenance Suggestions

* Root protection
  
  Enable root protection on designated interfaces.
* BPDU protection
  
  Configure BPDU protection on devices.
* TC protection
  
  Configure TC protection on devices.
* Loop prevention
  
  Enable loop prevention on a root port or an alternate port.

#### Verifying the Security Hardening Result

* Run the **display stp** [ **instance** *instance-id* ][ **interface** { *interface-type interface-number* } ] [ **brief** ] command to check spanning-tree status and statistics.
* Run the **display stp region-configuration** command to check configurations of activated MST regions.
* Run the **display stp region-configuration** **digest** command to check the digest configurations of activated MST regions.