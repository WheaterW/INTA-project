ssh server timeout
==================

ssh server timeout

Function
--------



The **ssh server timeout** command sets the authentication timeout period of the SSH server.

The **undo ssh server timeout** command restores the default authentication timeout period of the SSH server.



By default, the SSH authentication timeout period is 60 seconds.


Format
------

**ssh server timeout** *seconds*

**undo ssh server timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *seconds* | Specifies the login timeout period of the SSH connection. | It is an integer data type. The value ranges from 1 to 120 seconds. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The configuration takes effect during the next login.This command takes effect for both IPv4 and IPv6 connections.




Example
-------

# Configure the authentication timeout interval value as 90 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ssh server timeout 90

```