traffic-segment default-policy
==============================

traffic-segment default-policy

Function
--------



The **traffic-segment default-policy** command configures the default access control policy for EPG members. This policy takes effect for members in an EPG and members in different EPGs.

The **undo traffic-segment default-policy** command restores the default access control policy for EPG members.



By default, the access control policy for EPG members is deny.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-segment default-policy** { **permit** | **deny** }

**undo traffic-segment default-policy** { **permit** | **deny** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **permit** | Allows packets to pass. | - |
| **deny** | Discards the packets. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a network, you can deploy different servers in EPGs as required. The servers that belong to an EPG are EPG members. Servers in the same EPG are members of the EPG, and servers in different EPGs are members between EPGs. You can run the **traffic-segment default-policy** command to specify an access control policy for EPG members to implement traffic control for EPG members (including members in an EPG and members between EPGs).


Example
-------

# Configure the default access control policy to allow EPG members to communicate with each other.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment default-policy permit

```