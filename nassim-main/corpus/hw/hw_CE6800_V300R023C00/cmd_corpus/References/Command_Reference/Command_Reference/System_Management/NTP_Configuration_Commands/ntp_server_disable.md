ntp server disable
==================

ntp server disable

Function
--------



The **ntp server disable** command disables the NTP server function.

The **undo ntp server disable** command enables the NTP server function.

The **ntp ipv6 server disable** command disables the NTP IPv6 server function.

The **undo ntp ipv6 server disable** command enables the NTP IPv6 server function.



By default, the NTP server functionality is enabled. NTP server functionality will be disabled when the first configuration of the NTP function takes effect.


Format
------

**ntp** [ **ipv6** ] **server** **disable**

**undo ntp** [ **ipv6** ] **server** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Indicates NTP IPv6 services. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The NTP server function is enabled by default. To improve security, the system automatically disables the NTP server function when the first NTP configuration command takes effect. You need to run the **undo ntp server disable** command to enable the server function.The NTP IPv6 server function is enabled by default. To improve security, the system automatically disables the NTP IPv6 server function when the first NTP configuration command takes effect. You need to run the **undo ntp ipv6 server disable** command to enable the server function.



**Configuration Impact**



Running the ntp server [ipv6] disable command disables IPv4 or IPv6 NTP server functionality.



**Precautions**



To enhance system security, the NTP IPv4 server by default does not process the packets sent from interfaces or addresses. To ensure that the server can properly process the synchronization requests from a client, run the **ntp server source-interface** command to configure the server to listen to the source interface or the **ntp server source-interface all enable** command to configure the server to listen to all interfaces.To enhance system security, the NTP IPv6 server by default does not process the packets sent from interfaces or addresses. To ensure that the server can properly process the synchronization requests from a client, run the **ntp ipv6 server source-address** command to configure the NTP server to listen to the source address or the **ntp ipv6 server source-interface all enable** command to configure the server to listen to all interfaces.




Example
-------

# Disable IPv6 NTP server functionality.
```
<HUAWEI> system-view
[~HUAWEI] ntp ipv6 server disable

```

# Disable IPv4 NTP server functionality.
```
<HUAWEI> system-view
[~HUAWEI] ntp server disable

```