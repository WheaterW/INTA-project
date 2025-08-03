Configuring the iNOF Reflector and Client
=========================================

Configuring the iNOF Reflector and Client

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Configure the local device as a reflector or client in the iNOF system.
   
   
   ```
   [role](cmdqueryname=role) { reflector | reflect-client }
   ```
   
   By default, no role is configured for the local device in an iNOF system.
5. Configure the local IP address of the device in the iNOF system.
   
   
   ```
   [service-address](cmdqueryname=service-address) { ip-address | ipv6-address } [ port-id port-id ]
   ```
   
   By default, no local IP address is configured for a device in an iNOF system.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The **port-id** *port-id* parameter specifies the port number used by the local device to transmit iNOF packets. All devices in the iNOF system must be configured with the same port number, which is 19516 by default.
   
   When configuring the local IP address for a device in an iNOF system, do not use the IP address of the device's management interface.
6. Specify the IP address of a client on the iNOF reflector.
   
   
   ```
   [peer](cmdqueryname=peer) { peer-address | peer-ipv6-address } reflect-client
   ```
   
   By default, no client IP address is specified on an iNOF reflector. After the configuration is complete, an iNOF connection is automatically established between the reflector and client.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The [**peer reflect-client**](cmdqueryname=peer+reflect-client) command needs to be run on a device to specify the IP address of a client only after the [**role**](cmdqueryname=role) **reflector** command is run on the device to configure it as an iNOF reflector.
   * If the iNOF zone configuration or [**peer reflect-client**](cmdqueryname=peer+reflect-client) configuration exists on the device, the device role cannot be changed to the iNOF client.
   * If two iNOF reflectors exist in an iNOF system, they must be specified as each other's client. In addition, other clients configured using the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command on the two reflectors must be the same. In this way, the two reflectors can back up each other to enhance the reliability of the iNOF system.
   * If an iNOF network has two iNOF reflectors, configurations that can be synchronized to the iNOF client on either reflector take effect in the entire iNOF system. The configurations include customized zone configuration, the function for automatically adding hosts to the iNOF default zone, iNOF zone isolation, and BFD for iNOF. To ensure that the two reflectors back up each other, the preceding configurations must be the same.
   * An iNOF reflector supports a maximum of 256 IPv4 client addresses and 256 IPv6 client addresses.
7. Exit the iNOF view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```