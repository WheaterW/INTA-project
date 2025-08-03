Closing a CLI Channel
=====================

Closing a CLI Channel

#### Application Phase

Execution phase


#### Function Prototype

result1\_value, result2\_description = \_ops.cli.close(fd)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| fd | Specifies a CLI channel handle. | It is generated through the API described in [Opening a CLI Channel](vrp_ops_cfg_0039.html). |



#### Return Values

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value and describes the result. This value is a character string.


#### Usage Description

After a device delivers CLIs, you can close a CLI channel to release VTY resource.


#### Usage Examples

When a subscription event is matched, you can close the CLI channel.

```
ret = _ops.cli.close(handle)
```