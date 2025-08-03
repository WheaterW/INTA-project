Configuring FM
==============

Configuring FM

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the alarm management view.
   
   
   ```
   [alarm](cmdqueryname=alarm)
   ```
3. (Optional) View the current alarm severity.
   
   
   ```
   [display alarm information](cmdqueryname=display+alarm+information) [ name alarm-name ]
   ```
4. Configure an alarm severity.
   
   
   ```
   [alarm](cmdqueryname=alarm) alarm-name severity { critical | major | minor | warning } [ instance instance-name ]
   ```
5. Configure one or more of the following functions as required:
   
   
   * Configure delayed alarm reporting.
     1. Enable delayed alarm reporting.
        ```
        [delay-suppression enable](cmdqueryname=delay-suppression+enable)
        ```
     2. (Optional) Configure an alarm reporting delay period.
        ```
        [suppression alarm](cmdqueryname=suppression+alarm) alarm-name { cause-period cause-seconds | clear-period clear-seconds }
        ```
        
        By default, the alarm reporting delay period varies with applications. You can run the **undo suppression alarm** command and then the **display alarm information** command to view the default reporting delay period.
        
        To configure a reporting delay period for an active alarm, specify the **cause-period** parameter. To configure a reporting delay period for a clear alarm, specify the **clear-period** parameter.
   * Disable alarm correlation suppression.
     1. Enable the alarm correlation analysis function.
        ```
        [correlation-analyze enable](cmdqueryname=correlation-analyze+enable)
        ```
     2. Disable NMS host-based alarm correlation suppression.
        ```
        undo [alarm correlation-suppress enable target-host](cmdqueryname=alarm+correlation-suppress+enable+target-host)  [ ipv6 ] ip-address securityname { security-name | cipher security-string  } [ vpn-instance vpn-instance-name ]
        ```
        
        By default, alarm correlation suppression is enabled.
   * Disable the wrapping function of historical alarm records.
     ```
     [history record-wrap disable](cmdqueryname=history+record-wrap+disable)
     ```
   * Run the following command in the user view to disable the alarm reporting function for CLI users:
     ```
     [undo terminal alarm](cmdqueryname=undo+terminal+alarm)
     ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display alarm information**](cmdqueryname=display+alarm+information) [ **name** *alarm-name* ] command to check the alarm configuration.
* Run the **display this** command in the alarm management view to check the alarm configuration.
* Run the [**display system osnode-group**](cmdqueryname=display+system+osnode-group) command to view information about all OS node groups of the physical device.