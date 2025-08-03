display license cloud server
============================

display license cloud server

Function
--------



The **display license cloud server** command is used to view the registration information of devices and cloud license servers.




Format
------

**display license cloud server**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After configuring the cloud license server of the device, this command is used to view the registration information of the device and the cloud license server to determine whether the registration is successful.

**Prerequisites**

Run the **license cloud server** command to configure the IP address and port number of the cloud license server. Otherwise, no command output is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Query the registration information of devices and cloud servers.
```
<HUAWEI> display license cloud server
Server name              : aaaaa
Server IP address        : 192.168.4.221
Server port              : 18089
Registration status      : register
Policy name              : cloud

```

**Table 1** Description of the **display license cloud server** command output
| Item | Description |
| --- | --- |
| Server IP address | IP address of the cloud server. |
| Server port | Port of the cloud server. |
| Server name | Cloud server name. |
| Registration status | Registration status of devices and cloud servers. |
| Policy name | Strategy name. |