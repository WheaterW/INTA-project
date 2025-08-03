Configuring the NAT ALG Function
================================

The NAT ALG function implements transparent translation for some application layer protocols.

#### Usage Scenario

Packets of many application layer protocols contain user information, including IP addresses and port numbers. These protocol packets may fail to be forwarded because NAT can only identify the IP addresses and port numbers in TCP/UDP headers of user traffic and cannot identify the IP addresses and port numbers carried in these protocol packets. For special protocols, such as FTP, the Data field in a packet contains IP address or port information. In this case, an inconsistency or errors occur because NAT does not take effect on an IP address or port information in the Data field of a packet. A good way to solve the NAT issue for these special protocols is to use the ALG function. Functioning as a special conversion agent for application protocols, the ALG interacts with the NAT device to establish states. The ALG uses NAT state information to change the specific data in the Data field of IP packets and to complete other necessary work, so that application protocols can run across internal and external networks.

NAT ALG supports the following application protocols: ICMP, UDP-based SIP, TCP-based RTSP, PPTP, DNS, and FTP.


#### Pre-configuration Tasks

Before configuring the NAT ALG function, complete the following tasks:

* Configure basic NAT functions.
* Configure the NAT conversion function.


[Enabling the NAT ALG Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0032.html)

Packets of some protocols, such as FTP and ICMP, contain IP addresses and port numbers in the Data field. To translate the IP addresses and port numbers contained in data, enable the NAT ALG function.

[Configuring the DNS Mapping Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0333.html)

The DNS mapping function enables users on an enterprise network to send packets carrying DNS domain names to access a DNS server on a public network.

[Verifying the NAT ALG Configurations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0034.html)

After configuring the NAT ALG function, you can view the configured NAT instance.