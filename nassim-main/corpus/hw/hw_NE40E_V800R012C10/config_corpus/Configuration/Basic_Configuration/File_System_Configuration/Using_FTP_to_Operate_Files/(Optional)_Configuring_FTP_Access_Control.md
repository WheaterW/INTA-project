(Optional) Configuring FTP Access Control
=========================================

An ACL can be configured to allow only specified clients to access an FTP server.

#### Context

When a device functions as an FTP server, you can configure an ACL to allow only the clients that meet the rules specified in the ACL to access the FTP server.

Perform the following steps on the device that functions as an FTP server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) *acl-number*
   
   
   
   The ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
   
   
   
   A rule is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**ftp**](cmdqueryname=ftp) [ [**ipv6**](cmdqueryname=ipv6) ] [**acl**](cmdqueryname=acl) { *acl-number* | *name* }
   
   
   
   An FTP ACL is configured.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.