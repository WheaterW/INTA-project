Checking Security Risks
=======================

You can check security risks in the system and eliminate them based on the provided suggestions.

#### Context

Due to variations in security performance between protocols, some protocols may pose security risks. You can run the [**display security risk**](cmdqueryname=display+security+risk) command to check security risks in the system and eliminate the risks based on the provided suggestions. For example, SNMPv1 is insecure. If this protocol is configured, the command output will prompt you to use SNMPv3.


#### Procedure

1. Run the [**display security risk**](cmdqueryname=display+security+risk) [ [ **feature** *feature-name* ] | [ **level** *level-para* ] | [ **type** *type-para* ] ]\* command in the user view to check security risks in the system and corresponding suggestions for eliminating the risks.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The security risks that can be queried vary with user levels. Administrators can view all security risks in the system, whereas other users can only view the security risks of or below their levels.

#### Example

Run the [**display security risk**](cmdqueryname=display+security+risk) command to check security risks in the system.

```
<HUAWEI> display security risk
Risk level       : high    
Feature name     : SNMP
Risk Type        : insecure-protocol
Risk information : SNMP V1/V2c is enabled.
Repair action    : Disable SNMP V1/V2c and enable SNMP V3 only. 

Risk Level       : medium 
Feature Name     : FTPS
Risk Type        : insecure-protocol
Risk Information : FTP is not a secure protocol. 
Repair Action    : It is recommended to use SFTP.
```