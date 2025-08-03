Understanding IPv6 IS-IS Authentication
=======================================

Understanding IPv6 IS-IS Authentication

#### Definition

IS-IS authentication is implemented based on an authentication field carried in IS-IS packets. After receiving IS-IS packets from a remote routing device, a local routing device accepts them only if they contain the same authentication password as the locally configured one. This mechanism protects the local routing device.


#### Related Concepts

[Table 1](#EN-US_CONCEPT_0000001130782424__table2685515181819) describes IS-IS authentication types.

**Table 1** Authentication types
| Authentication Type | Definition |
| --- | --- |
| Area authentication | Is configured in the IS-IS view to authenticate Level-1 CSNPs, PSNPs, and LSPs. |
| Routing domain authentication | Is configured in the IS-IS view to authenticate Level-2 CSNPs, PSNPs, and LSPs. |
| Interface authentication | Is configured in the interface view to authenticate Level-1 and Level-2 IIHs.  NOTE:  An interface can be configured to perform interface authentication in either of the following ways:   * The interface sends IIHs with the authentication TLV and verifies the authentication information in received IIHs. * The interface sends IIHs with the authentication TLV but does not verify the authentication information in received IIHs. |


![](public_sys-resources/note_3.0-en-us.png) 

For area authentication and routing domain authentication, you can configure a device to authenticate LSPs and SNPs separately in any of the following ways:

* The device sends LSPs and SNPs both with the authentication TLV and verifies the authentication information in received LSPs and SNPs.
* The device sends LSPs and SNPs both with the authentication TLV and verifies only the authentication information in received LSPs.
* The device sends LSPs with the authentication TLV and verifies the authentication information in received LSPs. The device sends SNPs without the authentication TLV and does not verify the authentication information in received SNPs.
* The device sends LSPs and SNPs both with the authentication TLV but does not verify the authentication information in received LSPs or SNPs.

Based on the authentication modes of packets, the authentication is classified into the following types:

* Simple authentication: A configured password is directly added to packets for authentication. This authentication mode is insecure.
* Message-digest algorithm 5 (MD5) authentication: A configured password is hashed using the MD5 algorithm, and the ciphertext password is added to packets for authentication. This authentication mode improves password security.
* Keychain authentication: It further improves network security with a configurable keychain that changes with time.
* HMAC-SHA256 authentication: A configured password is hashed using the HMAC-SHA256 algorithm, and the ciphertext password is added to packets for authentication. This authentication mode improves password security.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The simple authentication and MD5 authentication are insecure. You are therefore advised to use keychain or HMAC-SHA256 authentication.

#### Fundamentals of IPv6 IS-IS Authentication

IS-IS authentication is implemented based on an authentication field carried in IS-IS packets. When receiving IS-IS packets from a remote device, a local device discards them if they do not contain the same authentication password as the locally configured one. This mechanism protects the local device.

IS-IS authentication information is carried in a TLV, which is described as follows:

* Type: indicates the type of a packet, which is 1 byte. The value defined by ISO is 10, whereas the value defined by IP is 133.
* Length: indicates the length of the authentication TLV and is 1 byte.
* Value: indicates the authentication information, including the authentication type and password, and ranges from 1 to 254 bytes. [Table 2](#EN-US_CONCEPT_0000001130782424__table57921951504) describes different authentication type values.
  
  **Table 2** Authentication types
  | Authentication Type Value | Description |
  | --- | --- |
  | 0 | Reserved |
  | 1 | Simple authentication |
  | 3 | HMAC-SHA256 authentication |
  | 54 | MD5 authentication and keychain authentication |
  | 255 | Private routing domain authentication |

**Interface authentication**: Interfaces send IIHs with the authentication TLV and authenticate IIHs based on the local password. Interconnected interfaces must be configured with the same password.

**Area authentication**: All routing devices in an area must have the same authentication mode and keychain configured.

**Routing domain authentication**: All Level-2 and Level-1-2 routing devices in an IS-IS domain must have the same authentication mode and keychain configured.

![](public_sys-resources/note_3.0-en-us.png) 

When configuring IS-IS authentication, ensure that the authentication modes and passwords of all devices in the same area or routing domain are consistent so that IS-IS packets can be flooded normally.

An IS-IS neighbor relationship cannot be established if interface authentication fails. However, an IS-IS neighbor relationship can be established even if IS-IS area or routing domain authentication fails.

When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration script as a plaintext if you select the plaintext mode, which has a high risk. For security purposes, you are advised to change the password periodically.



For security purpose,you are not advised to use the weak security algorithm or weak security protocols provided by this feature. If you need to use the weak security algorithm or protocols, run the **install feature-software WEAKEA** command to install the weak security algorithm or protocol feature package WEAKEA. By default, the device provides the weak security algorithm or protocol feature package WEAKEA. For details about how to install or uninstall the feature package, see "Upgrade Maintenance Configuration" in Configuration Guide > System Management Configuration.

The following commands can be used only after the weak security algorithm/protocol feature package is installed.

| Command | Parameters Available Only After Feature Package Installation |
| --- | --- |
| [**area-authentication-mode**](cmdqueryname=area-authentication-mode) { **simple** { **plain** *simple-plain* | [ **cipher** ] *simple-cipher* } | **md5** { **plain** *plain* | [ **cipher** ] *cipher* } } [ **ip** | **osi** ] [ [ **snp-packet** { **send-only** | **authentication-avoid** } ] | **all-send-only** ] | **md5** |
| [**domain-authentication-mode**](cmdqueryname=domain-authentication-mode) { **simple** { **plain** *simple-plain* | [ **cipher** ] *simple-cipher* } | **md5** { **plain** *plain* | [ **cipher** ] *cipher* } } [ **ip** | **osi** ] [ [ **snp-packet** { **send-only** | **authentication-avoid** } ] | **all-send-only** ] | **md5** |
| [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) { **simple** { [ **cipher** ] *simple-cipher* | **plain** *simple-plain* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **ip** | **osi** ] [ **send-only** ] | **md5** |
| [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) { **simple** { [ **cipher** ] *simple-cipher* | **plain** *simple-plain* } | **md5** { [ **cipher** ] *cipher* | **plain** *plain* } } [ **level-1** | **level-2** ] [ **ip** | **osi** ] [ **send-only** ] | **md5** |