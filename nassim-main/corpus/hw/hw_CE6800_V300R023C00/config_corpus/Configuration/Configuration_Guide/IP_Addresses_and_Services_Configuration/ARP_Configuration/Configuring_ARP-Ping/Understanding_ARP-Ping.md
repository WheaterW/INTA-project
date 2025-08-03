Understanding ARP-Ping
======================

Understanding ARP-Ping

#### ARP-Ping IP

Before configuring an IP address for a device, check whether the IP address is being used by sending ARP request or ICMP request messages. Generally, the ping operation can be used to check whether an IP address is being used. However, if a firewall is configured for the device using the IP address and the firewall is configured not to respond to ping messages, the IP address may be mistakenly considered available. To resolve this problem, configure ARP-Ping IP. ARP messages are Layer 2 protocol messages and, in most cases, can pass through a device that is configured not to respond to ping messages.

**Figure 1** ARP-Ping IP implementation  
![](figure/en-us_image_0000001130783866.png)

As shown in [Figure 1](#EN-US_CONCEPT_0000001130624046__fig1315213624212), DeviceA uses ARP-Ping IP to check whether the IP address 10.1.1.2 is being used. After DeviceA receives an ARP reply message from HostA with the IP address 10.1.1.2, DeviceA displays the MAC address of HostA along with a message indicating that the IP address is being used.

The ARP-Ping IP implementation process is as follows:

1. After IP address 10.1.1.2 is specified using a command on DeviceA, DeviceA broadcasts an ARP request message and starts a timer for ARP reply messages.
2. When HostA on the same LAN receives the ARP request message, it finds that the destination IP address in the message is the same as its own IP address and sends an ARP reply message to DeviceA.
3. When DeviceA receives the ARP reply message, it compares the source IP address in the message with the IP address specified in the command.
   * If the two IP addresses are the same, DeviceA displays the source MAC address in the ARP reply message along with a message indicating that the IP address is being used. In addition, DeviceA stops the timer for ARP reply messages.
   * If the two IP addresses are different, DeviceA discards the ARP reply message and displays a message indicating that the IP address is not being used by any host.
4. If DeviceA does not receive any ARP reply messages before the timer for ARP reply messages expires, it displays a message indicating that the IP address is not being used by any host.

#### ARP-Ping MAC

A host's MAC address is the fixed address of the NIC on the host. It does not usually need to be configured manually; however, there are exceptions. For example, if a device has multiple interfaces and the manufacturer does not specify MAC addresses for these interfaces, MAC addresses must be configured. In VRRP scenarios, a virtual MAC address must be configured for a VRRP group. Before configuring a MAC address, use ARP-Ping MAC to check whether the MAC address is being used.

**Figure 2** ARP-Ping MAC implementation  
![](figure/en-us_image_0000001176743527.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001130624046__fig538151217479), DeviceA uses ARP-Ping MAC to check whether the MAC address *XXXX-XXXX-XXXX* is being used. After receiving ICMP Echo reply messages from all hosts on the network, DeviceA displays the IP address of the host with the MAC address *XXXX-XXXX-XXXX* along with a message indicating that the MAC address is being used.

The ARP-Ping MAC implementation process is as follows:

1. After the MAC address *XXXX-XXXX-XXXX* is specified using a command on DeviceA, DeviceA broadcasts an ICMP Echo request message and starts a timer for ICMP Echo reply messages.
2. After receiving the ICMP Echo request message, all the other hosts on the same LAN send ICMP Echo reply messages to DeviceA.
3. After DeviceA receives an ICMP Echo reply message from a host, DeviceA compares the source MAC address in the message with the MAC address specified in the command.
   * If the two MAC addresses are the same, DeviceA displays the source IP address in the ICMP Echo reply message along with a message indicating that the MAC address is being used. In addition, DeviceA stops the timer for ICMP Echo reply messages.
   * If the two MAC addresses are different, DeviceA discards the ICMP Echo reply message and displays a message indicating that the MAC address is not being used by any host.
4. If DeviceA does not receive any ICMP Echo reply messages before the timer for ICMP Echo reply messages expires, it displays a message indicating that the MAC address is not being used by any host.

#### Application Scenarios

ARP-Ping applies to directly connected Ethernet LANs or Layer 2 Ethernet VPNs. ARP-Ping checks whether an IP or MAC address to be configured is being used, preventing address conflicts.