Opening a CLI Channel
=====================

Opening a CLI Channel

#### Application Phase

Execution phase


#### Function Prototype

result1\_handle, result2\_description = \_ops.cli.open()


#### Parameter Description

None


#### Return Values

**result1\_handle** and **result2\_description** in the function prototype indicate return values.

First return value: The value **None** indicates an error. Other values indicate command handles.

The second return value indicates the failure cause if the first return value is **None**.


#### Usage Description

Commands can be delivered to a device only after the CLI channel is opened in a Python script.

A script can be used to create only one CLI channel. If an attempt is made to create a second CLI channel using this script, the system returns a failure.

A VTY resource is consumed for every CLI channel opened. The [**display users**](cmdqueryname=display+users) command shows that a VTY resource is consumed by an assistant (Assistant: Name). When only three or less VTY resources are available, opening a CLI channel fails. Therefore, after a CLI channel is created and commands are executed in the script, the CLI channel needs to be closed in a timely manner through the API (\_ops.cli.close(fd)) described in [Closing a CLI Channel](vrp_ops_cfg_0041.html) to save VTY resources.

The APIs described in [Executing Commands](vrp_ops_cfg_0040.html) and [Closing a CLI Channel](vrp_ops_cfg_0041.html) use the first return value of the interface for opening a CLI channel as the input parameter. So the return value must be specified when the opening CLI channel API is used.


#### Usage Examples

When the subscribed event is matched, the CLI channel is opened and related commands are executed.

```
handle, err_desp= _ops.cli.open()            # Open a CLI channel.
_ops.cli.execute(handle,"system-view")       # Run the system-view command to enter the system view.
_ops.cli.execute(handle,"system-view")       # Run the pm command to enter the PM view.
```