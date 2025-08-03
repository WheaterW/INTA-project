sname
=====

sname

Function
--------

The **sname** command configures the name of the server from which the DHCP client obtains the startup configuration file.

The **undo sname** command deletes the configured name of the server from which the DHCP client obtains the startup configuration file.

By default, no name is configured for the server from which the DHCP client obtains the startup configuration file.



Format
------

**sname** *sname*

**undo sname**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sname* | Specifies the name of the server from which the DHCP client obtains the startup configuration file. | The value is a string of 1 to 63 case-sensitive characters. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Besides assigning IP addresses, a DHCP server can also provide the required network configuration parameters, such as the startup configuration file name for the DHCP client. After the name of the server from which the DHCP client obtains the startup configuration file is configured using the **sname** command, the DHCP client obtains the startup configuration file from this server.

**Precautions**

Ensure that the route between the DHCP client and the file server from which the DHCP client obtains the startup configuration file is reachable.



Example
-------

# In the IP address pool view, configure the name of the server from which the DHCP client obtains the startup configuration file as example.
```
<HUAWEI> system-view
[~HUAWEI] ip pool p1
[*HUAWEI-ip-pool-p1] sname example

```