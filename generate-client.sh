set -e
dir=${PWD}
parentdir="$(dirname "$dir")"

REPO_TAG=$1
FILE=https://raw.githubusercontent.com/sirspock/dbpedia_api/$REPO_TAG/openapi.yaml
docker run \
    -e PYTHON_POST_PROCESS_FILE="/usr/local/bin/yapf -i" \
    -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli \
     generate  \
     -i $FILE \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id dbpedia \
     --git-user-id sirspock  \

popd
