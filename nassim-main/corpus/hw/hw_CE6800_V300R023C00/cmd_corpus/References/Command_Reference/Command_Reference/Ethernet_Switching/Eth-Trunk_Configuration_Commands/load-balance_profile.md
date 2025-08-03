load-balance profile
====================

load-balance profile

Function
--------



The **load-balance profile** command displays the default load balancing profile view or configures a load balancing profile and displays its view.

The **undo load-balance profile** restores the default load balancing profile.



By default, there is a load balancing profile named default.


Format
------

**load-balance profile** *profile-name*

**undo load-balance profile** *profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Configures the name of a load balancing profile. | The value is a string of 1 to 31 case-sensitive characters. The string cannot contain the following characters: | > $. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Only one load balancing profile can be created. By default, the load balancing profile name is default. When a new load balancing profile is created, the existing one is replaced.


Example
-------

# Create a load balancing profile named abc and enter the load balancing profile view.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc

```