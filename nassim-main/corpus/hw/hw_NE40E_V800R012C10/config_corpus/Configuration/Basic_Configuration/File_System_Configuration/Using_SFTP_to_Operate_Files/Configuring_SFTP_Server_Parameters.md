Configuring SFTP Server Parameters
==================================

You can configure a device to support the SSH protocol of earlier versions, configure or change the listening port number of an SFTP server, and set an interval at which key pairs are updated.

#### Context

[Table 1](#EN-US_TASK_0172359931__tab_dc_vrp_vfm_cfg_001801) describes SSH server parameters.

**Table 1** SSH server parameters
| SFTP Server Parameter | Description |
| --- | --- |
| Listening port number of an SFTP server | If the standard port is used as the listening port of the SFTP server, attackers may continuously access this port, consuming a large amount of bandwidth and deteriorating server performance. As a result, authorized users may fail to access the server. After the listening port number of the SFTP server is changed, attackers do not know the new listening port number, which prevents attackers from accessing the listening port and improves security. |
| Interval at which key pairs are updated | After an interval is set, key pairs are updated at the configured interval to improve security. |
| Timeout period for SSH authentication | If a user fails to log in when the timeout period for SSH authentication expires, the system disconnects the current connection to ensure system security. |
| Maximum number of clients that can be connected to the server | If the specified maximum number is less than the number of clients that are being connected to the server, the logged-in users will not be forced offline, and the server no longer accepts new connection requests. |
| ACL for the SSH server | An ACL on the SSH server specifies the clients that can access the SSH server running IPv6. This configuration prevents unauthorized users from accessing the SSH server, ensuring data security. |
| Keepalive feature | After this feature is enabled, the SSH server returns keepalive responses to an SSH client to check whether the connection between them is normal, facilitating fast fault detection. |
| Timeout period for disconnecting an SFTP client from the SFTP server | If the idle time of a connection exceeds a configured timeout period, the system automatically ends the connection to prevent users who do not perform any operations from occupying connection resources for a long time. |
| Source interface of an SSH server | After the source interface is specified, the system only allows SFTP users to log in to the SSH server through the source interface. SFTP users logging in through other interfaces are denied. |
| Bogus-list mode of SSH server authentication | Disabling the bogus-list mode of SSH server authentication reduces the authentication duration for some SFTP users to log in to the server in password authentication mode. |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform one or more operations described in [Table 2](#EN-US_TASK_0172359931__tab_dc_vrp_vfm_cfg_001802).
   
   
   
   **Table 2** Configurations of SFTP server parameters
   | Item | Operation |
   | --- | --- |
   | (Optional) Enable compatibility with earlier SSH versions. | Run the [**ssh server compatible-ssh1x enable**](cmdqueryname=ssh+server+compatible-ssh1x+enable) command.  NOTE:  If the SSH server is enabled to be compatible with earlier SSH versions, the system prompts a security risk. |
   | (Optional) Configure a listening port number for the SFTP server. | Run the [**ssh server port**](cmdqueryname=ssh+server+port) *port-number* command.  If a new listening port number is set, the SFTP server terminates all established connections before using the new port number to listen for connection requests. |
   | (Optional) Configure the interval at which key pairs are updated. | Run the [**ssh server rekey-interval**](cmdqueryname=ssh+server+rekey-interval) *hours* command. |
   | (Optional) Configure the timeout period for SSH authentication. | Run the [**ssh server timeout**](cmdqueryname=ssh+server+timeout) *seconds* command. |
   | (Optional) Configure the maximum number of clients that can be connected to the SSH server. | Run the [**sftp max-sessions**](cmdqueryname=sftp+max-sessions) *max-session-count* command.  If the maximum number is changed to a value less than the number of login users, login users' connections are retained but new access requests are rejected. |
   | (Optional) Configure an ACL for the SSH server. | Run the [**ssh [ ipv6 ] server acl**](cmdqueryname=ssh+%5B+ipv6+%5D+server+acl) { *acl-number* | *acl6-name* } command. |
   | (Optional) Enable the keepalive feature on the SSH server. | Run the [**ssh server keepalive enable**](cmdqueryname=ssh+server+keepalive+enable) command. |
   | (Optional) Configure a timeout period for disconnecting an SFTP client from the SFTP server. | Run the [**sftp idle-timeout**](cmdqueryname=sftp+idle-timeout) *minutes* [ *seconds* ] command.  You can run the [**sftp idle-timeout**](cmdqueryname=sftp+idle-timeout) **0** **0** command to disable the function of disconnecting the client from the SFTP server in case of timeout. |
   | Specify the source interface or source address for the SSH server. | * Run the [**ssh server-source**](cmdqueryname=ssh+server-source) **-i** { *interface-type* *interface-number* | *interface-name* } command to specify the source interface for the SSH server. * Run the [**ssh server-source**](cmdqueryname=ssh+server-source) **all-interface** command to allow any interface on the SSH server as its source interface. * Run the [**ssh ipv6 server-source**](cmdqueryname=ssh+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ] command to specify a source IPv6 address for the SSH server. * Run the [**ssh ipv6 server-source**](cmdqueryname=ssh+ipv6+server-source) **all-interface** command to allow any IPv6 interface on the SSH server as its source interface. * Run the [**ssh server-source**](cmdqueryname=ssh+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ip-address* command to specify a source IPv4 interface for the SSH server and set the interface isolation attribute for the SSH server. * Run the [**ssh ipv6 server-source**](cmdqueryname=ssh+ipv6+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ipv6-address* command to specify a source IPv6 interface for the SSH server and set the interface isolation attribute for the SSH server. NOTE:  After the **all-interface** parameter is configured, users can log in to the SSH server through all valid interfaces, which increases system security risks. Therefore, you are advised to cancel this configuration.  After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded. |
   | (Optional) Configure the bogus-list mode of SSH server authentication. | Run the [**ssh server authentication-method bogus-list disable**](cmdqueryname=ssh+server+authentication-method+bogus-list+disable) command. |
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.