Subscribing to KPI Events
=========================

Subscribing to KPI Events

#### Application Phase

Subscription phase


#### Function Prototype

kpi\_event = ops.kpi.event(tag)

ops.kpi.event.add\_kpi(kpi\_xpath)

ops.kpi.event.add\_inner(cid, kid)

ops.kpi.event.set\_threshold(relation, threshold)

ops.kpi.event.set\_compute\_rule(function, para = "")

result1\_value, result2\_description = ops.kpi.subscribe(kpi\_event)


#### Parameter Description

| Parameter | Description | Value |
| --- | --- | --- |
| tag | Specifies conditions. | The value is a string of 1 to 7 case-insensitive characters, consists of letters, digits, and underscores (\_), and starts with a letter. The value of tag cannot be **""**, **None**, **and**, **or**, or **andnot**, and cannot contain the end character **\0**. |
| kpi\_xpath | Specifies the name of the KPI to be subscribed to. | The value is the sampling path XPath that can be configured for the telemetry function. |
| cid | Specifies the ID of a component. | The value is an integer. You can run the **display middleware litedb**{ **slot** *slotId* [ **cpu** *cpuId* ] } **command** "record kpimappingdata" command in the diagnostic view and obtain the component ID based on the **componentID** field in the command output. |
| kid | Specifies the ID of a KPI. | The value is an integer. You can run the **display middleware litedb**{ **slot** *slotId* [ **cpu** *cpuId* ] } **command** "record kpimappingdata" command in the diagnostic view and obtain the KPI ID based on the **kpiID** field in the command output. |
| relation | Specifies the relational function used for triggering conditions. | The value is of the enumerated type:   * >=: greater than or equal to * >: greater than * <=: less than or equal to * <: less than * ==: equal to * !=: not equal to |
| threshold | Specifies a threshold. | The value is a string of 1 to 49 characters, excluding the end character **\0**. |
| function | Specifies a preprocessing function. | The value is of the enumerated type. Five types of functions are supported: avg, max, min, minus, and roc. |
| para | Specifies the parameters for the preprocessing function. | The value is an integer. If the preprocessing function is avg, max, or min, you need to set this parameter. |



#### Return Values

In the function prototype, **kpi\_event** indicates the generated KPI event instance, which is used for setting event rules and subscribing to events.

**result1\_value** and **result2\_description** in the function prototype indicate return values.

**result1\_value** is the first return value, with value 0 indicating a success, and value 1 indicating a failure.

**result2\_description** is the second return value, indicating the failure cause. It is returned only when the first return value is 1.


#### Usage Description

By subscribing to KPI events, users can monitor important data such as the CPU usage and memory usage.

When the KPI event subscription interface (ops.kpi.subscribe) is used:

* The system automatically obtains the script name. Ensure that the script name ends with .py. Otherwise, event subscription fails.
* If the KPI event creation interface (ops.kpi.event) is used to create multiple events in the same script, ensure that the event names (tags) are different.
* When subscribing to KPI events, you do not need to enter the message type (message\_type). The default message type is subscribe, indicating data subscription.
* There are two enumerated values of the subscription type: inner and xpath. The inner type corresponds to an internal KPI. For example, the KPI name of the CPU usage is 167/0. The xpath type corresponds to the resource node path. The KPI name of the CPU usage is huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage.
* If the subscription type is multiple, you need to specify the AND or OR relationship between multiple event subscriptions. If the relationship is not specified, the subscription fails.

#### Usage Examples

Create a script named test\_inner.py, subscribe to KPI events of the inner type, and trigger an alarm when the CPU usage exceeds 90%.

```
def ops_condition(_ops)
    e1 = _ops.kpi.event("cpu")
    e1.add_inner(10167, 0)
    e1. set_threshold(">", 90)
    e1. set_compute_rule("avg", 5)
    _ops.kpi.subscribe(e1)
```

Create a script named test\_xpath.py, subscribe to XPath KPI events, and trigger an alarm when the CPU usage exceeds 90%.

```
def ops_condition(_ops)
    e1 = _ops.kpi.event("cpu")
    e1.add_kpi("huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage")
    e1. set_threshold(">", 90)
    e1. set_compute_rule("avg", 5)
    _ops.kpi.subscribe(e1)
```

Subscribe to multiple KPI events at the same time and specify the OR relationship between the events.

```
def ops_condition(_ops)
    e1 = _ops.kpi.event("cpu1")
    e1.add_inner(10167, 0)
    e1. set_threshold(">", 90)
    e1. set_compute_rule("avg", 5)
    _ops.kpi.subscribe(e1)
 
    e2 = _ops.kpi.event("cpu2")
    e2.add_kpi("huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage")
    e2. set_threshold(">", 90)
    e2. set_compute_rule("avg", 5)
    _ops.kpi.subscribe(e2)
 
    _ops.correlate("cpu1 and cpu2")
```