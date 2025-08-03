EVA Implementation Based on JSON Scripts
========================================

EVA obtains data by loading and parsing JSON scripts. Some JSON scripts are preset on the device before delivery. EVA also provides JSON script-based functions that allow you to customize a JSON script to subscribe to required data.

#### JSON Scripts

JSON scripts are classified into single-task scripts and PMI scripts based on the number of scripts in the script file.

* Single-task scripts
  
  A single-task script is a JSON script file that contains only one script.
  
  An example of a single-task script is as follows:
  
  ```
  {
  	"ItemName": {
  		"description": "",
  		"define": {},
  		"events": {},
  		"strategy": "",
  		"tasks": {}
          }
  }
  ```
* PMI scripts
  
  A PMI script is a JSON script file that contains multiple scripts. After the PMI script is loaded and registered on the device, the device has the PMI function. The PMI result is saved to the **flash:/eva** directory and the file name is **eva\_inspection\_***current time***.zip**.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  The content of a single script in a PMI script is compressed in single-line mode. Each script must occupy a line.
  
  An example of a PMI script is as follows:
  
  ```
  {"ItemName1": {"description": "","define": {},"events": {},"strategy": "","tasks": {}}}
  {"ItemName2": {"description": "","define": {},"events": {},"strategy": "","tasks": {}}}
  {"ItemName3": {"description": "","define": {},"events": {},"strategy": "","tasks": {}}}
  ```

JSON scripts are classified into preset scripts and customized scripts based on whether they are preset on the device before delivery.

* Preset scripts
  
  A preset script is a script delivered with the device. By default, the preset scripts are automatically loaded and registered.
  
  EVA presets a JSON script on a device to query exception information on the device. The script issues the diagnosis command to query device exception information every 24 hours. If any exception information is found, a failure message is displayed.
  
  + SystemExceptionCheck.json
    ```
    {
    	"SystemExceptionCheck": {
    		"description": "system exception check",
    		"define":{
    			"str_Prob_Adv": "**There were CPU exceptions.@@@**Please contact engineers."
    		},
    		"events": {
    			"e1": {
    				"trigger": "eva.cycle(24)"  
    			}
    		},
    		"strategy": "e1",
    		"tasks": {
    			"mainTask": {
    				"parameters": {
    					"cmd": "display exception 10 verbose all" 
    				},
    				"action": "eva.cli(\"diagnose\",${cmd})",
    				"publish": {
    					"exp_Result": "${result}" 
    				},
    				"switch": {
    					"eva.fail(${str_Prob_Adv})": "eva.strContainsIgnoreCase(${exp_Result}, \"Exception info\") == true" 
    			}
    		}
    	}
    }
    
    ```
