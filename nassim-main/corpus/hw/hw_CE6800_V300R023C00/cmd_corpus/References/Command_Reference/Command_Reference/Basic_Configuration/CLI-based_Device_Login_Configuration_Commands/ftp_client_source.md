ftp client source
=================

ftp client source

Function
--------



The **ftp client source** command sets the interface and IP addresses of the FTP client to establish the connection with FTP server.

The **undo ftp client source** command cancels the interface and IP address of the FTP client.



By default, the source address is set to 0.0.0.0.


Format
------

**ftp client source** { **-a** *ip-address* | **-i** { *interface-type* *interface-number* | *interface-name* } }

**undo ftp client source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-a** *ip-address* | Specifies the IP address used to establish FTP connections.  If the IP address is not specified, the command can be successfully executed but the function does not take effect. | The value is in dotted decimal notation. |
| **-i** *interface-name* | Specifies the source interface. | - |
| *interface-type* | Specifies the type of the source interface for the Telnet client to establish a connection to the server. | - |
| *interface-number* | Specifies the number of the source interface for the Telnet client to establish a connection to the server. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If no source IP address or interface is specified in the ftp command, the default address and interface set in this command will be used.
* If the source IP address and interface are specified in the ftp command, they will be used instead of the default address and interface.
* This command takes effect only for IPv4.

**Precautions**

* If the value of ip-address or interface-type interface-number does not exist, the command can be configured but does not take effect.
* If the specified source interface has been bound to a VPN instance, the client is also bound to the VPN instance.
* After the bound source interface is deleted, the interface configuration in the command is not deleted, but the function does not take effect. After the source interface with the same name is reconfigured, the function is restored.

Example
-------

# Set the FTP source as loopback interface.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] ip address 10.1.1.1 16
[*HUAWEI-LoopBack0] quit
[*HUAWEI] ftp client source -i loopback 0

```

# Set the FTP source IPv4 address as 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ftp client source -a 10.1.1.1

```