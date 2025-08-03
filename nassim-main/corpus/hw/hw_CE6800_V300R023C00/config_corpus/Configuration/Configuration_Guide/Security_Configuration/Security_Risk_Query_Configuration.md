Security Risk Query Configuration
=================================

Security Risk Query Configuration

#### Context

Due to variations in security performance between protocols or between algorithms, some protocols may pose security risks. You can run the **security risk query** command to check security risks in the system and clear the risks based on the provided suggestions. For example, if SNMPv1 is configured, the **security risk query** command output will prompt for the use of SNMPv3.


#### Licensing Requirements

The security risk query function is not under license control.


#### Hardware Requirements

All products support the security risk query function.


#### Feature Requirements

None


#### Procedure

* In the user view, run the [**display security risk**](cmdqueryname=display+security+risk) [ [ **feature** *feature-name* ] | [ **level** *level-para* ] | [ **type** *type-para* ] ] \* command to query security risks in the system and suggested solutions for the risks.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  The security risks that can be queried vary with user levels. The system administrators can view all security risks in the system. Other users can only view the security risks matching their levels.
* In the user view, run the [**display security configuration**](cmdqueryname=display+security+configuration) [ **feature** *feature-name* ] command to query security configurations in the system.