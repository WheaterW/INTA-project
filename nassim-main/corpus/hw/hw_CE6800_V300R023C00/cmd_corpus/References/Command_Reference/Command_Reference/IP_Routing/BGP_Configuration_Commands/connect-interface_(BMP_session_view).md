connect-interface (BMP session view)
====================================

connect-interface (BMP session view)

Function
--------



The **connect-interface** command specifies a source interface to send BMP messages and a source IP address to set up a BMP session.

The **undo connect-interface** command restores the default configuration.



By default, no source interface is specified to send BMP messages.


Format
------

**connect-interface** { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-name* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }

**undo connect-interface**

**undo connect-interface** { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-name* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *ipv4-source-address* | Specifies a source IPv4 address to set up a BMP session. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status of devices in real time, such as the status of BGP peer relationship establishment and termination and route updates.After a TCP connection is established between a monitoring server and a device to be monitored, the device sends unsolicited BMP messages to the monitoring server to report BGP running statistics. After receiving these BMP messages, the monitoring server parses them and displays the BGP running status in the monitoring view. By analyzing the headers in the BMP messages, the monitoring server can determine from which BGP peer the routes carried in the messages were received. By default, the source interface used to send BMP messages is not specified after a TCP connection is established between a monitoring server and a device to be monitored. If the device encounters a failure, the source interface used to send BMP messages may change. In this case, the monitoring server cannot determine whether the new source interface belongs to a new device. To address this problem, run the **connect-interface** command to specify a source interface to send BMP messages.The **connect-interface** command can be run in both the BMP view and BMP session view. If the command is run in both views, the configuration in the BMP session view takes precedence over that in the BMP view.



**Precautions**



If the command is run more than once, the latest configuration overrides the previous one.You can only run the **connect-interface** command in the BMP view to configure a source IPv4 address for sending BMP messages. This operation will re-establish all IPv4 BMP sessions for which no source address or source interface is configured.By default, an interface on a device is a Layer 3 interface. After you run the **connect-interface** command to specify an interface, changing the interface type to Layer 2 may affect Layer 3 services. Therefore, exercise caution when changing the interface type.




Example
-------

# Specify a source IPv4 address to set up a BMP session.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] connect-interface 10.1.1.1

```