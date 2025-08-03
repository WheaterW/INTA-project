accounting-copy radius-server
=============================

accounting-copy radius-server

Function
--------

The **accounting-copy radius-server** command enables the RADIUS accounting packet copy function and configures a RADIUS server template for level-2 accounting.

The **undo accounting-copy radius-server** command disables the RADIUS accounting packet copy function.

By default, the RADIUS accounting packet copy function is disabled.



Format
------

**accounting-copy radius-server** *template-name*

**undo accounting-copy radius-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of a RADIUS server template. | The value is a string of 1 to 32 case-sensitive characters, and cannot contain spaces. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The existing RADIUS server on the network performs authentication, authorization, and accounting for users. User login and logout information is sent to the server through accounting packets. Users want to deploy an independent RADIUS accounting server (called the level-2 RADIUS accounting server) to obtain user login and logout information for analyzing user behavior and managing users'; access to the network. However, the device currently does not send accounting packets to the level-2 RADIUS accounting server. In this case, you can configure the RADIUS accounting packet copy function on the device. After this function is configured, the device sends user login and logout information to the level-2 RADIUS accounting server through accounting packets for third-party user behavior analysis.

**Prerequisites**

The RADIUS server template has been created using the **radius-server template** command.

**Precautions**

Ensure that the IP address of the configured level-2 RADIUS accounting server is different from that of the level-1 RADIUS accounting server (including the active/standby RADIUS accounting server).Ensure that the level-2 RADIUS accounting server template configured in the domain is different from the RADIUS server template for authentication and accounting in the domain. If they are the same, the accounting-copy radius-server command cannot be configured and the system displays an error message during the command configuration.



Example
-------

# In the huawei domain, set the IP addresses of the RADIUS authentication and accounting servers to 10.1.1.1, their port numbers to 1813 and 1814, respectively, and RADIUS server template to t1. Set the IP address and port number of the RADIUS server for level-2 accounting to 10.1.1.2 and 1814, respectively, and the RADIUS server template to t2.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template t1
[*HUAWEI-radius-t1] radius-server authentication 10.1.1.1 1813
[*HUAWEI-radius-t1] radius-server accounting 10.1.1.1 1814
[*HUAWEI-radius-t1] quit
[*HUAWEI] radius-server template t2
[*HUAWEI-radius-t2] radius-server accounting 10.1.1.2 1814
[*HUAWEI-radius-t2] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] domain huawei
[*HUAWEI-aaa-domain-huawei] radius-server t1
[*HUAWEI-aaa-domain-huawei] accounting-copy radius-server t2

```