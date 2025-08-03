display auto-defend whitelist
=============================

display auto-defend whitelist

Function
--------



The **display auto-defend whitelist** command displays information about the attack source tracing whitelist.




Format
------

**display auto-defend whitelist slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the whitelist for attack source tracing is configured or when you locate faults on network, run the **display auto-defend whitelist** command to verify whitelist information. If no whitelist is configured, the command displays no whitelist information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the attack source tracing whitelist in the slot.
```
<HUAWEI> display auto-defend whitelist slot 1
  Protocol       Interface                 IP                   ACL      Status
-------------------------------------------------------------------------------
    DHCP          100GE1/0/1               --                   --        auto
    DHCP          100GE1/0/1               --                   --        auto
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display auto-defend whitelist** command output
| Item | Description |
| --- | --- |
| Protocol | Protocol type of the packets excluded from attack source tracing. |
| Interface | Interface on which inbound packets are excluded from attack source tracing. |
| IP | Source IP address of the packets excluded from attack source tracing. If not source IP address is specified in the whitelist rule, this field displays --. |
| ACL | ACL number specified in a manually configured whitelist rule. If the whitelist rule is automatically delivered, this field displays --. |
| Status | Type of the whitelist rule, which can be:  auto: An automatically delivered whitelist rule is triggered by services.  manual: You can run the auto-defend whitelist command in the attack defense policy view to manually configure an attack source tracing whitelist. |