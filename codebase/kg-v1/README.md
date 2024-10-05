# Knowledge Graph v1

## Running
### Default ports and profiles

#### Note: Valid Vertical Names: Make sure use below string till we make it config driven.

    Common
    Telecom,
    Retail,
    Media,
    Hydrocarbons,
    SmartCities,
    Healthcare,
    Agriculture,
    Education,
    HumanResources,
    CyberSecurity


#### IP: 10.161.209.143

| service | Profile | Port | Notes |
|-----------|-----------|------|----------------------------|
| add-collection-type-service | debug | 31001 | AddCollectionType|
| add-entity-service | debug | 31002 | Dependency MetadataLookup, Identity, Config, DeleteEntity service |
| metadata-lookup-service | debug | 31003 | |
| delete-entity-service | debug | 31004 |  |
| add-attribute-type-service | debug | 31006 |  |
| add-bizid-to-entity-service | debug | 31007 | |
| add-predicate-service | debug | 31008 | |
| get-entity-service | debug | 31009 | |
| get-predicate-service | debug | 31010 | |
| has-entity-service | debug | 31011 | |
| has-biz-id-service | debug | 31012 | |
| delete-collection-service | debug | 31013 | |
| get-attribute-service | debug | 31014 | |
| get-canonical-name-service | debug | 31015 | |
| graph-query-service | debug | 31016 | |
| get-alias-service | debug | 31017 | |
| get-all-biz-id-types-of-entity-id-service | debug | 31018 | |
| get-entities-with-alias-name-service | debug | 31019 | |
| has-canonical-name-service | debug | 31020 | |
| get-entities-with-canonical-name-service | debug | 31021 | |
| delete-attribute-service | debug | 31022 | |
| delete-predicate-service | debug | 31023 | |
| add-attribute-service | debug | 31024 | |
| delete-bizid-service | debug | 31025 | |
| add-canonical-name-service | debug | 31026 | |
| delete-canonical-name-service | debug | 31027 | |
| delete-attribute-type-service | debug | 31028 | |
| enrich-api-service | debug | 31029 | |
| get-all-entity-ids-using-biz-id-service | debug | 31030 | |
| delete-entity-alias-service | debug | 31031 | |
| get-bizid-of-entityid-service | debug | 31032 | |
| has-any-biz-id-service | debug | 31033 | |
| update-bizid-to-entity-service | debug | 31034 | |
| update-canonical-name-service | debug | 31035 | |
| get-schema-service | debug | 31036 | |
| get-all-children-service | debug | 31038 | |
| entity-id-lookup-service | debug | 31039 | |
| get-edge-service | debug | 31044 | |
| get-attribute-value-service | debug | 31045 | |
| get-attribute-id-service | debug | 31046 | |
| get-context-value-id-service | debug | 31047 | |
| get-entity-id-by-name-service | debug | 31048 | |
| get-context-service | debug | 31051 | |
| get-attribute-value-id-service | debug | 31052 | |
| search-entity-by-context-service | debug | 31053 | |
| search-entity-context-service | debug | 31054 | |
| get-attribute-service-v2 | debug | 31055 | |
| metadata-lookup-service-v2 | debug | 31056 | |
| get-valid-entity-attribute-values-given-filter-service | debug | 31057 | |

## Delete Collection 

- Schema Layer is not getting cleanup

## Add Collection Type

### Tech Debt
- Required Attribute passing is based on required flag in 'attribute_schema'
- Qualifiers are not supported over dynamic attributes
- All BrainQuantities are not supported
- Environment variable need to be introduced in deployment configuration

### Install dependencies
```bash
pip3 install -r requirements.txt --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/
```

### Python Native Client

```python
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2 import AddCollectionTypeRequest
from jio.brain.proto.knowledge.api.schema.add_collection_type_pb2_grpc import AddCollectionTypeServiceStub

channel = grpc.insecure_channel(add_collection_type_channel)
stub = AddCollectionTypeServiceStub(channel)
response = stub.serve(request)
```


## Add Entity Service

