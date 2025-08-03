display task-group
==================

display task-group

Function
--------



The **display task-group** command displays information about a task group.




Format
------

**display task-group** [ *task-group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-group-name* | Task group name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

A task group is a collection of tasks. Tasks can be added to a task group by the read, write-read, and debug permissions or a combination of the three permissions. A task is a set of commands. Generally, a feature or function command belongs to one task. To meet refined permission management, a feature can have multiple tasks. This parameter is predefined in the system and cannot be added, modified, or deleted.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display task group information.
```
<HUAWEI> display task-group
2021-02-24 15:49:40.890                                                                                                             
------------------------------------------------------                                                                              
Task-group-name                          Task-group-id                                                                              
------------------------------------------------------                                                                              
manage-tg                                            1                                                                              
system-tg                                            2                                                                              
monitor-tg                                           3                                                                              
visit-tg                                             4                                                                              
panel-tg                                             5                                                                              
operationlog-tg                                      6                                                                              
syslog-tg                                            7                                                                              
logthreat-tg                                         8                                                                              
alertlog-tg                                          9                                                                              
business-tg                                         10                                                                              
logdownload-tg                                      11                                                                              
session-tg                                          12                                                                              
sysstat-tg                                          13                                                                              
diagnose-tg                                         14                                                                              
pktcapture-tg                                       15                                                                              
statisticacl-tg                                     16                                                                              
sec-tg                                              17                                                                              
nat-tg                                              18                                                                              
cgn-tg                                              19                                                                              
traffic-tg                                          20                                                                              
defend-tg                                           21                                                                              
aspf-tg                                             22                                                                              
cert-tg                                             23                                                                              
address-tg                                          24                                                                              
service-tg                                          25                                                                              
app-tg                                              26                                                                              
authserver-tg                                       27                                                                              
ippool-tg                                           28                                                                              
timerange-tg                                        29                                                                              
urlclass-tg                                         30                                                                              
signature-tg                                        31                                                                              
av-tg                                               32                                                                              
ips-tg                                              33                                                                              
healtcheck-tg                                       34                                                                              
globalsettings-tg                                   35                                                                              
slaquality-tg                                       36                                                                              
urlfilter-tg                                        37                                                                              
interface-tg                                        38                                                                              
pairitf-tg                                          39                                                                              
zone-tg                                             40                                                                              
dns-tg                                              41                                                                              
dhcps-tg                                            42                                                                              
route-tg                                            43                                                                              
ipsec-tg                                            44                                                                              
gre-tg                                              45                                                                              
sysconf-tg                                          46                                                                              
manager-tg                                          47                                                                              
vsys-tg                                             48                                                                              
highreltability-tg                                  49                                                                              
logconf-tg                                          50                                                                              
license-tg                                          51                                                                              
updatecenter-tg                                     52                                                                              
sysupdate-tg                                        53                                                                              
cfgmanager-tg                                       54                                                                              
devm-tg                                             55                                                                              
common-tg                                           56                                                                              
nge-tg                                              57                                                                              
ssl-tg                                              58                                                                              
smp-tg                                              59                                                                              
other-tg                                            60                                                                              
cli-tg                                              61                                                                              
------------------------------------------------------                                                                              
Total 61

```

**Table 1** Description of the **display task-group** command output
| Item | Description |
| --- | --- |
| Task-group-name | Task group name. |
| Task-group-id | Task group ID. |