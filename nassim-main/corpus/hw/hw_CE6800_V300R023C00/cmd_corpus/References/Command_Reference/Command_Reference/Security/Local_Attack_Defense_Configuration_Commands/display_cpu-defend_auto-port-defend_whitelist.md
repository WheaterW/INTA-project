display cpu-defend auto-port-defend whitelist
=============================================

display cpu-defend auto-port-defend whitelist

Function
--------



The **display cpu-defend auto-port-defend whitelist** command displays information about the interface attack defense whitelist.




Format
------

**display cpu-defend auto-port-defend whitelist slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the whitelist for port attack defense is configured or when you locate faults on network, run the **display auto-port-defend whitelist** command to verify whitelist information. If no whitelist is configured, the command displays no whitelist information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the interface attack defense whitelist in the slot.
```
<HUAWEI> display cpu-defend auto-port-defend whitelist slot 1
  Protocol       Interface                 IP                                         ACL      Status                               
-----------------------------------------------------------------------------------------------------                               
    --              --                     --                                        2000      manual                               
    --           100GE1/0/1                --                                         --       manual                               
-----------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend auto-port-defend whitelist** command output
| Item | Description |
| --- | --- |
| Protocol | Protocol type of packets free from the interface attack defense action. If no packet protocol type is specified in the whitelist rule, this field displays --. |
| Interface | Interface free from the attack defense action. If the whitelist is configured based on ACL rules, this field displays --. |
| IP | Source IP address of packets free from the interface attack defense action. If no IP address is specified in the whitelist rule, this field displays --. |
| ACL | ACL number specified in a manually configured whitelist rule. If the whitelist is configured based on interfaces or is automatically delivered, this field displays --. |
| Status | Type of the whitelist rule, which can be:   * auto: An automatically delivered whitelist rule is triggered by services. * manual: You can run the auto-port-defend whitelist whitelist-number { acl acl-number | interface interface-type interface-number } command in the attack defense policy view to configure a whitelist for port attack defense. |