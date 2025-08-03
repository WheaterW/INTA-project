state
=====

state

Function
--------



The **state** command configures the state of a local access user.



By default, a local access user is in active state after being created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**state** { **active** | **block** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **active** | Permit the user to deal with the authen request. | - |
| **block** | Prohibits the user(s) from dealing with the authentication request. | - |



Views
-----

aaa-access-user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When some services are configured for local access users, new users are not expected to access the network to prevent exceptions during the configuration. Configure the domain to be in the blocked state to prevent new users from accessing the network. After the configuration is complete, set the status to active.


Example
-------

# Set the state of the local access user hello@163.net to blocking.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-access-user hello@163.net
[*HUAWEI-aaa-access-user-hello@163.net] state block

```