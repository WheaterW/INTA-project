role
====

role

Function
--------



The **role** command configures the local device as a reflector or client in an iNOF system.

The **undo role** command restores the default configuration.



By default, no role is configured for the local device in an iNOF system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**role** { **reflect-client** | **reflector** }

**undo role** { **reflect-client** | **reflector** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **reflect-client** | Configures a device as a client. | - |
| **reflector** | Configures a device as a reflector. | - |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Devices in an iNOF system need to manage hosts connected to the system. When there are a large number of access devices, you need to configure hosts to be managed on each access device. To simplify operations, you can configure the iNOF reflector function so that iNOF devices exchange iNOF packets to synchronize related configurations.You can run this command to configure the local device as a reflector or client in the iNOF system.


Example
-------

# Configure the local device as a client in the iNOF system.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] role reflect-client

```