AddEntity services is used to add an Entity Instance to Knowledge Graph in a provided collection. Collection Type should be present before adding the instance.

### Python Native Client

```python
from jio.brain.proto.knowledge.base.entity_pb2 import Entity

from jio.brain.proto.knowledge.api.data.add_entity_pb2 import AddEntityRequest

from jio.brain.proto.knowledge.api.data.add_entity_pb2_grpc import AddEntityServiceStub

channel = grpc.insecure_channel(localhost:31002)
stub = AddEntityServiceStub(channel)
response = stub.serve(request)
```


## AddBizIdToEntity 

### Tech Debt
- Deduplication of BizID missing 
- Primary BizID should be immutable 


### Python SDK

    /test/api/add-entity/client.py 



### Tech Debt
- BrainStatusCode Needs to be added in Error Handling Scenarios.
- Environment Variables for Identity, Config Service should come from the Environment.

## Get Entity Service
### Host and Port: 


### Tech Debt
- BrainStatusCode Needs to be added in Error Handling Scenarios.
- Environment Variables for Identity, Config Service should come from the Environment.



## Deployment K8S 


### API Deployment K8S

```bash
kubectl apply -f k8s/api/add_entity_deployment.yaml -n storage-garden
```

```bash
kubectl apply -f k8s/ingress/configmap/cofigmap.yaml -n storage-garden
```

```bash
kubectl patch deployment nginx-ingress-ingress-nginx-controller -n storage-garden --patch "$(cat k8s/ingress/nginx-ingress-controller-patch.yaml)"

kubectl patch service nginx-ingress-ingress-nginx-controller -n storage-garden --patch "$(cat k8s/ingress/nginx-ingress-svc-controller-patch.yaml)"
```

```bash

kubectl get service -n storage-garden nginx-ingress-ingress-nginx-controller

NAME                                     TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)                                                                                                      AGE
nginx-ingress-ingress-nginx-controller   LoadBalancer   10.0.30.232   10.161.209.143   31001:31001/TCP,31002:31002/TCP,31003:31003/TCP,31004:31004/TCP,31005:31005/TCP,80:31738/TCP,443:30915/TCP   21d
```

```bash
kubectl get service -n storage-garden

NAME                                               TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)                                                                                                      AGE
add-collection-type-service                        ClusterIP      10.0.246.159   <none>           31001/TCP                                                                                                    18d
add-entity-service                                 ClusterIP      10.0.143.224   <none>           31002/TCP                                                                                                    14d
delete-entity-service                              ClusterIP      10.0.238.204   <none>           31004/TCP                                                                                                    48s
metadata-lookup-service                            ClusterIP      10.0.148.219   <none>           31003/TCP                                                                                                    40m
nginx-ingress-ingress-nginx-controller             LoadBalancer   10.0.30.232    10.161.209.143   31001:31001/TCP,31002:31002/TCP,31003:31003/TCP,31004:31004/TCP,31005:31005/TCP,80:31738/TCP,443:30915/TCP   21d
nginx-ingress-ingress-nginx-controller-admission   ClusterIP      10.0.22.117    <none>           443/TCP
```


```bash

kubectl proxy

kubectl describe secret dashboard-admin-sa-token-598w2

http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/shell/storage-garden

```

