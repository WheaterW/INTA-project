tftp
====

tftp

Function
--------



The **tftp** command uploads the local file to the TFTP server or download the file from the TFTP server to the local machine.




Format
------

**tftp** [ **-a** *source-ip-address* | **-i** { *interface-name* | *interface-type* *interface-number* } ] *host-ip-address* [ **vpn-instance** *vpn-instance-name* | **public-net** ] { **get** | **put** } *source-filename* [ *destination-filename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *source-ip-address* | Specifies the source IPv4 address of the local machine. | The value is in dotted decimal notation. |
| **-i** *interface-name* | Specifies the source interface name. | - |
| *interface-type* | Specifies the source interface type. | - |
| *interface-number* | Specifies the source interface number. | - |
| *host-ip-address* | Specifies the IPv4 address or host name for the TFTP server.  To view the mapping between the IPv4 address and host name, run the display dns dynamic-host or display ip host command. | * If the value is an IPv4 address, it is in dotted decimal notation. * If the value is a host name, it is a string of case-sensitive characters without spaces. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **public-net** | Indicates that the TFTP server on the public network is connected. | - |
| **get** | Specifies the downloading files from the remote TFTP server. | - |
| **put** | Specifies the uploading local files to the remote TFTP server. | - |
| *source-filename* | Specifies the name of the source file. | Source file name is string data type. The string length range is from 1 to 128 characters. It can contain alphanumeric and special characters. |
| *destination-filename* | Specifies the name of the destination file. | Source file name is string data type. The string length range is from 1 to 128 characters. It can contain alphanumeric and special characters. |



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

# Download the file from the remote server.
```
<HUAWEI> tftp 10.1.1.2 get sample.txt sample1.txt

```

# Upload the file to the remote server.
```
<HUAWEI> tftp 10.1.1.2 put sample.txt

```

# Download files from the remote server through the VPN instance named vpn1.
```
<HUAWEI> tftp -a 10.1.1.2 vpn-instance vpn1 10.1.1.1 get sample.txt sample1.txt

```