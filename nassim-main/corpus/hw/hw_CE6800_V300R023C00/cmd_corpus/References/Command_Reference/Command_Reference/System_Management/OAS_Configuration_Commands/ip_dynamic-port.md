ip dynamic-port
===============

ip dynamic-port

Function
--------



The **ip dynamic-port** command sets the port number range for an open system.

The **undo ip dynamic-port** command cancels the port number range setting for an open system.



By default, no port number range is specified for an open system.


Format
------

**ip dynamic-port** *low-port* **to** *high-port*

**undo ip dynamic-port** *low-port* **to** *high-port*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *low-port* | Specifies the start port number. | The value is an integer in the range from 1025 to 65535. |
| **to** *high-port* | Specifies the end port number. | The value is an integer in the range from 1025 to 65535. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In the open solution, a service app needs to communicate with a third-party app in the Linux OS. The port number range used for the communication must be specified. You can run this command to set the port number range. The service app subscribes to the configuration information of the command line to determine whether to communicate with the Linux system or with the internal system.

**Precautions**

When this command is configured, the specified port number range of the ipv4 tcp, ipv6 tcp, ipv4 udp and ipv6 udp types is occupied. A maximum of 500 port numbers can be configured.


Example
-------

# Set the open port number range to 50020 to 50030.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ip dynamic-port 50020 to 50030

```