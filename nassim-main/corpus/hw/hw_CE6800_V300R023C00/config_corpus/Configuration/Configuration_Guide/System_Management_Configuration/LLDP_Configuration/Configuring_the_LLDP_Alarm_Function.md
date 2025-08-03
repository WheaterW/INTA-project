Configuring the LLDP Alarm Function
===================================

Configuring the LLDP Alarm Function

#### Context

After the LLDP alarm function is configured on a device, the device sends alarms to the NMS when information about neighbors changes.

To avoid network flapping caused by frequent LLDP alarms being sent to the NMS, configure a delay for the device to send alarms. The delay for sending LLDP alarms should be appropriate. You can adjust this parameter based on the load of a network.

* The longer the delay, the lower the frequency of network topology changes on a device. However, if the delay for sending LLDP alarms is too long, the NMS cannot trace changes of the neighbor status. As a result, the NMS cannot refresh network topology for a device in a timely manner.
* The shorter the delay, the higher the frequency of network topology changes on a device. This helps the NMS refresh network topology on the device in a timely manner. However, if the delay is too short, the NMS refreshes status information about neighbors frequently. This causes flapping of network topology on a device, increases the load on the system, and wastes resources.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the LLDP alarm function.
   
   
   ```
   [snmp-agent trap enable feature-name](cmdqueryname=snmp-agent+trap+enable+feature-name) lldp [ trap-name { hwlldpinterfaceremtableschange  | lldpremtableschange } ]
   ```
   
   
   After the LLDP alarm function is enabled for a device, the device sends alarms to the NMS when one of the following events occurs.
   * The status of an interface neighbor node changes. The corresponding alarm is **LLDP 1.3.6.1.4.1.2011.5.25.134.2.8** **hwLldpInterfaceRemTablesChange**.
   * The status of an LLDP neighbor changes. The corresponding alarm is **LLDP 1.0.8802.1.1.2.0.0.1 lldpRemTablesChange**.
   
   The LLDP alarm function takes effect globally to control the capability to send LLDP alarms on all interfaces on a device.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The network topology changes frequently when the networking is first formed. After the LLDP alarm function is enabled for a device, the device will frequently send alarms to the NMS. This increases the load on the system and wastes resources. It is recommended that you disable the LLDP alarm function when the networking is first formed.
3. (Optional) Set the delay for sending LLDP neighbor information change alarms.
   
   
   ```
   [lldp trap-interval](cmdqueryname=lldp+trap-interval) interval
   ```
   
   
   
   By default, the delay for sending LLDP neighbor information change alarms is 5 seconds. Generally, you are advised to set the delay for sending LLDP neighbor information change alarms to the default value.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display snmp-agent trap feature-name**](cmdqueryname=display+snmp-agent+trap+feature-name) **lldp all** command to check all alarm messages of the LLDP module.
* Run the [**display lldp local**](cmdqueryname=display+lldp+local) [ **interface** *interface-type interface-number* ] command to check the local LLDP status.