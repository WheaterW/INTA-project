trace-prefix all (BMP Session IPv4 unicast view)
================================================

trace-prefix all (BMP Session IPv4 unicast view)

Function
--------



The **trace-prefix all** command configures BMP to monitor the trace data of all IPv4 public network unicast routes.

The **undo trace-prefix all** command restores the default configuration.



By default, BMP does not monitor the trace data of any IPv4 public network unicast routes.


Format
------

**trace-prefix all**

**undo trace-prefix all**


Parameters
----------

None

Views
-----

BMP Session IPv4 unicast view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, BMP does not report the trace data of BGP routes on a device. As a result, you can only manually query the trace data of the device's BGP routes.To resolve this issue, run the trace-prefix all command on the device after a connection is established between the device and BMP server. The command configures BMP to monitor the trace data of all IPv4 public network unicast routes in real time. After the configuration, BMP can monitor how the routes are processed in response to the following main items:

* Import route-policy for routes received from a specified peer (configured using the **peer route-policy import** command)
* Export route-policy for routes to be advertised to a specified peer (configured using the **peer route-policy export** command)
* Export route-policy for BGP VPN routes (configured using the **export route-policy** command)
* Import route-policy for BGP VPN routes (configured using the **import route-policy** command)
* Route-policy for routes imported using the network command
* Route-policy for summary routes
* Route withdrawal


Example
-------

# Configure BMP to report the trace data of all IPv4 public network unicast routes to a BMP server.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] ipv4 unicast
[*HUAWEI-bmp-session-10.1.1.1-ipv4-unicast] trace-prefix all

```