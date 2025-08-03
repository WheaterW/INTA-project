ztp certificate-remote
======================

ztp certificate-remote

Function
--------



The **ztp certificate-remote** command configures the device to download a CA certificate from a bootstrap server.

The **undo ztp certificate-remote** command disables the device from downloading a CA certificate from a bootstrap server.



By default, a device is not configured to download a CA certificate from a bootstrap server.


Format
------

**ztp certificate-remote** { *ipv4-addr* | **ipv6** *ipv6-addr* } [ **vpn-instance** *vpnvalue* ] **port** *portvalue* **ssl-policy** *policyname* [ **verify-type** **esn** ]

**undo ztp certificate-remote** { *ipv4-addr* | **ipv6** *ipv6-addr* } [ **vpn-instance** *vpnvalue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6-addr* | IPv6 address of the bootstrap server. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpnvalue* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. \_public\_ cannot be used as the VPN instance name. |
| **port** *portvalue* | Port number of the bootstrap server. | The value is an integer ranging from 1 to 65535. |
| **ssl-policy** *policyname* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters, including letters, digits, and underscores (\_). It cannot contain spaces. |
| **verify-type** | Authentication type.  If this parameter is not specified, the IP address pair is used for authentication. | - |
| **esn** | Indicates that the authentication type is ESN. | - |
| **certificate-remote** *ipv4-addr* | IP address of the bootstrap server. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If NCE does not initialize a certificate, run the **ztp certificate-remote** command to enable the device to download a CA certificate from the BootStrap server. The certificate name is NCE-bootstrap.pem. During ZTP deployment, the CA certificate is used for certificate authentication and NETCONF connection establishment with NCE. Currently, NCE integrates the functions of the BootStrap server.A maximum of 10 BootStrap servers can be configured on the device. The BootStrap servers with the same IP address and VPN instance name are considered as one BootStrap server. The interaction process between the device and BootStrap server is as follows:

1. The device proactively establishes an HTTPS connection with the BootStrap server.
2. The device sends a request packet to the BootStrap server to download the CA certificate. The request packet carries the ESN of the device or the IP address of the BootStrap server. If verify-type esn is specified, the request packet carries the ESN of the device. If verify-type esn is not specified, the request packet carries the IP address of the BootStrap server.
3. The BootStrap server searches for the CA certificate based on the ESN or IP address in the request packet and sends a packet carrying the CA certificate to the device. The packet also carries the ESN of the device or the IP address of the BootStrap server.
4. After receiving the response packet from the BootStrap server, the device terminates the HTTPS connection with the BootStrap server, parses the response packet, and verifies the validity of the response packet. If verify-type esn is specified, the device uses the ESN for authentication when parsing the packet. If verify-type esn is not specified, the device uses the IP address of the BootStrap server for authentication when parsing the packet. If the verification fails, the CA certificate cannot be obtained. In this case, the system attempts to obtain the CA certificate from the next BootStrap server until the CA certificate is obtained successfully.

**Prerequisites**

You are advised to run the **ssl policy** command to create an SSL policy and run the **pki-domain default** command in the SSL policy view to bind the default domain to the SSL policy. If these commands are not preconfigured, run them before running the **ztp certificate-remote** command.

**Configuration Impact**

After this command is run, the device automatically imports the initial certificate of the device to the realm named default for establishing an HTTPS connection with the bootstrap server. After obtaining the CA certificate from the bootstrap server, the device disconnects the HTTPS connection with the bootstrap server and deletes the initial certificate of the device from the default realm.After successfully obtaining the CA certificate NCE-bootstrap.pem from the bootstrap server, the device automatically imports the certificate to the default realm.

**Precautions**

After NCE-bootstrap.pem is imported to the default domain, if you need to download the CA certificate from the BootStrap server again, delete the imported certificate from the default domain and run the **ztp certificate-remote** command again.


Example
-------

# Configure the device to download a CA certificate from the bootstrap server. Set the IP address of the bootstrap server to 10.1.1.1, port number to 30217, SSL policy name to ztp\_policy, and certificate authentication type to IP address.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ztp_policy
[*HUAWEI-ssl-policy-ztp_policy] pki-domain default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-ssl-policy-ztp_policy] quit
[*HUAWEI] ztp certificate-remote 10.1.1.1 port 30217 ssl-policy ztp_policy

```

# Configure the device to download a CA certificate from the bootstrap server. Set the IP address of the bootstrap server to 2001:db8:1::1, port number to 30217, SSL policy domain name to ztp\_policy, and certificate authentication type to ESN.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy ztp_policy
[*HUAWEI-ssl-policy-ztp_policy] pki-domain default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:y
[*HUAWEI-ssl-policy-ztp_policy] quit
[*HUAWEI] ztp certificate-remote ipv6 2001:db8:1::1 port 30217 ssl-policy ztp_policy verify-type esn

```