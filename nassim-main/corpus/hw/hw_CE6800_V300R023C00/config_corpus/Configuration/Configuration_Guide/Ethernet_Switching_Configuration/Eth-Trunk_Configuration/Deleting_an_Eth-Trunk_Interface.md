Deleting an Eth-Trunk Interface
===============================

Deleting an Eth-Trunk Interface

#### Prerequisites

An Eth-Trunk interface and its member interfaces have been configured on a device.


#### Procedure

**Deleting a specified member interface from an Eth-Trunk interface**

Before removing a member interface from an Eth-Trunk interface, you are advised to run the **shutdown** command and then the **undo shutdown** command on the member interface.

You can use either of the following methods to delete a specified member interface from an Eth-Trunk interface:

* Delete a member interface in the Eth-Trunk interface view.
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     ```
     [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
     ```
  3. Delete a specified member interface.
     ```
     [undo trunkport](cmdqueryname=undo+trunkport) interface-type { interface-number1 [ to interface-number2 ] } &<1-16>
     ```
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
* Delete the Eth-Trunk interface to which a member interface belongs in the member interface view.
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk member interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Delete the Eth-Trunk interface.
     ```
     undo eth-trunk
     ```
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```

**Deleting an Eth-Trunk interface**

Delete all member interfaces from an Eth-Trunk interface.

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Delete all member interfaces from an Eth-Trunk interface. For details, see [Delete a member interface in the Eth-Trunk interface view](#EN-US_TASK_0000001130621692__li16260347113217).
3. Delete the Eth-Trunk interface.
   ```
   undo interface eth-trunk trunk-id
   ```
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

![](public_sys-resources/note_3.0-en-us.png) 

If a Layer 3 sub-interface is created in an Eth-Trunk interface, run the [**undo interface eth-trunk**](cmdqueryname=undo+interface+eth-trunk) *trunk-id.subnumber* command in the system view to delete the Layer 3 sub-interface and then delete the Eth-Trunk interface.



#### Example

**Delete 100GE 1/0/1 from Eth-Trunk 1.**

Method 1:

```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[~HUAWEI-Eth-Trunk1] undo trunkport 100ge 1/0/1
```

Method 2:

```
<HUAWEI> system-view
[~HUAWEI] interface 100ge 1/0/1
[~HUAWEI-100GE1/0/1] undo eth-trunk
```

**You can delete Eth-Trunk 1 after all member interfaces are deleted from Eth-Trunk 1.**

```
<HUAWEI> system-view
[~HUAWEI] undo interface eth-trunk 1   
```