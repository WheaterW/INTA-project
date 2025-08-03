ssh user service-type
=====================

ssh user service-type

Function
--------



The **ssh user service-type** command configures a service type for an SSH user.



By default, the service type of the SSH user is not configured.


Format
------

**ssh user** *user-name* **service-type** **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Indicates the name of an SSH user. | The name is a string of 1 to 253 characters. |
| **all** | Indicates that SFTP, STelnet, SCP, or SNETCONF can be used as the service mode. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the user does not exist, a new SSH user with the specified user-name is created and the configured service type is adopted for the user.


Example
-------

# Configure the service type for SSH users.
```
<HUAWEI> system-view
[~HUAWEI] ssh user john service-type all

```