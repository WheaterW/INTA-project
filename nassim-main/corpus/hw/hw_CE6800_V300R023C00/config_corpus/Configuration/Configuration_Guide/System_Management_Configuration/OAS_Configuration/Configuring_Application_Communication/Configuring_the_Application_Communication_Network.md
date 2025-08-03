Configuring the Application Communication Network
=================================================

Configuring the Application Communication Network

#### Prerequisites

The service interface and east/west interface require IP addresses of physical interfaces or loopback interfaces. It is recommended that loopback interfaces be used to prevent services from being affected by physical interface going down.

The management interface requires a physical interface's IP address. It is recommended that a service interface on the panel be used to prevent application traffic from affecting the management services.


#### Context

The application communication network supports three types of interfaces: service interface, east/west interface, and management interface. The IP addresses of the three types of interfaces are created by the system by default and can be modified by users.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the OAS function.
   
   
   ```
   [oas enable](cmdqueryname=oas+enable)
   ```
3. Enter the OAS view.
   
   
   ```
   [oas](cmdqueryname=oas)
   ```
4. Set the range of port numbers used by the OAS.
   
   
   ```
   [ip dynamic-port](cmdqueryname=ip+dynamic-port) low-port to high-port
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The applications in the OAS and the host cannot use the same service interface.
5. Set the source IP address and MTU used by the OAS.
   
   
   ```
   [ipv4 source address](cmdqueryname=ipv4+source+address) sourceAddress [ mtu mtuValue ]
   ```
   
   You are advised to use a reachable loopback interface address.
6. Set an IP address and MTU for the OAS management interface.
   
   
   ```
   [ipv4 management-interface](cmdqueryname=ipv4+management-interface) { address mgmtAddress mgmtMask | mtu mgmtMtu }
   ```
   
   You are advised to use the IP address of the management interface on the device.
7. Configure the destination IP address and MTU for east/west communication in the OAS.
   
   
   ```
   [ipv4 east-west](cmdqueryname=ipv4+east-west) { destination destAddress | mtu mtuValue }
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Example

# Configure the application communication network.

1. Enter the OAS view.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] oas enable
   [*DeviceA-oas] oas
   ```
2. Set the range of port numbers used by the OAS to 50020 to 50030.
   ```
   [*DeviceA-oas] ip dynamic-port 50020 to 50030
   ```
3. Set the source IP address of the OAS to 10.0.0.1 and the MTU to 1700.
   ```
   [*DeviceA-oas] ipv4 source address 10.0.0.1 mtu 1700
   [*DeviceA-oas] ipv4 source address 10.0.0.2 mtu 1700
   ```
4. Set the IP address of the management interface to 10.0.0.2 and the MTU to 9600.
   ```
   [*DeviceA-oas] ipv4 management-interface address 10.0.0.3 24
   [*DeviceA-oas] ipv4 management-interface mtu 9600
   ```
5. Configure the destination IP address and MTU for east/west communication in the OAS.
   ```
   [*DeviceA-oas] ipv4 east-west mtu 1600
   [*DeviceA-oas] ipv4 east-west destination 10.0.0.4
   [*HUAWEI] commit
   ```


#### Verifying the Configuration

Run the [**display oas ip dynamic-port**](cmdqueryname=display+oas+ip+dynamic-port) command to check the configured port range.