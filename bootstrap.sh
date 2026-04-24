#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/YOUR_ORG/YOUR_REPO.git}"

echo "==> Substituindo URL do repositório nos manifests..."
find argocd/ k8s/ -type f \( -name "*.yaml" -o -name "*.yml" \) \
  -exec sed -i "s|https://github.com/YOUR_ORG/YOUR_REPO.git|${REPO_URL}|g" {} +

echo "==> Instalando ArgoCD (se ainda não instalado)..."
kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl wait --for=condition=available --timeout=120s deployment/argocd-server -n argocd

echo "==> Registrando repositório público (sem senha)..."
kubectl apply -f argocd/repo-secret.yaml

echo "==> Criando AppProject..."
kubectl apply -f argocd/project.yaml

echo "==> Criando Applications..."
kubectl apply -f argocd/application-dev.yaml
kubectl apply -f argocd/application-prod.yaml

echo ""
echo "✅ ArgoCD configurado. Acesse a UI com:"
echo "   kubectl port-forward svc/argocd-server -n argocd 8080:443"
echo "   Usuário: admin"
echo "   Senha:   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d"
