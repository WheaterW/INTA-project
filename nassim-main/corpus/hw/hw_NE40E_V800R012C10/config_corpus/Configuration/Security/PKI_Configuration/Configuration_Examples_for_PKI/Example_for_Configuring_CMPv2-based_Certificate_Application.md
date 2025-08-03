Example for Configuring CMPv2-based Certificate Application
===========================================================

This section provides an example for applying for certificates in CMPv2 mode and configuring automatic certificate update.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001836667822__fig1), configure CMPv2-based certificate application from the CA server for authenticating the identity of DeviceA.

**Figure 1** Network diagram of CMPv2-based certificate application  
![](images/fig_dc_vrp_pki_cfg_001401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Apply for CA and local certificates in offline mode and import them to the local device.
2. Create a public-private key pair.
3. Configure entity information.
4. Configure a CMP session.
5. Configure CMPv2-based certificate application, import generated certificates, and configure automatic update.

#### Data Preparation

To complete the configuration, you need the following data:

* Local and CA certificates obtained in offline mode
* Entity information, PKI domain, and certificate download mode

#### Procedure

1. Configure offline certificate application. For details, see [Example for Configuring Offline Certificate Application](dc_vrp_pki_cfg_0017.html). Obtain the local certificate (for example, **huaweitest.pem**) and CA certificates (for example, **HUAWEITESTCA.pem** and **HUAWEITESTCA2.pem**). Then, import the certificates.
   
   
   ```
   <DeviceA> system-view
   [~DeviceA] pki import-certificate local filename huaweitest.pem
   [~DeviceA] pki import-certificate ca filename HUAWEITESTCA.pem
   [~DeviceA] pki import-certificate ca filename HUAWEITESTCA2.pem
   ```
2. Create an RSA key pair used for CMPv2-based certificate application.
   
   
   ```
   [~DeviceA] rsa pki local-key-pair cmpsession create
   [*DeviceA] commit
   ```
3. Configure entity information used for CMPv2-based certificate application.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   During entity information configuration, you must configure a common entity name. Determine whether to configure other attributes based on the certificate issuing policy on the CA server. If the attributes used to filter certificates do not match the certificate issuing policy, certificate application may fail.
   
   
   
   ```
   [~DeviceA] pki entity huaweitest
   [*DeviceA--pkientity-huaweitest] common-name huaweitest
   [*DeviceA--pkientity-huaweitest] quit
   [*DeviceA] commit
   ```
4. Configure a CMP session.
   
   
   ```
   [~DeviceA] pki domain huaweitest
   [*DeviceA-pki-domain-huaweitest] pki cmp session huaweitest
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request ca-name "/CN=HUAWEITEST-CA2"
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request authentication-cert huaweitest.pem
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request  entity huaweitest
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request server url http://192.0.2.1:8080//ejbca/publicweb/cmp/HUAWEITEST-CA
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request rsa local-key-pair cmpsession regenerate 4096
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] commit
   [~DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] quit
   [~DeviceA-pki-domain-huaweitest] quit
   ```
5. Configure the local device to send an initialization request to apply for certificates.
   
   
   ```
   [~DeviceA] pki domain huaweitest
   [~DeviceA-pki-domain-huaweitest] pki cmp initial-request
   [~DeviceA-pki-domain-huaweitest] quit
   [*DeviceA] commit
   ```
6. Delete the original certificate files (local certificate **huaweitest.pem** and CA certificates **HUAWEITESTCA.pem** and **HUAWEITESTCA2.pem**), and import the newly downloaded local certificate **huaweitest\_ir.cer** and CA certificates **huaweitest\_ca0.cer** and **huaweitest\_ca1.cer**.
   
   
   ```
   [~DeviceA] pki delete-certificate local filename huaweitest.pem
   [~DeviceA] pki delete-certificate ca filename HUAWEITESTCA.pem
   [~DeviceA] pki delete-certificate ca filename HUAWEITESTCA2.pem
   [~DeviceA] pki import-certificate local filename huaweitest_ir.cer
   [~DeviceA] pki import-certificate ca filename huaweitest_ca0.cer 
   [~DeviceA] pki import-certificate ca filename huaweitest_ca1.cer
   ```
7. Configure the certificates used for identity authentication in the CMP request and enable automatic certificate update.
   
   
   ```
   [~DeviceA] pki domain huaweitest
   [~DeviceA-pki-domain-huaweitest] pki cmp session huaweitest
   [~DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] undo cmp request authentication-cert
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] cmp request authentication-cert huaweitest_ir.cer
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] certificate auto-update enable
   [*DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] commit
   [~DeviceA-pki-domain-huaweitest-pki-cmp-session-huaweitest] quit
   [~DeviceA-pki-domain-huaweitest] quit
   ```

#### Configuration Files

DeviceA configuration file

```
#
 sysname DeviceA  
#
pki entity huaweitest
 common-name huaweitest
#
pki domain huaweitest
 pki cmp session huaweitest
  cmp request ca-name "/CN=HUAWEITEST-CA2"
  cmp request authentication-cert huaweitest.pem
  cmp request entity huaweitest
  cmp request server url http://192.0.2.1:8080//ejbca/publicweb/cmp/HUAWEITEST-CA
  cmp request rsa local-key-pair cmpsession regenerate 4096
  cmp request authentication-cert huaweitest_ir.cer
  certificate auto-update enable
#
return
```