(Optional) Configuring a Device to Insert the Interface-Id or Remote-Id Option into DHCPv6 Messages
===================================================================================================

(Optional) Configuring a Device to Insert the Interface-Id or Remote-Id Option into DHCPv6 Messages

#### Context

The Interface-Id and Remote-Id options defined in DHCPv6 record client location information, including the inbound interface of DHCPv6 Request messages and the DUIDs of clients. To enable a DHCPv6 server to allocate network parameters such as IPv6 addresses to clients based on client location information, configure the device functioning as a DHCPv6 relay agent to insert the Interface-Id or Remote-Id option in DHCPv6 messages.

After this function is configured, the device inserts the Interface-Id or Remote-Id option into a Request message received from a client based on the configured option information, constructs a Relay-forward message, and forwards the message to the DHCPv6 server. The server then allocates network parameters such as an IPv6 address to the client based on the option information and sends a Relay-reply message to the DHCPv6 relay agent. After receiving the Relay-reply message, the DHCPv6 relay agent removes the Interface-Id or Remote-Id option from the message and then forwards the message to the client or another relay agent.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure the format of the Interface-Id or Remote-Id option as required.
   
   
   
   **Table 1** Configuring the format of the Interface-Id or Remote-Id option
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the format of the Interface-Id option to be inserted into DHCPv6 messages. | [**dhcpv6 interface-id format**](cmdqueryname=dhcpv6+interface-id+format) { **default** | **user-defined** *user-defined-text* } If the **user-defined** parameter is specified, you can define the option format using the following methods: * Definition based on keywords: The Interface-Id option is defined based on the keywords supported by the format. For example, if the name of the device to which users are connected and the ID of the outer VLAN to which they belong need to be recorded, the format can be defined as "%sysname %svlan." If the device name is HUAWEI and the S-VLAN ID is 100, the user location information recorded by the Interface-Id option is "HUAWEI 100."    ```   [~HUAWEI] dhcpv6 interface-id format user-defined "%sysname %svlan"    ``` * Definition based on common character strings: The Interface-Id option is directly defined as a character string. For example, if all users on an interface are located in an office building named N8, the Interface-Id option can be directly defined as "N8."    ```   [~HUAWEI] dhcpv6 interface-id format user-defined "N8"    ``` * Mixed definition: The Interface-Id option is defined by both keywords and common character strings. For example, the Interface-Id option can be defined as "%sysname N8."    ```   [~HUAWEI] dhcpv6 interface-id format user-defined "%sysname N8"    ``` | By default, the format of the Interface-Id option in DHCPv6 messages is **default**, that is, "%04svlan.%04cvlan.%mac:%portname."  The value of *svlan* or *cvlan* is an integer that consists of four characters. If the value is shorter than four characters, 0s are prefixed. For example, if the outer VLAN ID, inner VLAN ID, and inbound interface in a DHCPv6 message received by the device is 11, 22, and VLANIF 100, respectively, and the device MAC address is 00-e0-fc-12-34-56, the Interface-Id option generated during parsing is 0011.0022.00e0fc123456:vlanif100. |
   | Configure the format of the Remote-Id option to be inserted into DHCPv6 messages. | [**dhcpv6 remote-id format**](cmdqueryname=dhcpv6+remote-id+format) { **default** | **user-defined** *user-defined-text* } | By default, the format of the Remote-Id option in DHCPv6 messages is **default**, that is, "%duid %portname:%04svlan.%04cvlan."  The method for defining the Remote-Id option format is the same as that for defining the Interface-Id option format. |
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable the device to insert the Interface-Id or Remote-Id option into DHCPv6 messages.
   
   
   
   **Table 2** Enabling the device to insert the Interface-Id or Remote-Id option into DHCPv6 messages
   | Operation | Command | Description |
   | --- | --- | --- |
   | Enable the device to insert the Interface-Id option into DHCPv6 messages. | [**dhcpv6 interface-id insert enable**](cmdqueryname=dhcpv6+interface-id+insert+enable) | By default, a device is enabled to insert the Interface-Id option into DHCPv6 messages. |
   | Enable the device to insert the Remote-Id option into DHCPv6 messages. | [**dhcpv6 remote-id insert enable**](cmdqueryname=dhcpv6+remote-id+insert+enable) | By default, a device is disabled from inserting the Remote-Id option into DHCPv6 messages. |
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```