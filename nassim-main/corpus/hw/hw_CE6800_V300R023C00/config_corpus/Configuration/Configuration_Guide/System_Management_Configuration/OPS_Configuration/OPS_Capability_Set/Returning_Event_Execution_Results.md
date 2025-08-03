Returning Event Execution Results
=================================

Returning Event Execution Results

#### Application Phase

Execution phase of resident scripts


#### Function Prototype

\_ops.result(status)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| status | Specifies the user script execution result. | The value 0 indicates that the user script is executed successfully, and a value other than 0 indicates that the user script fails to be executed. |



#### Return Values

None


#### Usage Description

In addition to this API, you can also use the return function to return the result.

* If neither \_ops.result() nor return is used, the default value 1 is returned.
* If both \_ops.result() and return are used, the result returned by \_ops.result() takes effect.

If the result API is invoked for multiple times, the value returned by the first result function takes effect.


#### Usage Examples

The device starts a process, and then the process enters the waiting state to wait for the next matching of the subscribed event.

```
test.py 
import ops 
def ops_execute(_ops): 
       a, description= _ops.context.save("wait1",'ac1') 
       _ops.result(1) 
       _ops.wait() 
       a, description= _ops.context.save("wait2",'ac2') 
       return 0
```