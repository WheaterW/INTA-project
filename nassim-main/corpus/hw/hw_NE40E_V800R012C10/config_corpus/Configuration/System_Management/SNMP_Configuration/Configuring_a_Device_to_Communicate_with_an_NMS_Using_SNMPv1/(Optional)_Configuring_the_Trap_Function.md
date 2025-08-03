(Optional) Configuring the Trap Function
========================================

The device can be configured to send specified traps to the NMS, which facilitates fault locating. To enhance the trap transmission security, specify parameters for sending traps.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**snmp-agent trap**](cmdqueryname=snmp-agent+trap) **enable** command to enable the device to send traps to the NMS.
3. Run the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) *feature-name* **trap-name** *trap-name* command to enable the device to send a trap of a specified feature to the NMS.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) If the [**snmp-agent trap enable**](cmdqueryname=snmp-agent+trap+enable) command has been run to enable the trap functions of all modules, or the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) command has been run to enable a specific trap function, note the following points:
   * To disable the trap functions of all modules, run the [**snmp-agent trap disable**](cmdqueryname=snmp-agent+trap+disable) command.
   * To restore the trap functions of all modules to the default status, run the [**undo snmp-agent trap enable**](cmdqueryname=undo+snmp-agent+trap+enable) or [**undo snmp-agent trap disable**](cmdqueryname=undo+snmp-agent+trap+disable) command.
   * To disable the trap function for a specified module, run the [**undo snmp-agent trap enable feature-name**](cmdqueryname=undo+snmp-agent+trap+enable+feature-name) command.
   * To delete all the trap function configurations of a feature in a one-click manner, run the [**clear configuration snmp-agent trap enable feature-name**](cmdqueryname=clear+configuration+snmp-agent+trap+enable+feature-name) command.
   * You can run the [**display snmp-agent trap all**](cmdqueryname=display+snmp-agent+trap+all) command to view the current status and default status of all traps in all features.
4. Run either or both of the following commands as required to specify the source IP address for sending traps:
   
   
   * Run the [**snmp-agent trap source**](cmdqueryname=snmp-agent+trap+source) *interface-type* *interface-number* command to specify a source interface for sending traps. After a source interface is specified, its IP address is used as the source IP address of traps. To ensure device security, you are advised to configure the IP address of the local loopback interface as that of the source interface. The source interface of traps specified on the Router must be the same as that specified for the Router on the NMS. Otherwise, the NMS does not accept the traps sent from the Router.
   * Run the [**snmp-agent trap source ipv6**](cmdqueryname=snmp-agent+trap+source+ipv6) *ipv6-address* [ **vpn-instance** *vpn-name* ] command to specify a source IPv6 address for sending traps.
5. Run the [**snmp-agent trap source-port**](cmdqueryname=snmp-agent+trap+source-port) *port-number* command to specify the number of the source port that sends traps.
   
   
   
   To improve network security, configure a specific source port number for traps. After that, the user terminal's firewall filters packets based on the port number.
6. (Optional) Run the [**snmp-agent trap type**](cmdqueryname=snmp-agent+trap+type) { **base-trap** | **entity-trap** } command to set the format of traps sent to the NMS.
   
   
   
   In VS mode, this command is supported only by the admin VS.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.