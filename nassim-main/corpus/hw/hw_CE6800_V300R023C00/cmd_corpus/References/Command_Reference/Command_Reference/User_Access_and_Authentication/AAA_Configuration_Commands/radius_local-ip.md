radius local-ip
===============

radius local-ip

Function
--------

The **radius local-ip** command configures the local IP address of the UDP socket with a local port number in the range of 1024-55535.

The **undo radius local-ip** command deletes the local IP address of the UDP socket with the local port number in the range of 1024-55535.

By default, no UDP socket with the local IP address of any and a local port number in the range of 1024-55535 is created.



Format
------

**radius local-ip any**

**radius local-ip** *ip-address* [ *vpn-name* ]

**undo radius local-ip any**

**undo radius local-ip** *ip-address* [ *vpn-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the local IP address. | The value is a unicast address in dotted decimal notation. |
| *vpn-name* | Specifies local VPN instance. | The value must be an existing VPN instance name. |
| **any** | Specifies the local IP address as any. | - |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If the socket is created for receiving packets, for security purposes, at least one of the local and remote IP addresses of the socket is not any IP address. To meet this requirement, run the **radius local-ip** command to configure the local IP address and local VPN for the UDP socket with a local port number in range 1024-55535.

**Precautions**

The radius local-ip <ip-address> [ <vpn-name> ] commands can be configured at most four times.

The radius local-ip any and radius local-ip <ip-address> [ <vpn-name> ] commands can be configured together.The radius local-ip any and radius local-ip <ip-address> [ <vpn-name> ] commands take effect for UDP ports in range 1024-55535.

Example
-------

# Configure the local IP address and VPN instance of the UDP socket with a local port number in the range of 1024 to 55535.
```
<HUAWEI> system-view
[~HUAWEI] radius local-ip 192.168.92.148 huawei

```