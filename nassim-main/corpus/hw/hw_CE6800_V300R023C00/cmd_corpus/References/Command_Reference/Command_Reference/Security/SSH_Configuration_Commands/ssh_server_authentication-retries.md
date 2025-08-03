ssh server authentication-retries
=================================

ssh server authentication-retries

Function
--------



The **ssh server authentication-retries** command sets the number of retry times to authenticate an SSH connection.

The **undo ssh server authentication-retries** command restores the default number of retry times.



By default, the default number of retry times is 3.


Format
------

**ssh server authentication-retries** *times*

**undo ssh server authentication-retries**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *times* | Specifies the number of retry times to authenticate an SSH connection. | The value ranges from 1 to 5. |



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

# Set the number of retry times to 4.
```
<HUAWEI> system-view
[~HUAWEI] ssh server authentication-retries 4

```