Protocol Security Risks
=======================

Protocol Security Risks

#### Context

Protocols have different security performances, and some protocols may have security risks. Run the [**display security risk**](cmdqueryname=display+security+risk) command to identify security risks in the system. Then clear the security risks according to the repair action in the command output. For example, if SNMPv1 is configured, the [**display security risk**](cmdqueryname=display+security+risk) command output will prompt for the use of SNMPv3.


#### Procedure

1. Run [**display security risk**](cmdqueryname=display+security+risk) [ [ **feature** *feature-name* ] | [ **level** *level-para* ] | [ **type** *type-para* ] ]\*
   
   
   
   Security risks in the system and suggested solutions are displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The security risks that are displayed vary with user levels. The system administrators can view all security risks in the system. Other users can only view the security risks whose level is lower than or equal to their levels.

#### Verifying the Security Hardening Result

Run the [**display security risk**](cmdqueryname=display+security+risk) command to view security risks in the system.