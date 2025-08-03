ipv4 vpn (BMP session view)
===========================

ipv4 vpn (BMP session view)

Function
--------



The **ipv4 vpn** command creates and displays the BMP session IPv4 VPN view.

The **undo ipv4 vpn** command deletes the BMP session IPv4 VPN view.



By default, the BMP session IPv4 VPN view does not exist.


Format
------

**ipv4 vpn**

**undo ipv4 vpn**


Parameters
----------

None

Views
-----

BMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To create and enter the BMP session IPv4 VPN view, run the ipv4 vpn command in the BMP session view.



**Follow-up Procedure**

After this configuration is performed, you can run either of the following commands as needed:

* trace-prefix route-distinguisher vrfRD ipv4-address mask-length: configures BMP to report the trace data of a specified VPNv4 route and the IPv4 VPN unicast route (transformed from the VPNv4 route) to the BMP server.
* trace-prefix route-distinguisher vrfRD all: configures BMP to report the trace data of all VPNv4 routes and IPv4 VPN unicast routes (transformed from the VPNv4 routes) to the BMP server.


Example
-------

# Create and enter the BMP session IPv4 VPN view.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] ipv4 vpn
[*HUAWEI-bmp-session-10.1.1.1-ipv4-vpn]

```