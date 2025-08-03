(Optional) Configuring NetBIOS Services for DHCPv4 Clients
==========================================================

You can configure NetBIOS services for DHCPv4 clients to enable users to obtain NetBIOS services automatically. Then, users can use easy-to-memorize hostnames rather than complicated IP addresses.

#### Context

Perform the following steps on the device (DHCPv4 server) that provides NetBIOS services for DHCPv4 clients:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** { **local** | **remote** } | **server** ]
   
   
   
   An address pool is created, and its view is displayed.
3. Run [**netbios-name-server**](cmdqueryname=netbios-name-server) *ip-address* &<1-8>
   
   
   
   A NetBIOS server address is configured for clients of the address pool.
4. Run [**netbios-type**](cmdqueryname=netbios-type) { **b-node** | **h-node** | **m-node** | **p-node** }
   
   
   
   A NetBIOS node type is configured for the DHCPv4 client.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

For clients running the operating system of Microsoft and using NetBIOS for communication, the Windows Internet Naming Service (WINS) server provides resolution from hostnames to IP addresses. As such, WINS settings are required on most clients running the Windows operating system.

When a DHCPv4 client on a WAN uses NetBIOS for communication, a mapping between the hostname and IP address needs to be set up. Based on the modes of obtaining mapping, NetBIOS nodes are classified into the following types:

* b-node: A broadcast node obtains the binding by broadcasting a request to NetBIOS servers.
* h-node: A hybrid node is a b-node that obtains the binding through peer-to-peer communication.
* m-node: A mixed node obtains the binding in a way combining the modes that the b-node and p-node use.
* p-node: A peer-to-peer node obtains the binding by communicating with a NetBIOS server.