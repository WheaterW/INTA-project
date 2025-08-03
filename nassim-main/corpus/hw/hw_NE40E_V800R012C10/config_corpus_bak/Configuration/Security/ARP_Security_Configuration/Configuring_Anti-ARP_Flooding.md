Configuring Anti-ARP Flooding
=============================

Anti-ARP Flooding functions relieve CPU load and prevent an ARP entry overflow, ensuring normal network operation.

#### Usage Scenario

Attackers forge and send to a device excessive ARP request messages and gratuitous ARP messages with IP addresses that cannot be mapped to MAC addresses. As a result, the device's ARP buffer overflows, and the device is incapable of caching valid ARP entries. In this case, valid ARP messages cannot be transmitted.

The ARP anti-flooding function can effectively reduce the CPU load and prevent ARP entry overflow, ensuring the normal running of network devices.


#### Pre-configuration Tasks

Before configuring anti-ARP flooding, complete the following tasks:

* Configure the physical parameters for the interface and ensure that the physical layer status of the interface is Up.
* Configure the link layer parameters for the interface and ensure that the link layer protocol status of the interface is Up.


[Restricting Dynamic ARP Entry Learning](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0020.html)

When a large number of ARP entries are generated on a specified interface, you can prevent the interface to dynamically learn ARP entries.

[Strict ARP Learning](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0004.html)

Strict Address Resolution Protocol (ARP) learning enabled allows the device to learn the media access control (MAC) addresses of only the ARP reply packets in response to the ARP request packets sent by itself. Therefore, this function prevents attacks caused by sending ARP request packets and ARP reply packets that are not in response to the request packets that the device itself sends.

[ARP Entry Limit](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0010.html)

After Address Resolution Protocol (ARP) entry limit is enabled, the device limits the number of ARP entries that an interface can learn, to prevent ARP entry overflow and improve ARP entry security.

[Configuring an ARP Packet Rate Limit](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0011.html)

If a device receives excessive Address Resolution Protocol (ARP) packets in a short period, the device becomes busy learning entries and replying to the ARP packets, which can interrupt the processing of other services. To resolve this problem, configure an ARP packet rate limit on the device.

[Configuring an ARP Miss Message Rate Limit](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0012_1.html)



[(Optional) Enabling the Device to Record Logs and Generate Alarms About Potential Attacks](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0022.html)

To locate and resolve potential attacks, you can enable the device to record logs and generate alarms about potential attacks.

[Disabling Gratuitous ARP Packet Sending](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0023_1.html)

You can disable an interface from sending gratuitous ARP packets to prevent CPU overload.

[Configuring Gratuitous ARP Packet Discarding](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0013_1.html)

After gratuitous Address Resolution Protocol (ARP) packet discarding is configured, the device discards all received gratuitous ARP packets to prevent excessive CPU consumption.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp-sec_cfg_0014.html)

This section describes how to verify the configuration of anti-ARP flooding.