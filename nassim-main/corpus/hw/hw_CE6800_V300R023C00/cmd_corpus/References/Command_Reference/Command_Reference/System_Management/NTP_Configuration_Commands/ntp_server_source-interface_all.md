ntp server source-interface all
===============================

ntp server source-interface all

Function
--------



The **ntp server source-interface all enable** command enables the NTP/NTP IPv6 server to listen to all interfaces.

The **ntp server source-interface all disable** command disables the NTP/NTP IPv6 server from listening to all interfaces.



By default, the NTP server does not listen to any interface.


Format
------

**ntp** [ **ipv6** ] **server** **source-interface** **all** **enable**

**ntp** [ **ipv6** ] **server** **source-interface** **all** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Indicates the NTP IPv6 service. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the NTP server does not listen to any interface. You can run this command to enable the NTP server to listen to all interfaces.

**Precautions**

* If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.
* After this command is run, the NTP server receives and processes NTP packets received by all interfaces and addresses. This increases the possibility of attacks on the NTP server and reduces system security. Therefore, exercise caution when running this command.
* If the ntp [ipv6] server source-interface all enable command is configured together with the ntp server source-interface or ntp ipv6 server source-address command, the ntp [ipv6] server source-interface all enable command takes effect, and the server receives and processes packets received by all interfaces and addresses.


Example
-------

# Disable the NTP IPv6 server from listening to all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] ntp ipv6 server source-interface all disable
Warning: The NTP IPv6 server listening all interface is disabled. Run the server source-interface command to specify the ntp IPv4 server listening function.

```

# Enable the NTP IPv4 server to listen to all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] ntp server source-interface all enable
Warning: NTP IPv4 server listening all interface will be enabled. Continue? [Y/N]:y

```

# Enable the NTP IPv6 server to listen to all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] ntp server source-interface all enable
Warning: NTP IPv6 server listening all interface will be enabled. Continue? [Y/N]:y

```

# Disable the NTP IPv4 server from listening to all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] ntp server source-interface all disable
Warning: The NTP IPv4 server listening all interface is disabled. Run the server source-interface command to specify the ntp IPv4 server listening function.

```