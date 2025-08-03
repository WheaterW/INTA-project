EVA Fundamentals
================

EVA Fundamentals

#### Implementation

EVA is a function that uses scripts to analyze and judge data collected by devices and perform troubleshooting based on the analysis and judgment result. You can load a customized script on a device. The device parses the script, collects data based on a defined event, and executes the action defined in the script based on a strategy.

EVA can obtain the following data using scripts: data dynamically subscribed through telemetry, log data subscribed through the log module, alarm data subscribed through the alarm module, subscribed KPI data, and data queried using the NETCONF function.

EVA provides the following capabilities:

* Data openness based on scripts
  
  With the programmability of the device, EVA allows you to define data subscription interfaces in scripts.
* Powerful data processing
  
  EVA provides data calculation and data judgment functions. Data calculation functions can be used to calculate the average, maximum, and minimum values. You can directly invoke these functions in scripts to process subscribed data.
* Strategy customization and open fault orchestration
  
  EVA supports customized strategies, in which one or more faults can be combined using strategy formulas.
* Action execution
  
  EVA provides action execution capabilities. When a fault strategy formula is met, EVA executes actions in a customized strategy to troubleshoot device faults.

The preceding capabilities can be used only after the EVA module is introduced to customized scripts. Currently, EVA supports only Python and JSON scripts.


#### Working Process

[Figure 1](#EN-US_CONCEPT_0000001512831026__fig4283162494414) shows the EVA working process. You can introduce the EVA module to a customized script, upload the compiled script to the device, and register the script. EVA automatically parses the script and runs the content defined in the script to analyze the device status data and troubleshoot faults.

**Figure 1** EVA working process  
![](../images/en-us_image_0000001513030614.png)

By default, EVA subscribes to data including the CPU usage and memory usage, and stores the data generated within a period of time in the memory. You can query this historical data.


#### Basic Concepts in an EVA Script

* Event
  
  An event is used to define the entry conditions for running a script.
* Strategy
  
  A strategy is used to define an event or an event combination condition for executing a task or an action.
* Task (used only in JSON scripts)
  
  A task is used to define an action triggered by a strategy and the relationship between actions. Each task contains one action.
  
  If the service logic is complex, you can define multiple tasks and define in a task the jump relationship between the task and other tasks. The service logic of the loop type is also defined in a task.
* Action
  
  Actions are used to define device behaviors, including command delivery (currently, only display and search commands can be run), NETCONF operations (only Get operations are supported currently), and data calculation.

In EVA scripts, events are used to define fault symptoms, and strategies and tasks/actions are used to define operations performed after faults occur. The device automatically records fault data after a fault occurs, without the need of manually collecting onsite data by O&M personnel.