### v1 Release Features 
---
#### Data APIs
---
<table style="width: 118px; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="width: 43.7px;text-align: center;">S.no.</td>
<td style="width: 14.3px;text-align: center;">Object</td>
<td style="width: 15px;text-align: center;">Create</td>
<td style="width: 15px;text-align: center;">Read</td>
<td style="width: 15px;text-align: center;">Update</td>
<td style="width: 15px;text-align: center;">Delete</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">1.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">Entity</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_entity">add-entity-api</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_entity">get-entity-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/update_canonical_name">update-canonical-name-api</a>, <a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/update_bizid_to_entity">update-bizid-to-entity-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_entity">delete-entity-api</a></td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">2.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">Predicate</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">❌</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_predicate">add-predicate-api</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_predicate">get-predicate-api</a></td>
<td style="width: 15px;text-align: center;">NA</td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_predicate">delete-predicate-api</a></td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">3.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">Canonical</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_canonical_name">add-canonical-name-api</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_canonical_name">get-canonical-name-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/update_canonical_name">update-canonical-name-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_canonical_name">delete-canonical-name-api</a></td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">4.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">Alias</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">❌</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_entity_alias">add-entity-alias-api</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_alias">get-alias-api</a></td>
<td style="width: 15px;text-align: center;">NA</td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_entity_alias">delete-entity-alias-api</a></td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">5.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">BizId</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_bizid_to_entity">add-bizid-to-entity-api</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_bizid_of_entityid">get-bizid-of-entityid-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/update_bizid_to_entity">update-bizid-to-entity-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_bizid">delete-bizid-api</a></td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;" rowspan="2">6.</td>
<td style="width: 14.3px;text-align: center;" rowspan="2">Attributes</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
<td style="width: 15px;text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_attribute">add-attribute</a></td>
<td style="width: 14.3px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_attribute">get-attribute-api</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_attribute">upsert_attribute</a></td>
<td style="width: 15px;text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_attribute">delete-attribute</a></td>
</tr>
</tbody>
</table>
<p></p>

#### Schema APIs
---
<table style="width: 118px;">
<tbody>
<tr>
<td style="width: 43.7px; text-align: center;">S.no.</td>
<td style="width: 14.3px; text-align: center;">Object</td>
<td style="width: 15px; text-align: center;">Create</td>
<td style="width: 15px; text-align: center;">Read</td>
<td style="width: 15px; text-align: center;">Update</td>
<td style="width: 15px; text-align: center;">Delete</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;" rowspan="2">1.</td>
<td style="width: 14.3px; text-align: center;" rowspan="2">Collection-Type</td>
<td style="width: 15px; text-align: center;">✅</td>
<td style="width: 15px; text-align: center;">✅</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">❌</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_collection_type">add-collection-type-api</a></td>
<td style="width: 14.3px; text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_schema">get-schema</a></td>
<td style="width: 15px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;">NA</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;" rowspan="2">2.</td>
<td style="width: 14.3px; text-align: center;" rowspan="2">Attribute-Type</td>
<td style="width: 15px; text-align: center;">✅</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">✅</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/add_attribute_type">add-attribute-type-api</a></td>
<td style="width: 14.3px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/delete_attribute_type">delete-attribute-type</a></td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;" rowspan="2">3.</td>
<td style="width: 14.3px; text-align: center;" rowspan="2">BizId</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">✅</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">❌</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;">NA</td>
<td style="width: 14.3px; text-align: center;"><a href="https://github.com/KrishnaKumarTiwari/kg-v1/tree/v1/src/test/api/get_all_biz_id_types_of_entity_id">get-bizid-type-api</a></td>
<td style="width: 15px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;">NA</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;" rowspan="2">4</td>
<td style="width: 14.3px; text-align: center;" rowspan="2">Entity-Type</td>
<td style="width: 15px; text-align: center;">❌</td>
<td style="width: 15px; text-align: center;">&nbsp;❌</td>
<td style="width: 15px; text-align: center;">&nbsp;❌</td>
<td style="width: 15px; text-align: center;">&nbsp;❌</td>
</tr>
<tr>
<td style="width: 43.7px; text-align: center;">NA</td>
<td style="width: 14.3px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;">NA</td>
<td style="width: 15px; text-align: center;">NA</td>
</tr>
</tbody>
</table>
<p></p>

#### Key

Legend| Meaning
-----|-----|
❌|   denotes, we have did not have these APIs in earlier versions, so we need to develop them from scratch
⌛|    denotes, we have it in earlier version, but not yet converted for v1 usage
✅|   denotes, that the API is converted for v1 usage and deployed too.


## Testing
#### Install pytest and pytest-html plugin:
```bash
pip install pytest
pip install pytest-html
```

#### To run test for has_entity API (from src directory):
```bash
make test_pytest_has_entity
```

#### To generate report.html:
```bash
make test_pytest_generate_report
```
