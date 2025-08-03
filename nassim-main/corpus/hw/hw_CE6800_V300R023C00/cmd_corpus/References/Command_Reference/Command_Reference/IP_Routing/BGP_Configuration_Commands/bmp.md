bmp
===

bmp

Function
--------



The **bmp** command starts BMP and then displays the BGP Monitoring Protocol (BMP) view or displays the BMP view directly.

The **undo bmp** command deletes all BMP configurations.



By default, BMP is disabled in the system.


Format
------

**bmp**

**undo bmp**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BMP is used to monitor BGP running status, such as BGP peer relationship establishment and termination and route updates. If you want to connect a device to a monitoring server, run the **bmp** command on the device to start BMP and perform configurations in the displayed BMP view.




Example
-------

# Start BMP and enter the BMP view.
```
<HUAWEI> system-view
[~HUAWEI] bmp

```