* Customized scripts
  
  A customized script is a script edited by users based on the JSON function type provided by EVA. For details about the functions used for customizing a script, see [JSON Function Types Supported by EVA](#EN-US_CONCEPT_0000001563990837__section9145021617).

#### Data Storage

The device processes data in different ways based on the functions contained in a JSON script.

* If eva.fail is executed, the data collected by the task is stored in the **flash:/eva/checkresult** directory. The file name is **checkresult\_***current time* and the file name extension is .zip or .txt.
* If eva.singleCollect() is executed, the data collected by the task is stored in the **flash:/eva/collection** directory. The file name is **collection\_***current time* and the file name extension is .zip or .txt.
* If eva.singleCollect() and eva.fail are not executed, the collected data is not stored.

If the JSON script is a PMI script, the device compresses the contents in the **flash:/eva/checkresult** and **flash:/eva/collection** directories into the **eva\_inspection\_***current time***.zip** package and saves the package to the **flash:/eva** directory after the PMI. After the **eva\_inspection\_***current time***.zip** package is compressed, the content in the **flash:/eva/collection** directory is deleted. If the device directly downloads the script from the FTP or SFTP server and installs and registers the script, it automatically uploads the content in the **flash:/eva** directory to the server and deletes the **eva\_inspection\_***current time***.zip** package after the PMI.

If the PMI script is delivered by a PMI tool, the PMI tool obtains the **eva\_inspection\_***current time***.zip** file and deletes the file and PMI script after the PMI is complete.


#### JSON Function Types Supported by EVA

**Fields in a JSON Script of EVA**

An example of a JSON script is as follows:

```
{"ItemName": {"description": "","define": {},"events": {},"strategy": "","tasks": {}}}
```

**Table 1** Fields in a JSON script of EVA
| Field | Description | Attribute | Type | Value Range |
| --- | --- | --- | --- | --- |
| *ItemName* | Script name. | Mandatory | Customized | The value is a string of 2 to 31 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_).  For a single-task script, the script name must be the same as the value of *ItemName*. The script name is *ItemName*.json. |
| description | Script description. | Optional | Keyword | The value is a string of 1 to 256 characters. Chinese characters and special characters are supported. Each Chinese character is considered as three English characters. |
| define | Global variable definition. | Optional | Keyword | For details, see [â¢ Global variable define](#EN-US_CONCEPT_0000001563990837__li8888135525910). |
| events | Event definition. | Mandatory | Keyword | For details, see [â¢ events](#EN-US_CONCEPT_0000001563990837__li7946141105211). |
| strategy | Strategy definition. | Mandatory | Keyword | For details, see [â¢ strategy](#EN-US_CONCEPT_0000001563990837__li15817536540). |
| tasks | Task definition. | Mandatory | Keyword | For details, see [â¢ tasks](#EN-US_CONCEPT_0000001563990837__li1925501419555). |

* **Global variable define**
  
  The global variable **define** is used to define global variables for the entire script. A maximum of 15 global variables can be defined. Other variables cannot be referenced.
  
  ```
  "define": {"name": value}
  ```
  
  **Table 2** Fields in the global variable **define**
  | Field | Description | Attribute | Type | Value Range |
  | --- | --- | --- | --- | --- |
  | *name* | Name of a variable. | Mandatory | Customized | The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). The variable name must be globally unique and cannot be **result**. |
  | *value* | Value of a variable. | Mandatory | Customized | For details about the variable types supported by the global variable **define**, see [Table 3](#EN-US_CONCEPT_0000001563990837__table4198711614). |
  
  
  **Table 3** Variable types supported by **define**
  | Variable Type | Usage Description | Value Description |
  | --- | --- | --- |
  | Boolean type | "define": {"aa": *value*} | *value*: The value can be true or false. |
  | Integer type | "define": {"bb": *value*} | *value*: The value ranges from 0 to 4294967295. |
  | Character string type | "define": {"MemoryXpath": "*value*"} | *value*: The value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters. |
  | String array type | "define": {"cc": ["*value1*", â¦â¦, "*valuen*"]} | The total length of array members cannot exceed 1600 characters. The members are character strings. Chinese characters are supported. Each Chinese character is considered as three English characters. |
  | Integer array type | "define": {"dd": [*value1*, â¦â¦, *value80*]} | A maximum of 80 members are supported. The value of each member ranges from 0 to 4294967295. |
  | Object type | "define": {"ee": {"*name*": "*value*"}} | Only one layer of object is supported. An object supports a maximum of five members.  *name*: specifies the variable name in the object value. The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). The variable name must be globally unique and cannot be **result**.  *value*: specifies the value of the variable in the object value. The value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters. |
  
  An example of a variable of the Boolean type is as follows:
  
  ```
  "define": {"aa": false}
  ```
  
  An example of a global variable of the integer type is as follows:
  
  ```
  "define": {"bb": 123}
  ```
  
  An example of a global variable of the character string type is as follows:
  
  ```
  "define": {"MemoryXpath": "huawei-cpu-memory:cpu-memory/board-cpu-core-infos/board-cpu-core-info"}
  ```
  
  An example of a global variable of the string array type is as follows:
  
  ```
  "define": {"cc": ["system", "user", "diagnose"]}
  ```
  
  An example of a global variable of the integer array type is as follows:
  
  ```
  "define": {"dd": [1, 2, 3]}
  ```
  
  An example of a global variable of the object type is as follows:
  
  ```
  "define": {"ee": {"eee1": "huawei-cpu-memory:cpu-memory/board-cpu-core-infos/board-cpu-core-info",
  		  "eee2": "cde"}}
  ```
  
  Variables defined by **define** can be referenced by the entire script. The reference mode of all variables is ${}. [Table 4](#EN-US_CONCEPT_0000001563990837__table8539113819290) lists the supported variable reference formats.
  
  **Table 4** Variable reference formats in a JSON script
  | Variable Reference Format | Format Description | Parameter Description |
  | --- | --- | --- |
  | ${*value*1} | All variable types can be referenced. | *value1* specifies the name of a variable. |
  | ${*value1*[*number*]} | The type of the referenced variable is string array or integer array. | *value1* specifies the name of a variable.  *number* specifies the array sequence, such as 0, 1, and 2. |
  | ${*value1*[*value2*]} | The type of the referenced variable is string array or integer array. | *value1* and *value2* specify variable names. |
  | ${*value1*.*value2*} | The type of the referenced variable is object. | *value1* specifies the name of a variable.  *value2* specifies the name of the variable in the object value. |
* **events**
  
  **events** describes data subscription, processing, and judgment. A single event or multiple events can be configured. A maximum of five events are supported.
  
  ```
  "events": {"name1": {"trigger": "Trigger-Condition1"},{"name2": {"trigger": "Trigger-Condition2"}}
  ```
  
  **Table 5** Fields in **events**
  | Field | Description | Attribute | Type | Value Range |
  | --- | --- | --- | --- | --- |
  | *name* | Event name. | Mandatory | Customized | The value is a string of two case-sensitive characters. It starts with a letter and can contain only letters and digits. |
  | trigger | Trigger condition. | Mandatory | Keyword | - |
  | *Trigger-Condition* | Trigger condition. | Mandatory | Customized | For details about the value, see [Table 6](#EN-US_CONCEPT_0000001563990837__table87171339235). |
  
  
  **Table 6** Event triggering conditions
  | Trigger Type | Function Name | Usage | Parameter Description |
  | --- | --- | --- | --- |
  | Triggered by KPI conditions | eva.kpi | eva.kpi(*kpiXpath*) > *value*1 | *kpiXpath*: specifies the sampling path. Currently, only the KPI sampling path (for example, CPU usage) queried using the [**display telemetry sensor-path**](cmdqueryname=display+telemetry+sensor-path) command is supported. For details about the supported comparison operators, see [Table 7](#EN-US_CONCEPT_0000001563990837__table6605131219326). The return value is true or false.  *value1*: The value is an integer. |
  | Triggered by logs | eva.logEvent | eva.logEvent("*value2*", "*value3*") | Only non-trap logs are supported.  *value2*: specifies the name of the log template to be subscribed to.  *value3*: specifies the digest of the log information to be subscribed to.  For example, in the AAA/6/RDACCTUP, *value2* is AAA and *value3* is RDACCTUP. |
  | Triggered by alarms | eva.alarmEvent | eva.alarmEvent("*value5*") | *value5*: specifies the digest of the alarm information to be subscribed to.  For example, in **BFD\_1.3.6.1.4.1.2011.5.25.38.3.1 hwBfdSessDown**, *value5* is **hwBfdSessDown**. |
  | Triggered at a scheduled time | eva.cycle | eva.cycle(*value4*) | *value4*: specifies the interval for triggering an event. The value is an integer in the range from 1 to 65535, in hours. Only one timer can be used in an event. |
  | Triggered only once | eva.singleCollect | eva.singleCollect() | The event is triggered only once. The JSON script is automatically uninstalled after it is executed. This trigger condition can be used only in a single-event script.  NOTE:  In a PMI script, **events** can only use eva.singleCollect. |
  
  
  **Table 7** Comparison operators supported in JSON scripts
  | **Operator** | Usage Description | **Description** |
  | --- | --- | --- |
  | **==** | a == b | Whether **a** is equal to **b**. |
  | **!=** | a !=b | Whether **a** is not equal to **b**. |
  | **>** | a>b | Whether **a** is greater than **b**. |
  | **<** | a<b | Whether **a** is less than **b**. |
  | **>=** | a>=b | Whether **a** is greater than or equal to **b**. |
  | **<=** | a<=b | Whether **a** is less than or equal to **b**. |
* **strategy**
  
  **strategy** is used to define the entry conditions of subsequent tasks. When there are multiple events, logical relationships between the events are used to make a judgment.
  
  ```
  "strategy": "event1 | event2"
  ```
  
  **Table 8** Fields in **strategy**
  | Field | Description | Attribute | Type | Value Range |
  | --- | --- | --- | --- | --- |
  | *event1* | Event name. | Mandatory | Customized | Event name defined in the event. |
  | | | Logical operator. | Optional | - | For details, see [Table 9](#EN-US_CONCEPT_0000001563990837__table5668944123617). |
  | *event2* | Event name. | Optional | Customized | Event name defined in the event. |
  
  
  **Table 9** Logical relationships supported by **strategy**
  | **Logical Operator** | Usage Description | **Description** | Value Range |
  | --- | --- | --- | --- |
  | & | *arg1* & *arg2* | The expression result is true only when both events *arg1* and *arg2* are true within one minute. Otherwise, false is returned. | *arg1*, *arg2*, and *arg3* specify defined event names. |
  | | | *arg1* | *arg2* | The expression result is false only when both events *arg1* and *arg2* are false within one minute. Otherwise, true is returned. |
  | () | (*arg1* | *arg2*)& *arg3* | () is a priority symbol, indicating that the | operation is performed on events *arg1* and *arg2* first, and then the & operation is performed on the | operation result and *arg3*.  The expression result is true only when both events *arg1* and *arg2* are true and event *arg3* is true within one minute. Otherwise, false is returned. |
* **tasks**
  
  **tasks** describes the action of an event. The first task in a script must be named **mainTask**. The names of other tasks can be customized but cannot be defined as **mainTask**. A maximum of 15 tasks can be created for a script.
  
  ```
  "tasks":{
      "mainTask":{
          "parameters":{},
          "loop":"",
          "action":"",
          "publish":{},
          "switch":{}
      }
  }
  ```
  
  **Table 10** Fields in **tasks**
  | Field | Description | Attribute | Type | Value Range |
  | --- | --- | --- | --- | --- |
  | mainTask | Task name. | Mandatory | Keyword/Customized | **mainTask** is a keyword and is the first task of the script.  The names of other tasks can be customized. The value is a string of 1 to 32 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_).  A task name in a script must be unique. |
  | parameters | Defines variables in the task. | Optional | Keyword | For details, see [âª parameters](#EN-US_CONCEPT_0000001563990837__li1495135155417). |
  | loop | Defines the cyclic execution of the task. | Optional | Keyword | For details, see [âª loop](#EN-US_CONCEPT_0000001563990837__li7514181154613). |
  | action | Defines the action to be executed. | Mandatory | Keyword | For details, see [âª action](#EN-US_CONCEPT_0000001563990837__li10676174694520). |
  | publish | Defines the parameters to be published to scripts. | Optional | Keyword | For details, see [âª publish](#EN-US_CONCEPT_0000001563990837__li1698584819450). |
  | switch | Defines the conditions for switching from the current task to a lower-level task. | Optional | Keyword | For details, see [âª switch](#EN-US_CONCEPT_0000001563990837__li1192831504615). |
  
  + **parameters**
    
    **parameters** is used to define variables used in a task. A variable applies to the current task. Each task supports a maximum of five variables.
    
    If the input parameter of a function is of the array or object type, you must define a variable and then reference the variable in the input parameter of the function.
    
    ```
    "parameters":{"name":"value"}
    ```
    
    **Table 11** Fields in **parameters**
    | Field | Description | Attribute | Type | Value Range |
    | --- | --- | --- | --- | --- |
    | *name* | Name of a variable. | Mandatory | Customized | The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). |
    | *value* | Value of a variable. | Mandatory | Customized | For details about the variable types supported by **parameters**, see [Table 12](#EN-US_CONCEPT_0000001563990837__table2097173723618). |
    
    
    **Table 12** Variable type supported by **parameters**
    | Variable Type | Usage Description | Value Range |
    | --- | --- | --- |
    | Boolean type | "parameters": {"aa": *value*} | *value*: The value can be true or false. |
    | Integer type | "parameters": {"bb": *value*} | *value*: The value ranges from 0 to 4294967295. |
    | Character string type | "parameters": {"MemoryXpath": "*value*"} | *value*: The value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters. |
    | String array type | "parameters": {"cc": ["*value1*", â¦â¦, "*value80*"]} | The total length of array members cannot exceed 1600 characters. The members are character strings. Chinese characters are supported. Each Chinese character is considered as three English characters. |
    | Integer array type | "parameters": {"dd": [*value1*, â¦â¦, *value80*]} | The number of members supported ranges from 1 to 80. The value of each member ranges from 0 to 4294967295. |
    | Object type | "parameters": {"ee": {"name": "*value*"} | Only one layer of object is supported. An object supports one to five members.  *name*: specifies the variable name in the object value. The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). The variable name must be globally unique and cannot be **result**.  *value*: specifies the value of the variable in the object value. The value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters.  NOTE:  When a variable of the object type is defined in **parameters**, the variable cannot be referenced in the object. |
    
    Variables defined by **parameters** can be referenced by **action**, **switch**, and **publish**. The reference mode of all variables is ${}. [Table 4](#EN-US_CONCEPT_0000001563990837__table8539113819290) lists the supported variable reference formats.
    
    **parameters** definition and reference example:
    
    ```
    "parameters":{
        "cmd":"display memory slot ${slot-id} cpu ${cpu-id}",
        "view":"system"
    },
    "action":"eva.cli(${view}, &{cmd})"
    ```
  + loop
    
    **loop** indicates that the task and all its lower-level tasks are executed cyclically. The entire script supports a maximum of three layers of loops.
    
    ```
    "loop":"index in ${value}"
    ```
    
    **Table 13** Fields in **loop**
    | Field | Description | Attribute | Type | Value Range |
    | --- | --- | --- | --- | --- |
    | *index* | Name of a variable, which is used to indicate the subscript of an array. The usage method is the same as that of **parameters**. | Mandatory | Customized | It does not need to be defined. The value starts from 0 and is incremented by 1 for each cycle. |
    | in | Fixed field. | Mandatory | Keyword | - |
    | *value* | Name of a variable of the array type. | Mandatory | Customized | The value must be a defined variable name of the array type. |
    
    In the following example, when **loop** is executed for the first time, index is 0 and ${cmd[index]} is device. When **loop** is executed for the second time, index is 1 and ${cmd[index]} is clock.
    
    ```
    "Task1":{
      "define":{ "cmd": ["device", "clock"]}, 
      "events":{ "e1": {"trigger": "eva.singleCollect()"},
      "tasks": {
         "mainTask": {
    	"loop": "index in ${cmd}",
            "action": "eva.cli(\"user\", \"display ${cmd[index]}\")"
             }
          }
    }
    ```
  + action
    
    **action** is used to define the actions allowed in a task, including command delivery, NETCONF operation delivery, character string regular expression parsing functions, character string operation functions, array operation functions, and other functions for data judgment. Only one action can be used in a task, and only one function can be used in an action.
    
    The standard output result of **action** is **result**. You can only use **publish** to publish **result** to other tasks. [Table 14](#EN-US_CONCEPT_0000001563990837__table861543851718) describes the usage of **result**.
    
    **Table 14** Usage description of **result**
    | Usage Mode | Usage Description |
    | --- | --- |
    | ${result} | Obtains the return result of **action** in the task. |
    | ${result[*number*]} | Used when the return result of **action** is of the array type (for example, the result returned by eva.cliArray).  *number*: specifies the value of the array subscript. The value must be an integer and cannot be a variable.  Example:  The return result of **action** is ["slotA","slotB","slotC"]. ${result[0]} is slotA. |
    | ${result[*number*].*info*} | Used when the return result of **action** is of the object array type (for example, the result returned by eva.netconfGet).  *number*: specifies the value of the array subscript. The value must be an integer and cannot be a variable.  *info*: specifies the element name in the information obtained using NETCONF, that is, the name of a leaf node or another node in the YANG file.  Example:  The return result of **action** is as follows:  [  {slotid: 1,  portid: 1,  state: "up"},  {slotid: 1,  portid: 2  state: "up"}  ]  ${result[1].portid} is 2. |
    | ${result.*info*} | Used when the return result of **action** is of the object type (for example, the result returned by eva.netconfGet).  *info*: specifies the element name in the information obtained using NETCONF, that is, the name of a leaf node or another node in the YANG file.  Example:  The return result of **action** is as follows:  portinfo: {  slotid: 1,  portid: 2,  state: "up"}  ${result.slotid} is 1. |
    | ${result.*info*[*number*]} | The return result of **action** is of the object type and an object in the result is an array (for example, the result returned by eva.netconfGet).  *info*: specifies the element name in the information obtained using NETCONF, that is, the name of a leaf node or another node in the YANG file.  *number*: specifies the value of the array subscript. The value must be an integer and cannot be a variable.  Example:  The return result of **action** is as follows:  slotinfo: {  portinfo: [1,3,4,7],  slotState: "up"}  ${result.portinfo[2]} is 4. |
    
    
    **Table 15** Command line delivery function
    | Function Name | Function Description | Usage | Parameter Description | Function Return Value |
    | --- | --- | --- | --- | --- |
    | eva.cliRegexp | Indicates that a single command is delivered and the command output is parsed. | eva.cliRegexp(*view*, *cmd*, *clirule*) | *view*: specifies the command view. Currently, only the user, system, and diagnostic views are supported.  *cmd*: specifies the command. Currently, only commands starting with display, and search fes table are supported. The value can be a string literal or a string variable. When an array variable is used, the variable must be an array variable with a subscript.  *c**lirule*: indicates that the command output is matched using a regular expression. If multiple regular expressions are defined, the command output is matched based on each regular expression, and one result is displayed for each regular expression. A maximum of five regular expressions are supported.  *cmdArray*: indicates a command line array consisting of multiple command lines. The type of the variable is string array.  NOTE:  Ensure that the values of the *view*, *cmd*, and *cmdArray* parameters are correct. Otherwise, the delivery fails and the function return value is empty. | Indicates the display command output filtered by the regular expression. The value is a character string. |
    | eva.cli | Indicates that a single command is delivered and the command output is not parsed. | eva.cli(*view*, *cmd*) | Indicates the display command output. The value is a character string. |
    | eva.cliArray | Indicates that multiple commands are delivered and the command outputs are not parsed. | eva.cliArray(*view*, *cmdArray*) | Indicates the display command output. The value is a string array. |
    
    The following is an example of using the eva.cliRegexp function:
    
    ```
    "parameter": {
      "cmd": "display interface brief",
      "clirule": {
        "EthTrunk": "\\s*Eth-Trunk(\\d+)\\s*(?:down|up)\\s*(?:down|up)"
                             }
    },
    "action": "eva.cliRegexp(\"user\",${cmd},${clirule})"
    ```
    
    The following is an example of using the eva.cli function:
    
    ```
    "action": "eva.cli(\"user\",\"display interface brief\")"
    ```
    
    The following is an example of using the eva.cliArray function:
    
    ```
    "parameter": {
      "cli-view": "user",
      "cli-array": ["display version","display device"]
    },
    "action": "eva.cliArray(${cli-view},${cli-array})"
    ```
    
    **Table 16** NETCONF operation delivery function
    | Function Name | Function Description | Usage | Parameter Description | Function Return Value |
    | --- | --- | --- | --- | --- |
    | eva.netconfGet | Queries information using NETCONF. It is equivalent to the GET operation of NETCONF. | eva.netconfGet (*xpath*) | *xpath*: specifies the XPath. For details, see the YANG API Reference.  NOTE:  Ensure that the value of the *xpath* parameter is correct. Otherwise, the delivery fails and the function return value is empty. | The value is an integer, character string, object, or object array. |
    
    
    **Table 17** String regular expression parsing function
    | Function Name | Function Description | Usage | Parameter Description | Function Return Value |
    | --- | --- | --- | --- | --- |
    | eva.regexp | Indicates regular expression matching for character strings. | eva.regexp(*str*, *regexp*) | *str*: specifies the character string to be matched.  *regexp*: specifies the name of a variable of the object type. This variable specifies a regular expression. Multiple regular expressions are supported. | The value is an object. |
    
    
    **Table 18** Character string operation functions
    | Function Name | Function Description | Parameter Description | Function Return Value |
    | --- | --- | --- | --- |
    | eva.strContains(*str1*, *str2*) | Indicates whether the character string *str1* contains the character string *str2*. The characters are case sensitive. | *str1* and *str2*: can be string literals or string variables. When the value is a string literal, the value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters. | The value is of the Boolean type and can be true or false. |
    | eva.strContainsIgnoreCase(*str1*, *str2*) | Indicates whether the character string *str1* contains the character string *str2*. The characters are case insensitive. |
    | eva.strEquals(*str1*, *str2*) | Indicates whether the character strings *str1* and *str2* are the same. The characters are case sensitive. |
    | eva.strEqualsIgnoreCase(*str1*, *str2*) | Indicates whether the character strings *str1* and *str2* are the same. The characters are case insensitive. |
    | eva.strcat(*str1*, *str2*) | The character strings *str1* and *str2* are concatenated and the concatenated character string is saved in *str1*. A maximum of 2048 characters can be saved. | *str1*: The value must be a string variable. *str2*: The value can be a string literal or a string variable. When *str2* is a string literal, the value is a string of 1 to 256 characters. Chinese characters are supported. Each Chinese character is considered as three English characters. | No result is returned. |
    
    
    **Table 19** Array operation functions
    | Function Name | Function Description | Parameter Description | Function Return Value |
    | --- | --- | --- | --- |
    | eva.arrayCount(*array*) | Indicates the number of members in the array *array*. | *array*: can be an integer array or a string array. | The value is an integer. The actual number of members in the array is returned. |
    | eva.arrayNumAdd(*array1*, *array2*) | Indicates that the integer arrays *array1* and *array2* are combined. | *array1* and *array2*: must be integer arrays. | The value is an integer array. A new array after combination is returned. |
    | eva.arrayStrAdd(*array1*, *array2*) | Indicates that the string arrays *array1* and *array2* are combined. | *array1* and *array2*: must be string arrays. | The value is a string array. A new array after combination is returned. |
    | eva.sum(*array*) | Indicates that all members in the integer array *array* are summed up. | *array*: must be an integer array. | The value is an integer. The sum result is returned. |
    
    
    **Table 20** Other functions
    | Function Name | Function Description | Parameter Description | Function Return Value |
    | --- | --- | --- | --- |
    | eva.pass() | Indicates that the result of the script meets the pass conditions. | - | No result is returned. When this function is used as an action function, result cannot be used. |
    | eva.norelated() | Indicates that the result of the script is irrelevant to the check scenario. | - |
    | eva.fail(*value*) | Indicates that the result of the script does not meet the pass conditions. This function saves the information collected during the running. | *value*: You can enter a string of 1 to 256 characters, or reference a string variable. |
    | eva.noop() | Unconditional execution. | - |
  + publish
    
    **publish** is used to publish specified parameters. The published parameters can be used by the current task and its lower-level tasks. A maximum of five **publish** variables can be configured for each task.
    
    ```
    "publish":{"name":"value"}
    ```
    
    **Table 21** Fields in **publish**
    | Field | Description | Attribute | Type | Value Range |
    | --- | --- | --- | --- | --- |
    | *name* | Parameter name. | Mandatory | Customized | The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). |
    | *value* | Parameter value. | Mandatory | Customized | *value* can be one of the following:  - Reference the variables defined by **define** or the variables defined by **parameter** in the same task. - Result of **action**. - Parameter value type, which is similar to that in **parameter**. For details, see [Table 12](#EN-US_CONCEPT_0000001563990837__table2097173723618). |
    
    The following is an example of using **publish**:
    
    ```
    "publish":{
       "memoryinfos": "${result}",
       "memory": "${memoryinfomation}
    }
    ```
  + switch
    
    **switch** is used to define the conditions for switching from the current task to a lower-level task. A maximum of 14 lower-level tasks are supported. A lower-level task cannot be switched to an upper-level task. When the conditions of multiple lower-level tasks are met, the first lower-level task that meets the conditions is executed first, and then the second lower-level task that meets the conditions is executed.
    
    ```
    "switch": {"name": "jump-condition"}
    ```
    
    **Table 22** Fields in **switch**
    | Field | Description | Attribute | Type | Value Range |
    | --- | --- | --- | --- | --- |
    | *name* | Name of a lower-level task. | Mandatory | Customized | The value must be a defined lower-level task name, eva.pass(), eva.norelated(), or eva.fail(*value*). The value is a string of 2 to 16 case-sensitive characters. It starts with a letter and can contain only letters, digits, and underscores (\_). |
    | *jump**-condition* | Jump condition. | Mandatory | Customized | It can be integer comparison, Boolean comparison, or unconditional jump. The operation result is true or false. If a function is used in a jump condition, the function must be on the left of the operator.  NOTE:  If a function is used in a jump condition, the following functions are supported:  - eva.strContains(str1, str2) - eva.strContainsIgnoreCase(str1, str2) - eva.strEquals(str1, str2) - eva.strEqualsIgnoreCase(str1, str2) - eva.arrayCount(array) - For details about the operators in integer comparison, see [Table 7](#EN-US_CONCEPT_0000001563990837__table6605131219326). Example: "task1": "a > b" - For Boolean comparison, the operators are == and != and the value on the right of the operator must be of Boolean type, for example, "task2": "eva.strContains(*str1*, *str2*) == true". - Example of unconditional jump: "task3": "noop" |