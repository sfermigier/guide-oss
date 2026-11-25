# Intelligence artificielle

Exécuter soi-même un modèle de langage répond à trois préoccupations : garder les données dans son système d’information, maîtriser les coûts et ne pas dépendre d’une interface propriétaire susceptible de changer sans préavis. La chaîne comprend plusieurs couches à choisir séparément : un serveur d’inférence, une interface, une base vectorielle pour la recherche documentaire (RAG) et des outils de suivi et d’évaluation (MLOps).

Il faut distinguer **modèle ouvert** et **modèle libre**. Un modèle ouvert (*open weights*) publie ses poids, parfois sous une licence qui restreint les usages. Un modèle libre au sens de l’*Open Source AI Definition* (OSAID 1.0) de l’Open Source Initiative doit fournir, sous des conditions approuvées par l’OSI, ses paramètres, le code complet d’entraînement et d’exécution et des informations sur les données assez détaillées pour qu’une personne compétente puisse construire un système équivalent. Les données elles-mêmes peuvent ne pas être publiées. Un logiciel libre de cette page peut donc exécuter un modèle qui ne l’est pas : les deux licences se vérifient indépendamment.

Pour les bases vectorielles, voir Qdrant dans [Moteurs de recherche](../web-communication/moteurs-de-recherche.md) et l’extension pgvector de PostgreSQL dans [Bases de données relationnelles](../sgbd-middleware/bases-de-donnees.md#postgresql).

## vLLM

Site
: <https://vllm.ai/>

Porteur
: une fondation (PyTorch Foundation)

Licence
: Apache 2.0

vLLM est un moteur d’inférence pour modèles de langage, né à l’université de Californie à Berkeley et hébergé depuis mai 2025 par la PyTorch Foundation.

Il vise le service à de nombreux utilisateurs simultanés sur un serveur équipé d’accélérateurs : regroupement continu des requêtes, gestion paginée de la mémoire, répartition d’un modèle sur plusieurs GPU. Son interface compatible avec celle d’OpenAI permet de réutiliser les clients existants.

Son exploitation suppose de dimensionner la mémoire graphique et de suivre un rythme de publication rapide. vLLM est écrit principalement en Python.

## llama.cpp

Site
: <https://github.com/ggml-org/llama.cpp>

Porteur
: une communauté (avec le soutien de Hugging Face)

Licence
: MIT

llama.cpp, lancé par Georgi Gerganov, exécute des modèles de langage sur du matériel ordinaire, avec ou sans GPU. Son équipe a rejoint Hugging Face en février 2026 en conservant, selon l’annonce, son autonomie technique.

Le projet utilise le format de fichier GGUF et des modèles quantifiés, c’est-à-dire dont la précision numérique est réduite pour économiser la mémoire. Il fournit une bibliothèque, des outils en ligne de commande et un serveur HTTP.

Il convient aux postes isolés, aux petits serveurs et à l’embarqué. Pour un service partagé par de nombreux utilisateurs, vLLM est à évaluer en parallèle. llama.cpp est écrit en C et C++.

## Ollama

Site
: <https://ollama.com/>

Porteur
: un éditeur (Ollama Inc.)

Licence
: MIT

Ollama simplifie le téléchargement et l’exécution de modèles sur un poste ou un serveur : une commande suffit à récupérer un modèle. Une API locale le met à disposition des applications.

C’est une bonne entrée en matière pour un développeur ou une maquette. L’éditeur propose aussi des modèles hébergés : un déploiement qui doit rester local le vérifiera dans sa configuration.

La licence MIT concerne le logiciel, tandis que chaque modèle du catalogue a la sienne. L’API n’est pas à exposer sans authentification placée en amont. Ollama est écrit en Go.

## LibreChat

Site
: <https://www.librechat.ai/>

Porteur
: un éditeur (ClickHouse)

Licence
: MIT

LibreChat est une interface de conversation web, auto-hébergeable, qui donne accès depuis un même écran à des modèles locaux ou à des services distants. ClickHouse a annoncé l’acquisition du projet en novembre 2025.

Elle gère plusieurs utilisateurs, l’historique des conversations, les agents et les outils externes par le protocole MCP.

Connecter un service distant revient à lui transmettre le contenu des conversations : la liste des fournisseurs autorisés est donc une décision de sécurité. LibreChat est écrit en TypeScript.

## MLflow

Site
: <https://mlflow.org/>

Porteur
: une fondation (Linux Foundation)

Licence
: Apache 2.0

MLflow, lancé par Databricks, est une plateforme de suivi du cycle de vie des modèles : journal des expériences, comparaison des paramètres et des résultats, registre de modèles et déploiement.

Le projet a étendu son périmètre aux applications fondées sur des modèles de langage, avec la collecte de traces et l’évaluation des réponses.

L’auto-hébergement demande une base de données et un stockage pour les artefacts, ainsi qu’une réflexion sur l’authentification. MLflow est écrit principalement en Python.

## Autres

- LocalAI, serveur d’inférence multi-modèles compatible avec l’API d’OpenAI (MIT) : <https://localai.io/>
- RAGFlow, moteur de RAG (Apache 2.0) : <https://ragflow.io/>
- LangChain, bibliothèque de composition d’applications (MIT) : <https://github.com/langchain-ai/langchain>
- Langfuse, observabilité des applications à modèles de langage (MIT, hors modules commerciaux) : <https://langfuse.com/>
