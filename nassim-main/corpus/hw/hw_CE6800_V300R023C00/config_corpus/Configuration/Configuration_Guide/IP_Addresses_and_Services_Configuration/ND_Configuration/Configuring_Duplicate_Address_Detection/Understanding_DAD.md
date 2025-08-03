Understanding DAD
=================

Understanding DAD

#### Definition

DAD checks whether an IPv6 unicast address is being used before the address is assigned to an interface. DAD is required if IPv6 addresses are configured automatically. An IPv6 unicast address that is assigned to an interface but not verified by DAD is called a tentative address. An interface cannot use such an address for unicast communication but will join two multicast groups: all-nodes multicast group and solicited-node multicast group.


#### Fundamentals

* DAD
  
  IPv6 DAD is similar to IPv4 gratuitous ARP. A node sends an NS message that requests the tentative address as the destination address to the solicited-node multicast group. If the node receives an NA message in response, another node is using the tentative address for communication. In this case, the node does not use the tentative address for communication.
  
  [Figure 1](#EN-US_CONCEPT_0000001176662039__fig1769043710131) shows a DAD example.
  
  **Figure 1** DAD example  
  ![](figure/en-us_image_0000001130782328.png)
  
  The IPv6 address FC00::1 is assigned to HostA as a tentative IPv6 address. To check the validity of this address, HostA sends an NS message containing the requested address FC00::1 to the solicited-node multicast group to which FC00::1 belongs. Because FC00::1 is not specified, the source address of the NS message is an unspecified address. After receiving the NS message, HostB processes the message as follows:
  
  + If FC00::1 is a tentative address of HostB, HostB does not use this address as an interface address, nor does it send an NA message.
  + If FC00::1 is in use on HostB, HostB sends an NA message to FF02::1 carrying the IP address FC00::1. In this way, HostA can find and mark the duplicate tentative address after receiving the message, and the address does not take effect on HostA.
* Address conflict self-recovery
  
  When DAD detects an address conflict on an interface, the IPv6 protocol status of the interface becomes down. The interface can go up only after being configured manually. To address this issue, deploy address conflict self-recovery. This function allows DAD to continue detection until the conflict is removed and the IPv6 protocol status of the interface becomes up. Address conflict self-recovery applies to the following scenarios:
  
  + A device receives an NA message after sending an NS message (common address conflict).
  + A device receives an NS message with the same target address but a different source MAC address from a peer device while sending an NS message.
  + A device receives an NS message with the same target address and source MAC address from a peer device while sending an NS message.
  
  [Figure 2](#EN-US_CONCEPT_0000001176662039__fig17924347164816) shows the principles of address conflict self-recovery in a common address conflict scenario. The principles of address conflict self-recovery in other scenarios are similar to those in a common address conflict scenario.
  
  **Figure 2** Network diagram of address conflict self-recovery  
  ![](figure/en-us_image_0000001130622548.png)
  
  At t1, HostA sends an NS message. After receiving an NA message from HostB, HostA continues to perform address conflict detection at t2 and send an NS message to HostB.
  
  + If HostB replies with an NA message, HostA continues to perform address conflict detection at the next time and send an NS message to HostB.
  + If HostB does not reply with an NA message, the address is available and HostA stops sending NS messages to HostB.