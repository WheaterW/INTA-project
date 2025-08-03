scp
===

scp

Function
--------



The **scp** command upload files to or download files from the SCP server.




Format
------

**scp** [ **-a** *source-ip-address* ] [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **public-net** | **vpn-instance** *vpn-instance-name* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** { *prefer-kex* } ] ] \* *source-filename* *destination-filename*

**scp ipv6** [ [ **vpn-instance** *vpn-instance-name* ] | **public-net** ] [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | [ [ **-a** *source-ipv6-address* ] | [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** { *prefer-kex* } ] ] \* *source-filename* *destination-filename*

**scp -i** { *interface-name* | *interface-type* *interface-number* } [ **-force-receive-pubkey** ] [ [ **-port** *server-port* ] | [ **identity-key** *identity-key-type* ] | [ **user-identity-key** *user-key* ] | **-r** | **-c** | [ **-cipher** *cipher* ] | [ **-prefer-kex** { *prefer-kex* } ] ] \* *source-filename* *destination-filename*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies the source IPv4 address. | The value is in dotted decimal notation. |
| **-a** *source-ipv6-address* | Specifies the source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **-force-receive-pubkey** | Indicates that a server forcibly receives public key authentication. | - |
| **-port** *server-port* | Specifies the port number of the remote SCP server. | The value is an integer ranging from 1 to 65535. The default value is 22. |
| **public-net** | Specifies the public network where the server resides. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name on the remote SCP server. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **identity-key** *identity-key-type* | Specifies a public key algorithm for server authentication. | Currently, RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, DSA, and ECC are supported. The default public key algorithms are RSA\_SHA2\_512 and RSA\_SHA2\_256.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits. Use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| **user-identity-key** *user-key* | Specifies a public key algorithm for user authentication. | Currently, RSA\_SHA2\_512, RSA\_SHA2\_256, RSA, DSA, and ECC are supported. The default public key algorithms are RSA\_SHA2\_512 and RSA\_SHA2\_256.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits. Use the more secure RSA SHA2-512 or RSA SHA2-256 authentication algorithm. |
| **-r** | Uploads or downloads files in batches. | - |
| **-c** | Enables compression. | - |
| **-cipher** *cipher* | Specifies an encryption algorithm for file upload or download. | Encryption algorithms supported depend on the ssh client cipher command settings. |
| **-prefer-kex** *prefer-kex* | Specifies the preferred key exchange algorithm. | The preferred key exchange algorithms supported depend on the algorithm type configured using the ssh client key-exchange command. |
| *source-filename* | Specifies the name of the source file to be uploaded or downloaded. | The value is a string of 1 to 256 case-sensitive characters without spaces. |
| *destination-filename* | Specifies the name of the destination file to uploaded or downloaded. | The value is a string of 1 to 256 case-sensitive characters without spaces. |
| **ipv6** | Specifies the IPv6 SCP. | - |
| **-oi** | Specifies the source interface for the IPv6 client, including the name, type and number of the interface. The IPv6 address configured in this interface view is the source IPv6 address of the packet. If no IPv6 address is configured for the source interface, the connection cannot be set up. | - |
| *interface-type* | Specifies the type the outbound interface. | - |
| *interface-number* | Specifies the number of the outbound interface. | - |
| **-i** *interface-name* | Specifies the name of the outbound interface. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

SCP is a secure file transfer method based on SSH2.0. Different from SFTP, SCP supports batch file upload or download.

* If a VPN instance name is specified, the SCP client logs in to the SCP server in the specified VPN instance.
* To enhance security, use -a to configure a loopback address as the source IP address or use -i to configure a loopback interface as the outbound interface.
* If -r is specified, you can use the wildcard (\*) to upload or download files in batches, for example, *.txt or huawei.*.
* If -c is specified, files are compressed before being transferred. File compression may take a long time and affect the file transfer rate. Therefore, compression is not recommended.Files on the SCP server are in the format of username@hostname:[ path ] [ filename ].
* username is the user name for logging in to the SCP server.
* hostname is the name or IP address of the SCP server.
* path is the working directory on the SCP server.
* filename is the name of a file.If filename and path are not specified, the system uploads files to the root directory of the working directory on the SCP server. If filename is specified, the system uploads files to the SCP server If hostname is an IPv6 address, the IPv6 address must be included in square brackets ([ ]), for example, john@[2001:db8:1::1]:.
* If the destination host address is an IPv6 link-local address, the local outbound interface must be specified.
* If the destination file has the same name as an existing directory, the source file is copied to the specified directory and the name of the newly generated file is the same as the source file name. If the destination file has the same name as an existing file, the system prompts you to replace the existing file and names each file with filename. If path is specified but filename is not specified, the system uploads files to the specified path on the SCP server.

**Prerequisites**

A VPN instance has been configured.The SCP service function has been enabled using the **scp server enable** command.

**Precautions**

* If a source IP address or a source interface is not specified, the system uses the source IP address or source interface specified in the **scp client-source** command.
* If a source IP address or source interface has been specified, the system does not use the source IP address or source interface specified in the **scp client-source** command.
* If a source IP address has been specified and VPN instance name is not specified, then the system uses Global VPN If it is configured else uses public vpn.
* in the source-filename and destination-filename fields, specifying the full file directory names as command keywords is recommended. If you specify the file names as command keywords, the command fails to be run because the command keywords are the same as the file names.

Example
-------

# Use aes256\_ctr to encrypt the file license.txt, and use port 1026 to upload the file to the working directory on the remote SCP server. The SCP client and SCP server belong to the same VPN instance vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] scp -a 10.1.1.1 -port 1026 vpn-instance vpn1 -cipher aes256_ctr license.txt john@10.10.10.1:
Trying 10.10.10.1 ...
Press CTRL+K to abort
Connected to 10.10.10.1 ...
Enter password:
license.txt                       100%     38529827Bytes          165Kb/s

```