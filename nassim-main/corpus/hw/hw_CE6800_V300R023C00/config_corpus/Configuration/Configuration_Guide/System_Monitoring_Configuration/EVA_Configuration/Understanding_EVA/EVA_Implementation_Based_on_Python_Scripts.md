EVA Implementation Based on Python Scripts
==========================================

EVA adds a data subscription module to the Python framework of the OPS and obtains data by loading and parsing Python scripts. Some Python scripts are preset on the device before delivery. EVA also provides Python script-based functions that allow you to customize a Python script to subscribe to required data.

#### Python Scripts

* Preset Python scripts
  
  EVA presets two Python scripts on the device to process CPU usage and memory usage. Data concerning CPU usage and memory usage in these scripts come from the huawei-cpu-memory.yang model used for telemetry data collection. The thresholds of CPU usage and memory usage are both set to 90 in these scripts. When the average value of last three CPU usages or memory usages exceeds the threshold, a log is generated in the script to record the IDs of the involved slot and CPU.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  After the device starts for the first time, you need to configure gRPC to register the preset Python scripts because the addkpi function is used in the preset Python scripts.
  
  + cpuHigh.py
    ```
    def condition():
        e1 = eva.Event()
        kpi1 = e1.addkpi("huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage")
        e1.ret = eva.avg(kpi1, 3) > 90
         
        s1 = eva.Strategy()
        s1.formula = e1
        action1 = eva.log("board  ${e1.slot-id}--${e1.cpu-id} overload")
        s1.addaction(action1)
    ```
  + memHigh.py
    ```
    def condition(): 
        e1 = eva.Event()
        kpi1 = e1.addkpi("huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info/os-memory-usage")
        e1.ret = eva.avg(kpi1, 3) > 90
         
        s1 = eva.Strategy()
        s1.formula = e1
        action1 = eva.log("board  ${e1.slot-id}--${e1.cpu-id} mem overload")
        s1.addaction(action1)
    ```
