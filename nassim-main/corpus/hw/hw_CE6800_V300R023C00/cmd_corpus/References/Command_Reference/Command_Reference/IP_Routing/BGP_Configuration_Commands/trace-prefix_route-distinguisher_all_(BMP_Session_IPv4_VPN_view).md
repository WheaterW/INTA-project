trace-prefix route-distinguisher all (BMP Session IPv4 VPN view)
================================================================

trace-prefix route-distinguisher all (BMP Session IPv4 VPN view)

Function
--------



The **trace-prefix route-distinguisher all** command configures BMP to monitor the trace data of all VPNv4 routes with a specified RD and IPv4 VPN unicast routes transformed from the VPNv4 routes.

The **undo trace-prefix route-distinguisher all** command restores the default configuration.



By default, BMP does not monitor the trace data of any VPNv4 route or IPv4 VPN unicast route transformed from the VPNv4 route.


Format
------

**trace-prefix route-distinguisher** *vrfRD* **all**

**undo trace-prefix route-distinguisher** *vrfRD* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *vrfRD* | Specifies the route distinguisher of a VPN instance. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |



Views
-----

BMP Session IPv4 VPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, BMP does not report the trace data of BGP routes on a device. As a result, you can only manually query the trace data of the device's BGP routes.To resolve this issue, run the trace-prefix route-distinguisher all command on the device after a connection is established between the device and BMP server. The command configures BMP to monitor the trace data of all VPNv4 routes and IPv4 VPN unicast routes (transformed from the VPNv4 routes) in real time. After the configuration, BMP can monitor how the routes are processed in response to the following main items:

* Import route-policy for routes received from a specified peer (configured using the **peer route-policy import** command)
* Export route-policy for routes to be advertised to a specified peer (configured using the **peer route-policy export** command)
* Export route-policy for BGP VPN routes (configured using the **export route-policy** command)
* Import route-policy for BGP VPN routes (configured using the **import route-policy** command)
* Route-policy for routes imported using the network command
* Route-policy for summary routes
* Route withdrawal


Example
-------

# Configure BMP to report the trace data of all VPNv4 routes and IPv4 VPN unicast routes (transformed from the VPNv4 routes) to a BMP server.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] ipv4 vpn
[*HUAWEI-bmp-session-10.1.1.1-ipv4-vpn] trace-prefix route-distinguisher 1:1 all

```