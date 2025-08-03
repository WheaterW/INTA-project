server-source
=============

server-source

Function
--------



The **server-source** command specifies a source interface for the HTTP server to receive and respond to requests from a client.

The **server-source all-interface** command allows all interfaces on the device to be used by the HTTP server to receive and respond to requests from a client.

The **undo server-source** command restores the default configuration.



By default, no HTTP server source interface is specified.


Format
------

**server-source** { *interface-name* | *interface-type* *interface-number* }

**server-source all-interface**

**undo server-source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of a source interface. | - |
| *interface-type* | Specifies the type of a source interface. | - |
| *interface-number* | Specifies the number of a source interface. | - |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, you can run this command to specify a source interface for an HTTP server. This configuration allows only authorized users to log in to the HTTP server.You can run the **server-source** command with the <interface-name>|<interface-type> <interface-number> parameter specified to specify the source interface for the HTTP server to receive and respond to request packets from the client.To enable an HTTP server to use all interfaces to receive and respond to requests from clients, you can run the **server-source all-interface** command.

**Prerequisites**

A loopback interface has been created if you want to specify it as the source interface of an HTTP server using the **server-source** command. Otherwise, the command cannot be executed.

**Configuration Impact**

If a source interface is specified for an HTTP server, HTTP users can log in only through the specified source interface.

**Precautions**

If you run both the server-source { <interface-name> | <interface-type> <interface-number> } and **server-source all-interface** commands, the last configured one takes effect.After the **server-source all-interface** command is run, the device responds to request packets from any IP address, which poses security risks. Therefore, you are not advised to run this command.


Example
-------

# Configure loopback 1 as a source interface for the HTTP server to receive and respond to requests from a client.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] ip address 10.1.1.1 255.255.255.255
[*HUAWEI-LoopBack1] quit
[*HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] server-source LoopBack1

```

# Enable the HTTP server to use all interfaces to receive and respond to requests from a client.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] server-source all-interface

```