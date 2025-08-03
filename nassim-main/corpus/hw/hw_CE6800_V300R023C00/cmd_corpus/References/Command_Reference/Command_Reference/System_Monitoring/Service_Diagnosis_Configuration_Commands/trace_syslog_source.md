trace syslog source
===================

trace syslog source

Function
--------



The **trace syslog source** command sets the source interface from which the device exports diagnosis information to a log server.

The **undo trace syslog source** command cancels the configuration of the source interface from which the device exports diagnosis information to a log server.



By default, no interface is specified to export diagnosis information to the log server.


Format
------

**trace syslog source** { *interface-type* *interface-number* | *interface-name* }

**undo trace syslog source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After you specify an interface for exporting diagnosis information to a log server, the system specifies the IP address of this interface as the source IP address of service diagnosis packets. In this way, the log server can identify the source of diagnosis information.

**Prerequisites**

The device has been configured to export diagnosis information to a log server using the **trace object** command.

**Precautions**

The **trace syslog source** command is not recorded in the configuration file. After the device restarts, the configured source interface for exporting diagnosis information is invalid. To set the source interface, run the **trace syslog source** command again.


Example
-------

# Set 100GE1/0/1 as the source interface for exporting diagnosis information to the log server.
```
<HUAWEI> system-view
[~HUAWEI] trace syslog source 100GE 1/0/1

```