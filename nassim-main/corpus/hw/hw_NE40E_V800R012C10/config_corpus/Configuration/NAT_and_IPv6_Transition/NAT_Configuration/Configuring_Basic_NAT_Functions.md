Configuring Basic NAT Functions
===============================

This section describes how to configure basic NAT functions.

#### Usage Scenario

Basic NAT function configurations are as follows:

* A NAT instance is bound to a NAT service board on a device. The device sends packets to the NAT service board for NAT processing.
* A public IPv4 address range in a NAT address pool can be assigned to a specific NAT instance so that the instance can translate IPv4 addresses between public and private networks.

Dedicated NAT and On-board NAT

NAT can be categorized into dedicated NAT and on-board NAT based on NAT service board types. Dedicated NAT provides better performance than on-board NAT and is more suitable for scenarios with a large number of NAT services.

* **Dedicated NAT**
  
  NAT is implemented by a dedicated service board without any interface, such as a VSUP-100. As this type of board does not provide any interface, it does not support direct service access. It performs NAT only when service packets are diverted to it. After NAT, the packets need to be forwarded to other interface boards before being forwarded to the next-hop device.
* **On-board NAT**
  
  NAT is implemented through the main control board equipped on a device. This type of board can directly access and forward services, and perform NAT for the service packets.


#### Prerequisites

Before you configure basic NAT functions, complete the following tasks:

* Verify that a service board is working properly.
* Run the [**license active**](cmdqueryname=license+active) **file-name** command to upload a NAT license when configuring dedicated NAT.
* Configure data link layer protocol parameters and IP addresses for interfaces so that the data link layer protocol on each interface can go Up.


[Enabling Dedicated NAT](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0121.html)

Using the VSUPA-100 board for NAT is also called dedicated NAT. NAT must be enabled on the board before NAT is performed.

[Creating a NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0011_atn.html)

This section describes how to create a NAT instance. The NAT instance implements NAT functions.

[Binding a Service Board to a NAT Instance](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0012.html)

Creating a NAT instance is a prerequisite for NAT. However, you need to bind the NAT instance to a board so that pre-NAT packets can be processed by the corresponding service board.

[Creating a NAT Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0013.html)

You can create a NAT address pool and bind it to a NAT instance to translate between private and public IPv4 addresses.

[Creating a CGN Global Address Pool](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0112_1.html)

Two types of CGN global address pools are available: static address pool and dynamic address pool. The difference between the two types of CGN global address pools is that the address segments in a dynamic global address pool require a CGN device to dynamically apply for address segments from a RADIUS server, whereas the address segments in a static global address pool are manually configured on a CGN device. A NAT instance dynamic address pool can apply for address segments from either a static or dynamic global address pool. A CGN global address pool supports both centralized and distributed CGN scenarios.

[(Optional) Configuring Port Allocation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0014_1.html)

Configuring a port allocation mode helps manage port resources.

[(Optional) Creating a NAT Policy Template](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0016_1.html)

Configure NAT policy templates so that NAT configuration policies can be issued by a RADIUS server.

[(Optional) Configuring the IP Address of the Next Hop to Which Packets Are Redirected](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0011.html)

This section describes how to configure the IP address of the next hop to which packets are redirected.

[Verifying the Configuration of Basic NAT Functions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0017.html)

After configuring basic NAT functions, verify the configuration.