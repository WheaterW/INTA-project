Improving IS-IS Network Security
================================

On a network that requires high security, you can configure IS-IS authentication.

#### Usage Scenario

IS-IS authentication or optional checksum can improve IS-IS network security.

* IS-IS authentication encapsulates authentication information into Hello packets, Link State Protocol Data Units (LSPs), and Sequence Number Protocol Data Units (SNPs). After an IS-IS device receives the packets, it checks whether the encapsulated authentication information is correct. The IS-IS device only accepts the packets with correct authentication information. The authentication mechanism enhances IS-IS network security. IS-IS authentication consists of area authentication, routing domain authentication, and interface authentication.
  
  IS-IS authentication ensures that the data is correctly transmitted at the network layer.
* IS-IS optional checksum encapsulates checksum Type-Length-Values (TLVs) into SNPs and Hello packets. After an IS-IS device receives the packets, it checks whether the checksum TLVs are correct. The IS-IS device only accepts the packets with correct checksum TLVs. The authentication mechanism enhances IS-IS network security.
  
  IS-IS optional checksum ensures that the data is correctly transmitted at the link layer.


#### Pre-configuration Tasks

Before configuring IS-IS authentication, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html).
* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html).
* [Configure a keychain](dc_vrp_keychain_cfg_0005.html)


[Configuring IS-IS Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0117.html)

After IS-IS authentication is configured, authentication information can be encapsulated into LSPs, SNPs, or Hello packets to ensure packet transmission security.

[Configuring the Optional Checksum](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0118.html)

The optional checksum encapsulates optional checksum Type-Length-Values (TLVs) into SNPs and Hello packets. After an IS-IS device receives the packets, it checks whether the checksum TLVs are correct, which improves network security. 

[Verifying the Configuration of Improving IS-IS Network Security](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_0071.html)

After improving IS-IS network security, check the information about IS-IS neighbors to determine whether the IS-IS authentication succeeds.