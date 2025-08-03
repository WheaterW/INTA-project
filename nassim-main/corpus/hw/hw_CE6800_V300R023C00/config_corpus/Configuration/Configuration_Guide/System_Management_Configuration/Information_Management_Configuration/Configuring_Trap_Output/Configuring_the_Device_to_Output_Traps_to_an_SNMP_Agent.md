Configuring the Device to Output Traps to an SNMP Agent
=======================================================

Configuring the Device to Output Traps to an SNMP Agent

#### Context

After traps are output to the SNMP agent, you can view device information on the NMS and locate device faults in a timely manner. Before configuring the device to output traps to an NMS server, configure the device to output traps to an SNMP agent. In this way, the SNMP agent sends traps to the NMS server.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Specify the channel used by the device to output traps to an SNMP agent.
   
   
   ```
   [info-center snmp channel](cmdqueryname=info-center+snmp+channel) { channel-number | channel-name }
   ```
3. Specify the channel used by the device to output traps to the trap buffer.
   
   
   ```
   [info-center trapbuffer channel](cmdqueryname=info-center+trapbuffer+channel) { channel-number | channel-name } [ size size ]
   ```
4. Set a rule for outputting traps to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } trap { state { off | on } | level severity } *
   ```
5. Enable the SNMP agent function.
   
   
   ```
   [snmp-agent](cmdqueryname=snmp-agent)
   ```
   
   The SNMP agent can work properly and receive traps only when the SNMP agent function is enabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For details on how to configure the SNMP agent, see "SNMP Configuration" in Configuration Guide > System Management Configuration.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```