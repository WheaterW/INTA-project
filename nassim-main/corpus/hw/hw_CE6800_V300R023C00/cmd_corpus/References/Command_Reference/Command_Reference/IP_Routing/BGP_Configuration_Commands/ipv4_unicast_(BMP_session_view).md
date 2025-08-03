ipv4 unicast (BMP session view)
===============================

ipv4 unicast (BMP session view)

Function
--------



The **ipv4 unicast** command creates and displays the BMP session IPv4 unicast view.

The **undo ipv4 unicast** command deletes the BMP session IPv4 unicast view.



By default, the BMP session IPv4 unicast view does not exist.


Format
------

**ipv4 unicast**

**undo ipv4 unicast**


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



To create and enter the BMP session IPv4 unicast view, run the ipv4 unicast command in the BMP session view.



**Follow-up Procedure**

After this configuration is performed, you can run either of the following commands as needed:

* trace-prefix ipv4-address mask-length: configures BMP to report the trace data of a specified IPv4 public network unicast route to the BMP server.
* trace-prefix all: configures BMP to report the trace data of all IPv4 public network unicast routes to the BMP server.


Example
-------

# Create and enter the BMP session IPv4 unicast view.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] bmp-session 10.1.1.1
[*HUAWEI-bmp-session-10.1.1.1] ipv4 unicast
[*HUAWEI-bmp-session-10.1.1.1-ipv4-unicast]

```