* Customized Python scripts
  
  EVA also supports customized Python scripts. For details about the classes and functions used for customizing a script, see [Python Function Types Supported by EVA](#EN-US_CONCEPT_0000001584547617__en-us_concept_0000001175292940_section181111048125912).

#### Python Function Types Supported by EVA

The EVA Python module consists of three classes and three types of functions, which comply with the Python syntax.

* Classes built in the EVA Python module
  + Event class: describes data subscription, processing, and judgment.
    
    **Table 1** Event class description
    | Class | Example | Description |
    | --- | --- | --- |
    | Event | e1=eva.Event() | Complies with the standard Python syntax and is used to generate objects of the Event class.  The constructor has no parameter. Its return value is an object of the Event class, which contains a maximum of 15 bytes. |
    
    
    **Table 2** Member functions of the Event class
    | Function Name | Function Description | Example | Parameter | Return Value |
    | --- | --- | --- | --- | --- |
    | addkpi | Subscribes to telemetry data. | e1=eva.Event()  kpi1=e1.addkpi(arg1) | **arg1** indicates the sampling path XPath that can be configured for the telemetry function. | Data returned by the XPath. |
    | addinnerkpi | Subscribes to internal KPI data. | e1 = eva.Event()  kpi1 = e1.addinnerkpi(arg1, arg2) | **arg1** indicates the ID of a component, which is an integer. You can run the **display middleware litedb** { **slot** *slotId* [ **cpu** *cpuId* ] } **command** "record kpimappingdata" command in the diagnostic view to check the **component ID** field.  **arg2** indicates the ID of an internal KPI, which is an integer. You can run the **display middleware litedb** { **slot** *slotId* [ **cpu** *cpuId* ] } **command** "record kpimappingdata" command in the diagnostic view to check the **kpi ID** field. | Internal KPI data returned by the specified component. |
    
    
    **Table 3** Member attributes of the Event class
    | Attribute | Example | Description |
    | --- | --- | --- |
    | ret | e1=eva.Event()  kpi1=e1.addkpi(arg1)  e1.ret=kpi1 >M  **M** is a positive integer, and **>** is a comparison operator of Python. [Table 4](#EN-US_CONCEPT_0000001584547617__en-us_concept_0000001175292940_table555316451110) lists the comparison operators supported by EVA. | **ret** indicates the logical operation result of the telemetry data **kpi1** and threshold **M**.  - True: **kpi1** is greater than **M**. - False: **kpi1** is less than or equal to **M**. |
    | frequency | e1=eva.Event()  e1.frequency=N  **N** is a positive integer. | **frequency** indicates the number of consecutive times an event occurs. When the number reaches the value of **frequency**, the event is identified as a fault. |
    
    
    **Table 4** Comparison operators supported by EVA
    | Operator | Example | Description |
    | --- | --- | --- |
    | == | a==b | Whether **a** is equal to **b**. |
    | != | a!=b | Whether **a** is not equal to **b**. |
    | > | a>b | Whether **a** is greater than **b**. |
    | < | a<b | Whether **a** is less than **b**. |
    | >= | a>=b | Whether **a** is greater than or equal to **b**. |
    | <= | a<=b | Whether **a** is less than or equal to **b**. |
  + LogEvent class: describes the subscription to device logs.
    
    **Table 5** LogEvent class description
    | Class | Example | Description |
    | --- | --- | --- |
    | LogEvent | e1=eva.LogEvent (arg1,arg2) | Complies with the standard Python syntax and is used to generate objects of the LogEvent class.  The constructor supports the **arg1** and **arg2** parameters, each of which is a string of characters. **arg1** indicates the name of a module to be subscribed to, and **arg2** indicates a system event name of this module. |
  + Strategy class: describes the orchestration and execution actions of events.
    
    **Table 6** Strategy class description
    | Class | Example | Description |
    | --- | --- | --- |
    | Strategy | s1=eva.Strategy() | Complies with the standard Python syntax and is used to generate objects of the Strategy class.  The constructor has no parameter. Its return value is an object of the Strategy class, which contains a maximum of 15 bytes. |
    
    
    **Table 7** Member functions of the Strategy class
    | Function Name | Function Description | Example | Parameter | Return Value |
    | --- | --- | --- | --- | --- |
    | addaction | Adds actions to the action list of the strategy object. | s1=eva.Strategy()  s1.addaction(arg1) | **arg1** indicates an action function built in the EVA module. For details about the action functions supported by the EVA module, see [Table 11](#EN-US_CONCEPT_0000001584547617__en-us_concept_0000001175292940_table1456815410112).  A strategy can contain a maximum of five actions. | None |
    
    
    **Table 8** Member attributes of the Strategy class
    | Attribute | Example | Description |
    | --- | --- | --- |
    | formula | s1=eva.Strategy()  s1.formula = e1 & e2  **e1** and **e2** indicate the event objects defined in the script. **&** indicates the logical relationship between the events.  NOTE:  **e1** and **e2** must be objects of the Event class. | Strategy formula, which consists of event objects and logical operators. For details about the logical operators supported by EVA, see [Table 9](#EN-US_CONCEPT_0000001584547617__en-us_concept_0000001175292940_table205611146115).  s1.formula = e1 & e2  If both **e1** and **e2** occur within the time period specified by **validTime**, the strategy is matched successfully.  NOTE:  A strategy formula can contain a maximum of five event objects. |
    | validTime | s1=eva.Strategy()  s1. validTime = N  **N** is a positive integer. | Validity period, in seconds.  Describes the time difference between the first event and the last event when multiple events in a formula occur.  All events in a strategy formula are considered to have occurred only when the time difference between the first event and the last event is less than or equal to the time period specified by **validTime**. |
    
    
    **Table 9** Logical operators supported by EVA
    | Operator | Example | Description |
    | --- | --- | --- |
    | & | arg1&arg2 | **arg1** and **arg2** are event objects. The expression result is true only when both **arg1** and **arg2** are true. |
    | | | arg1|arg2 | **arg1** and **arg2** are event objects. The expression result is false only when both **arg1** and **arg2** are false. |
    | () | (arg1|arg2)&arg3 | **arg1**, **arg2**, and **arg3** are event objects. () is a priority symbol, indicating that the | operation is performed on **arg1** and **arg2** first, and then the & operation is performed on the | operation result and **arg3**. |
* Functions built in the EVA Python module
  + Calculation function: calculates the data subscribed through telemetry and KPI data.
    
    **Table 10** Built-in calculation functions
    | Function Name | Function Description | Usage | Parameter Description |
    | --- | --- | --- | --- |
    | eva.avg | Calculates the average value of data obtained the last *N* times. The return value is a floating-point number. | eva.avg(arg1,arg2) | - **arg1** indicates the data defined in the EVA script. - **arg2** indicates the value of *N*, which is an integer in the range from 1 to 3. If the value of *N* is greater than 3, the value 3 is used. |
    | eva.max | Calculates the maximum value of data obtained the last *N* times. The return value is a floating-point number. | eva. max (arg1,arg2) | - **arg1** indicates the data defined in the EVA script. - **arg2** indicates the value of *N*, which is an integer in the range from 1 to 3. If the value of *N* is greater than 3, the value 3 is used. |
    | eva.min | Calculates the minimum value of data obtained the last *N* times. The return value is a floating-point number. | eva.min(arg1,arg2) | - **arg1** indicates the data defined in the EVA script. - **arg2** indicates the value of *N*, which is an integer in the range from 1 to 3. If the value of *N* is greater than 3, the value 3 is used. |
    | eva.minus | Calculates the difference between the current and previous data values. | eva.minus (arg1) | **arg1** indicates the KPI value defined in the EVA script. |
    | eva.roc | Calculates the change ratio of data values using the following formula: Change ratio = (Current data value â Previous data value/Previous data value) | eva.roc(arg1) | **arg1** indicates the data defined in the EVA script. |
  + Action function: defines the actions to be executed in a strategy.
    
    **Table 11** Action functions
    | Function Name | Function Description | Usage | Parameter Description |
    | --- | --- | --- | --- |
    | eva.log | Displays logs. | eva.log(arg1) | **arg1** is a character string. You can use $ in the character string to reference the data attributes obtained from the XPath. |
    | eva.exescript | Runs the next script. | eva.exescript (arg1,arg2) | - **arg1** indicates the name of the EVA script to be executed. - **arg2** indicates the maximum duration for running the EVA script. The unit is second. |
    | eva.get | Obtains data. | eva.get(arg1) | **arg1** indicates the XPath supported by NETCONF. |
  + Cross-script parameter transfer function: includes the output parameter and input parameter functions, which are used to transfer parameters between multiple scripts.
    - Output parameter function: sends parameters from the current script to the script that invokes them.
    - Input parameter function: receives parameters from the script that provides them.
    
    **Table 12** Cross-script parameter transfer functions
    | Function Name | Function Description | Usage | Parameter Description |
    | --- | --- | --- | --- |
    | eva.outPara | Output parameter function. | eva.outPara(arg1,arg2) | - **arg1** indicates the alias of the output parameter. - **arg2** indicates the output parameter of the EVA script. Generally, **arg2** comes from a key node in an XPath. |
    | eva.getPara | Input parameter function. | eva.getPara (arg1) | **arg1** indicates the alias of the output parameter of the invoked script. |