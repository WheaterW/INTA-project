authorization-modify mode
=========================

authorization-modify mode

Function
--------



The **authorization-modify mode** command configures the update mode for user authorization information delivered by the authorization server.

The **undo authorization-modify mode** command restores the default update mode for user authorization information delivered by the authorization server.



By default, the update mode of user authorization information delivered by the authorization server is overlay. That is, the new user authorization information overwrites all existing user authorization information.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authorization-modify mode** { **modify** | **overlay** }

**undo authorization-modify mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **modify** | Indicates the modify mode. | - |
| **overlay** | Indicates the overlay mode. | - |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the **authorization-modify mode** command to configure one of the following update modes for user authorization information delivered by the authorization server:

* modify: modification mode indicating that new user authorization information overwrites only existing user authorization information of the same type.
* overlay: overwriting mode indicating that new user authorization information overwrites all existing user authorization information.

Example
-------

# Set the update mode of user authorization information delivered by the authorization server to modify.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-modify mode modify

```