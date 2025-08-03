Configuring Service Diagnosis
=============================

Configuring Service Diagnosis

#### Context

You can create diagnosis objects based on attributes, which vary according to services.

For the DHCP service, you can create diagnosis objects based on MAC addresses.

![](public_sys-resources/note_3.0-en-us.png) 

Service diagnosis affects system performance. Therefore, enable service diagnosis only when fault locating is required. After faults are located, immediately run the [**undo trace enable**](cmdqueryname=undo+trace+enable) command to disable service diagnosis.

Service diagnosis commands are at level 3 (management level). That is, only users at privilege level 3 can run service diagnosis commands.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable service diagnosis.
   
   
   ```
   [trace enable](cmdqueryname=trace+enable) [ brief ]
   ```
   
   By default, service diagnosis is disabled.
   
   The [**trace enable**](cmdqueryname=trace+enable) [ **brief** ] command configuration is not recorded in the configuration file and will be lost after the device restarts. To use the service diagnosis function after the device restarts, run this command again.
3. Create a diagnosis object.
   
   
   
   For CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
   
   ```
   [trace object](cmdqueryname=trace+object) { mac-address mac-address | ip-address ip-address [ vpn-instance vpn-instance-name ] } * [ output { command-line | file file-name | syslog-server syslog-server-ip } ]
   ```
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   ```
   [trace object](cmdqueryname=trace+object) { mac-address mac-address | ip-address ip-address [ vpn-instance vpn-instance-name ] | interface { interface-type interface-number } | user-vlan user-vlan-id | user-name username } } * [ output { command-line | file file-name | syslog-server syslog-server-ip } ]
   ```
   
   By default, no diagnosis object is created. If the **output** parameter is not specified, diagnostic information is displayed on the CLI by default.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to export diagnostic information to a specified file. To configure the terminal display function, run the [**terminal monitor**](cmdqueryname=terminal+monitor) and **[**terminal debugging**](cmdqueryname=terminal+debugging)** commands in the user view.
4. (Optional) Save the diagnostic information in the device buffer to a file.
   
   
   ```
   [save trace information](cmdqueryname=save+trace+information)
   ```
   
   After you specify the **file** *file-name* parameter in the **trace object** command to save diagnostic information to a file, the system saves diagnostic information in the device buffer first, and then saves the diagnostic information to the specified file when the buffer is full. If you need to view diagnostic information in real time, run the [**save trace information**](cmdqueryname=save+trace+information) command to save diagnostic information in the buffer to the file immediately.
5. (Optional) Specify the interface through which diagnostic information is exported to a log server.
   
   
   ```
   [trace syslog source](cmdqueryname=trace+syslog+source) { interface-type interface-number | interface-name }
   ```
   
   By default, no interface is specified to export diagnostic information to a log server.
   
   * You can specify the interface only when a device is configured to export diagnostic information to a log server.
   * The configuration of this command is not recorded in the configuration file and will be lost after the device restarts. To export diagnostic information to a log server through a specified interface, run this command again.

#### Verifying the Configuration

* Run the [**display trace information**](cmdqueryname=display+trace+information) command to check information about service diagnosis.
* Run the [**display trace instance**](cmdqueryname=display+trace+instance) [ *instance-start-id* [ *instance-end-id* ] | **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** *interface-type* *interface-number* ] command to check diagnosis instances on the device.![](public_sys-resources/note_3.0-en-us.png) 
  
  Only the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S support the **interface** *interface-type* *interface-number* parameter.
* Run the [**display trace object**](cmdqueryname=display+trace+object) [ *service-object-id* ] command to check the configuration of a diagnosis object.