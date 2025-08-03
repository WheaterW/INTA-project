assistant
=========

assistant

Function
--------



The **assistant** command creates a maintenance assistant or displays a maintenance assistant view.

The **undo assistant** command cancels the configuration.



By default, no maintenance assistant is created.


Format
------

**assistant** *assistant-name*

**undo assistant** *assistant-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *assistant-name* | Specifies the name of a maintenance assistant. | The value is a string of 1 to 15 characters starting with letters and containing only underlines (\_), letters, and numbers.  The value is case-sensitive when being configured for the first time and becomes case-insensitive during subsequent access or quotation. |



Views
-----

OPS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a triggering condition and a working task, run the assistant command. When the working condition is met, the system automatically runs the commands in the command line file.

**Configuration Impact**

After the triggering condition of a maintenance assistant is met, the task is placed in the scheduling queue and waits to be executed. This is called an instance of the task. Only one task instance can be executed at any time. Task instances in a scheduling queue are executed in sequence. To be specific, when a task instance is being executed, other task instances in the scheduling queue are not executed.

**Follow-up Procedure**

* Run the condition alarm level, condition name, or condition timer cron command to configure a triggering condition.
* Run the execute command, execute batch-file, or execute python command to configure a working task.

**Precautions**

* The OPS supports a maximum of 100 maintenance assistant tasks.
* When task instances are executed in a scheduling queue, the same instance of the same task can be executed only once, and repeated instances will be combined.
* A maintenance assistant task is ready only after the triggering condition and working task are configured.
* When the triggering conditions for multiple maintenance assistant tasks are met, the tasks are executed in sequence. When a maintenance assistant task is being performing or is waiting for scheduling in a queue, the maintenance assistant task does not trigger a second queuing.
* If one condition triggers multiple maintenance assistant tasks, these tasks are executed in no specific sequence.
* If the triggering condition is modified when a maintenance assistant task is being performed, the task is forcibly ended and is not performed until the new triggering condition is met.
* Running the shutdown (maintenance assistant view) command before modifying the configuration of a maintenance assistant task is recommended.

Example
-------

# Create a maintenance assistant named ops and enter the maintenance assistant view.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant ops
[*HUAWEI-ops-assistant-ops]

```