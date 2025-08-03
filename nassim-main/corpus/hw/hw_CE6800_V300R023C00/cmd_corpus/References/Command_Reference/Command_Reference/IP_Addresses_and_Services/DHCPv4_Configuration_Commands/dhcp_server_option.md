dhcp server option
==================

dhcp server option

Function
--------

The **dhcp server option** command sets user-defined option for an interface address pool.

The **undo dhcp server option** command deletes user-defined option from an interface address pool.

By default, no user-defined option is configured in an interface address pool.



Format
------

**dhcp server option** *code* { **ascii** *ascii-string* | **hex** *hex-string* | **cipher** *cipher-string* | **ip-address** *ip-address* &<1-8> }

**dhcp server option** *code* **sub-option** *sub-code* { **ascii** *sub-ascii-string* | **hex** *sub-hex-string* | **cipher** *sub-cipher-string* | **ip-address** *sub-ip-address* &<1-8> }

**undo dhcp server option** [ *code* [ **sub-option** *sub-code* ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *code* | Specifies the code for a user-defined option. | The value is an integer that ranges from 1 to 254, except values 1, 3, 6, 15, 44, 46, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 82, 120, 121, and 184.  The formats of Option121 and Option184 are different from those of other options.  There are well-known options and customized options. For details about well-known options, see RFC 2132. |
| **ascii** *sub-ascii-string* | Specifies the user-defined option code as an ASCII character string. | The value is a string of 1 to 253 case-sensitive characters, spaces supported. |
| **ascii** *ascii-string* | Specifies the user-defined option code as an ASCII character string. | The value is a string of 1 to 255 case-sensitive characters that can contain spaces. |
| **hex** *hex-string* | Specifies a user-defined option as hexadecimal characters. | The value is a string of 2 to 254 case-insensitive hexadecimal characters with an even number of digits, for example, hh or hhhh. The value can contain digits (0-9), uppercase letters (A-F), and lowercase letters (a-f). |
| **hex** *sub-hex-string* | Specifies a user-defined option as hexadecimal characters. | The value is a string of 2 to 252 case-insensitive hexadecimal characters with an even number of digits, for example, hh or hhhh. The value can contain digits (0-9), uppercase letters (A-F), and lowercase letters (a-f). |
| **cipher** *cipher-string* | Specifies the user-defined option code as a ciphertext character string. | The value is a string of case-sensitive characters. It cannot contain spaces. The entered ciphertext character string can be in cleartext or ciphertext. The ciphertext is a character string starting and ending with %@ %# or %+ %#. If spaces are used, the string must start and end with double quotation marks (").   * If a cleartext string is specified, the value is a string of 1 to 255 characters. * If a ciphertext string is specified, the value is a string of 20 to 432 characters.   No matter whether the character string is entered in cleartext or ciphertext, the character string is displayed in ciphertext in the configuration file and in cleartext in packets. |
| **cipher** *sub-cipher-string* | Specifies the user-defined option code as a ciphertext character string. | The value is a string of case-sensitive characters. It cannot contain spaces. The entered ciphertext character string can be in cleartext or ciphertext. The ciphertext is a character string starting and ending with %@ %# or %+ %#. If spaces are used, the string must start and end with double quotation marks (").   * If a cleartext string is specified, the value is a string of 1 to 253 characters. * If a ciphertext string is specified, the value is a string of 20 to 432 characters.   No matter whether the character string is entered in cleartext or ciphertext, the character string is displayed in ciphertext in the configuration file and in cleartext in packets. |
| **ip-address** *ip-address* | Specifies a user-defined option as an IP address. | The value is in dotted decimal notation. |
| **ip-address** *sub-ip-address* | Specifies a user-defined option as an IP address. | The value is in dotted decimal notation. |
| **sub-option** *sub-code* | Specifies the code of a user-defined sub-option. | The value is an integer that ranges from 1 to 254. For details about well-known options, see RFC 2132. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. The Option field in a DHCP packet carries control information and parameters, including basic information such as the DNS service, NetBIOS service, and IP address lease. If a DHCP server is configured with option, when a DHCP client applies for an IP address from an interface address pool, the client can obtain configurations in the Option field of the DHCP response packet from the DHCP server without having to configure the DNS service, NetBIOS service, or IP address lease separately.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

* If an option contains a password, the ascii or hex type is insecure. You are advised to set the cipher type. A secure password should contain at least two types of the following: lowercase letters, uppercase letters, digits, and special characters. In addition, the password must consist of at least six characters.
* You can run the **dhcp server option** command to configure common functions, such as the NetBIOS service and IP address lease of the client. The configuration of related commands takes precedence. These commands take precedence over the **dhcp server option** command.
* You can run the **option** command to configure user-defined options for a global address pool.
* When an enterprise intranet user uses a proxy server to connect to the Internet, you need to set proxy server parameters to enable the browser to access the Internet. The network agent self-discovery protocol implements the automatic configuration of these parameters. The network administrator does not need to set these parameters on each client. To implement automatic network proxy discovery, the network administrator needs to deploy the proxy server configuration file in advance and run the **dhcp server option 252 ascii ascii-string** command to specify the URL of the configuration file. ascii-string specifies the URL of the configuration file, which is in the format of http://xxx/proxy.pac. Set ascii-string based on the actual path where the configuration file is stored. When a browser accesses the network, the browser applies for the URL of the proxy server configuration file from the DHCP server and downloads the file for automatic configuration. After the configuration is complete, the browser can access the Internet. The ascii-string cannot be enclosed in double quotation marks ("ascii-string"). Otherwise, terminals cannot parse Option 252.


Example
-------

# Set Option64 to 0x11 (a hexadecimal number) for the interface address pool on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server option 64 hex 11
Info: The option configuration will be saved without encryption in the current format, which poses a high security risk. You are advised to use the cipher format.

```