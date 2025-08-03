Obtaining Environment Variables
===============================

Obtaining Environment Variables

#### Application Phase

Subscription and execution phases


#### Function Prototype

result1\_value, result2\_description = \_ops.environment.get("envName")


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| envName | Specifies the name of an environment variable. | The value is a string of 1 to 31 characters. |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value and is an environment variable value. The value is a character string or **None**. If the first return value is a digit, it must be converted through int(). If the first return value is a character string, **None** indicates a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

Environment variables are classified into user-defined environment variables and system environment variables.

* System environment variables are supported by a device by default, and cannot be created, deleted, or modified. A system environment variable name starts with an underscore (\_), and a system environment variable value is determined by the system.
  
  System environment variables include:
  
  + Public environment variables: can be used for all types of events.
  + Event environment variables: can only be used for specified events. Its value is obtained when an event is triggered and indicates some information about the event.
  
  If the subscribed event does not occur, some event-related environment variables cannot be obtained.
  
  [Table 1](#EN-US_TOPIC_0000001654962764__table438893613816) shows the system environment variables currently supported by the OPS.
  
  **Table 1** System environment variables
  | Event | Environment Variable Name | Environment Variable Description | Application Phase |
  | --- | --- | --- | --- |
  | All events | \_event\_type | Event type | Execution phase |
  | \_event\_name | Event name | Execution phase |
  | \_event\_datetime | Time when an event is received | Execution phase |
  | \_event\_level | Event level | Execution phase |
  | \_assistant\_name | Assistant name, or script name | Subscription and execution phases |
  | \_sysname | Device name | Subscription and execution phases |
  | \_event\_hits | Number of times that the current event occurs within the last period | Execution phase |
  | \_para\_xxx | Event parameters | Execution phase |
  | Command | \_cli\_input | Command entered by a user (an incomplete keyword, such as **dis dev**) | Execution phase |
  | \_cli\_command | Command entered by a user (a complete keyword, such as **display device**) | Execution phase |
  | \_cli\_view | CLI view name | Execution phase |
  | \_cli\_trigger | CLI triggering point | Execution phase |
  | \_cli\_username | User name | Execution phase |
  | \_cli\_vty | User channel | Execution phase |
  | \_cli\_ip | User channel IP address | Execution phase |
  | Timer | \_timer\_type | Timer type | Execution phase |
  | Route change | \_routing\_network | Network prefix | Execution phase |
  | \_routing\_mask | Network mask | Execution phase |
  | \_routing\_protocol | Network protocol | Execution phase |
  | \_routing\_type | Change type | Execution phase |
  | \_routing\_nexthop | Next hop | Execution phase |
  | \_routing\_interface | Interface name | Execution phase |
  | \_routing\_cost | Cost value | Execution phase |
  | \_routing\_preference | Priority value | Execution phase |
  | Alarm | \_alarm\_name | Alarm name | Execution phase |
  | \_alarm\_datetime | Time when an alarm was generated | Execution phase |
  | \_alarm\_state | Alarm status | Execution phase |
  | \_alarm\_level | Alarm severity (**critical**, **major**, **minor**, or **warning**) | Execution phase |
  | \_para\_xxx | Alarm event parameters | Execution phase |
  | Trap | \_trap\_oid | Trap OID | Execution phase |
  | System log | \_syslog\_content | System log content | Execution phase |
* User-defined environment variables
  
  In a Python script, you can enter a self-defined environment variable name in the location where a parameter needs to be entered to indicate that an environment variable value needs to be referenced. When the system is running the Python script, it replaces the environment variable name with an environment variable value. To change the parameter value, you can directly change it on the device without having to change and install the Python script again. You can use self-defined environment variables to simplify the configuration and improve flexibility and feasibility of Python scripts.
  
  The name of a user-defined environment variable starts with a letter and can contain letters, digits, and underscores (\_). It applies to all types of events and can be used in the subscription and execution phases. The value can be configured using the [**environment**](cmdqueryname=environment) command. You can create, modify, and delete user-defined variables.

#### Usage Examples

After the subscribed event is matched, the current lsID value is output to the terminal.

```
import ops
opsObj = ops.ops()
value, result = _opsObj.environment.get("_sysname")
print("result is", result, "and sysname is", value)
```