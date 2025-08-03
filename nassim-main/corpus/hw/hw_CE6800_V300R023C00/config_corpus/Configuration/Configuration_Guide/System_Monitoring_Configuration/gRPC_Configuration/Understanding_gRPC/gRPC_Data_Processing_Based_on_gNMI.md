gRPC Data Processing Based on gNMI
==================================

In [Figure 1](#EN-US_CONCEPT_0000001564006061__fig192693715416), in dial-in mode, gRPC provides data configuration and query functions using the Capabilities, Set, Get, and Subscribe methods defined in the gRPC Network Management Interface (gNMI) protocol.

**Figure 1** gRPC-based data query and configuration fundamentals diagram  
![](figure/en-us_image_0000001513045838.png)
#### Capabilities Method

**The Capabilities method is used to obtain device model capabilities. Its process is as follows:**

1. The gRPC client sends an RPC request (Capabilities) defined in the gNMI protocol.
   * gNMI defines the RPC method and packet structure in the **gnmi.proto** file. To obtain the **gnmi.proto** file, see [Obtaining the gnmi.proto File](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto).
2. The gRPC server parses the request packet and detects that a Capabilities method is used in the RPC request.
   * Operation authentication: All users who successfully log in to the device can use the Capabilities method to obtain device capabilities.
   * Log recording: The gRPC server records logs.
3. The gRPC server obtains the existing model capability set on the device. The model information includes:
   * Model name, such as huawei-ifm
   * Organization, such as Huawei Technologies Co., Ltd.
   * Model version, such as 2018-11-23 and 1.0.0.
4. The gRPC server returns the capability set to the client.

![](public_sys-resources/note_3.0-en-us.png) 

* If the YANG model changes due to a patch installation, the gRPC server loads the new model and ensures it takes effect.
* If the Capabilities method contains unimplemented parameters, parameters fail verification, or an error occurs on the model obtaining interface, the gRPC server records a Capabilities method execution failure log and waits for the client to re-send a correct Capabilities request.
* When the YANG model on the gRPC server changes, the gRPC server does not notify the client. To obtain the latest YANG model, the client must call the Capabilities method.

**The Capabilities packet format is as follows**:

# Response packet.
```
++++++++ Received get response: ++++++++  
 supported_models { 
name:"openconfig-interfaces"  
organization:"OpenConfig workinggroup"  
version:"2.3.0" 
} 
supported_models { 
name:"huawei-ifm" 
organization:"Huawei Technologies Co.,Ltd."  
version:"2018-11-23" 
} 
supported_encodings:JSON 
gNMI_version:"0.7.0"
```


#### Get Method

**The process of the Get method is as follows**:

1. The gRPC client sends an RPC request (Get) defined in the gNMI protocol.
   * gNMI defines the RPC method and packet structure in the **gnmi.proto** file. To obtain the **gnmi.proto** file, see [Obtaining the gnmi.proto File](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto).
   * The Get method uses JSON to encode service data.
   * The Get method includes the following parameters.
     
     **Table 1** Parameters in the Get method
     | Parameter | Description |
     | --- | --- |
     | ALL | Corresponds to NETCONF <get> and includes configuration data and status data. |
     | CONFIG | Corresponds to NETCONF <get-config> and includes configuration data. |
2. The gRPC server queries data.
   * Operation authentication: During a Get operation, the system performs authentication to check whether the user has sufficient permission to access the specified path. If the authentication fails, the system returns an authentication failure error and terminates the operation.
   * Log recording: The gRPC server records operation logs that contain service data. Sensitive information in the service data will be shielded.
   * Transaction management: Query for multiple paths in a request packet is supported. All path query results are returned only after the query is complete. If an error occurs (for example, NotFound) during the query for multiple paths, the query is terminated, an error message is displayed, and all cached query results are discarded.
   * Object: The Get operation can be performed on a container and its sub-nodes, or on a leaf node.
   * Capacity: The maximum size of a response packet is 20 MB. If the maximum size is exceeded, an error is reported.

**The Get packet format is as follows**:

* Input path for a container or list node: openconfig-telemetry:telemetry-system/sensor-groups/sensor-group[sensor-group-id=s1]# Query packet.
  ```
  ++++++++ Sending get request: ++++++++
  path {
    elem {
      name: "openconfig-telemetry:telemetry-system"
    }
    elem {
      name: "sensor-groups"
    }
    elem {
      name: "sensor-group"
      key {
        key: "sensor-group-id"
        value: "s1"
      }
    }
  }
  type: CONFIG
  encoding: JSON
  ```
  
  # Response packet.
  ```
  notification {
    timestamp: 1717732971365270000
    update {
      path {
        elem {
          name: "openconfig-telemetry:telemetry-system"
        }
        elem {
          name: "sensor-groups"
        }
        elem {
          name: "sensor-group"
          key {
            key: "sensor-group-id"
            value: "s1"
          }
        }
      }
      val {
        json_val: "{\n\t\"sensor-group-id\":\t\"s1\",\n\t\"config\":\t{\n\t\t\"sensor-group-id\":\t\"s1\"\n\t},\n\t\"state\":\t{\n\t\t\"sensor-group-id\":\t\"s1\"\n\t},\n\t\"sensor-paths\":\t{\n\t\t\"sensor-path\":\t[{\n\t\t\t\t\"path\":\t\"huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test\",\n\t\t\t\t\"config\":\t{\n\t\t\t\t\t\"path\":\t\"huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test\",\n\t\t\t\t\t\"huawei-openconfig-telemetry-ext:reset-when-start\":\tfalse,\n\t\t\t\t\t\"huawei-openconfig-telemetry-ext:depth\":\t1\n\t\t\t\t},\n\t\t\t\t\"state\":\t{\n\t\t\t\t\t\"path\":\t\"huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test\",\n\t\t\t\t\t\"huawei-openconfig-telemetry-ext:reset-when-start\":\tfalse,\n\t\t\t\t\t\"huawei-openconfig-telemetry-ext:depth\":\t1\n\t\t\t\t}\n\t\t\t}]\n\t}\n}"
      }
    }
  }
  ```
* Input path for a leaf node: openconfig-telemetry:telemetry-system/sensor-groups/sensor-group[sensor-group-id=s1]/sensor-paths/sensor-path/path# Query request packet.
  ```
  ++++++++ Sending get request: ++++++++
  path {
    elem {
      name: "openconfig-telemetry:telemetry-system"
    }
    elem {
      name: "sensor-groups"
    }
    elem {
      name: "sensor-group"
      key {
        key: "sensor-group-id"
        value: "s1"
      }
    }
    elem {
      name: "sensor-paths"
    }
    elem {
      name: "sensor-path"
    }
    elem {
      name: "path"
    }
  }
  type: CONFIG
  encoding: JSON
  ```
  
  # Response packet.
  ```
  notification {
    timestamp: 1717735053530627000
    update {
      path {
        elem {
          name: "openconfig-telemetry:telemetry-system"
        }
        elem {
          name: "sensor-groups"
        }
        elem {
          name: "sensor-group"
          key {
            key: "sensor-group-id"
            value: "s1"
          }
        }
        elem {
          name: "sensor-paths"
        }
        elem {
          name: "sensor-path"
          key {
            key: "path"
            value: "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test"
          }
        }
        elem {
          name: "path"
        }
      }
      val {
        json_val: "\"huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test\""
      }
    }
  }
  
  ```

#### Set Method

**The Set method is used to deliver configurations to the device. The process is as follows:**

1. The gRPC client sends an RPC request (Set) defined in the gNMI protocol.
   * gNMI defines the RPC method and packet structure in the **gnmi.proto** file. To obtain the **gnmi.proto** file, see [Obtaining the gnmi.proto File](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto).
   * The Set method uses JSON to encode service data. Each field can carry a namespace. If no namespace is carried, the namespace of the parent container node is inherited by default.
   * The Set method includes the following parameters.
     
     **Table 2** Parameters in the Set method
     | Parameter | Description |
     | --- | --- |
     | DELETE | Corresponds to NETCONF <delete> and is used to delete configuration data. |
     | REPLACE | Corresponds to NETCONF <replace> and is used to replace configuration data. |
     | UPDATE | Corresponds to NETCONF <merge> and is used to update or create configuration data. |
2. The gRPC server modifies the device data based on the request.
   * Operation authentication: During a Set operation, the system performs authentication to check whether the user has sufficient permission to access the specified path. If the authentication fails, the system returns an authentication failure error and terminates the operation.
   * Log recording: The gRPC server records operation logs that contain service data. Sensitive information in the service data will be shielded.
   * Transaction management: When a request packet carries multiple operations such as the delete, replace, and update operations, the gRPC server sequentially performs the operations in compliance with the gNMI protocol.
   * Object operation: The Set operation can be performed on a container and its sub-nodes, or on a leaf node.
   * Capacity: The maximum size of a request packet is 1 MB.
3. The gRPC server returns data to the client.

![](public_sys-resources/note_3.0-en-us.png) 

Operations take effect when they are all successfully performed. If any operation fails, all operations do not take effect and a failure message is returned.

**The Set packet format is as follows**:

* Input path for a Delete operation: openconfig-telemetry:telemetry-system/sensor-groups/sensor-group[sensor-group-id=s1]# Configuration request packet.
  ```
  ++++++++ Sending set request: ++++++++
  path {
    elem {
      name: "openconfig-telemetry:telemetry-system"
    }
    elem {
      name: "sensor-groups"
    }
    elem {
      name: "sensor-group"
      key {
        key: " sensor-group-id"
        value: "s1"
      }
    }
  }
  
  ```
  
  # Response packet.
  ```
  ++++++++ Received set response: ++++++++
  response {
    path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
      elem {
        name: "sensor-group"
        key {
          key: "sensor-group-id"
          value: "s1"
        }
      }
    }
    op: DELETE
  }
  timestamp: 1717685040830542000
  ```
* Replace operation (without a key).
  + Input path: openconfig-telemetry:telemetry-system/sensor-groups
  + Input data in JSON format:
    ```
    {
      "sensor-group": {
    	"sensor-group-id": "s1",
        "config": { "sensor-group-id": "s1" },
        "sensor-paths": {
          "sensor-path": {
            "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
            "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
          }
        }
      }
    }
    ```# Configuration request packet.
  ```
  ++++++++ Sending set request: ++++++++
  path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
    val {
      json_val: "{
  	"sensor-group": {
  	  "sensor-group-id": "s1",
        "config": { "sensor-group-id": "s1" },
        "sensor-paths": {
          "sensor-path": {
            "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
            "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
          }
        }
      }
      }"
    }
  }
  ```
  
  # Response packet.
  ```
  ++++++++ Received set response: ++++++++
  response {
    path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
    }
    op: REPLACE
  }
  timestamp: 1717729434261195000
  ```
* Replace operation (with a key).
  + Input path: openconfig-telemetry:telemetry-system/sensor-groups/sensor-group[sensor-group-id=s1]
  + Input data in JSON format:
    ```
    {
      "sensor-paths": {
        "sensor-path": {
          "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
          "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
        }
      }
    }
    ```# Configuration request packet.
  ```
  ++++++++ Sending set request: ++++++++
  path {
    elem {
      name: "openconfig-telemetry:telemetry-system"
    }
    elem {
      name: "sensor-groups"
    }
    elem {
      name: "sensor-group"
      key {
        key: "sensor-group-id"
        value: "s1"
      }
    }
    val {
      json_val: "{
  	"sensor-paths": {
  	  "sensor-path": {
          "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
          "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
        }
      }
  	}"
    }
  }
  ```
  
  # Response packet.
  ```
  ++++++++ Received set response: ++++++++
  response {
    path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
      elem {
        name: "sensor-group"
        key {
          key: "sensor-group-id"
          value: "s1"
        }
      }
    }
    op: REPLACE
  }
  timestamp: 1717731861486329000
  ```
* Update operation (without a key).
  + Input path: openconfig-telemetry:telemetry-system/sensor-groups
  + Input data in JSON format:
    ```
    {
      "sensor-group": {
    	"sensor-group-id": "s1",
        "config": { "sensor-group-id": "s1" },
        "sensor-paths": {
          "sensor-path": {
            "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
            "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
          }
        }
      }
    }
    ```# Configuration request packet.
  ```
  ++++++++ Sending set request: ++++++++
  path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
    val {
      json_val: "{
  	"sensor-group": {
  	  "sensor-group-id": "s1",
        "config": { "sensor-group-id": "s1" },
        "sensor-paths": {
          "sensor-path": {
            "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
            "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
          }
        }
      }
      }"
    }
  }
  ```
  
  # Response packet.
  ```
  ++++++++ Received set response: ++++++++
  response {
    path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
    }
    op: UPDATE
  }
  timestamp: 1717731674036991000
  ```
* Update operation (with a key).
  + Input path: openconfig-telemetry:telemetry-system/sensor-groups/sensor-group[sensor-group-id=s1]
  + Input data in JSON format:
    ```
    {
      "sensor-paths": {
        "sensor-path": {
          "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
          "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
        }
      }
    }
    
    ```# Configuration request packet.
  ```
  ++++++++ Sending set request: ++++++++
  path {
    elem {
      name: "openconfig-telemetry:telemetry-system"
    }
    elem {
      name: "sensor-groups"
    }
    elem {
      name: "sensor-group"
      key {
        key: "sensor-group-id"
        value: "s1"
      }
    }
    val {
      json_val: "{
  	"sensor-paths": {
  	  "sensor-path": {
          "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test",
          "config": { "path": "huawei-telemetry-sample-test:telemetry-sample-test/datatype-tests/datatype-test" }
        }
      }
  	}"
    }
  }
  ```
  
  # Response packet.
  ```
  ++++++++ Received set response: ++++++++
  response {
    path {
      elem {
        name: "openconfig-telemetry:telemetry-system"
      }
      elem {
        name: "sensor-groups"
      }
      elem {
        name: "sensor-group"
        key {
          key: "sensor-group-id"
          value: "s1"
        }
      }
    }
    op: UPDATE
  }
  timestamp: 1717732374267855000
  ```
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  Restrictions on leafref: When a parent node is associated with a child node through leafref, these two nodes must be both in a path or defined in JSON\_VAL. Otherwise, the operations on these two nodes will be different and will fail to be executed.
  
  Cause: The operation on nodes in a path is None, while the operation on nodes defined in JSON\_VAL is REPLACE or UPDATE. If one of two nodes associated through leafref is in a path and the other is defined in JSON\_VAL, operation consistency check will fail.
  
  For example, in the openconfig-telemetry.yang model, the key defined in the parent node **list subscription** is **subscription-name**, which is associated with **subscription-name** in child node **config** through leafref. The preceding restriction applies to data in **config**. If the path is set to:
  
  ```
  "openconfig-telemetry:telemetry-system/subscriptions/persistent/subscription[subscription-name=abc]
  ```
  
  If JSON\_VAL is defined as:
  
  ```
  {"config": {"originated-qos-marking": "30","encoding":"openconfig-telemetry-types:ENC_PROTO3"}}
  ```
  
  The following error is returned:
  
  ```
  The target node of the leafref type and the source node have different operations.
  ```
  
  To rectify the error, set the path to:
  
  ```
  "openconfig-telemetry:telemetry-system/subscriptions/persistent/subscription[subscription-name=abc]/config"
  ```
  
  Define JSON\_VAL as:
  
  ```
  {"originated-qos-marking": "30","encoding":"openconfig-telemetry-types:ENC_PROTO3"}
  ```
  
  In this case, the parent and child nodes associated through leafref are both in a path and can be correctly executed.

#### Subscribe Method

**The Subscribe method is used to collect device status and configurations periodically or in event-driven mode. Its process is as follows:**

1. The gRPC client sends an RPC request (Subscribe) defined in the gNMI protocol.
   * gNMI defines the RPC method and packet structure in the **gnmi.proto** file. To obtain the **gnmi.proto** file, see [Obtaining the gnmi.proto File](https://github.com/openconfig/gnmi/blob/master/proto/gnmi/gnmi.proto).
   * The Subscribe method uses JSON/PROTO/JSON\_IETF to encode service data.
   * The Subscribe method includes the following parameters.
     
     **Table 3** Parameters in a Subscribe request
     | Layer 1 Parameter | Layer 1 Parameter Description | Layer 2 Parameter | Layer 2 Parameter Description |
     | --- | --- | --- | --- |
     | Prefix | Prefix. | path | Sampling path prefix. |
     | target | When the target parameter is set on the client, the response message from the server needs to carry the parameter. |
     | Subscription | There can be one or more groups of subscription parameters of this level in a Subscribe request. | path | Sampling path. |
     | mode | Sampling mode. Currently, the following modes are supported:  + ON\_CHANGE + SAMPLE |
     | sample\_interval | Sampling interval.  + The sampling interval takes effect only when the sampling mode is SAMPLE. + When the sampling mode is ON\_CHANGE, the sampling interval must be set to 0. |
     | SubscriptionListData | There can be only one group of subscription parameters of this level in a Subscribe request. | marking | Configured DSCP value. The value ranges from 0 to 63. |
     | mode | Subscription mode. Currently, STREAM is supported. |
     | allow\_aggregation | Whether the client allows elements with the aggregation flag to be combined in a gNMI message. This parameter is valid only in PROTO encoding mode. The values are as follows: + TRUE: Aggregation is allowed. + FALSE: Aggregation is not allowed. |
     | encoding | Encoding mode. Currently, the following modes are supported: + JSON + PROTO + JSON\_IETF |
     | updates\_only | Only incremental data is sent. This parameter is valid when the device sampling mode is ON\_CHANGE+.  NOTE:  There are two modes for the device to implement ON\_CHANGE. In mode 1, only incremental data is sent. In mode 2, full data is sent for the first time, and only incremental data is sent subsequently. |
2. The gRPC server parses the request packet and detects that a Subscribe method is used in the RPC request. The server collects data based on the parameters set in the packet and sends the collected data to the client.

**The Subscribe packet format is as follows**:

```
# Subscribe request packet
++++++++ Sending subscribe request: ++++++++
prefix {
	elem {
		name: "huawei-debug:debug"
	}
	target: "TARGET"
}
Subscription {
	path {
	  elem {
		name: "cpu-infos"
	  }
	  elem {
		name: "cpu-info"
	  }
	}
	mode: SAMPLE
	sample_interval: 1000
}
SubscriptionListData {
	marking: 63
	mode: STREAM
	allow_aggregation: false
	encoding: JSON
	updates_only: false
}
```

# JSON response packet.

```
++++++++ Received subscribe response: ++++++++
<subscibegNMI>: update {
  timestamp: 1626429829051000000
  update {
    path {
      elem {
        name: "huawei-debug:debug"
      }
      elem {
        name: "cpu-infos"
      }
      elem {
        name: "cpu-info"
      }
    }
    val {
      json_val: "[{\"position\":\"17\",\"overload-threshold\":90,\"unoverload-threshold\":75,\"interval\":8,\"index\":17891329,\"system-cpu-usage\":6,\"monitor-number\":48,\"monitor-cycle\":10,\"overload-state-change-time\":\"0000-00-00 00:00:00\",\"current-overload-state\":\"Unoverload\"}]"
    }
  }
  delete {
  }
}

<subscibegNMI>: sync_response: true
```

# PROTO response packet (allow\_aggregation = false).

```
++++++++ Received subscribe response: ++++++++
<subscibegNMI>: update {
  timestamp: 1626430004019000000
  prefix {
    elem {
      name: "huawei-debug:debug"
    }
    elem {
      name: "cpu-infos"
    }
    elem {
      name: "cpu-info"
      key {
        key: "position"
        value: "17"
      }
    }
  }
  update {
    path {
      elem {
        name: "overload-threshold"
      }
    }
    val {
      uint_val: 90
    }
  }
  update {
    path {
      elem {
        name: "unoverload-threshold"
      }
    }
    val {
      uint_val: 75
    }
  }
  update {
    path {
      elem {
        name: "interval"
      }
    }
    val {
      uint_val: 8
    }
  }
  update {
    path {
      elem {
        name: "index"
      }
    }
    val {
      uint_val: 17891329
    }
  }
  update {
    path {
      elem {
        name: "system-cpu-usage"
      }
    }
    val {
      uint_val: 3
    }
  }
  update {
    path {
      elem {
        name: "monitor-number"
      }
    }
    val {
      uint_val: 48
    }
  }
  update {
    path {
      elem {
        name: "monitor-cycle"
      }
    }
    val {
      uint_val: 10
    }
  }
  update {
    path {
      elem {
        name: "overload-state-change-time"
      }
    }
    val {
      string_val: "0000-00-00 00:00:00"
    }
  }
  update {
    path {
      elem {
        name: "current-overload-state"
      }
    }
    val {
      string_val: "Unoverload"
    }
  }
  delete {
  }
}

<subscibegNMI>: sync_response: true
```

# PROTO response packet (allow\_aggregation = true).

```
++++++++ Received subscribe response: ++++++++
<subscibegNMI>: update {
  timestamp: 1626430056356000000
  update {
    path {
      elem {
        name: "huawei-debug:debug"
      }
      elem {
        name: "cpu-infos"
      }
      elem {
        name: "cpu-info"
      }
    }
    val {
      proto_bytes: "0a023137105a184b2008288180c40830033830400a4a13303030302d30302d30302030303a30303a3030520a556e6f7665726c6f6164"
    }
  }
  delete {
  }
}

<subscibegNMI>: sync_response: true
```

#### Common Error Logs

1. The TLS encryption channel does not support the Capabilities, Get, Set, and Subscribe methods.
   ```
   rpc error: code = PermissionDenied desc = Need use tls.
   ```
2. The user name or password is incorrect.
   ```
   rpc error: code = Unauthenticated desc = Invalid authentication credentials.
   ```
3. Parameters are invalid.
   * The input **Path** field is invalid.
     ```
     rpc error: code = InvalidArgument desc = Argument 'Path' error.
     ```
   * The input JSON data is invalid.
     ```
     rpc error: code = InvalidArgument desc = The JSON value is invalid.
     ```
4. No data is available.
   ```
   rpc error: code = NotFound desc = Not found.
   ```