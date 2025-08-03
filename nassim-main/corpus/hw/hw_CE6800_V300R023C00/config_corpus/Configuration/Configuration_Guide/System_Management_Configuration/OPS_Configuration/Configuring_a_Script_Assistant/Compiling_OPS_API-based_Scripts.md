Compiling OPS API-based Scripts
===============================

Compiling OPS API-based Scripts

#### Context

In an OPS script file, you can define operations on YANG model nodes to manage services through OPS APIs.

The OPS API is a RESTful open and programmable interface. The following table lists the operations supported by the OPS, RESTCONF, and NETCONF.

**Table 1** Operations supported by the OPS, RESTCONF, and NETCONF
| OPS | RESTCONF | NETCONF |
| --- | --- | --- |
| create | POST | <edit-config> (nc:operation="create") |
| create | POST | rpc |
| delete | DELETE | <edit-config> (nc:operation="delete") |
| patch | PATCH | <edit-config> (nc:operation="merge") |
| get | GET | <get-config>, <get> |
| set | PUT | <edit-config> (nc:operation="replace") |

Zero Touch Provisioning (ZTP) can invoke OPS scripts to implement automatic service deployment when a device starts without any configuration file.

You can compile Python scripts that are manually run and scripts defined in the ops\_execute() function of the script assistant based on the following procedure and specifications.


#### Procedure

1. Run the import ops statement to invoke the OPSConnection(object) function to establish a connection to the OPS interface.
2. Compile the OPS script.
   
   
   ```
   import ops                                                       # Imports the OPS module. This is a fixed format.
   import string                                                    # Fixed format.
   uri = "/restconf/data/huawei-aaa:aaa/domains"                    # XPath based on the RESTCONF packet header and YANG model of the service module. For the create, delete, get, and set operations, the parameter in the path is fixed to data.
   uri = "/restconf/operations/huawei-cfg:set-startup "             # XPath based on the RESTCONF packet header and YANG model of the service module. For RPC operations, the parameter in the path is fixed to operations.
   host = "localhost"                                               # Fixed format.
   req_data = None                                                  # Service body. Enter the data to be added in XML format. If no data is added, enter None.
   opos_conn = ops.OPSConnection(host)                              # Interface function that triggers OPS connection establishment.
   ret, _, rsp_data = ops_conn.create/delete/get/set(uri, req_data, timeout = time-value) # Triggers various operations. The timeout parameter specifies an OPS request timeout period. If the OPS request timeout period is reached, the OPS request is canceled, and a timeout error is returned. This parameter is optional. Its value is an integer ranging from 0 to 4294967295, in seconds. The default value is 0, indicating that there is no timeout period for OPS requests.
   ```
   
   **Table 2** Script compiling for various OPS operations
   | Operation | Rule Description | Script Example |
   | --- | --- | --- |
   | create | Creates a node. The parameter in the URI is fixed to **data**. | ``` import ops import string import hashlib uri = "/restconf/data/huawei-aaa:aaa/domains" host = "localhost" req_data = '''<domain>         <domainName>test1</domainName>         <authenSchemeName>default</authenSchemeName>         <acctSchemeName>default</acctSchemeName>         <authorSchemeName>default</authorSchemeName>         <domainState>active</domainState>         <accessLimit>283648</accessLimit>         <serviceTerminal>true</serviceTerminal>         <serviceTelnet>true</serviceTelnet>         <serviceFtp>true</serviceFtp>         <serviceSsh>true</serviceSsh>         <serviceSnmp>true</serviceSnmp>         <serviceDot1x>true</serviceDot1x>         <serviceHttp>true</serviceHttp>     </domain>''' ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.create(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |
   | create | RPC operation. The parameter in the URI is fixed to **operations**. | ``` import ops import string import hashlib uri = "/restconf/operations/huawei-cfg:set-startup" host = "localhost" req_data = '''<input>     <filename>vrpcfg1.zip</filename> </input>''' ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.create(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |
   | delete | No service body is allowed. | ``` import ops import string import hashlib uri = "/restconf/data/huawei-aaa:aaa/domains/domain=test1" host = "localhost" req_data = None ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.delete(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |
   | patch | Modifies an existing service. A service that does not exist cannot be created. | ``` import ops import string import hashlib uri = "/restconf/data/huawei-aaa:aaa/domains/domain" host = "localhost" req_data = '''<domain>         <domainName>test1</domainName>         <authenSchemeName>default</authenSchemeName>         <acctSchemeName>default</acctSchemeName>         <authorSchemeName>default</authorSchemeName>         <domainState>active</domainState>         <accessLimit>283648</accessLimit>         <serviceTerminal>true</serviceTerminal>         <serviceTelnet>true</serviceTelnet>         <serviceFtp>true</serviceFtp>         <serviceSsh>true</serviceSsh>         <serviceSnmp>true</serviceSnmp>         <serviceDot1x>true</serviceDot1x>         <serviceHttp>true</serviceHttp>     </domain>''' ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.patch(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |
   | get | * No service body is allowed. * When querying a list node, you must specify a key node or filter criteria. | ``` import ops import string import hashlib print("hello") print("world") uri = "/restconf/data/huawei-aaa:aaa/domains/domain=test1" host = "localhost" req_data = None ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.get(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |
   | set | N/A | ``` import ops import string import hashlib uri = "/restconf/data/huawei-aaa:aaa/domains/domain" host = "localhost" req_data = '''<domain>         <domainName>test1</domainName>         <authenSchemeName>default</authenSchemeName>         <acctSchemeName>default</acctSchemeName>         <authorSchemeName>default</authorSchemeName>         <domainState>active</domainState>         <accessLimit>283648</accessLimit>         <serviceTerminal>true</serviceTerminal>         <serviceTelnet>true</serviceTelnet>         <serviceFtp>true</serviceFtp>         <serviceSsh>true</serviceSsh>         <serviceSnmp>true</serviceSnmp>         <serviceDot1x>true</serviceDot1x>         <serviceHttp>true</serviceHttp>     </domain>''' ops_conn = ops.OPSConnection(host) ret, _, rsp_data = ops_conn.set(uri, req_data) print(('install_ops_script ret {}, rsp_data {}'.format(ret, rsp_data))) ``` |