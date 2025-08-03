Configuring the SCP Server
==========================

This section describes how to configure the SCP server to establish a secure connection to the SCP client to implement secure remote access.

#### Context

SCP is a secure file transfer method based on SSH2.0. To use SCP to access other devices, configure user interfaces to support SSH.


#### Procedure

1. Configure VTY user interfaces to support SSH (for details, see [Configuring VTY User Interfaces to Support SSH](dc_vrp_basic_cfg_0039.html)).
2. Configure an SSH user (for details, see [Configuring an SSH User and Specifying a Service Type](dc_vrp_basic_cfg_0040.html)).
3. Perform the following operations as required:
   
   
   * To enable the IPv4 SCP service, run the [**scp server enable**](cmdqueryname=scp+server+enable) or [**scp ipv4 server enable**](cmdqueryname=scp+ipv4+server+enable) command.
   * To enable the IPv6 SCP service, run the [**scp server enable**](cmdqueryname=scp+server+enable) or [**scp ipv6 server enable**](cmdqueryname=scp+ipv6+server+enable) command.
4. (Optional) Run [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) *min-len*
   
   
   
   The minimum key length supported during Diffie-hellman-group-exchange key exchange with the SSH client is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the SSH client supports the Diffie-hellman-group-exchange key exchange algorithm with a length greater than 1024 bits, you are advised to run the [**ssh server dh-exchange min-len**](cmdqueryname=ssh+server+dh-exchange+min-len) command to set the minimum key length to 3072 bits to improve security.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.