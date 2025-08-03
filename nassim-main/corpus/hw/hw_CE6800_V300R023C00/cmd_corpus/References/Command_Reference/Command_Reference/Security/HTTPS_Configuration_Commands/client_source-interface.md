client source-interface
=======================

client source-interface

Function
--------



The **client source-interface** command binds a source interface to an HTTP client.

The **undo client source-interface** command unbinds the source interface from an HTTP client.



By default, an HTTP client source is selected by the app or sock.


Format
------

**client source-interface** { *interface-name* | *interface-type* *interface-number* }

**undo client source-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of a source interface of an HTTP client. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of a source interface of an HTTP client. | - |
| *interface-number* | Specifies the number of a source interface of an HTTP client. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

HTTP view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve system security, you can specify the source interface of the HTTP client and use the bound source interface address to establish a connection.

**Prerequisites**

If a loopback interface is used, ensure that the loopback interface has been created and an IPv4 address has been configured for the loopback interface. Otherwise, this command cannot be executed successfully.

**Configuration Impact**

After the source interface of an HTTP client is specified successfully, the client can establish a connection only through the specified source interface.


Example
-------

# Configure the source interface of the HTTP client to be LoopBack1.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack1
[~HUAWEI-LoopBack1] ip address 10.1.1.1 24
[*HUAWEI-LoopBack1] quit
[*HUAWEI] http
[*HUAWEI-http] client source-interface LoopBack1

```