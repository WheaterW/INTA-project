Querying Security Configurations
================================

You can run commands to query security configurations in the system.

#### Context

Due to different security performance of protocols, some protocols used during configuration may have security risks. You can run the [**display security configuration**](cmdqueryname=display+security+configuration) command to check security configurations in the system.


#### Procedure

1. In the user view, run [**display security configuration**](cmdqueryname=display+security+configuration) [ **feature** *feature-name* ]
   
   
   
   Security configurations in the system are displayed.

#### Example

Run the [**display security configuration**](cmdqueryname=display+security+configuration) command to check the security configurations in the system. This example uses only some fields in the command output.

```
<HUAWEI> display security configuration
Feature Name  : FTPS
Security Item : ftp security configuration
Item content  : Ftp server is disabled.Ftp Ipv6 server is disabled.IP block feature is disabled.The FTP server does not bind all interface.

Feature Name  : TELNET
Security Item : telnet security configuration
Item content  : The Telnet server function is used.The TELNET server bind all interface.

Feature Name  : VTY
Security Item : Protocol used by VTY
Item content  : SSH
```