(Optional) Configuring the Trap Function
========================================

(Optional) Configuring the Trap Function

#### Context

The device can be configured to send specified traps to the NMS, which facilitates fault locating. To enhance the trap transmission security, specify parameters for sending traps.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to send traps to the NMS.
   
   
   ```
   [snmp-agent trap enable](cmdqueryname=snmp-agent+trap+enable)
   ```
3. Enable the function of sending a specified trap of a feature to the NMS.
   
   
   ```
   [snmp-agent trap enable feature-name](cmdqueryname=snmp-agent+trap+enable+feature-name) feature-name trap-name trap-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) If the [**snmp-agent trap enable**](cmdqueryname=snmp-agent+trap+enable) command has been run to enable the trap functions of all modules, or the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) command has been run to enable a specific trap function, note the following points:
   * To disable the trap functions of all modules, run the [**snmp-agent trap disable**](cmdqueryname=snmp-agent+trap+disable) command.
   * To restore the trap functions of all modules to the default status, run the [**undo snmp-agent trap enable**](cmdqueryname=undo+snmp-agent+trap+enable) or [**undo snmp-agent trap disable**](cmdqueryname=undo+snmp-agent+trap+disable) command.
   * To disable the trap function for a specified module, run the [**undo snmp-agent trap enable feature-name**](cmdqueryname=undo+snmp-agent+trap+enable+feature-name) command.
   * To delete all the trap function configurations of a feature in a one-click manner, run the [**clear configuration snmp-agent trap enable feature-name**](cmdqueryname=clear+configuration+snmp-agent+trap+enable+feature-name) command.
4. Disable the trap function for interface status.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Disable the trap function for interface status.
      ```
      [undo enable snmp trap updown](cmdqueryname=undo+enable+snmp+trap+updown)
      ```
      
      By default, the trap function is enabled for all interfaces. When the interface status changes, a trap is generated. When an interface flaps, the interface frequently sends traps to the NMS, which increases the processing load of the NMS. In this case, you can disable the trap function on the interface.
   3. Return to the system view.
      ```
      [quit](cmdqueryname=quit)
      ```
5. Set the source address of traps. Perform one or two of the following operations as required:
   
   
   * Set the source interface of traps. The IPv4 address of the source interface is used as the source IPv4 address of traps.
     ```
     [snmp-agent trap source](cmdqueryname=snmp-agent+trap+source) { interface-name | interface-type interface-number }
     ```
     
     To ensure device security, you are advised to specify the local loopback interface as the source interface of traps.
     
     The source interface of traps specified on the device must be the same as that specified on the NMS. Otherwise, the NMS cannot receive the traps sent from the device.
   * Set the source IPv6 address of traps.
     ```
     [snmp-agent trap source](cmdqueryname=snmp-agent+trap+source) [ipv6](cmdqueryname=ipv6) ipv6-address [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name ]
     ```
6. Set a source port number for traps.
   
   
   ```
   [snmp-agent trap source-port](cmdqueryname=snmp-agent+trap+source-port) port-number
   ```
   
   
   
   To improve network security, configure a specific source port number for traps. In this case, the user terminal's firewall filters packets based on the port number.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```