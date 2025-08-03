load configuration replace
==========================

load configuration replace

Function
--------



The **load configuration replace** command loads the configuration file on a local or remote server to replace the running configuration on the current device.




Format
------

**load configuration file** *filename* **replace** [ **relative** ]

**load configuration server** *ip-address* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **ftp** | **sftp** } **username** *user-name* **password** *password* **file** *filename* **replace** [ **relative** ]

**load configuration server ipv6** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **ftp** | **sftp** } **username** *user-name* **password** *password* **file** *filename* **replace** [ **relative** ]

**load configuration server http url** *url-address* [ **vpn-instance** *vpn-instance-name* ] [ **file** *filename* ] **replace** [ **relative** ]

**load configuration server** *ip-address* [ **vpn-instance** *vpn-instance-name* ] **transport-type** **sftp** **file** *filename* **replace** [ **relative** ] **username** *user-name* **password**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **relative** | Specifies that only configurations in the current view are replaced. | - |
| **server** *ip-address* | Specifies the IPv4 address of the remote server. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **transport-type** | Specifies a file transfer mode. | - |
| **ftp** | Transfers files through FTP. | - |
| **sftp** | Transfers files through SFTP. | - |
| **username** *user-name* | Specifies the user name of a remote server. | The value is a string of 1 to 64 case-sensitive characters, spaces and question marks not supported. |
| **password** *password* | Specifies the password of a remote server. | The value is a string of case-sensitive characters, including letters and digits. The string can contain spaces if it is enclosed in double quotation marks ("). A simple password is a string of 1 to 255 characters, while a ciphertext password is a string of 20 to 432 characters. |
| **file** *filename* | Specifies the name of the configuration file to be loaded. | The value is a string of case-sensitive characters. The value can contain uppercase letters, lowercase letters, digits, and special characters, but cannot contain spaces. The value is a string of 1 to 128 characters (including the suffix).  The following special characters are not allowed: ~ ? \* / \ : " | < > [ ] ; & $ ` !. The first and last characters cannot be periods (.).  The file name extension must be .cfg, .zip, .dat, .bat, .txt, or the text file does not contain the file name extension. In FTP or SFTP mode, the file name can contain the server directory name. The file name cannot contain the following special characters: ~ ? \* / \ : " | < > [ ] ; & $ ` !. |
| **ipv6** *ipv6-address* | Specifies the IPv6 address of a remote server. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **http** | Specifies access to the remote server by HTTP. | HTTP and HTTPS can be used. |
| **url** *url-address* | Specifies the URL path of the configuration file on the remote server. | It is a string data type. The value range is from 1 to 255 characters. |



Views
-----

All views except the user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If multiple devices need to share the same source configuration file, to ensure that the configuration data on all the devices is consistent, run one of the following commands as required:

* To load a local configuration file and use the configurations in the configuration file to replace the configurations in the running configuration file, run the load configuration file replace [ relative ] command.
* To load the configuration file on a remote IPv4 server and use the configurations in the configuration file to replace the configurations in the running configuration file on the local device, run the load configuration server <ipv4Addr> [ vpn-instance <vpnName> ] transport-type { ftp | sftp } username <usernameVal> password <passwordVal> file <fileName> replace [ relative ] command.
* To load the configuration file on a remote IPv6 server and use the configurations in the configuration file to replace the configurations in the running configuration file on the local device, run the load configuration server ipv6 <ipv6Addr> [ vpn-instance <vpnName> ] transport-type { ftp | sftp } username <usernameVal> password <passwordVal> file <fileName> replace [ relative ] command.
* To obtain the configuration file on a remote server based on a specified URL and use the configurations in the configuration file to replace the configurations in the running configuration file on the local device, run the load configuration server http url <urlVal> [ vpn-instance <vpnName> ] [ file <saveFileName> ] replace [ relative ] command.The **load configuration replace** command can replace all configurations in the running configuration file on the local device or only the configurations in a specified view, depending on the content in the source configuration file to be loaded. To replace only the configurations in a specified view, specify relative in the command.

**Follow-up Procedure**

After the configuration file is loaded and replaced, the file enters the candidate configuration database. Run the **commit** command for relevant configurations to take effect.

**Precautions**

1. The configuration file to be loaded must exist and meet the following conditions:

* The configuration file can contain only configuration commands, view switching commands, and #. When other types of commands (such as display query commands, reset/save/ping maintenance commands, quit, commit, return, upgrade-compatible commands, and one-phase commands) are executed, the device reports an error and continues to load subsequent commands.
* The interactive commands in the configuration file support only Y/N interaction.
* The indentation of commands in the configuration file must be correct. The commands in the system view and the level-1 view under the system view must be left-aligned, the commands in the level-1 view must be indented by one space, and the commands in each subsequent view must be indented by one more space.
* If the number sign (#) is left-aligned, the system view is displayed. If the number sign (#) is indented, it is used to isolate command blocks; in this case, the number sign (#) must be aligned with the first command in the following command block. If the number sign (#) is incorrectly used, configurations may be lost, or commands may be run in an unexpected view.
* The configuration file name extension must be .zip, .cfg, .txt, .dat, or .bat, or the file name does not have an extension. In FTP or SFTP mode, the file name can contain a server directory name. It is recommended that the directory name contain a slash (/). A file name does not contain the special characters: ~ ? \* / : " | < > [ ].
* Both .cfg and .txt files are text files whose content can be directly viewed. If a .cfg or .txt file is specified as the configuration file to be loaded, the system restores the commands in the file one by one when the configuration file is loaded.
* A .zip file is obtained by compressing a .cfg file, occupying less space. If a .zip file is specified as the configuration file to be loaded, the system decompresses the file into a .cfg file, and then restores the commands in the .cfg file one by one when the configuration file is loaded. The .cfg file must have the same name as the .zip file. Otherwise, the configuration file fails to be loaded.
* A .dat file is a compressed file, which can be in binary or text mode. Only a .dat file exported from a Huawei device is supported, and the file cannot be modified manually. Otherwise, the file fails to be loaded.
* A .bat file is used for batch processing. It is a text file that can be modified manually.

1. After the configuration replacement command is executed, pay attention to the replacement result displayed in the prompt message. You can run the **commit** command only after confirming that the replacement result is correct and meets the expectation. This prevents service functions from being affected after the configurations are committed when only partial configurations are successfully replaced.
2. When FTP/STFP is used to load the configuration file on a specified remote server, the remote file is first obtained to the root directory of the device. Ensure that there is sufficient space for storing the file and no file with the same name exists.
3. You are not advised to manually construct a configuration file. If the format of the constructed configuration file is incorrect, configuration restoration may fail or an error may occur during configuration restoration.
4. This function can be performed only in two-phase validation mode.
5. If the command to be replaced depends on some configurations and cannot be delivered separately or deleted using the undo command, the configuration replacement fails.

Example
-------

# Load a local configuration file named config.cfg to replace the running configuration.
```
<HUAWEI> system-view
[~HUAWEI] load configuration file config.cfg replace

```

# Load the config.cfg file transferred from a remote server at 10.1.1.1 through SFTP to replace the running configuration on the current device.
```
<HUAWEI> system-view
[~HUAWEI] load configuration server 10.1.1.1 transport-type sftp username huawei123 password YsHsjx_202206 file config.cfg replace

```

# Use HTTPS to obtain the configuration file config.cfg on the remote server and deliver only the configurations in the AAA view.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] certificate load pem-cert client.crt key-pair rsa key-file client.key auth-code cipher YsHsjx_202206
[*HUAWEI-ssl-policy-policy1] signature algorithm-list ecdsa-secp256r1-sha256 ecdsa-secp384r1-sha384 ecdsa-secp521r1-sha512 ed25519 ed448 rsa-pss-pss-sha256 rsa-pss-pss-sha384 rsa-pss-pss-sha512 rsa-pss-rsae-sha256 rsa-pss-rsae-sha384 rsa-pss-rsae-sha512 rsa-pkcs1-sha256 rsa-pkcs1-sha384 rsa-pkcs1-sha512 ecdsa-sha1 ecdsa-sha224 rsa-sha1 rsa-sha224 dsa-sha1 dsa-sha224 dsa-sha256 dsa-sha384 dsa-sha512
[*HUAWEI-ssl-policy-policy1] quit
[*HUAWEI] http
[*HUAWEI-http] client ssl-policy abc
[*HUAWEI-http] quit
[*HUAWEI] commit
[~HUAWEI] aaa
[*HUAWEI-aaa] load configuration server http url https://10.1.1.1/https/config.cfg replace relative

```