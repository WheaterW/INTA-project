About This Document
===================

About_This_Document

#### Purpose

This document provides the basic concepts, configuration procedures, and configuration examples in different application scenarios of the value-added services feature.


#### Licensing Requirements

For details about the License, see the License Guide.

* Enterprise users: [License Usage Guide](https://support.huawei.com/enterprise/en/doc/EDOC1100194032)


#### Related Version

The following table lists the product version related to this document.

| Product Name | Version |
| --- | --- |
| HUAWEI NE40E-M2 series | V800R023C00SPC500 |
| iMaster NCE-IP | V100R023C00SPC100 |



#### Intended Audience

This document is intended for:

* Data configuration engineers
* Commissioning engineers
* Network monitoring engineers
* System maintenance engineers

#### Security Declaration

* Notice on Limited Command Permission
  
  The documentation describes commands when you use Huawei devices and make network deployment and maintenance. The interfaces and commands for production, manufacturing, repair for returned products are not described here.
  
  If some advanced commands and compatible commands for engineering or fault location are incorrectly used, exceptions may occur or services may be interrupted. It is recommended that the advanced commands be used by engineers with high rights. If necessary, you can apply to Huawei for the permissions to use advanced commands.

* Encryption algorithm declaration
  
  The encryption algorithms DES/3DES/RSA (with a key length of less than 3072 bits)/MD5 (in digital signature scenarios and password encryption)/SHA1 (in digital signature scenarios) have a low security, which may bring security risks. If protocols allowed, using more secure encryption algorithms, such as AES/RSA (with a key length of at least 3072 bits)/SHA2/HMAC-SHA2 is recommended.
  
  For security purposes, insecure protocols Telnet, FTP, and TFTP as well as weak security algorithms in BGP, LDP, PCEP, MSDP, DCN, TCP-AO, MSTP, VRRP, E-Trunk, AAA, IPsec, BFD, QX, SSH, SNMP, IS-IS, RIP, SSL, NTP, OSPF, and keychain features are not recommended. To use such weak security algorithms, run the undo crypto weak-algorithm disable command to enable the weak security algorithm function.  For details, see the Configuration Guide.
* Password configuration declaration
  
  + When the password encryption mode is cipher, avoid setting both the start and end characters of a password to "%^%#". This causes the password to be displayed directly in the configuration file.
  + To further improve device security, periodically change the password.
* MAC addresses and Public IP addresses Declaration
  + For purposes of introducing features and giving configuration examples, the MAC addresses and public IP addresses of real devices are used in the product documentation. Unless otherwise specified, these addresses are used as examples only.
  + Open-source and third-party software may contain public addresses (including public IP addresses, public URLs/domain names, and email addresses), but this product does not use these public addresses. This complies with industry practices and open-source software usage specifications.
  + For purposes of implementing functions and features, the device uses the following public IP addresses:
    
    **Table 1** Public IP Address List
    | Public IP address | Description |
    | --- | --- |
    | http://www.huawei.com | Huawei official website address |
    | support\_e@huawei.com | Huawei Enterprise User Service Mailbox |
* Personal data declaration
  + Your purchased products, services, or features may use users' some personal data during service operation or fault locating. You must define user privacy policies in compliance with local laws and take proper measures to fully protect personal data.
  + When discarding, recycling, or reusing a device, back up or delete data on the device as required to prevent data leakage. If you need support, contact after-sales technical support personnel.
* Preset Certificate Usage Declaration
  
  Huawei certificates preset on Huawei devices during production are mandatory identity credentials for Huawei devices. The usage declarations of preset certificates are as follows:
  
  + Huawei preset certificates are used only to establish initial security channels for devices to connect to the customer network and to connect devices in the deployment phase. Huawei does not promise or guarantee the security of preset certificates.
  + The customer shall handle the security risks and security events caused by using Huawei preset certificates as service certificates and be responsible for the consequences.
  + Huawei preset certificates expire from 2041. You can run the **display pki cert\_list domain default** command to check the actual validity period.
  + After a preset certificate expires, services using the certificate are interrupted.
  + It is recommended that customers deploy the PKI system to issue certificates for devices and software on the live network and manage the lifecycle of the certificates. To ensure security, certificates with short validity periods are recommended.
  + The Huawei PKI root certificate is used for initial configuration and connection of Huawei products during network access. You are advised to disable this certificate after completing the network access configuration and configuring a CA certificate you have obtained for the products. (This certificate can be re-enabled if a new Huawei device needs to be verified for network access.) If you do not disable this certificate, security risks exist and you should be liable for the consequences caused by related security events.
* Product Lifecycle
  
  Huawei's regulations on product lifecycle are subject to the *Product End of Life Policy*. For details about this policy, visit the following web page: <https://support.huawei.com/ecolumnsweb/en/warranty-policy>
* Vulnerability
  
  Huawei's regulations on product vulnerability management are subject to the *Vul. Response Process*. For details about this process, visit the following web page: <https://www.huawei.com/en/psirt/vul-response-process>
  
  For vulnerability information, enterprise customers can visit the following web page: <https://securitybulletin.huawei.com/enterprise/en/security-advisory>
* Huawei Enterprise End User License Agreement
  
  This agreement is the end user license agreement between you (an individual, company, or any other entity) and Huawei for the use of the Huawei Software. Your use of the Huawei Software will be deemed as your acceptance of the terms mentioned in this agreement. For details about this agreement, visit the following web page: <https://e.huawei.com/en/about/eula>
* Lifecycle of Product Documentation
  
  Huawei after-sales user documentation is subject to the *Product Documentation Lifecycle Policy*. For details about this policy, visit the following web page: <https://support.huawei.com/enterprise/en/bulletins-website/ENEWS2000017761>
* Rights and Responsibilities of Initial Digital Certificates on Huawei Devices
  
  The initial digital certificates delivered with Huawei devices are subject to *Rights and Responsibilities of Initial Digital Certificates on Huawei Devices*. For details about this document, visit <https://support.huawei.com/enterprise/en/bulletins-service/ENEWS2000015789>.
* Device Upgrade and Patch Installation Declaration
  
  When upgrading or installing a patch on a device, use the software digital signature (OpenPGP) verification tool to verify the software. To prevent software from being tampered with or replaced, you are advised to perform this operation.
* Feature declaration
  
  + The NetStream feature may be used to analyze the communication information of terminal customers for network traffic statistics and management purposes. Before enabling the NetStream feature, ensure that it is performed within the boundaries permitted by applicable laws and regulations. Effective measures must be taken to ensure that information is securely protected.
  + The mirroring feature may be used to analyze the communication information of terminal customers for a maintenance purpose. Before enabling the mirroring function, ensure that it is performed within the boundaries permitted by applicable laws and regulations. Effective measures must be taken to ensure that information is securely protected.
  + The packet header obtaining feature may be used to collect or store some communication information about specific customers for transmission fault and error detection purposes. Huawei cannot offer services to collect or store this information unilaterally. Before enabling the function, ensure that it is performed within the boundaries permitted by applicable laws and regulations. Effective measures must be taken to ensure that information is securely protected.
  + The remote mirroring, and lawful interception features are restricted by the contract signed between the customer and Huawei. These features may not be purchased or used by you. The documents related to these features are confidential information and are not provided in this documentation. To purchase or use these features, contact Huawei engineers to obtain *Remotemirrior*, and *Lawful Interception**.*
* Reliability design declaration
  
  Network planning and site design must comply with reliability design principles and provide device- and solution-level protection. Device-level protection includes planning principles of dual-network and inter-board dual-link to avoid single point or single link of failure. Solution-level protection refers to a fast convergence mechanism, such as FRR and VRRP. If solution-level protection is used, ensure that the primary and backup paths do not share links or transmission devices. Otherwise, solution-level protection may fail to take effect.


#### Special Declaration

* This document package contains information about the NE40E. For details about hardware, such as devices or boards sold in a specific country/region, see Hardware Description.
* This document serves only as a guide. The content is written based on device information gathered under lab conditions. The content provided by this document is intended to be taken as general guidance, and does not cover all scenarios. The content provided by this document may be different from the information on user device interfaces due to factors such as version upgrades and differences in device models, board restrictions, and configuration files. The actual user device information takes precedence over the content provided by this document. The preceding differences are beyond the scope of this document.
* The maximum values provided in this document are obtained in specific lab environments (for example, only a certain type of board or protocol is configured on a tested device). The actually obtained maximum values may be different from the maximum values provided in this document due to factors such as differences in hardware configurations and carried services.
* Interface numbers used in this document are examples. Use the existing interface numbers on devices for configuration.
* The pictures of hardware in this document are for reference only.
* The supported boards are described in the document. Whether a customization requirement can be met is subject to the information provided at the pre-sales interface.
* In this document, public IP addresses may be used in feature introduction and configuration examples and are for reference only unless otherwise specified.
* The configuration precautions described in this document may not accurately reflect all scenarios.
* Log Reference and Alarm Reference respectively describe the logs and alarms for which a trigger mechanism is available. The actual logs and alarms that the product can generate depend on the types of services it supports.
* All device dimensions described in this document are designed dimensions and do not include dimension tolerances. In the process of component manufacturing, the actual size is deviated due to factors such as processing or measurement.


#### Symbol Conventions

The symbols that may be found in this document are defined as follows.

| Symbol | Description |
| --- | --- |
|  | Indicates a hazard with a high level of risk which, if not avoided, will result in death or serious injury. |
|  | Indicates a hazard with a medium level of risk which, if not avoided, could result in death or serious injury. |
|  | Indicates a hazard with a low level of risk which, if not avoided, could result in minor or moderate injury. |
|  | Indicates a potentially hazardous situation which, if not avoided, could result in equipment damage, data loss, performance deterioration, or unanticipated results.  NOTICE is used to address practices not related to personal injury. |
|  | Supplements the important information in the main text.  NOTE is used to address information not related to personal injury, equipment damage, and environment deterioration. |



#### Command Conventions

The command conventions that may be found in this document are defined as follows.

| Convention | Description |
| --- | --- |
| **Boldface** | The keywords of a command line are in **boldface**. |
| *Italic* | Command arguments are in *italics*. |
| [ ] | Items (keywords or arguments) in brackets [ ] are optional. |
| { x | y | ... } | Optional items are grouped in braces and separated by vertical bars. One item is selected. |
| [ x | y | ... ] | Optional items are grouped in brackets and separated by vertical bars. One item is selected or no item is selected. |
| { x | y | ... }\* | Optional items are grouped in braces and separated by vertical bars. A minimum of one item or a maximum of all items can be selected. |
| [ x | y | ... ]\* | Optional items are grouped in brackets and separated by vertical bars. Several items or no item can be selected. |
| &<1-n> | The parameter before the & sign can be repeated 1 to n times. |
| # | A line starting with the # sign is comments. |



#### Change History

Changes between document issues are cumulative. The latest document issue contains all the changes made in earlier issues.

| Product Version | Issue | Release Date |
| --- | --- | --- |
| V800R023C00SPC500 | 08 | 2025-02-15 |
| V800R023C00SPC500 | 07 | 2024-11-15 |
| V800R023C00SPC500 | 06 | 2024-09-15 |
| V800R023C00SPC500 | 05 | 2024-07-15 |
| V800R023C00SPC500 | 04 | 2024-05-15 |
| V800R023C00SPC500 | 03 | 2024-03-15 |
| V800R023C00SPC500 | 02 | 2023-12-31 |
| V800R023C00SPC500 | 01 | 2023-09-30 |