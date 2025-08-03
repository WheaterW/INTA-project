statistics-timer
================

statistics-timer

Function
--------



The **statistics-timer** command configures an interval at which the router sends BGP running statistics to a monitoring server.

The **undo statistics-timer** command restores the default configuration.



By default, the interval at which the router sends BGP running statistics to the monitoring server is 3600s.


Format
------

**statistics-timer** *time*

**undo statistics-timer** *time*

**undo statistics-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies the interval at which the router sends BGP running statistics to the monitoring server. | The value is an integer ranging from 15 to 65535, in seconds. |



Views
-----

BMP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To configure an interval at which the router sends BGP running statistics to a monitoring server, run the **statistics-timer** command. You can configure the interval based on the network stability requirements. If BGP requires high stability, configure a small interval. However, if the router sends BGP running statistics frequently, a large amount of bandwidth resources will be consumed. Therefore, retaining the default value is recommended.




Example
-------

# Set the interval at which the router sends BGP running statistics to a monitoring server to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bmp
[*HUAWEI-bmp] statistics-timer 100

```