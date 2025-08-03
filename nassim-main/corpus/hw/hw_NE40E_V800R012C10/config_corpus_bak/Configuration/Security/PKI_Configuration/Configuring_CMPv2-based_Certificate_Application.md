Configuring CMPv2-based Certificate Application
===============================================

Configuring CMPv2-based certificate application involves creating public-private key pairs, configuring entity information, configuring CMP sessions, and obtaining certificates.

#### Usage Scenario

Two devices need to obtain each other's identity information during IPsec negotiation. The NE40E can use either a pre-shared key or certificate for identity authentication. If you use certificates for device identity authentication, configure the devices to obtain certificates before they perform IPsec negotiation.

The NE40E can obtain certificates in offline mode or CMPv2 mode. CMPv2 is recommended for obtaining and managing certificates on a network that has a large number of devices and supports CMPv2.


#### Pre-configuration Tasks

Before configuring CMPv2-based certificate application, complete the following tasks:

* Complete basic configurations for a CA server so that the CA server can automatically issue certificates.
* Check that external certificates have been preconfigured during initial authentication.


[Configuring a Key Pair](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_00041.html)

Before applying for and using a certificate, configure a key pair.

[Configuring Entity Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pki_cfg_0005a.html)

When applying for certificates, an entity must add entity information to a certificate request file and send the file to a CA. The CA uses a piece of important information to describe an entity, and identifies the entity using a unique distinguished name (DN).

[Configuring CMP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_cmp_0003.html)

To configure a CMP session, specify an RSA key pair, a CA server name, and PKI entity information used to obtain a certificate using CMPv2.

[Configuring CMPv2-based Certificate Application](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_cmp_0004.html)

CMPv2-based certificate application involves two types of CMP requests: initialization requests (IRs) and key update requests (KURs).

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_cmp_0005.html)

After configuring CMPv2-based certificate application, check the configuration.