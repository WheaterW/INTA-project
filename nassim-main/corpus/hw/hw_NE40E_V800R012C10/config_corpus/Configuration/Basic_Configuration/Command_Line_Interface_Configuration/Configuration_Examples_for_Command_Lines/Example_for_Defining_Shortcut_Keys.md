Example for Defining Shortcut Keys
==================================

If shortcut keys are defined on a Router, all users can use the shortcut keys regardless of their levels.

#### Networking Requirements

A Router is deployed.


#### Precautions

If a user does not have the right to execute the command associated with a defined shortcut key, the system makes no response when the user presses this shortcut key.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Define the shortcut key **Ctrl+U** and associate it with the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command.
2. Press **Ctrl+U** at the prompt of [~HUAWEI].

#### Data Preparation

To complete the configuration, you need the following data:

* Shortcut key name
* Name of the command to be associated with the shortcut key

#### Procedure

1. Define the shortcut key **Ctrl+U** and associate it with the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] hotkey ctrl_u "display ip routing-table"
   ```
   ```
   [*HUAWEI] commit
   ```
2. Press **Ctrl**+**U** at the prompt of [~HUAWEI].
   
   
   ```
   [~HUAWEI] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: Public
   ```
   ```
            Destinations : 8        Routes : 8
   ```
   ```
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   ```
   ```
        10.1.1.1/32    Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
         10.2.0.0/16   Direct 0    0           D  10.3.150.51     GigabitEthernet0/0/0
   ```
   ```
      10.3.150.51/32   Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
     10.3.255.255/32   Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.0/8   Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
   127.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   ```
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```

#### Configuration Files

None