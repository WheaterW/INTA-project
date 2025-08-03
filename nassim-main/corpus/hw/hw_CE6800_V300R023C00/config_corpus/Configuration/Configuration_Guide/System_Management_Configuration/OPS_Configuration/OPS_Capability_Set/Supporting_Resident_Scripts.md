Supporting Resident Scripts
===========================

Supporting Resident Scripts

#### Application Phase

Execution phase


#### Function Prototype

result1\_value = \_ops.wait()


#### Parameter Description

None


#### Return Values

**result1\_value** in the function prototype indicates the return value.

First return value: The value 0 indicates that the action is executed successfully, and a non-zero value indicates that the action times out.


#### Usage Description

In most circumstances, a process needs to be started before and stopped after a Python script is executed. It takes some time to start and stop a process. If the subscription event in the script is triggered for multiple times, the device needs to start a process before executing the action defined in the subscription phase and stop the process after the action is complete. In this case, you can use a resident script to reduce the time a device waits for a process to start or stop.

Resident scripts (also called high-speed scripts) are usually used together with loop counters. After a subscription event is matched, the device starts a process when it performs the action for the first time. After this action is complete, the process is suspended and the number of cycles decreases by one. When the event is matched again, the next action is triggered, and the number of cycles is decreased by one again. This step is repeated until the number of cycles in the script reaches 0, at which point the process is stopped.

The API described in [Returning Event Execution Results](vrp_ops_cfg_0049.html) returns the script processing result and suspends the script until the next event occurs. This implements resident script processing.


#### Usage Examples

The device starts a process, and then the process enters the waiting state to wait for the next matching of the subscribed event.

```
test.py 
import ops 
def ops_execute(_ops): 
       a, description = _ops.context.save("wait1",'ac1') 
       _ops.result(1) 
       _ops.wait() 
       a, description = _ops.context.save("wait2",'ac2') 
       return 0
```