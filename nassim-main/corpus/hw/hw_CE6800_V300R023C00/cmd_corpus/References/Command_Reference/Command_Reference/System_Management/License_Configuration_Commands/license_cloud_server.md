license cloud server
====================

license cloud server

Function
--------



The **license cloud server** command is used to create the ip address and the port of the cloud license server in the system.

The **undo license cloud server** command is used to delete the ip address and the port of the cloud license server in the system.



By default, the system does not have a cloud license server configured.


Format
------

**license cloud server** *server-name* **ip** *ip-value* **port** *port-value*

**undo license cloud server** *server-name* [ **ip** *ip-value* **port** *port-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *server-name* | Specifies the name of the cloud license server. | The value is a string of 5 to 127 case-sensitive characters without spaces. |
| **ip** *ip-value* | Specifies the IP address of the cloud server. | The value is in dotted decimal notation. |
| **port** *port-value* | Specifies the port of the cloud license server. | The value is an integer ranging from 1 to 65535. |
| *ip-value-str* | Specifies the IP address of the cloud server. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device uses the non-cloud license mode. To switch the device to the cloud license mode, you need to configure the IP address and port number of the cloud license server so that the device can apply for license resources from the cloud license server.

**Precautions**

You need to ensure that the IP address and port number of the configured cloud server are correct. You can check whether the registration is successful through the command display license cloud server.


Example
-------

# Configure the IP address and port number of the cloud license server.
```
<HUAWEI> system-view
[~HUAWEI] license cloud server server001 ip 10.1.1.1 port 8081

```

# Delete the configured IP address and port number of the cloud license server.
```
<HUAWEI> system-view
[~HUAWEI] undo license cloud server server001 ip 10.1.1.1 port 8081
Warning: This operation will disconnect the device with the cloud license server. Continue? [Y/N]:Y

```