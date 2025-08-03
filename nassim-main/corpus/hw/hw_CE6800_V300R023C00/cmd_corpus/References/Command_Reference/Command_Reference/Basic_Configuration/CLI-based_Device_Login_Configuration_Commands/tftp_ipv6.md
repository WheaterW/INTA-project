tftp ipv6
=========

tftp ipv6

Function
--------



The **tftp ipv6** command uploads the local file to the TFTP server or download the file from the TFTP server to the local machine.




Format
------

**tftp ipv6** [ **-a** *source-ipv6-address* ] *tftp-server-ipv6* [ [ **vpn-instance** *vpn-instance-name* ] | **public-net** ] [ **-oi** { *interface-name* | *interface-type* *interface-number* } ] { **get** | **put** } *source-filename* [ *destination-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ipv6-address* | Specifies the source IPv6 address of the local machine. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *tftp-server-ipv6* | Specifies the IPv6 address or host name for the IPv6 TFTP server.  To view the mapping between the IPv6 address and host name, run the display dns dynamic-host or display ip host command. | The value is a string case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name for the TFTP server. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **public-net** | Indicates that the TFTP server on the public network is connected. | - |
| **-oi** *interface-type* *interface-number* | Specifies the source interface type and number. | - |
| **get** | Specifies the downloading files from the remote TFTP server. | - |
| **put** | Specifies the uploading local files to the remote TFTP server. | - |
| *source-filename* | Specifies the source file name. | Source file name is string data type. The string length range is from 1 to 255 characters. It can contain alphanumeric and special characters. |
| *destination-filename* | Specifies the destination file name. | Destination file name is string data type. The string length range is from 1 to 255 characters. It can contain alphanumeric and special characters. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Specify the valid source IP address to communicate with the server.

**Configuration Impact**

If you do not specify the destination file name, the source file name is considered as destination file name.

**Precautions**



This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.




Example
-------

# Obtain data from the peer TFTP server.
```
<HUAWEI> tftp ipv6 fe80::250:daff:fe91:e058 -oi 100GE 1/0/1 get filetoget filetoget

```