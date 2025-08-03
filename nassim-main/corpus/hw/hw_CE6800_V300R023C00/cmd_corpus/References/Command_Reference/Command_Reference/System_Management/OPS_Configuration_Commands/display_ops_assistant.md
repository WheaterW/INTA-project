display ops assistant
=====================

display ops assistant

Function
--------



The **display ops assistant** command displays information about a maintenance assistant.




Format
------

**display ops assistant** *method* [ **name** *assistant-name* ]

**display ops assistant** *method* **default** [ **name** *asstDefName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *method* | Displays the operation mode of a specified assistant. | The value can be current, history, or verbose.   * current: indicates the status of a configured assistant. * history: indicates the running records of a configured assistant. * verbose: displays detailed information about a configured assistant. |
| **name** *assistant-name* | Specifies the name of a maintenance assistant. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **default** | Specifies information about a default maintenance assistant. | - |
| *asstDefName* | Specifies the name of a default maintenance assistant. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view information about a maintenance assistant, run the display ops assistant command.After an alarm is generated, a log is recorded, or a timer expires, the maintenance assistant can be executed.

* The alarm content is displayed in XML format in the command output.
* The log content is displayed in the format specified in the log file in the command output.
* The timer is displayed in the time format in the command output.A maximum of the latest 100 maintenance assistant executions can be displayed in history information.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of configured OPS assistants.
```
<HUAWEI> display ops assistant current name a1
--------------------------------------------------------
Assistant          State      Condition         Type    
--------------------------------------------------------
a1                 ready      timer             command 
--------------------------------------------------------

```

# Display the running records of configured OPS assistants.
```
<HUAWEI> display ops assistant history default
Assistant history information
  Name                  : _bfd_mtp.py
  Type                  : script
  Default assistant     : yes
  1. Running information
    Trigger condition   : subscribe
    Trigger event name  : --
    Trigger time        : 2020-03-29 06:38:56
    Execute start time  : 2020-03-29 06:38:56
    Execute end time    : 2020-03-29 06:39:19
    Execute result      : normal
                
Assistant history information
  Name                  : _bgp_mtp.py
  Type                  : script
  Default assistant     : yes
  1. Running information
    Trigger condition   : subscribe
    Trigger event name  : --
    Trigger time        : 2020-03-29 06:38:56
    Execute start time  : 2020-03-29 06:38:56
    Execute end time    : 2020-03-29 06:39:20
    Execute result      : normal

```

# Display the status of default OPS assistants in the current system.
```
<HUAWEI> display ops assistant current default
--------------------------------------------------------
Assistant          State      Condition         Type    
--------------------------------------------------------
_bfd_mtp.py        ready      alarm             script 
_bgp_mtp.py        ready      alarm             script  
_isis_mtp.py       ready      multiple          script  
_lacp_mtp.py       ready      event             script  
_ospf_mtp.py       ready      event             script  
_ospfv3_mtp.py     ready      event             script  
--------------------------------------------------------

```

**Table 1** Description of the **display ops assistant** command output
| Item | Description |
| --- | --- |
| Assistant history information | Historical information of a maintenance assistant. |
| Assistant | Task name. |
| State | Status of a maintenance assistant:   * init: The maintenance assistant is in the initial state after being created. * ready: The maintenance assistant is ready to perform an action after an event is triggered. * pending: The maintenance assistant has been triggered by an event and is waiting for scheduling. * running: indicates the running state. |
| Condition | Trigger conditions for a maintenance assistant to perform tasks:   * timer: triggered by a timer. * event: triggered by an event. * alarm: triggered by an alarm. * syslog: triggered by system logs. * snmp-notification: triggered by an SNMP notification. * multiple: triggered by multiple conditions. |
| Type | Type of tasks that can be configured for a maintenance assistant:   * script: The maintenance assistant is created using a script. * command: The maintenance assistant is configured using commands. |
| Name | Task name. |
| Default assistant | Whether it is the default maintenance assistant task:   * no. * yes. |
| Running information | Running information of a maintenance assistant. |
| Trigger condition | Trigger conditions for a maintenance assistant to perform tasks:   * timer: triggered by a timer. * event: triggered by an event. * alarm: triggered by an alarm. * syslog: triggered by system logs. * snmp-notification: triggered by an SNMP notification.   subscribe indicates to subscribe to a maintenance assistant. |
| Trigger event name | Name of the event triggering a maintenance assistant task. |
| Trigger time | Time when a maintenance assistant task is triggered. |
| Execute start time | Time when a maintenance assistant task starts. |
| Execute end time | Time when a maintenance assistant task ends. |
| Execute result | Result of a maintenance assistant task. |