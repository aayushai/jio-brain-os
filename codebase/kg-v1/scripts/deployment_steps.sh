## Create deployment:

# Set these variables:
# API name goes like: add_entity, add_predicate
export image_tag=${image_tag}
export api_name=${api_name}
export namespace=${namespace}
# Port number: 31001, 31002
export port=${port}
export api_name_hyphen=$(echo ${api_name} | tr '_' '-')
export api_dir=../src/api/${api_name}
export config_file=${api_dir}/config.py
export test_config_file=test/${api_dir}/config.py
export dockerfile=${api_dir}/Dockerfile
export docker_template=./dockerfile_template
export deployment_template=./deployment_template

ansible-playbook deploy.yml --extra-vars "api_name=$api_name  port=$port image_tag=${image_tag}" --tags="login,test_client"

# Add port to config.py
#sed -ie 's:^SERVER_PORT.*:SERVER_PORT = '${port}':g' ${config_file}
#yes | rm ${config_file}e

# Add port to test config.py
#sed -ie 's/localhost.[0-9]*/localhost:'${port}'/g' $test_config_file
#yes | rm ${test_config_file}e

# Run server
#make server_${api_name}

# Run client
#make client_${api_name}

# Create Dockerfile
envsubst '${api_name},${port}' < $docker_template > $dockerfile 
docker build -f ${dockerfile} -t jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag} .
docker run -p ${port}:${port} -d jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag}
# Docker push
az acr login -n jiocontainerregistry.azurecr.io
docker push jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag}

# Deployment file
# Login
envsubst '${api_name},${port},${api_name_hyphen}' < ${deployment_template} > k8s/api/${api_name}_deployment.yaml
kubectl apply -f k8s/api/${api_name}_deployment.yaml -n ${namespace}
kubectl get pods -n ${namespace}
kubectl get deployments -n ${namespace}
kubectl get services -n ${namespace}

# Configmap
printf "\n    ${port}: \"${namespace}/${api_name_hyphen}-service:${port}\"" >> k8s/ingress/configmap/cofigmap.yaml
kubectl apply -f k8s/ingress/configmap/cofigmap.yaml -n ${namespace}
kubectl get configmaps -n ${namespace} -o yaml

# Ingress controller patch
printf "\n            - containerPort: ${port}\n              hostPort: ${port}" >> k8s/ingress/nginx-ingress-controller-patch.yaml
kubectl patch deployment nginx-ingress-ingress-nginx-controller -n ${namespace} --patch "$(cat k8s/ingress/nginx-ingress-controller-patch.yaml)"

# Ingress controller service patch
printf "\n    - nodePort: ${port}\n      port: ${port}\n      name: ${api_name_hyphen}-api" >> k8s/ingress/nginx-ingress-svc-controller-patch.yaml
kubectl patch service nginx-ingress-ingress-nginx-controller -n ${namespace} --patch "$(cat k8s/ingress/nginx-ingress-svc-controller-patch.yaml)"
kubectl get services nginx-ingress-ingress-nginx-controller -n ${namespace}

# telnet port 
telnet 10.161.209.143 ${port}


## Redeploy
docker build -f ${dockerfile} -t jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag} .
docker run -p ${port}:${port} -d jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag}
docker push jiocontainerregistry.azurecr.io/knowledge_graph/${api_name}_api:${image_tag}
kubectl delete deployments ${api_name_hyphen}-api-deployment -n ${namespace}
kubectl apply -f k8s/api/${api_name}_deployment.yaml -n ${namespace}