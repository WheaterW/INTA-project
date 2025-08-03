option
======

option

Function
--------

The **option** command configures the user-defined option that a DHCP server assigns to a DHCP client.

The **undo option** command deletes the user-defined option that a DHCP server assigns to a DHCP client.

By default, no user-defined option that a DHCP server assigns to a DHCP client is configured.



Format
------

**option** *code* **sub-option** *sub-code* { **ascii** *sub-ascii-string* | **hex** *sub-hex-string* | **cipher** *sub-cipher-string* | **ip-address** *sub-ip-address* &<1-8> }

**option** *code* { **ascii** *ascii-string* | **hex** *hex-string* | **cipher** *cipher-string* | **ip-address** *ip-address* &<1-8> }

**undo option** [ *code* [ **sub-option** *sub-code* ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *code* | Specifies the code of a user-defined option. | The value is an integer that ranges from 1 to 254, except the values 1, 3, 6, 15, 44, 46, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 82, 120, 121, and 184.  There are well-known options and user-defined options. For details about well-known options, see RFC 2132. |
| **sub-option** *sub-code* | Specifies the code of a user-defined sub-option. | The value is an integer that ranges from 1 to 254. For details about well-known options, see RFC 2132. |
| **ascii** *sub-ascii-string* | Specifies the user-defined option code as an ASCII character string. | The value is a string of 1 to 253 case-sensitive characters, spaces supported. |
| **ascii** *ascii-string* | Specifies the user-defined option code as an ASCII character string. | The value is a string of 1 to 255 characters, spaces supported. |
| **hex** *sub-hex-string* | Specifies a user-defined option as hexadecimal characters. | The value is a hexadecimal string with an even number of case-insensitive characters, for example, hh or hhhh. The value without spaces ranges from 2 to 252 characters. The value can be a combination of digits (0-9), uppercase letters (A-F), and lowercase letters (a-f). |
| **hex** *hex-string* | Specifies a user-defined option as hexadecimal characters. | The value is a hexadecimal string with an even number of case-insensitive characters, for example, hh or hhhh. The value without spaces ranges from 2 to 254 characters. The value can be a combination of digits (0-9), uppercase letters (A-F), and lowercase letters (a-f). |
| **cipher** *cipher-string* | Specifies the user-defined option code as a ciphertext character string. | The value is a string of case-sensitive characters in cleartext or ciphertext, spaces not supported. The ciphertext is a character string starting and ending with %@ %# or %+ %#. If spaces are used, the string must start and end with double quotation marks (").   * The value is a string of 1 to 255 characters in cleartext. * The value is a string of 20 to 432 characters in ciphertext.   No matter whether the character string is entered in cleartext or ciphertext, the character string is displayed in ciphertext in the configuration file and in cleartext in packets. |
| **cipher** *sub-cipher-string* | Specifies the user-defined option code as a ciphertext character string. | The value is a string of case-sensitive characters in cleartext or ciphertext, spaces not supported. The ciphertext is a character string starting and ending with %@ %# or %+ %#. If spaces are used, the string must start and end with double quotation marks (").   * The value is a string of 1 to 253 characters in cleartext. * The value is a string of 20 to 432 characters in ciphertext.   No matter whether the character string is entered in cleartext or ciphertext, the character string is displayed in ciphertext in the configuration file and in cleartext in packets. |
| **ip-address** *ip-address* | Specifies a user-defined option as an IP address. | The value is in dotted decimal notation. |
| **ip-address** *sub-ip-address* | Specifies a user-defined option as an IP address. | The value is in dotted decimal notation. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. The option field in a DHCP packet carries control information and parameters. If a DHCP server is configured with options, when a DHCP client applies for an IP address, the client can obtain the configurations in the option field of the DHCP response packet from the DHCP server. To configure user-defined options for an interface address pool, run the **dhcp server option** command.

**Prerequisites**

A global IP address pool has been created using the ip pool command.

**Precautions**

To ensure configuration accuracy, read the Request For Comments (RFC) before configuring options.

When the password is contained in option, the ascii or hex type is insecure. Set the option type to cipher. For security purposes, use a password that is at least six characters long and contains at least two types of the following: lowercase letters, uppercase letters, digits, and special characters.If the
**option** command is not run for the first time, the following configurations are affected:

* If the specified code is different from the original code, both configurations take effect.
* If the specified code is the same as the original code and a sub-code exists in the original configuration, the specified sub-code overwrites the original sub-code. If the specified sub-code is different from the original sub-code, both sub-codes take effect. If no sub-code is specified in the new configuration, the new configuration overrides the previous one. When no sub-code is specified in the existing command, the new configuration overrides the existing configuration.If the device functions as the DHCP server to assign IP addresses to APs, and the AC and APs are on different network segments, you need to configure the Option 43 field to specify the AC IP address for the APs. Otherwise, the APs cannot discover the AC. Run the option 43 { hex hex-string | [ sub-option 1 hex hex-string | sub-option 2 ip-address ip-address &<1-8> | sub-option 3 ascii ascii-string ] } command to specify an AC IP address for an AP using either of the following methods:

1. Run the **option 43 hex 031D3139322e3136382e3139342e35302c3139322e3136382e3139342e3534** command to configure the device to specify AC IP addresses 192.168.194.50 and 192.168.194.54 for APs. In this command, 03 is a fixed value; 1D indicates that the length of an IP address including dots (.) and the comma (,) is 29, and multiple IP addresses are separated by the comma (,); 3139322e3136382e3139342e3530 indicates the ASCII value of 192.168.194.50; 2C indicates the ASCII value of the comma (,); 3139322e3136382e3139342e3534 indicates the ASCII value of 192.168.194.54.
2. Run the **option 43 sub-option 1 hex C0A80001C0A80002** command to configure the device to specify AC IP addresses 192.168.0.1 and 192.168.0.2 for APs. In the command, C0A80001 indicates the hexadecimal format of 192.168.0.1, and C0A80002 indicates the hexadecimal format of 192.168.0.2.
3. Run the option 43 sub-option 2 ip-address 192.168.0.1 192.168.0.**2** command to configure the device to specify AC IP addresses 192.168.0.1 and 192.168.0.2 for APs.
4. Run the option 43 sub-option 3 ascii 192.168.0.1,192.168.0.**2** command to configure the device to specify AC IP addresses 192.168.0.1 and 192.168.0.2 for APs.If you need to configure multiple IP addresses when the option is specified as an ASCII character string, use commas (,) to separate the IP addresses.<br /> If the AC and APs are on the same network segment, you do not need to configure the Option 43 field, and the APs can discover the AC in broadcast mode. After Option 43 is configured, the APs unicast Discover Request packets to the IP address carried in Option 43 to discover the AC. If the APs do not receive any Discovery Response packet after sending unicast Discovery Request packets 10 consecutive times, the APs then broadcast packets to discover the AC.When an enterprise intranet user uses a proxy server to connect to the Internet, you need to set proxy server parameters to enable the browser to access the Internet. The network agent self-discovery protocol implements automatic configuration of these parameters. The network administrator does not need to set these parameters on each client. To implement automatic discovery of network agents, the network administrator needs to deploy the configuration file of the proxy server in advance, and then run the **option 252 ascii ascii-string** command to specify the URL of the configuration file. The URL of the configuration file is in the format of http://xxx/proxy.pac. Set ascii-string based on the actual path where the configuration file is stored. When accessing the Internet, the browser applies to the DHCP server for the URL of the proxy server configuration file, and then downloads the file for automatic configuration. After the configuration is complete, the browser can access the Internet.Do not add double quotation marks ("ascii-string") to the value of ascii-string. Otherwise, terminals cannot parse Option 252.


Example
-------

# In the global address pool global1, set Option 64 to 0x11 (a hexadecimal number).
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] option 64 hex 11
Info: The option configuration will be saved without encryption in the current format, which poses a high security risk. You are advised to use the cipher format.

```