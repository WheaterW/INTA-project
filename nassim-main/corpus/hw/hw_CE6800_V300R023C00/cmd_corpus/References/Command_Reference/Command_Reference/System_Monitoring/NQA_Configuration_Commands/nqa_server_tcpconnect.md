nqa server tcpconnect
=====================

nqa server tcpconnect

Function
--------



The **nqa server tcpconnect** command specifies a TCP server for an NQA test instance.

The **undo nqa server tcpconnect** command deletes a TCP server for an NQA test instance.



By default, no TCP server is configured for an NQA test.


Format
------

**nqa server tcpconnect** *ip-address* *port-number*

**nqa server tcpconnect vpn-instance** *vpn-instance-name* *ip-address* *port-number*

**undo nqa server tcpconnect** *ip-address* *port-number*

**undo nqa server tcpconnect vpn-instance** *vpn-instance-name* *ip-address* *port-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address monitored by the TCP server. | It is in dotted decimal notation. |
| *port-number* | Specifies the number of the port monitored by the TCP server. | The value is integer ranging from 1 to 65535. The well-known port number is not recommended. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance to which the TCP server belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Both the NQA client and server must be configured before an NQA TCP test instance is started. Otherwise, the test instance fails to be started.Configurations about the server that are performed on the client are as follows:

* Run the **destination-port** command on the client to configure the destination port number for the NQA test instance, that is, the port number enabled on the server. The client can access the server through the port specified using port-number.
* Run the **destination-address** command on the client to configure the destination address for the NQA test instance. The server is enabled to monitor the IP address specified using ip-address.If the client and server are connected using a VPN, run the vpn-instance command to specify a VPN instance.

**Precautions**

You must enable the TCP server using this command before performing the TCP test.


Example
-------

# Configure an NQA TCP listening server with the IP address 10.10.10.1 and TCP port number 2000.
```
<HUAWEI> system-view
[*HUAWEI] nqa server tcpconnect 10.10.10.1 2000

```

# Configure a TCP server with IP address 10.10.10.1, VPN instance vsi and TCP port number 2000.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vsi
[*HUAWEI-vpn-instance-vsi] quit
[*HUAWEI] nqa server tcpconnect vpn-instance vsi 10.10.10.1 2000

```