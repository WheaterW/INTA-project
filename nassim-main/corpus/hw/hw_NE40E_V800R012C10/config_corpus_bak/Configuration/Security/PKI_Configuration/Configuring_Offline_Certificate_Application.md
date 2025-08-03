Configuring Offline Certificate Application
===========================================

Configuring offline certificate application includes configuring key pairs, configuring entity information, and obtaining certificates.

#### Usage Scenario

Two devices need to obtain each other's identity information during IPsec negotiation. The NE40E can use either a pre-shared key or certificate for identity authentication. If you use certificates for device identity authentication, configure the devices to obtain certificates before they perform IPsec negotiation.

The NE40E can obtain certificates in offline mode or CMPv2 mode. The offline mode is applicable when a new certificate needs to be applied for. In this mode, the device administrator places the request file in the floppy disk, CD-ROM, or email and sends the file to the CA administrator to apply for a certificate.


#### Pre-configuration Tasks

Before configuring offline certificate application, complete the following tasks:

* Assign an IP address to each interface.
* Configure routes for devices to interwork.


[Configuring a Key Pair](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_0004.html)

Before applying for and using a certificate, configure a key pair.

[Configuring Entity Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_0005.html)

When applying for certificates, an entity must add entity information to a certificate request file and send the file to a CA. The CA uses a piece of important information to describe an entity, and identifies the entity using a unique distinguished name (DN).

[Obtaining Certificates](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_0006.html)

To use certificates to authenticate users, an entity needs to obtain local and CA certificates. A local certificate proves the identity of the entity, and a CA certificate proves that the local certificate is issued by a legal CA.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_0008.html)

After configuring PKI certificates, you can check the configuration.