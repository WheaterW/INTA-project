Create/Modify
=============

You can create or modify nodes of different types by directly specifying nodes or running the **touch** command.

#### Creating or Modifying a Container Node

Container nodes can be created or modified in either of the following ways:

* **Create a container node by specifying the name of the container node and enter the corresponding view.**
  
  For example, to enter the **bfd** view, run the following command:
  
  ```
  [(ex)ADMIN@HUAWEI]
  MDCLI> bfd
  
  [(ex)ADMIN@HUAWEI]/bfd
  MDCLI>
  ```
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  For a Presence Container node, the presence of the node indicates a certain meaning. When you enter the view, the node is created.
  
  For a non-Presence container node, specifying the name of the container node to enter the corresponding view only indicates that the view is displayed.
* **Run the** **touch** **command to create a container node.**
  
  For example, to enable the IPv6 function on an interface, run the following command: The CE6885-LL supports this function only in standard forwarding mode.
  
  ```
  [(ex)ADMIN@HUAWEI]
  MDCLI> touch ifm/interfaces/interface[name="MEth0/0/0"]/ipv6
  
  [*(ex)ADMIN@HUAWEI]
  MDCLI>
  ```

#### Creating or Modifying a List Node

List nodes can be created or modified in the following way:

* **Create a list node by specifying the list name and key list and display the list view.**
  
  For example, to create vlanif100 and enter the corresponding interface view, run the following command:
  
  ```
  [(ex)ADMIN@HUAWEI]/ifm/interfaces
  MDCLI> interface name vlanif100
  
  [*(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="vlanif100"]
  MDCLI>
  ```

#### Creating or Modifying a Leaf Node

**Create or modify a leaf node by specifying the name and value of the leaf node.**

For example, to set the administrative status of vlanif100 to up, run the following command:

```
[(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="vlanif100"]
MDCLI> admin-status up
```

In the YANG model, a leaf node can have a value or have no value.

For example, run the following command to create an empty leaf node:
```
[(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]/ethernet/main-interface/l2-attribute/bpdu-tunnel
MDCLI> enable [null]
```

If a value of the string type contains special characters such as spaces, line breaks, and tabs, you need to use quotation marks to enter the value. The MD-CLI supports the following three types of character strings:

* Unquoted string: a string that does not start with a single quotation mark (') or double quotation mark ("). Such a string cannot contain spaces, tabs, line breaks, carriage return characters, single or double quotation marks, or other characters that are used as separators in the string context. For example, to set the description of MEth0/0/0 to **To-DeviceB-MEth0/0/0**, run the following command:
  ```
  [(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
  MDCLI> description To-DeviceB-MEth0/0/0
  ```
* Single-quoted string: a string that starts and ends with a single quotation mark ('). Such a string cannot contain single-quoted characters or escape characters, meaning that all content is the original input characters. For example, to set the description of MEth0/0/0 to **To DeviceB MEth0/0/0**, run the following command:
  ```
  [(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
  MDCLI> description 'To DeviceB MEth0/0/0'
  ```
* Double-quoted string: a string that starts and ends with double quotation marks (" "). Such a string can use a backslash (\) to form escape characters. Currently, the MD-CLI supports only four escape characters:
  + \n: line break
  + \t: tab character
  + \": double-quoted character
  + \\: backslash character
  
  For example, to set the description of MEth0/0/0 to **To DeviceB's MEth0/0/0**, run the following command:
  
  ```
  [(ex)ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
  MDCLI> description "To DeviceB's MEth0/0/0"
  ```


#### Creating or Modifying a Leaf-List Node

Leaf-list nodes can be created or modified in the following way:

* **Create or modify a leaf-list node by specifying the name and value of the node.**
  
  For example, to add source security zones **zone1** and **zone2** to security policy **r1**, run the following command:
  
  ```
  [*(ex)ADMIN@HUAWEI]/sec-policy/vsys[name="default"]/static-policy/rule[name="r1"]
  MDCLI> source-zone zone1 zone2
  ```